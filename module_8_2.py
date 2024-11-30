def personal_sum(*numbers):
    data = 0
    incorrect_data = 0
    for a in numbers:
        for b in a:
            try:
                data += b
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {b}')
    return data, incorrect_data


def calculate_average(*numbers):
    try:
        sum_numbers = personal_sum(*numbers)
        return sum_numbers[0] / (len(*numbers) - sum_numbers[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
