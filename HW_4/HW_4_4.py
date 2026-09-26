#Даны два файла произвольного типа. Поменять местами их содержимое.Файлы должны быть
# бинарного типа.


f = open('file_HW_4_4_(1).json', 'r')
content_a = f.read()

f.close()

f = open('file_HW_4_4_(2).txt', 'r')
content_b = f.read()

f.close()

f = open('file_HW_4_4_(1).json', 'w')
f.write(content_b)

f.close()

f = open('file_HW_4_4_(2).txt', 'w')
f.write(content_a)

f.close()


