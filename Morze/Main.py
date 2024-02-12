
import Morze

if __name__ == '__main__':
    mode = 0

    # Выбор режима, пока не подана команда выход.
    while mode != 3:
        print("\nРежим работы:\n1) С вводом в консоль;\n2) С фалом;\n3) Выход.\n\nВвод: ", end='')
        try:
            mode = int(input())
        except:
            print("Неверный тип данных.")

        data = ''
        if mode == 1:
            print("Введите текст: ", end='')
            try:
                data = str(input())
            except:
                print("Неверный тип данных.")

        elif mode == 2:
            print("Введите путь к файлу: ", end='')
            try:
                filepath = str(input())
            except:
                print("Неверный тип данных.")

            file = open(filepath, 'r')
            try:
                data = file.read()
            finally:
                file.close()
        elif mode == 3:
            break
        
        # На случай, если будут сыпаться искючения или неверный ввод, отображать команды по-новой.
        while True:
            print("\nАлгоритм:\n1) Шифрование;\n2) Дешифрование.\n\nВвод: ", end='')
            try:
                mode = int(input())
            except:
                print("Неверный тип данных.")
            if mode == 1:
                data = Morze.Crypt(data)
            elif mode == 2:
                data = Morze.Decrypt(data)
            else:
                continue

            break
        
        # На случай, если снова будут сыпаться искючения или неверный ввод, отображать команды по-новой.
        while True:
            print("\nВывод данных:\n1) В консоль;\n2) В файл.\n\nВвод: ", end='')
            try:
                mode = int(input())
            except:
                print("Неверный тип данных.")

            if mode == 1:
                print("Обработанный текст: " + data)
            elif mode == 2:
                print("Введите путь к файлу: ", end='')
                try:
                    filepath = str(input())
                except:
                    print("Неверный тип данных.")

                file = open(filepath, 'w')
                try:
                    file.write(data)
                finally:
                    file.close()
            else:
                continue

            break