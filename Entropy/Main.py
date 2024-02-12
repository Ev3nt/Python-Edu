import Entropy

if __name__ == '__main__':
    mode = 0

    # Выбор режима, пока не подана команда выход.
    while mode != 2:
        print("\nРежим работы:\n1) С фалом;\n2) Выход.\n\nВвод: ", end='')
        try:
            mode = int(input())
        except:
            print("Неверный тип данных.")

        if mode == 1:
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
        elif mode == 2:
            break

        [power, Hartly, Shennon, redundancy] = Entropy.CalcEntropy(data)

        print(f"\nМощность алфавита: {power}\nЭнтропия Хартли: {Hartly}\nЭнтропия Шеннона: {Shennon}\nИзбыточность алфавита: {redundancy}\n")