# Разработать программу для работы с цветами и букетами, используя
# принципы объектно-ориентированного программирования.
# Необходимо:
# ● Определить иерархию классов цветов и реализовать несколько
# различных видов цветов.
# ● Для каждого цветка предусмотреть основные характеристики: название,
# стоимость и время жизни.
# ● Реализовать возможность собирать букет из разных цветов.
# ● Добавить в букет возможность использования аксессуаров и учитывать
# их стоимость при расчете общей стоимости букета.
# ● Реализовать метод для определения общей стоимости букета.
# ● Определить время увядания букета на основании среднего времени
# жизни всех цветов, входящих в него.
# ● Реализовать возможность сортировки цветов в букете по стоимости.
# ● Реализовать возможность проверить, присутствует ли определённый
# цветок в букете.
# При выполнении задания использовать классы, наследование, композицию и
# методы объектов.

from dataclasses import dataclass

@dataclass
class Flower:
    name: str
    price: float
    lifetime: int

    def show(self):
        print(f'Цветок: {self.name}, стоимость: {self.price} руб., время жизни: {self.lifetime} дней')


@dataclass
class Rose(Flower):
    def __init__(self, price: float, lifetime: int):
        super().__init__(name='Роза', price=price, lifetime=lifetime)


@dataclass
class Lily(Flower):
    def __init__(self, price: float, lifetime: int):
        super().__init__(name='Лилия', price=price, lifetime=lifetime)


@dataclass
class Pion(Flower):
    def __init__(self, price: float, lifetime: int):
        super().__init__(name='Пион', price=price, lifetime=lifetime)


@dataclass
class Accessory:
    name: str
    price: float


@dataclass
class Lenta(Accessory):
    def __init__(self, price: float):
        super().__init__(name='Лента', price=price)


@dataclass
class Card(Accessory):
    def __init__(self, price: float):
        super().__init__(name='Открытка', price=price)


@dataclass
class Package(Accessory):
    def __init__(self, price: float):
        super().__init__(name='Крафтовая бумага', price=price)


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def calculate_total_price(self):
        total_flowers = sum(flower.price for flower in self.flowers)
        total_accessories = sum(acc.price for acc in self.accessories)
        return total_flowers + total_accessories

    def calculate_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_flowers_by_price(self):
        def get_price(flower):
            return flower.price

        self.flowers.sort(key=get_price)

    def has_flower(self, flower_name):
        result = False

        for flower in self.flowers:
            name_in_bouquet = flower.name.lower()
            name_to_find = flower_name.lower()

            if name_in_bouquet == name_to_find:
                result = True

        return result

    def show_bouquet(self):
        print("Цветы:")
        for f in self.flowers:
            print(f"  - {f.name}: {f.price} руб.")
        print("Аксессуары:")
        for a in self.accessories:
            print(f"  - {a.name}: {a.price} руб.")


rose = Rose(250.50, 5)
rose.show()

lily = Lily(150.20, 7)
lily.show()

pion = Pion(130.30, 8)
pion.show()

my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(lily)
my_bouquet.add_flower(pion)

my_bouquet.add_accessory(Package(120.00))
my_bouquet.add_accessory(Lenta(35.50))

my_bouquet.show_bouquet()

print(f"Общая стоимость букета: {my_bouquet.calculate_total_price()} руб.")

box = my_bouquet.calculate_lifespan()
print("Время увядания букета (среднее):", box, "дней")

search_name = "Лилия"
if my_bouquet.has_flower(search_name):
    print(f"Цветок '{search_name}' присутствует в букете.")
else:
    print(f"Цветка '{search_name}' в букете нет.")

my_bouquet.sort_flowers_by_price()
print("После сортировки цветов по возрастанию цены:")
for f in my_bouquet.flowers:
    print(f"  - {f.name}: {f.price} руб.")