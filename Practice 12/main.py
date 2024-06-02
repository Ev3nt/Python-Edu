'''Main script file'''

from crypto import Crypt
import requests
import time

if __name__ == "__main__":
    caesar = Crypt()

    while True:
        try:
            mode = int(input("\nРежим работы:\n1) Брутфорс атака\n2) Выход.\n\nВвод: "))
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        if mode == 2:
            caesar.__del__()

            break

        if mode != 1:
            continue

        m = str(input("Введите текст: "))
        try:
            n = int(input("Введите мощность для перебора: "))
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        try:   
            with open('dictionary.txt', encoding='utf-8') as dictionary:
                text = dictionary.read()
        except FileNotFoundError:
            response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
            text = response.content.decode('cp1251')

            response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
            text += response.content.decode('cp1251')

            with open('dictionary.txt', 'wb') as dictionary:
                dictionary.write(text.lower().encode("utf-8"))
        
        dictionary = text.split()

        start = time.time()

        # Hello, world - ìĉĐĐēÐÄěēĖĐĈ
        bruted = caesar.brute(m, n)

        count = 0
        with open("options.txt", 'wb') as options:
            for (sentence, n) in bruted:
                letters = ".,!?:-+=/\\&8$#@%^*()[{]}"
                words = sentence

                for char in letters:
                    words = words.replace(char, '')

                words = words.split()
                size = len(words)

                for word in words:
                    if dictionary.count(word.lower()):
                        size -= 1

                if size == 0:
                    options.write((str(n) + ' : ' + sentence).encode('utf-8'))
                    count += 1
                    
        elapsed = time.time() - start

        print('\nБыло обнаружено ключей: ' + str(count))
        print('Затраченное время: ' + str(elapsed) + ' секунд')

