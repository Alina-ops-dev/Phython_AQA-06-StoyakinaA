#Дан файл целых чисел. Создать два новых файла, первый из которых
#содержит четные числа из исходного файла, а второй — нечетные (в том
#же порядке). Если четные или нечетные числа в исходном файле
#отсутствуют, то соответствующий результирующий файл оставить пустым.

f_source = open('file_HW_4_2.txt', 'r')
all_numbers = f_source.read().split()
f_source.close()

f_even = open('file_HW_4_2_(1).txt', 'w')
f_odd = open('file_HW_4_2_(2).txt', 'w')

for num in all_numbers:
    num = int(num)
    if num % 2 == 0:
        f_even.write(f"{num}\n")
    else:
        f_odd.write(f"{num}\n")
        print(num)

f_even.close()
f_odd.close()