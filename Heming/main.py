"""Beginning of Heming's algotrithm."""

import crypto
import haffman
import heming

if __name__ == "__main__":
    while True:
        print("\nРежим работы:\n1) С текстом;\n2) Выход.\n\nВвод: ", end='')
        try:
            mode = int(input())
        except ValueError:
            print("\nНеверный тип данных.")

            continue

        if mode == 2:
            break

        print("Введите текст: ", end='')
        text = input()
        source_lenght = len(text)

        codes = haffman.Haffman(text).get_codes()
        crypted = crypto.crypt(codes, text)

        hem = heming.Heming()

        crypted = hem.code(crypted, 1)
        noised = hem.noise(crypted, 2)
        encrypted = hem.code(noised, 0)
        encrypted = crypto.encrypt(codes, encrypted)[:source_lenght]

        if text != encrypted:
            print("Было найдено более 1-й ошибки!")

        print(f"Расшифрованное сообщение: {encrypted}")
