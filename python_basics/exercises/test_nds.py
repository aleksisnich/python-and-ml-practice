def CalcPrices(InputPriceWithNDS: float, ProcNDS: int, max_steps: int = 100):

    # Переводим входную цену с НДС в целые копейки
    input_with_nds_cents = int(InputPriceWithNDS * 100 + 0.5)

    best = None  # сохраняем лучший вариант

    # Перебираем кандидатов вокруг входного значения
    for step in range(max_steps + 1):
        for candidate_cents in [input_with_nds_cents - step, input_with_nds_cents + step]:
            if candidate_cents <= 0:
                continue  # цены не могут быть <= 0

            # Вычисляем цену без НДС
            without_num = candidate_cents * 100
            without_den = 100 + ProcNDS

            # Проверка, что без НДС получится ровно два знака после запятой
            if without_num % without_den == 0:
                without_cents = without_num // without_den

                # Разница с исходной ценой
                diff = abs(candidate_cents - input_with_nds_cents)

                # Сохраняем лучший вариант
                if best is None or diff < best[0]:
                    best = (diff, candidate_cents, without_cents)

                    if diff == 0:  # нашли точное совпадение
                        break
        if best is not None and best[0] == 0:
            break

    if best:
        # Переводим обратно в рубли
        CorrectedPriceWithNDS = best[1] / 100
        CorrectedPriceWithoutNDS = best[2] / 100
        return CorrectedPriceWithNDS, CorrectedPriceWithoutNDS
    else:
        return None, None

# Выводим наш результат:
def print_test(InputPriceWithNDS, ProcNDS):
    with_nds, without_nds = CalcPrices(InputPriceWithNDS, ProcNDS)

    print(f"InputPriceWithNDS = {InputPriceWithNDS:.10g}, ProcNDS = {ProcNDS}%")
    print(f"CorrectedPriceWithNDS = {with_nds:.10g}")
    print(f"CorrectedPriceWithoutNDS = {without_nds:.10g}")
    print(f"Разница с исходной ценой = {abs(InputPriceWithNDS - with_nds):.10g}")
    print("-" * 40)

# Примеры
print_test(1.81, 20)
print_test(1.81, 18)
print_test(1.83, 15)
print_test(123.4567, 15)
print_test(0.99, 5)
