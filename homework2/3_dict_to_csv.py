"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name,
   age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def mock_dictionary():
    return [
        {'name': 'Gloria', 'age': 23, 'job': 'Juniot Specialist'},
        {'name': 'Filip', 'age': 32, 'job': 'Supervisor'},
        {'name': 'Jane', 'age': 34, 'job': 'CEO'},
        {'name': 'Oskar', 'age': 43, 'job': 'CFO'},
        {'name': 'Timathy', 'age': 34, 'job': 'Solution Architect'},
        {'name': 'Luca', 'age': 41, 'job': 'Software Engineer'},
        {'name': 'Zosja', 'age': 20, 'job': 'Recruiter'},
        {'name': 'Eliash', 'age': 29, 'job': 'Head of Unit'},
    ]


def main():
    people = mock_dictionary()
    dialect = csv.excel
    dialect.delimiter = ";"
    with open('export_people.csv', 'w', encoding='utf-8', newline='') as f:
        fields = people[0].keys()
        writer = csv.DictWriter(f, fields, dialect=dialect)

        writer.writeheader()
        writer.writerows(people)


if __name__ == "__main__":
    main()
