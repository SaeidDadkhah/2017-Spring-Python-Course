class Car:
    def __init__(self, model, year, cost):
        self.__model = model
        self.__year = year
        self.__cost = cost

    def __str__(self):
        return '{} {}: {}'.format(self.__model,
                                  self.__year,
                                  self.__cost)

if __name__ == '__main__':
    car = Car('Pride', 2000, 26)
    print(car)