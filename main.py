import csv
import matplotlib.pyplot as plt

FILENAME = 'example.txt'
CHARACTER_LIST = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є',
                  'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л',
                  'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                  'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю',
                  'я'
                  'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є',
                  'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л',
                  'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
                  'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю',
                  'Я', '.', '-', '?', '!', "'", '"', ',']
RESULT_DICT = {}


def checker_character_from_file():
    count = 0
    with open(FILENAME, 'r', encoding='utf-8') as file:
        reader = file.read()

    for character_item in CHARACTER_LIST:
        for reader_item in reader:
            if reader_item == character_item:
                count += 1
                RESULT_DICT[character_item] = count
        count = 0

    return RESULT_DICT


def average_all_symbol_form_file():
    all_character = checker_character_from_file()
    result_list = []
    for value in all_character.values():
        average = value / sum(all_character.values())
        result_list.append(average)
    return result_list


def creating_table():
    average = average_all_symbol_form_file()
    character = checker_character_from_file()

    with open('../table.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Символи', 'Ki', 'Pi'])
        value = character.values()
        value_list = []
        average_list = []
        for average_item in average:
            average_list.append(average_item)
        for value_item in value:
            value_list.append(value_item)
        count = 0
        for item in character:
            writer.writerow((item, value_list[count], average_list[count]))
            count += 1
    drawing_schedule()


def drawing_schedule():
    plt.title('Графік символів')
    plt.xlabel('Всі символи в тексті')
    plt.ylabel('Окремі символи в тексті')
    key = checker_character_from_file()
    sum_of_value = []
    for i in key.values():
        sum_of_value.append(i)
    x_list = key.keys()
    y_list = key.values()
    plt.bar(x_list, y_list)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    creating_table()



