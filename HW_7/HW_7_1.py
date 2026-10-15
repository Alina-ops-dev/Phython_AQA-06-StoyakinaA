#1. Создайте класс CreditCard, описывающий кредитную карту. При создании объекта
#необходимо передавать номер счёта и начальный баланс карты. Реализуйте метод deposit(amount),
# который пополняет баланс на указанную сумму, метод withdraw(amount), который снимает указанную сумму,
# и метод show_info(), который выводит номер счёта и текущий баланс.
# Создайте три объекта класса CreditCard с разными номерами счетов и начальными балансами.
# Пополните баланс первой и второй карты, а с третьей карты снимите некоторую сумму.
# После выполнения операций выведите информацию о состоянии всех трёх карт.

class CreditCard:
    def __init__(self, card_number, initial_balance):
        self.card_number = card_number
        self.initial_balance = initial_balance

    # пополняет баланс на указанную сумму
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self.initial_balance += amount

    # снимает указанную сумму
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Сумма снятия не может быть ниже нуля')
        if amount > self.initial_balance:
            raise ValueError('Недостаточно средств')
        self.initial_balance -= amount

    # выводит номер счёта и текущий баланс
    def show_info(self):
        print(f'Счет №: {self.card_number} | Текущий баланс: {self.initial_balance} руб.')


credit_card1 = CreditCard('123-45-6789', 100000)
credit_card2 = CreditCard('987-65-4321', 0)
credit_card3 = CreditCard('158-00-1782', 800)

credit_card1.deposit(5000)
credit_card2.deposit(1500)
credit_card3.withdraw(300)

print('Состояние карт:')
credit_card1.show_info()
credit_card2.show_info()
credit_card3.show_info()