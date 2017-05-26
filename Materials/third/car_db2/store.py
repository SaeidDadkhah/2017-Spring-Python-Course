class Store:

    def __init__(self, phone, city):
        self.__phone = phone
        self.__city = city
        self.__cars = list()

    def add(self, car):
        self.__cars.append(car)

    def show_cars(self):
        print(self.__cars)

    def __str__(self):
        return '{}: {}'.format(self.__phone, self.__city)

cities = ['Teh', 'Esf']
