# -*- coding: utf-8 -*-
import random

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

# Итак, после частотного анализа есть ключ "йбоэшлкпсъхьвцычиюдазметгёфщняужр"
                      для алфавита         "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# И с ним текст не удалось вскрыть
# Из-за того, что текст мал и частоты несколько иные, чем в больших литературных текстах

# Проанализируем текст (википедия по теме Криптография нам в помощь)
# есть первые предположения
#         Жйрв Ъйедадвч                     
#         Шифр Виженера                     
# Жйрв Ъдвачзч (лсалвчьлъцэ нолшалы)
# Шифр Вернама (одноразовый блокнот) 
#        Ивйздвц илойчорчъйыацф жйрвлъ
#        Примеры полиалфавитных шифров
#      адздбшйэ чннчы
#      немецкий аббат

alf = list(Monoalphabet.alphabet)
key = list('.'*len(Monoalphabet.alphabet))

# проверим наши предположения
coded  = ['ъ 1467 глсх','Жйрв илойчорчъйыалэ ьчздац','Жйрв Ъйедадвч',
          'Жйрв Ъдвачзч (лсалвчьлъцэ нолшалы)','адздбшйэ чннчы','Ивйздвц илойчорчъйыацф жйрвлъ']
opened = ['в 1467 году','Шифр полиалфавитной замены','Шифр Виженера',
          'Шифр Вернама (одноразовый блокнот)','немецкий аббат','Примеры полиалфавитных шифров']

# подставим известные замены
for i in range(len(coded)):
    opn = opened[i].lower()
    sfr = coded[i].lower()
    for j in range(len(opn)):
        if opn[j] in alf:
            key[alf.index(opn[j])] = sfr[j]


# напечатаем алфавит и ключ
print( ''.join([c for c in alf]) )
print( ''.join([c for c in key]) )
# получилось так
# "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# "чнъгсд.еьйэшозалив.ыхр.б.ж..ц...."

# применим этот частичный ключ
k = ''.join([char for char in key])
cipher = Monoalphabet(k)
line = input()
while not line or line != '.':
    print(cipher.decode(line))
    line = input()
# получился вполне читаемый текст

# А потом сайт обновили и стало совсем не интересно
# Потому что в расшифрованном тексте есть такие строки

# class Vigenere:
#    alphabet = "абвгдемжзийклмнопрютуфхцпшщтыякуё"
# должно быть   "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#частичный ключ "чнъгсд.еьйэшозалив.ыхр.б.ж..ц...."
#заменим        "чнъгсдмеьйэшозаливюыхрфбпжщтцякуё"
#            символ "ф" в ключе нашли методом исключения
# и применим этот ключ
# См. 3_monoalphabet2.py

