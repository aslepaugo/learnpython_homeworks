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
    else: 
        if second_string == 'learn':
            return 3
        if len(first_string) > len(second_string):
            return 2


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #Not a string:
    print(string_comparator(1, 2)) 
    print(string_comparator(1, 'string')) 
    print(string_comparator('string', 2)) 
    #Equal strings
    print(string_comparator('string', 'string'))
    #Equal by len but not by content (None)
    print(string_comparator('string', 'strong'))
    #frist string len is higher but second is 'learn'
    print(string_comparator('string', 'learn'))
    #first string len is higher and second is not 'learn'
    print(string_comparator('string_string', 'string'))   
    #second string len is higher
    print(string_comparator('string', 'string_string'))
    #second string len is higher but it's 'learn'
    print(string_comparator('one', 'learn'))  

    
if __name__ == "__main__":
    main()
