# a = bool(0)
# print(a) # False
# a = bool(1)
# print(a) # True


# Операции с кортежами (Tuple)
# Все операции над списками, не изменяющие список (сложение, умножение на число, методы index() и count() и некоторые другие операции). Можно также по-разному менять элементы местами и так далее


# a = iter('asd')
# print(next(a))

# a = 1 and 2
# b = 0 and 2
# c = 2 and []
# s = '' and {}
# v = 1 or 2
# g = 0 or 2
# h = 2 or []
# j = '' or {}

# x = 4
# def asd():
#     x = 0
#     def ggwp():
#         global x
#         x += 1
#         return x
#     return ggwp
#
# if __name__ == '__main__':
#     try:
#         a = 1 / 0
#         print(a)
#     except :
#         print('неделимое')


# def a(x,y):
#     if x == 1 and y == 1 :
#         raise ZeroDivisionError
# a(1,1)

#
# print(dir([123]))
# print(['sad'].__class__)


class MyFirstClass:
    x = 4
    y = 2
    def __init__(self,a,v):
        self.a = a
        self.v = v
    def add(self):
        return self.a + self.v
c = MyFirstClass(1,2)
c.x = 10
c.o = 100
b = MyFirstClass(3,4)

print(c.add())
print(b.add())