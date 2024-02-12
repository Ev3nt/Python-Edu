import Entropy

if __name__ == '__main__':
    mode = 0

    # Выбор режима, пока не подана команда выход.
    while mode != 2:
        print("\nРежим работы:\n1) С фалом;\n2) Выход.\n\nВвод: ", end='')
        try:
            mode = int(input())
        except:
            print("\nНеверный тип данных.")

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
            break

        [power, Hartly, Shennon, redundancy] = Entropy.CalcEntropy(data)

        print(f"\nМощность алфавита: {power}\nЭнтропия Хартли: {Hartly}\nЭнтропия Шеннона: {Shennon}\nИзбыточность алфавита: {redundancy}\n")