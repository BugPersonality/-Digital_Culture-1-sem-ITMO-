import codecs
import re

def find_mistake(word, dict_words):
    min_len = 10000
    max_req = 0
    word_correct = ""

    for word_in_dict, req in dict_words:
        if min_len > distance(word_in_dict, word):

            min_len = distance(word_in_dict, word)
            word_correct = word_in_dict
        if min_len == distance(word_in_dict, word):
            min_len = distance(word_in_dict, word)
            if max_req < int(req):
                word_correct = word_in_dict
                max_req = int(req)
    return [word, word_correct, min_len]

def distance(a, b):
    n, m = len(a), len(b)

    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)

    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

brain_in = codecs.open("brain", "r", "utf_8_sig")
brain_out = codecs.open("brain_out", "w", "utf_8_sig")
dict_in = codecs.open("dict1", "r", )

text = brain_in.read()
dict = []   #словарь
dict_0 = []   #словарь c элементами indx 0
dict_1 = []   #словарь c элементами indx 1

for i in range(4773):
    i = dict_in.readline().split()  #добавляю словарь в массив без частоты встречаемости
    dict.append(i)
    dict_0.append(i[0])
    dict_1.append(i[1])

#разделяю текст на слова, с маленькой буквы, без [! ? , ; . : « ( ) »]
split_words = list(map(lambda word: word.lower(),re.findall("\w+-\w+|\w+",text)))

print("словоформы в моем тексте : \n", len(split_words), file=brain_out)

#создаю массив уникальных символов
set_words = list(set(split_words))
print("кол-во разныx словоформ : \n", len(set_words), file=brain_out)

count = 0   #счетчик для словоформ присутствующи в словаре
for i in set_words:
    if i in dict_0:
        count += 1
print("кол-во словоформ присутствующих в словаре : \n", count, file=brain_out)

potential_mistakes = []     #потенциальные ошибки
for i in split_words:
    if i not in dict_0:
        potential_mistakes.append(i)
print("кол-во потенциальных ошибкок : \n", len(potential_mistakes), file=brain_out)

potential_mistakes_corrections = []
for i in potential_mistakes:
    buf = find_mistake(i, dict)
    if buf[0] == buf[1]:
        potential_mistakes_corrections.append([i, "не найдено", ">2"])
    else:
        potential_mistakes_corrections.append(buf)

print("редакторское расстояние для потенциальной ошибки до ближайшего слова : \n",
      potential_mistakes_corrections, file=brain_out)

new_words = []
for i in split_words:       #проверял отдельно тк не мог найти ошибку в коде с двумя for
    if i == 'укий':
        new_words.append('узкий')
    elif i == 'чеверохолмья':
        new_words.append('четверохолмья')
    elif i == 'близи':
        new_words.append('вблизи')
    elif i == 'именение':
        new_words.append('изменение')
    elif i == 'колличество':
        new_words.append('количество')
    elif i == 'интерсеной':
        new_words.append('интересной')
    elif i == 'подолжением':
        new_words.append('продолжением')
    else:
        new_words.append(i)

"""После поиска и исправления ошибок повторяю расчеты """
print("\n --- После поиска и исправления ошибок повторяю расчеты --- \n", file=brain_out)
print("словоформы в моем тексте : \n", len(new_words), file=brain_out)
print("кол-во разныx словоформ : \n", len(list(set(new_words))), file=brain_out)

set_new_words = list(set(new_words))
count = 0   #счетчик для словоформ присутствующи в словаре
for i in set_new_words:
    if i in dict_0:
        count += 1

print("кол-во словоформ присутствующих в словаре : \n", count, file=brain_out)
print("\n --- Потенциальные ошибки --- \n", file=brain_out)

for i in potential_mistakes_corrections:
    print(i[0], " - ", i[1], " - ", i[2], file=brain_out)

print(' '.join(map(str, new_words)))        #исправленныый текст