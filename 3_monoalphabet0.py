# -*- coding: utf-8 -*-
import random
import operator

# частотный анализ текста
class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keytable):
        lowercase_code = {self.alphabet[i]:keytable[i] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():keytable[i].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}
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

#--- main -----

# частоты русских букв в виде словаря
# соберем и сравним с эталонной частотностью
#


RUSS = {'о':0.10983, 'е':0.08483, 'а':0.07998, 'и':0.07367, 'н':0.067, 'т':0.06318, 'с':0.05473, 'р':0.04746,
    'в':0.04533, 'л':0.04343, 'к':0.03486, 'м':0.03203, 'д':0.02977, 'п':0.02804, 'у':0.02615, 'я':0.02001,
    'ы':0.01898, 'ь':0.01735, 'г':0.01687, 'з':0.01641, 'б':0.01592, 'ч':0.0145, 'й':0.01208, 'х':0.00966,
    'ж':0.0094, 'ш':0.00718, 'ю':0.00639, 'ц':0.00486, 'щ':0.00361, 'э':0.00331, 'ф':0.00267, 'ъ':0.00037, 'ё':0.00013}

# посчитаем частоты для нашего шифротекста
freq = {key:0 for key in Monoalphabet.alphabet}
total_rus = 0

line = input()
while not line or line != '.':
    for char in line:
        if char.lower() in Monoalphabet.alphabet:
            freq[char.lower()]+=1
            total_rus += 1
    line = input()

# превратим счетчики в частоты
for k,v in freq.items():
    freq[k] =float(freq[k])/total_rus

# отсортируем по убыванию частот появления букв оба списка
sorted_rus = [k for k,v in sorted(RUSS.items(), key=operator.itemgetter(1), reverse=True)]
sorted_txt = [k for k,v in sorted(freq.items(), key=operator.itemgetter(1), reverse=True)]

# поставим в соответствие буквы из этих двух списков
alf = list(Monoalphabet.alphabet) # список из алфавита
key = list('.'*len(Monoalphabet.alphabet)) # здесь будет ключ
for i in range(len(alf)):
    key[alf.index(sorted_rus[i])] = sorted_txt[i]

# напечатаем алфавит и ключ
print( ''.join([c for c in Monoalphabet.alphabet]) )
print( ''.join([c for c in key]) )


# получилось так
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя
# йбоэшлкпсъхьвцычиюдазметгёфщняужр

# и применим этот ключ
# См. 3_monoalphabet2.py
# поправить строку
#  cipher = Monoalphabet("йбоэшлкпсъхьвцычиюдазметгёфщняужр")

# ничего хорошего не получилось - текст слишком мал!!!!

# посмотрим на текст. Если
#         ъ 1467 глсх
#Это
#         в 1467 году
#Если
#    Жйрв илойчорчъйыалэ ьчздац
#Это
#    Шифр полиалфавитной замены
# то согласно Частотности и получившегося соответствия  л-о д-е ч-а й-и а-н  -т  -с
# у нас есть небольшое смещение частот
# Посмотрим на текст еще раз. См. 3_monoalphabet1.py
