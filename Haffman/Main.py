import Haffman
import os
import datetime
import json
import re

if __name__ == '__main__':
    mode = 0

    # Выбор режима, пока не подана команда выход.
    while mode != 3:
        print("\nРежим работы:\n1) С файлом;\n2) Удаление каталогов;\n3) Выход.\n\nВвод: ", end='')
        try:
            mode = int(input())
        except:
            print("\nНеверный тип данных.")

            continue

        if mode == 1:
            while True:
                file = None

                print("\nВведите путь к файлу: ", end='')
                try:
                    filepath = str(input())
                except:
                    print("\nНеверный тип данных.")
                    continue

                try:
                    file = open(filepath, 'r')
                    data = file.read()
                except:
                    print("Невозможно открыть файл!")
                    continue

                if file:
                    file.close()

                break

        elif mode == 2:
            dirs = os.listdir()

            for dir in dirs:
                if re.fullmatch('\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}', dir):
                    os.remove(dir+"\code.json")
                    os.removedirs(dir)

            continue

        elif mode == 3:
            break

        haffman = Haffman.Haffman(data)
        codes = haffman.get_codes()

        folder = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        if not os.path.isdir(folder):
            os.mkdir(folder)

        file = open(folder + "/code.json", 'w')
        json.dump(codes, file)
        file.close()