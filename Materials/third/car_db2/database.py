from car_db2 import store
from car_db2 import car


class Database:
    def __init__(self, name):
        self.__name = name
        self.__stores = list()

    def add(self, store):
        self.__stores.append(store)

    def show_stores(self):
        for i in self.__stores:
            print(i)

    def get_store(self, index):
        return self.__stores[index]


db = Database('Iran')
s = store.Store('9', 'Teh')
db.add(s)
db.show_stores()
store = db.get_store(0)
c = car.Car('m', 2, 2)
store.add(c)