# -*- coding: utf-8 -*-
import random


class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}  # FIXME
        lowercase_decode = {keytable[i]:self.alphabet[i] for i in range(len(keytable))}
        uppercase_decode = {keytable[i].upper():self.alphabet[i].upper() for i in range(len(keytable))}
        self._decode = dict(lowercase_decode)
        self._decode.update(uppercase_decode)



    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])
#--- main ----
# См. 3_monoalphabet0.py
# Попытка частотного анализа
# cipher = Monoalphabet("йбоэшлкпсъхьвцычиюдазметгёфщняужр")
# c таким ключом все плохо

# См. 3_monoalphabet1.py
# получился вполне читаемый текст
# в котором есть строки

# class Vigenere:
#    alphabet = "абвгдемжзийклмнопрютуфхцпшщтыякуё"

# должно быть   "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#частичный ключ "чнъгсд.еьйэшозалив.ыхр.б.ж..ц...."
#заменим        "чнъгсдмеьйэшозаливюыхрфбпжщтцякуё"
# и применим этот ключ

cipher = Monoalphabet("чнъгсдмеьйэшозаливюыхрфбпжщтцякуё")


line = input()
while not line or line != '.':
    print(cipher.decode(line))
    line = input()

