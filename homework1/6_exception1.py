"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
QUESTIONAIRE = {
      "Привет!": "Привет!",
      "Как дела?": "Хорошо!", 
      "Что делаешь?": "Программирую",
      "Какой смысл жизни?": "...42",
      "Какая погода?": "Приемлимая",
      "Как тебя зовут?": "Пиу-пиу",
      "Кто ты?": "Мыслитель",
      }

def ask_user_dict(user_question):
    if user_question in QUESTIONAIRE:
        print(QUESTIONAIRE[user_question])

    
def ask_user():
    while True:
        try:
            ask_user_dict(input())
        except KeyboardInterrupt:
            print("Пока!")
            break
    
if __name__ == "__main__":
    ask_user()
