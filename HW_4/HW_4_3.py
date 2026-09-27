#Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты

f = open('file_HW_4_3.txt', 'r')
all_numbers = f.read().split()
f.close()

f = open('file_HW_4_3.txt', 'w')
for num in all_numbers:
    number = float(num)
    square = number ** 2
    f.write(f"{square}\n")

print(all_numbers)

f.close()