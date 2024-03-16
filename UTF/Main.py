import json
import UTF
import Entropy

if __name__ == '__main__':
    mode = 0

    # Выбор режима, пока не подана команда выход.
    while mode != 2:
        print("\nРежим работы:\n1) С файлом;\n2) Выход.\n\nВвод: ", end='')
        try:
            mode = int(input())
        except:
            print("\nНеверный тип данных.")

            continue

        if mode == 1:
            while True:
                file = None

                print("\nВведите путь к коду Хаффмана: ", end='')
                try:
                    filepath = str(input())
                except:
                    print("\nНеверный тип данных.")
                    continue

                try:
                    file = open(filepath, 'r')
                    codes = json.loads(file.read())

                except:
                    print("Невозможно открыть файл!")
                    continue

                if file:
                    file.close()

                break

        elif mode == 2:
            break

        while True:
            print("\nРежим работы:\n1) Шифрование;\n2) Дешифрование.\n\nВвод: ", end='')
            try:
                mode = int(input())
            except:
                print("\nНеверный тип данных.")

                continue

            if mode == 1 or mode == 2:
                break

        print("\nВведите путь к сообщению: ", end='')
        try:
            filepath = str(input())
        except:
            print("\nНеверный тип данных.")
            continue

        try:
            if mode == 1:
                file = open(filepath, 'r')
            else:
                file = open(filepath, 'rb')

            data = file.read()
        except:
            print("Невозможно открыть файл!")
            continue

        if file:
            file.close()

        resultSize = None
        sourceSize = len(data)
        [power, Hartly, Shennon, redundancy] = Entropy.CalcEntropy(data)

        if mode == 1:
            [data, bits] = UTF.Crypt(codes, data)
            avgBits = bits / sourceSize

            resultSize = len(data)
        elif mode == 2:
            data = UTF.Decrypt(codes, data)

        while True:
            file = None

            print("\nВведите название файла: ", end='')
            try:
                filepath = str(input())
            except:
                print("\nНеверный тип данных.")
                continue

            try:
                if mode == 1:
                    file = open(filepath, 'wb')
                else:
                    file = open(filepath, 'w')

                    while True:
                        print("\nВведите количество байт: ", end='')
                        try:
                            bytes = int(input())
                        except:
                            print("\nНеверный тип данных.")
                            continue

                        break

                    data = data[0:bytes]
                    

                file.write(data)
            except:
                print("Невозможно сохранить файл!")
                continue

            if file:
                file.close()

            break
        
        if resultSize != None:
            print(f"\nИсходный размер: {sourceSize}\nРазмер зашифрованного файла: {resultSize}\nМощность алфавита: {power}\nЭнтропия Хартли: {Hartly}\nЭнтропия Шеннона: {Shennon}\nИзбыточность алфавита: {redundancy}\nСреднее количество бит на символ: {avgBits}")
        
        mode = None