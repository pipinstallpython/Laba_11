#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime


def get_person():
    """"
    Запросить данные о человеке.
    """
    name = input("Фамилия Имя: ")
    number = int(input("Номер телефона: "))
    bday = list(map(int, input("Дата рождения: ").split('.')))
    d_bday = datetime.date(bday[2], bday[1], bday[0])

    # Создать словарь.
    return {
        'name': name,
        'number': number,
        'birthday': d_bday,
    }


def display_people(staff):
    """
    Список данных о людях.
    """
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 14
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^14} |'.format(
                "№",
                "Фамилия Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех людях.
        for idx, person in enumerate(staff, 1):
            print(
                f'| {idx:>4} |'
                f' {person.get("name", ""):<30} |'
                f' {person.get("number", 0):<20} |'
                f' {person.get("birthday")}      |'
            )
        print(line)

    else:
        print("Список людей пуст.")


def find_nomer(staff, nomer):
    """
    Выбрать людей с заданным номером телефона.
    """
    # Сформировать список людей.
    result = []

    for n in staff:
        if nomer in n.values():
            result.append(n)

    # Проверка на наличие записей
    if len(result) == 0:
        return print("Запись не найдена")

    # Возвратить список выбранных людей.
    return result


def main():
    """
    Главная функция программы.
    """
    # Список людей.
    people = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input("Введите команду >>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            person = get_person()

            # Добавить в словарь список.
            people.append(person)
            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('d_bday', ''))

        elif command == 'list':
            # Отобразить всех людей.
            display_people(people)

        elif command == 'find':
            n = int(input('Введите номер телефона: '))

            # Выбрать людей с заданной фамилией.
            finded = find_nomer(people, n)
            # Отобразить выбранных работников.
            display_people(finded)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n"
                  "add - добавить человека;\n"
                  "list - вывести список людей;\n"
                  "find - найти человека по фамилии;\n"
                  "help - отобразить справку;\n"
                  "exit - завершить работу с программой.\n")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()