import requests
import yaml
from datetime import datetime


class LLMClient:
    """
    LLM Strategic Agent Client (v3)
    --------------------------------
    Взаимодействие с Qwen3 API:
    - генерация YAML миссий (в т.ч. мультиагентных)
    - объяснение решений (rationale)
    - эмбеддинги для контекста
    """

    def __init__(
        self,
        base_url="http://Serv.sae.ru:8888/v1",
        model="qwen3-30b-a3b-instruct-2507",
        embed_model="text-embedding-trotr-paraphrase-multilingual-minilm-l12-v2",
        context_limit=4000,
    ):
        self.base_url = base_url
        self.model = model
        self.embed_model = embed_model
        self.context_limit = context_limit

        self.system_prompt = """
Ты — стратегический агент мультиагентной системы Aerostack2.
Твоя задача — переводить команды оператора на естественном языке в формализованные миссии
для одного или нескольких агентов (дронов, UGV, ретрансляторов, базовых станций).

Формат вывода (строго YAML, без Markdown и комментариев):
mission:
  id: auto
  name: auto_generated
  description: <краткое описание на русском>
  agents:
    - id: <имя_агента>
      role: <роль: scout / relay / carrier / base / rescuer ...>
      behaviors:
        - behavior: <тип_поведения>
          параметры...

Правила:
- Все позиции относительные [x, y, z], не GPS.
- Если упомянута зона “avoid”, добавь поведение “avoid_zone”.
- Если упомянут “ретранслятор” — добавь агента с ролью “relay”.
- Если команда сложная — разбей миссию на агентов.
- Всегда возвращай корректный YAML, без пояснений, без Markdown.
- Контекст ≤ 4000 токенов.
"""

    # --------------------------------------------------------------------------
    # Основная функция генерации миссий
    # --------------------------------------------------------------------------
    def generate_mission(self, prompt: str, max_tokens: int = 800):
        """
        Отправляет операторский запрос модели и получает YAML-миссию и объяснение.
        Возвращает dict:
        {
          "mission_yaml": "<yaml текст>",
          "explanation": "<пояснение>"
        }
        """
        url = f"{self.base_url}/chat/completions"
        headers = {"Content-Type": "application/json"}

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt.strip()},
                {"role": "user", "content": prompt.strip()},
            ],
            "max_tokens": max_tokens,
        }

        try:
            # Генерация YAML
            response = requests.post(url, headers=headers, json=payload, timeout=90)
            response.raise_for_status()
            data = response.json()
            yaml_text = data["choices"][0]["message"]["content"].strip()

            if not yaml_text.startswith("mission:"):
                raise ValueError("Ответ модели не соответствует YAML формату миссии.")

            # Получаем объяснение
            explanation = self.explain_plan(prompt, yaml_text)

            return {
                "mission_yaml": yaml_text,
                "explanation": explanation
            }

        except Exception as e:
            print(f"[LLMClient] Ошибка при генерации миссии: {e}")
            return {
                "mission_yaml": "",
                "explanation": f"Ошибка генерации миссии: {e}"
            }

    # --------------------------------------------------------------------------
    # Объяснение решений (rationale)
    # --------------------------------------------------------------------------
    def explain_plan(self, prompt: str, plan_yaml: str) -> str:
        """
        Объясняет структуру сгенерированной миссии.
        """
        url = f"{self.base_url}/chat/completions"
        headers = {"Content-Type": "application/json"}

        explain_prompt = f"""
Ты — аналитик стратегического планирования миссий в Aerostack2.
Объясни кратко, почему миссия сформирована именно так.
Запрос оператора: {prompt}
План миссии:
{plan_yaml}
"""

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "Ты эксперт по мультиагентным миссиям. Пиши лаконично и по существу."},
                {"role": "user", "content": explain_prompt.strip()},
            ],
            "max_tokens": 400,
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"[LLMClient] Ошибка при объяснении миссии: {e}")
            return "Ошибка при объяснении миссии."

    # --------------------------------------------------------------------------
    # Эмбеддинги для RAG
    # --------------------------------------------------------------------------
    def embed_text(self, text: str):
        url = f"{self.base_url}/embeddings"
        headers = {"Content-Type": "application/json"}
        payload = {"model": self.embed_model, "input": text}

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data["data"][0]["embedding"]
        except Exception as e:
            print(f"[LLMClient] Ошибка при создании эмбеддинга: {e}")
            return None

    # --------------------------------------------------------------------------
    # Сохранение миссий в лог
    # --------------------------------------------------------------------------
    def save_mission_to_file(self, mission_yaml: str, base_path: str = "~/ws_aerostack2/log_missions/") -> str:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"{base_path}/mission_{timestamp}.yaml".replace("~", "/home/nichi")
            with open(path, "w") as f:
                f.write(mission_yaml)
            return path
        except Exception as e:
            print(f"[LLMClient] Ошибка при сохранении миссии: {e}")
            return None
