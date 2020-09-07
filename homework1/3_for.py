"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def average_score_report(school):
    school_scores = []
    for school_class in school:
        school_scores += school_class['scores']
        print("В классе {} средний балл {:.2f}".format(school_class['school_class'], sum(school_class['scores']) / len(school_class['scores'])))
    print('-' * 32)
    print("В школе средний бал {:.2f}".format(sum(school_scores) / len(school_scores)))


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [
        {'school_class': '4а', 'scores': [3,4,5,2,3,4,5,4,3,4,3,3,4,5,3,2,3,4,5,3]},
        {'school_class': '4б', 'scores': [4,3,3,3,4,4,5,5,4,3,2,3,4,4,3,3,4,4,5,5]},
        {'school_class': '4в', 'scores': [3,3,3,4,4,4,5,5,5,4,4,3,4,3,3,2,2,3,4,4]},
        {'school_class': '5а', 'scores': [4,5,4,5,4,4,4,5,5,5,4,3,3,4,5,5,5,4,3,3]},
        {'school_class': '5б', 'scores': [4,4,4,4,4,4,5,5,5,4,4,5,4,4,3,4,5,4,5,4]},
        {'school_class': '5в', 'scores': [3,4,5,4,3,3,3,4,4,5,4,4,3,3,3,4,4,5,4,3]},
    ]

    average_score_report(school)
    
if __name__ == "__main__":
    main()
