"""def a(*args, **kwargs):
    print('k', 'a')
    print(args)
    print(kwargs)

a(1, 2)
a(start=1)
a(1, start=2, end=2)"""



class Human:
    def __init__(self, color):
        self.color = color


class Runner:
    def __init__(self, step_size):
        self.step_size = step_size


class Student(Human, Runner):
    def __init__(self, color, step_size):
        super().__init__(color)
        Runner.__init__(self, step_size)
        self.__h = 0

    def __add__(self, other):
        return Student(self.color, self.step_size + other.step_size)

    def __len__(self):
        return self.step_size

    def __str__(self):
        return '{color}: {step}'.format(color=self.color, step=self.step_size)

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h > 0:
            self.__h = h

    @h.getter
    def h(self):
        return '{:2.02f} m'.format(self.__h / 100)


a = Student('red', 12)
a.h = 175
print(a.h)

# import pdb
# pdb.set_trace()


import random
# random.seed(11)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.random())
print(random.choice([1, 5, 8]))
print(random.choices([1, 5, 8], k=2))
print(random.sample([1, 2, 3, 4], 3))
print(random.uniform(10, 20))
print(random.normalvariate(0, 1))

import re

r = re.compile('\+[0-9]{12}')
s = 'my phone: +989388835866, your phone: +989388835867'
sea = r.finditer(s)
print(sea)
print(r.findall(s))

