class Store:
    def __init__(self, phone, city):
        self.__phone = phone
        self.__city = city
        self.__cars = list()

    def add(self, car):
        self.__cars.append(car)

    def show_cars(self):
        print(self.__cars)


class Car:
    def __init__(self, model, year, cost):
        self.__model = model
        self.__year = year
        self.__cost = cost

    def __str__(self):
        return '{} {}: {}'.format(self.__model,
                                  self.__year,
                                  cost)


class Database:
    def __init__(self, name):
        self.__name = name
        self.__stores = list()

    def add(self, store):
        self.__stores.append(store)

    def show_stores(self):
        print(self.__stores)

    def get_store(self, index):
        return self.__stores[index]

database = Database('Iran')
while True:
    print('Select:')
    print('\t1. Add')
    print('\t2. Remove')
    cmnd = input('Enter the command: ')
    if cmnd.lower() == 'add':
        print('1. Store')
        print('2. Car')
        cmnd = input('Select: ')
        if cmnd.lower() == 'store':
            phone = input('Enter phone: ')
            city = input('Enter city: ')
            store = Store(phone, city)
            database.add(store)
        elif cmnd.lower() == 'car':
            model = input('Enter model: ')
            year = int(input('Enter year: '))
            cost = int(input('Enter cost: '))
            car = Car(model, year, cost)

            database.show_stores()
            cmnd = int(input('Select store: '))
            cmnd -= 1
            store = database.get_store(cmnd)
            store.add(car)
    elif cmnd.lower() == 'show cars':
        database.show_stores()
        cmnd = int(input('Select store: '))
        cmnd -= 1
        store = database.get_store(cmnd)
        store.show_cars()





