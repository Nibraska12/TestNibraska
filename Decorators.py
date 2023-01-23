#decorator это функция которая принимает другую функцию и возвращает функцию она нужна чтобы в функцию добавилось новое поведение или функционал

# def decorator(func):
#
#     def inner(*args,**kwargs):
#         print('start')
#         func(*args,**kwargs)
#         print('finish')
#     return inner
#
# #@decorator say = decorator(say)
# def say(name, surname, age):
#     print('hi',name, surname, age)
#
# say = decorator(say)
# say('vasya','jopa', '12')

 # wraps cохраняет значение __name__ и __doc__ в вашей изначальной функции


from functools import wraps

def table(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('<table>')

    return inner


def say():
    print('hi')


def sqr(x):
    """

    Функция возводит в квадрат х
    :param x:
    :return:
    """

    print(x**2)
#
# #@wraps  name "sqr" == sqr / doc "sqr" == sqr  а не inner
# sqr.__doc__
# sqr.__name__

