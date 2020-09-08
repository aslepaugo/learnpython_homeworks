"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string_comparator(first_string, second_string):
    if type(first_string) is not str or type(second_string) is not str:
        return 0
    if first_string == second_string:
        return 1   
    if len(first_string) > len(second_string):
        return 2
    if second_string == 'learn':
        return 3

def main():
    #Not a string:
    assert string_comparator(1, 2) == 0
    assert string_comparator(1, 'string') == 0
    assert string_comparator('string', 2) == 0
    #Equal strings
    assert string_comparator('string', 'string') == 1
    #Equal by len but not by content (None)
    assert string_comparator('string', 'strong') == None
    #frist string len is higher but second is 'learn'
    assert string_comparator('string', 'learn') == 2
    #first string len is higher and second is not 'learn'
    assert string_comparator('string_string', 'string') == 2
    #second string len is higher
    assert string_comparator('string', 'string_string') == None
    #second string len is higher but it's 'learn'
    assert string_comparator('one', 'learn') == 3

    
if __name__ == "__main__":
    main()
