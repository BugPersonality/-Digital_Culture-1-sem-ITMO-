import cv2
import math

def bin_code(number):   #считает количество ддвоичных знаков в числе
    number = bin(number)
    return len(number[2:])

image = cv2.imread("bmpimg.bmp.bmp")
out = open("count", "w")

Ftree = []      #Массив для Шеннона-Фано
binary_uniform_one_character_code = []      # двоичный равномерный односимвольный код
middle_len_bincode = 0  #длина средней длины двоичного кода
entropy = 0   #энтропия
middle_line = len(image) // 2   #номер средней строки
middle = []    #массив для средней строки
unique = []    #массив для уникальных эллементво из middle
unique_count = []   #массив для колличества символов из unique в middle
unique_frequency = []   #массив для частоты встречаемости символов из unique в middle
unique_len = len(unique)     #колличество эллементов в unique


for i in image[middle_line]:
    middle.append(i[0])   #заношу в массив средню строку
print("middle line:\n", middle, file=out)

for i in range(len(middle) - 1):
    middle[i] = int(round(middle[i] / 20) * 20)   #квантование среденей строки
print("middle line after quantization:\n", middle, file=out)

unique = list(set(middle))      #заношу в массив все уникальные эллементы
print("unique characters:\n", unique, file=out)

unique_len = len(unique)   #считаю количество уникальных символов
print("unique len:\n", unique_len, file=out)

for i in unique:
    unique_count.append([middle.count(i), i])  #считаю как часто уникальный символ встречается в middle
print("unique count:\n", unique_count, file=out)

for i in unique:
    unique_frequency.append([middle.count(i) / len(middle), i])     #считаю частоту встречаемости уникального символа в middle
unique_frequency = list(reversed(sorted(unique_frequency)))
print("unique frequency:\n", unique_frequency, file=out)

for i in range(12):    #считаю энтропию
    entropy += unique_frequency[i][0] * math.log(unique_frequency[i][0], 2)
entropy = entropy * (-1)
print("entropy:\n", entropy, file=out)

for i in range(13):     #определяю среднюю минимальную длину двоичного кода
    middle_len_bincode += bin_code(i)
middle_len_bincode = middle_len_bincode // 12
print("middle len bincode:\n", middle_len_bincode, file=out)

for i in range(12):
    if len(bin(i)[2:]) == 1:
        buff = "000" + str(bin(i)[2:])
        binary_uniform_one_character_code.append([buff, unique[i - 1]])
    if len(bin(i)[2:]) == 2:
        buff = "00" + str(bin(i)[2:])
        binary_uniform_one_character_code.append([buff, unique[i - 1]])
    if len(bin(i)[2:]) == 3:
        buff = "0" + str(bin(i)[2:])
        binary_uniform_one_character_code.append([buff, unique[i - 1]])
    if len(bin(i)[2:]) == 4:
        buff = str(bin(i)[2:])
        binary_uniform_one_character_code.append([buff, unique[i - 1]])
print("binary uniform one character code: \n", binary_uniform_one_character_code, file=out)

'''
new_unique = []
for i in range(12):
    new_unique.append(unique_frequency[i][1])   #Получил массив отсортированных уникальных элементво по частотам
print(new_unique)

print(list(reversed(sorted(unique_count)))) #вывел значение unique отсортированные по количеству встречаемости
'''



