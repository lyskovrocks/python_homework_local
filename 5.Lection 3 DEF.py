"""
Задние

Сделать функцию, которая определяет квадрат или нет
Дополнительно.
Сделать функцию, которая находит слово в строке и удаляет его, возвращает строку без слова
"""

# print(isSquare(25)) # True
# print(isSquare(30)) # False


# Дополнительно
# print(find_word('Строка для поиска слова и его удаления', 'слова'))
# Строка для поиска и его удаления

def isSquare(x):
  if (x ** 0.5).is_integer():
    return True
  else:
      return False
print(isSquare(11))


def find_word(sentence, word):
    new_sentence = sentence.split(' ')
    if word in new_sentence:
        new_sentence.pop(new_sentence.index(word))
        new_sentence = ' '.join(new_sentence)
    return new_sentence

print(find_word('Строка для поиска слова и его удаления','слова'))
