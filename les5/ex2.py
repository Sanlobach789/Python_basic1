f = open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task2.txt', 'r')
content = f.readlines()
line_count = len(content)
words = str(content).split(' ')
words_count = len(words)
print(content)
print("Количество строк в файле: " + str(line_count))
print("Количество слов в файле: " + str(words_count))
f.closed
