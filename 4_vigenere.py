# -*- coding: utf-8 -*-

class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        # словарь для нахождения номера буквы в алфавите
        self.alphaindex = {self.alphabet[index]: index for index in range(len(self.alphabet))}
        # вместо символов список номеров символов из ключевого слова
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    # алгоритм Цезаря со сдвигом shift
    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # заглавная буква
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line, key = None):
        if not key:
            key = self.key
        ciphertext = []
        i = 0
        for letter in line:
            shift = key[i]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
            i = (i + 1)%len(key)

        return ''.join(ciphertext)

    def decode(self, line): # процедура дешифрования
        # почти ничем не отличается от шифрования
        ciphertext = []
        i = 0
        for letter in line:
            shift = self.key[i]
            cipherletter = self.caesar(letter, -shift)
            ciphertext.append(cipherletter)
            i = (i + 1)%len(self.key)

        return ''.join(ciphertext)




# по открытому тексту line и соответствующему шифрованному code 
# и длине ключа keyword_len вычисляет ключ
def find_keyword(line,code, keyword_len):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphaindex = {alphabet[index]: index for index in range(len(alphabet))}

    keyword = [0]*len(line) # полезны будут только позиции где есть русские буквы
    final_keyword = [0]*keyword_len # итоговый ключ
    # другие буквы, пробелы и символы не шифруются и ключ не вычисляют
    # вычислим для каждой позиции, а первые keyword_len позиций будем уточнять каждый раз

    for i in range(len(line)):
        letter=line[i]
        cod_letter = code[i]
        if letter in alphaindex:  # строчная буква
            index = (alphaindex[cod_letter] - alphaindex[letter] )%len(alphabet)
            if final_keyword[i%keyword_len] == 0:
                final_keyword[i%keyword_len] = index
            keyword[i] = index # это только для иллюстрации
        elif letter.lower() in alphaindex:  # заглавная буква
            index = (alphaindex[cod_letter.lower()] - alphaindex[letter.lower()] )%len(alphabet)
            if final_keyword[i%keyword_len] == 0:
                final_keyword[i%keyword_len] = index
            keyword[i] = index
    return final_keyword, keyword

# --- main ------------------

# Штирлиц пользовался самой стойкой криптографией - доставал из шкафа книгу 
# и открывал каждый раз на другой странице (Он и книги мог брать разные)
# Наша версия - текст начинается со слов "Шифр Вернама (одноразовый блокнот)"

line = "Шифр Вернама (одноразовый блокнот)"
code = "Йыгь Оеюятыл (осябялуывиы пчъчньд)"
# №     1234567812345678123456781234567812
# Есть буква "н" 2 раза в позиции 1 
# и буква "а" 2 раза в позиции 4
# при длине ключа 8 шифрокоды одинаковые -
# значит длина ключа на самом деле 8
# в каждой позиции когда-нибудь найдется русская буква - значит все позиции ключа вычислимы

keyword_len = 8
# найдем ключ
print("------------- ПОИСК КЛЮЧА ------------------------")
(final_keycode, keycode) = find_keyword(line, code, keyword_len)
for i in range(int(len(keycode)/keyword_len+1)):
    print(keycode[i*keyword_len:(i+1)*keyword_len])
print(final_keycode) # ключ который собрался за несколько расшифрований
# а попробуем собрать слово из этих кодов
keyword=''
for i in range(keyword_len):
   keyword+=Vigenere.alphabet[final_keycode[i]]
print(keyword)

# получился такой результат
#[18, 19, 15, 12, 0, 13, 0, 14]
#[18, 19, 15, 12, 0, 0, 0, 14]
#[18, 19, 15, 12, 12, 13, 0, 14]
#[18, 0, 15, 12, 12, 13, 0, 14]
#[18, 0]
#[18, 19, 15, 12, 12, 13, 0, 14]
#столлман

print("------------- РАСШИФРОВКА ТЕКСТА ------------------------")
# теперь можем расшифровать текст (его можно подать на вход через оператор <имя_файла.txt)
cipher = Vigenere(keyword)

line = input()
while not line or line != '.':  # если встретим "." в начале строки - остановимся
    print(cipher.decode(line))
    line = input()




