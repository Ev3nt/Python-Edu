'''Main GUI file'''

import json
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import filedialog as fd
import crypto
import entropy

class MainWindow(tk.Tk):
    '''Main window class'''

    data = ''
    codes = ''
    r_var = None

    def __init__(self):
        super().__init__()

        button = tk.Button(self, text = "Открыть", command=self.load_text)
        button.pack()

        self.r_var = tk.BooleanVar() # переменная для отслеживания значения радиобатона
        self.r_var.set(True) # значение по умолчанию
        rb_1 = tk.Radiobutton(self, text='Кодирование', variable=self.r_var, value=True)
        rb_1.pack() # размещаем радиобатон в frame3 методом place
        rb_2 = tk.Radiobutton(self, text='Раскодирование', variable=self.r_var, value=False)
        rb_2.pack()

        button_exit = tk.Button(self, text="Выход", command=self.exit)
        button_exit.pack()

        self.bind("<Escape>", self.exit_callback)

    def load_text(self):
        '''Opening file'''
        file_name = fd.askopenfilename()
        try:
            mode = 'rb'
            encode = None
            if self.r_var.get():
                mode = 'r'
                encode = 'utf-8'

            with open(file_name, mode, encoding=encode) as file:
                self.data = file.read()
        except FileNotFoundError:
            return

        codes_file_name = fd.askopenfilename()
        try:
            with open(codes_file_name, 'r', encoding='utf-8') as file:
                self.codes = json.loads(file.read())
        except FileNotFoundError:
            return

        if self.r_var.get():
            source_size = len(self.data)
            [power, hartly, shennon, redundancy] = entropy.calc_entropy(self.data)
            [crypted, bits] = crypto.crypt(self.codes, self.data)
            result_size = len(crypted)
            avg_bits = bits / source_size

            showinfo(title="Информации о кодировании", message=f"\nИсходный размер: {source_size}\
                  \nРазмер зашифрованного файла: {result_size} \
                  \nМощность алфавита: {power} \
                  \nЭнтропия Хартли: {hartly} \
                  \nЭнтропия Шеннона: {shennon} \
                  \nИзбыточность алфавита: {redundancy} \
                  \nСреднее количество бит на символ: {avg_bits}")

            showinfo(title="Содержимое исходного файла", message=self.data)
            showinfo(title="Содержимое закодированного файла", message=crypted)

            self.data = crypted
        else:
            print(self.data)
            self.data = crypto.encrypt(self.codes, self.data)
            print(self.data)

        file_name = fd.asksaveasfilename()
        try:
            mode = 'w'
            encode = 'utf-8'
            if self.r_var.get():
                mode = 'wb'
                encode = None

            with open(file_name, mode, encoding=encode) as file:
                file.write(self.data)
        except FileNotFoundError:
            return

    def exit_callback(self, event):
        '''Exit key callback'''
        if event:
            self.exit()

    def exit(self):
        '''Exit window'''
        self.quit()

if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
