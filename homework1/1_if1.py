"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_responsibility(person_age):
    responsibility = ""
    if 2 < person_age < 6:
        responsibility = "Вам нужно быть в саду"
    elif 5 < person_age < 18:
        responsibility = "Вы должны учиться в школе"
    elif 17 < person_age < 23:
        responsibility = "Вы дожны учиться в ВУЗе"
    elif 22 < person_age < 71:
        responsibility = "Вам нужно работать"
    else:
        responsibility = "Род занятий не определен. Вы или слишком молоды или уже в преклонном возрасте"

    return responsibility

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = input("Please enter your age: ")
    user_responsibility = get_responsibility(int(user_age))
    print(user_responsibility)

if __name__ == "__main__":
    main()
