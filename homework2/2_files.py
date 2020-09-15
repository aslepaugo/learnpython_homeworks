"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке
    https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную,
   подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import os


def main():

    if not os.path.exists('referat.txt'):
        print("Download file from url https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0")
        print("and place with this script")
        return

    with open(r'referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    print('String lenght: {}'.format(len(content)))
    print('Words count: {}'.format(len(content.split(" "))))
    content = content.replace(".", "!")

    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    main()
