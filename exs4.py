# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

frase = list(input('Введите фразу из нескольких строк с пробелами >>> '))
words = []
word = ''

for el in frase:
    word = word + el
words.append(word)

n_words = str(words[0])
m_words = n_words.split(' ')

for ind, el in enumerate(m_words, 1):
    print(f'{ind} {el[0:10]}')
