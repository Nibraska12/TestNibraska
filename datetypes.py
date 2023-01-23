# def big_number(*args):
#     return sum(args)
# a = big_number(5,10,50,15,20)
# b = True if a >= 100 else False
# print(b)

# a = [int(c.get(number)) for number in b if number % 10 == 0]

# a = [number for number in range(0,11)]
# print(a)

# a = '1,10,100,1000,10000'
#  b = [int(string) for string in a.split(',')]
#  print(b)

# a = ['hagh', 'lave', 'banch', 'craken', 'zalypka']
# b = [string.replace('a','o') for string in a]
# print(b)

# a = list(range(0,101))
# b = [numbers for numbers in a if numbers % 2 == 0 ]
# print(b)

# a = [input('ur words') for _ in range(0,int(input()))]
# b = [a.remove('gang') for _ in range(a.count('gang'))]
# # if 'gang' in a:
# #     a.remove('gang')
# # print(a)

# a = [0, 0, 1, 0, 1, 0, 0, 1]
# zero = [ziro for ziro in a if ziro == 0]
# one = [odin for odin in a if odin == 1]

# for number in a:
#     if number == 0:
#         zero.append(number)
#     else:
#         one.append(one)

# a = [45,56,67,78,89]
# list[4]=55
# print(a)

a = {'asd': 2, 1:5 , 1.4:7, (123,123):4 , True:False, frozenset({213}):5  }
# print(a[frozenset({213})])
print(a.get((123,123,3,),'privet'))


from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def wheels(self):
        pass


class CarEngine(AbstractCar):

    @abstractmethod
    def engines(self):
        pass


# class BMW(CarEngine): #with property
#     def __init__(self, engine, color):
#         self.engine = engine
#         self.color = color
#
#     @property
#     def engines(self):
#         try:
#             return f"Ваш двигатель - {self.engine}"
#         except:
#             return "Двигатель в ремонте"
#
#     @engines.setter
#     def engines(self, value):
#         self.engine = value
#
#     @engines.deleter
#     def engines(self):
#         del self.engine
#
#     def get_color(self):
#         print('black')
#
#     def wheels(self):
#         print('asd')


# class BMW: #with staticmethod
#     def __init__(self, engine, color):
#         self.engine = engine
#         self.color = color
#
#     def engines(self):
#         return self.engine
#
#     def get_color(self):
#         return self.color
#
#     @staticmethod
#     def get_mul_of_2_numbers(value1, value2):
#         return value1 * value2
#
#     @staticmethod
#     def wheels():
#         return "4 колеса"



class BMW(CarEngine, object):  # with classmethod

    wheel = 1

    def __init__(self, engine, color):
        self.engine = engine
        self.color = color

    def engines(self):
        return self.engine

    def get_color(self):
        print('black')

    @classmethod
    def wheels(cls):
        cls.wheel += 1


if __name__ == "__main__":
    print(BMW.__mro__)

