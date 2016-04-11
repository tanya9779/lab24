﻿__author__ = 'Timofey Khirianov'
# -*- coding: utf-8 -*-


class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)

        lowercase_decode = {self.alphabet[i]:self.alphabet[(i-key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_decode = {self.alphabet[i].upper():self.alphabet[(i-key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._decode = dict(lowercase_decode)  
        self._decode.update(uppercase_decode)
        # FIXME

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        pass  # FIXME
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])


#key = int(input('Введите ключ:'))
key = 17
cipher = Caesar(key)
line = input()
while line != '.':
#    print(cipher.encode(line))
    print(cipher.decode(line))
    line = input()

