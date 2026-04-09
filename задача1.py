text = input("Введите слова через пробел: ")
words = text.split()
words2 = []

for i in words:
    if len(i) % 2 == 0:
        words2.append(i)

print(" ".join(words2))