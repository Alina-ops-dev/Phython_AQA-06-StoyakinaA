#2. Создайте класс ATM, описывающий работу банкомата. Банкомат должен хранить количество
# купюр номиналом 20, 50 и 100. Начальное количество купюр каждого номинала передается
# при создании объекта через __init__().Реализуйте метод add_money(),
# позволяющий добавить в банкомат купюры каждого номинала. Также реализуйте
# метод withdraw(amount) для снятия указанной суммы. Метод должен определить,
# может ли банкомат выдать запрошенную сумму имеющимися купюрами. Если операция возможна,
# необходимо уменьшить количество купюр в банкомате, вывести, сколько купюр каждого номинала
# было выдано, и вернуть True. Если указанную сумму выдать невозможно — вернуть False и оставить
# содержимое банкомата без изменений. Создайте объект ATM, добавьте в него несколько купюр и
# выполните несколько операций снятия денег.

class ATM:
    def __init__(self, notes_20=0, notes_50=0, notes_100=0):
        self.notes_100 = notes_100
        self.notes_50 = notes_50
        self.notes_20 = notes_20

    def add_money(self, nominal, count):
        if count <= 0:
            print('Количество должно быть больше нуля')
            return False

        if nominal == 100:
            self.notes_100 = self.notes_100 + count
        elif nominal == 50:
            self.notes_50 = self.notes_50 + count
        elif nominal == 20:
            self.notes_20 = self.notes_20 + count
        else:
            print(f'Банкомат не принимает купюры по {nominal} руб.')
            return False

        print(f'Внесено: {count} шт. по {nominal} руб.')
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print('Некорректная сумма')
            return False

        old_100 = self.notes_100
        old_50 = self.notes_50
        old_20 = self.notes_20

        give_100 = 0
        give_50 = 0
        give_20 = 0

        while amount >= 100 and self.notes_100 > 0:
            amount = amount - 100
            self.notes_100 = self.notes_100 - 1
            give_100 = give_100 + 1

        if amount % 20 != 0 and amount >= 50 and self.notes_50 > 0:
            amount = amount - 50
            self.notes_50 = self.notes_50 - 1
            give_50 = give_50 + 1

        while amount >= 50 and self.notes_50 > 0:
            amount = amount - 50
            self.notes_50 = self.notes_50 - 1
            give_50 = give_50 + 1

        while amount >= 20 and self.notes_20 > 0:
            amount = amount - 20
            self.notes_20 = self.notes_20 - 1
            give_20 = give_20 + 1


        if amount != 0:
            self.notes_100 = old_100
            self.notes_50 = old_50
            self.notes_20 = old_20
            print('Невозможно выдать указанную сумму имеющимися купюрами')
            return False

        # Печатаем, сколько купюр каждого номинала выдано
        print('Выдано:')
        if give_100 > 0:
            print(f'100 руб. — {give_100} шт.')
        if give_50 > 0:
            print(f'50 руб.  — {give_50} шт.')
        if give_20 > 0:
            print(f'20 руб.  — {give_20} шт.')
        return True


atm = ATM(notes_20=2, notes_50=2, notes_100=2)

print('Внесение купюр')
atm.add_money(100, 5)
atm.add_money(20, 3)
print()

print(' Снятие 470 руб.')
atm.withdraw(470)
print()
print('Снятие 150 руб.')
atm.withdraw(150)
print()
print('Снятие 30 руб.')
atm.withdraw(30)
print()