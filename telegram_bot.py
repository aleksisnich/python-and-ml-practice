from random import *
import json
import requests
import telebot
from telebot import types

books = []
films = []
API_URL = 'https://7012.deeppavlov.ai/model'
API_TOKEN = '7002491636:AAG04JvzXm0cx2YSgwXrnYyocAG0vaXXSBo'
bot = telebot.TeleBot(API_TOKEN)

mm = types.ReplyKeyboardMarkup(row_width=2) # row_width=2 означает, что у нашей клавиатуры будет по 2 кнопки в строке, как на скриншоте ниже.
button1 = types.KeyboardButton("Синяя таблетка")
button2 = types.KeyboardButton("Красная таблетка")
button3 = types.KeyboardButton("Список фильмов")
button4 = types.KeyboardButton("Список книг")
mm.add(button1, button2, button3, button4)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Выбери свою сторону!", reply_markup=mm)

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "Синяя таблетка":
        bot.send_message(message.chat.id, "Вы выбрали блаженную неизвестность иллюзии")
    elif message.text == "Красная таблетка":
        bot.send_message(message.chat.id, "Вы выбрали мучительную правдой реальность")
    elif message.text == "Список книг":
        books.append("Над пропастью во ржи")
        books.append("Чапаев и пустота")
        books.append("Война и мир")
        books.append("Заводной апельсин")
        books.append("Мастер и Маргарита")
        bot.send_message(message.chat.id, "Вот список книг")
        bot.send_message(message.chat.id, ", ".join(books))
        with open("books.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(books, ensure_ascii=False))
        bot.send_message(message.chat.id, "Ваш список был успешно сохранен в файле books.json")

    elif message.text == "Список фильмов":
        films.append("Матрица")
        films.append("Джокер")
        films.append("Начало")
        films.append("Область тьмы")
        films.append("Охотники за приведениями")
        bot.send_message(message.chat.id, "Вот список фильмов")
        bot.send_message(message.chat.id, ", ".join(films))
        with open("films.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(films, ensure_ascii=False))
        bot.send_message(message.chat.id, "Ваш список был успешно сохранен в файле films.json")

# @bot.message_handler(commands=['start']) #декоратор хз что это - связываем команду старт с ботом
# def start_message(message):
#     books.append("Над пропастью во ржи")
#     books.append("Чапаев и пустота")
#     books.append("Война и мир")
#     books.append("Заводной апельсин")
#     books.append("Мастер и Маргарита")
#     bot.send_message(message.chat.id,"Библиотека была загружена по умолчанию!")

# @bot.message_handler(commands=['all'])
# def show_all(message):
#     try:
#         bot.send_message(message.chat.id,"Вот список книг")
#         bot.send_message(message.chat.id, ", ".join(books))
#     except:
#         bot.send_message(message.chat.id, "Книг нема")
#
# @bot.message_handler(commands=['save'])
# def save_all(message):
#     with open("list.json", "w", encoding="utf-8") as fh:
#         fh.write(json.dumps(books, ensure_ascii=False))
#     bot.send_message(message.chat.id,"Ваш список был успешно сохранен в файле list.json")
#
@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = { 'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Что-то я ничего не нашел :-(")
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if "привет" in message.text.lower():
#         bot.send_message(message.chat.id, "Привет, я книжный бот и могу подсказать тебе список интересных книг:"
#                                           "- Для старта напиши /start"
#                                           "- Для просмотра списка книг напиши /all"
#                                           "- Для поиска в вики напиши /wiki")

bot.polling()
