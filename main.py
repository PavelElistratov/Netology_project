# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Goose:
    pass


Серый = Goose()
Серый.name = 'Серый'
Серый.weight = 10
print(Серый.name)
print(Серый.weight)

Белый = Goose()
Белый.name = 'Белый'
Белый.weight = 15
print(Белый.name)
print(Белый.weight)


class Cow:
    def __init__(self):  # действия при создании экземпляра класса
        self.name = 'Unnemed'
        self.weight = 0


Манька = Cow()
print(Манька.name)
Манька.total = 200  # Инициализация переменной не заданной при создании объкта
print(f'Общий надой - {Манька.total} литров')


class Sheep:
    def __init__(self):
        self.name = 'Unnemed'
        self.weight = 0
        self.total = 0

    def trim(self):  # функция стрижки
        self.total += 20
        print(f'Стрижка проведена. Всего шерсти {self.total} кг')


Барашек = Sheep()
Барашек.total = 100
print(Барашек.total)
Барашек.trim()  # вызов функции (метода) класса
print(Барашек.total)

Кудрявый = Sheep()


class Goat:  # Коза
    def __init__(self, name='Unnemed', weight=0):   # Запрос переменных при создании объекта, значения по-умолчанию
        self.name = name
        self.weight = weight
        self.total = 0
        self.voice = 'Мееее'

    def food(self):   # Функция (метод) кормления
        self.weight += 3
        print(f'{self.name} Кормление вес {self.weight}')


Рога = Goat('Рога', 30)
print(Рога.name)
print(Рога.weight)
Рога.food()

Копыта = Goat('Копыта')
print(Копыта.name)
print(Копыта.weight)


class Duck:
    voice = 'Кря-Кря'

    def __init__(self, name='Unnemed', weight=0):
        self.name = name
        self.weight = weight
        self.total = 0

    def food(self, food_weight=1):   # Функция кормления заданным кол-вом корма. По-умолчанию =1
        self.weight += food_weight
        print(f'{self.name} Кормление вес {self.weight}')

    def eggs(self, n=1):            # Функция яиц. По-умолчанию =1
        self.total += n
        print(f'{self.name} снесла {n} яиц, всего {self.total} яиц')


Кряква = Duck('Кряква', 5)
print(f'Утка {Кряква.name} весит {Кряква.weight} кг')
Кряква.total = 10
Кряква.food(5)
Кряква.eggs(2)

print(f'Коза {Копыта.name} говорит {Копыта.voice}, а утка говорит {Duck.voice} ')


# comment to commit
