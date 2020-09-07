"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def ask_user_dict(questionaire):
    
    user_question = input()

    if user_question in questionaire:
        print(questionaire[user_question])

    
def ask_user():
    questionaire = {
        "Привет!": "Привет!",
        "Как дела?": "Хорошо!", 
        "Что делаешь?": "Программирую",
        "Какой смысл жизни?": "...42",
        "Какая погода?": "Приемлимая",
        "Как тебя зовут?": "Пиу-пиу",
        "Кто ты?": "Мыслитель",
        }

    while True:
        try:
            ask_user_dict(questionaire)
        except(KeyboardInterrupt):
            print("Пока!")
            break

    
if __name__ == "__main__":
    ask_user()
