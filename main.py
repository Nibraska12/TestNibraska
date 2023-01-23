#2
# question = input('Any question ?')
# d = {'How old are u?': 21, 'How much brothers u have?': 1}
# if question in d:
#     print(d[question])
# else:
#     print('I miss u')
import datetime

# for i in d:
#     if question == i:
#         print(d[i])
#         break
# else:
#     print('I miss u')


#4
# list_of_manes = ['Artyr', 'Sergey', 'Nikita', 'Vlad']
# list_of_work_manes = []
# list_of_home_manes = []
# while True:
#     people = input('Who are u?')
#     if people in list_of_manes:
#         list_of_work_manes.append(people)
#         print('Coming to' , list_of_work_manes)
#
#     else:
#         None
#

#for name in list_of_manes:
    #if name not in list_of_work_manes:
        #list_of_home_manes.append(name)

#print(list_of_home_manes, 'homeboys')
#print(list_of_work_manes, ' boys at work')


#3
# credit_card = 100
# meals = {'Bread':15 , 'Milk':25, 'Meat':45, 'Cheese':35}
# bag = []
# while True:
#     meal = input('Which u wanna buy')
#     if meal in meals:
#         if credit_card >= meals[meal]:
#             credit_card -= meals[meal]
#             print(credit_card)
#             bag.append(meal)
#             print(bag)
#             print('U bought ', meal)
#         else:
#             print('U have no money to buy ', meal, 'please choose something else')
#     else:
#         print('Nety')
#     if credit_card < min(meals.values()):
#         print('U dont have money to buy something')
#         break




#1
#meal = input('What u bring it?')
#container_white = ['Apple','Coconut']
#container_black = ['Watermelon','Melon']
#if meal in container_black:
    #print('отклонено')
#elif meal in container_white:
    #print('Принято')
#else:
    #print('Его нет ни в одном списке')


# HOMEWORK ***********

#To next lesson you need to prepare( for, while, тернарный оператор, generator of list, date of types, if else elif, (and or is not == etc..))
#Iteration object, Iteration


# def calculate(*args, **kwargs):

# print(10,2,3,4, operations=["*", "+", "-"])   # 19


# def calculate(first_number,second_number,third_number,fourth_number, operations=None ):
#     if operations == "*":
#         return first_number * second_number + third_number - fourth_number
#
# print(calculate(first_number=10, second_number=2, third_number=3, fourth_number=4, operations ="*"))     19

# random = [1,2,6,5,4,3]
# sorting = []
# while random:
#     minimum = random[0]
#     for i in random:
#         if i < minimum:
#             minimum = i
#     sorting.append(minimum)
#     random.remove(minimum)
# print(sorting)

# def replace_symbols(all_symbols):
#     def decorator(func):
#         def asd(*args, **kwargs):
#             string = func(*args, **kwargs)
#             for symbl in all_symbols:
#                 string = string.replace(symbl, '')
#             return  string
#         return asd
#     return decorator
#
#
# @replace_symbols(all_symbols=['%', '#', '*', ")", '(', '^'])
# def symbols(undefined_str):
#     return undefined_str
#
# a = symbols("asd%asd#wqqw*asdsda)asdasd(asd^")

#
# a = [12,34,56,78,82,45,346,]
# b = [13,23,34,56]
# a.extend(b)
# print(a)

# zip



# a = ["Марина", "Маша", "Мандарин", "Маршрутка", "Макароны", "Маруся", "Манда"]
# b = ["Марина", "Маша", "Мандарин", "Маршрутка", "Макароны", "Маруся", "Нон"]
# def verif(list_of_string):
#     v = []
#     for i in list_of_string:
#         if i.startswith('Ма'):
#             v.append(i)
#         else:
#             v.append(False)
#     return all(v)
#
# print(verif(a))
# print(verif(b))


# def check_words(words):
#     for word in words:
#         if not word.startswith("Ма"):
#             return False
#     return True
#
# words1 = ["Марина", "Маша", "Мандарин", "Маршрутка", "Макароны", "Маруся", "Манда"]
# words2 = ["Марина", "Маша", "Мандарин", "Маршрутка", "Макароны", "Маруся", "Нон"]
#
# print(check_words(words1))
# print(check_words(words2))



# white = ["apple", "sousage"]
# black = ['peach','melon','lemon']
#
# def search(string):
#     v = string.split(',')
#     white_resault = []
#     black_resault = []
#     grey_resault = []
#     for i in v:
#         if i in white:
#             white_resault.append(i)
#         elif i in black:
#             black_resault.append(i)
#         else:
#             grey_resault.append(i)
#     return  f'white - {white_resault},black - {black_resault},grey - {grey_resault}'
#
#
# print(search("apple,sousage,lemon,milk"))


# def calc():
#     print("calculate")
#     while True:
#         print("choose action:\n""+\n""-\n""*\n""/\n""exit: q\n")
#         action = input("Выберите действие: ")
#         if action == "q":
#             print("exit")
#             break
#         if action in ('+', '-', '*', '/'):
#             x = int(input("Введите первое число"))
#             y = int(input("Введите второе число"))
#             if action == '+':
#                 print(x+y)
#             elif action == '-':
#                 print(x-y)
#             elif action == '*':
#                 print(x*y)
#             elif action == '/':
#                     if y != 0:
#                         print(x/y)
#                     else:
#                         print("division by zero")
# if __name__ == '__main__':
#     calc()

# def add(a, b):
#     return a + b
#
# def subtract(a ,b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# def choose_operation():
#     print('Выберете операцию:')
#     print('1 Сложить')
#     print('2 Вычесть')
#     print('3 Умножить')
#     print('4 Делить')
#
#     choice = int(input('Ваша операция? (1/2/3/4): '))
#
#     if choice == 1:
#         return add
#     elif choice == 2:
#         return subtract
#     elif choice == 3:
#         return multiply
#     elif choice == 4:
#         return divide
#
# def main():
#     operation = choose_operation()
#     a = float(input('Введите первое число: '))
#     b = float(input('Введите второе число: '))
#     result = operation(a, b)
#     operation_dict = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/' }
#     print(f'{a} {operation_dict[operation.__name__]} {b} = {result}')
# if __name__ == '__main__':
#     main()


# import pytz
#
#
# print('The timezones supported by pytz module:\n', pytz.all_timezones, '\n')
#
# print('Commonly used time-zones:\n', pytz.common_timezones, '\n')
# utc = pytz.utc
# dt = datetime.datetime.now(utc)
#
# print('TimeZome', dt.strftime("%2"))




#
# сars = [1,2,3,4,5]
#
# def carss(func):
#     for i in cars:
#         yield i*2
#
#
# doublecars = (i*2 for i in cars)
#


# import time
#
#
# def timeit(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Time Taken: {end - start } Seconds ')
#     return wrapper()
#
# # @timeit
# def my_function():
#     time.sleep(1)
#
#
# my_function = timeit(my_function)




# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(3))

# def outer_function(): # замыкание
#     x = 10
#
#     def inner_function():
#         print(x)
#     return inner_function
#
# closure = outer_function()
# closure()


# def calc(a):
#     return a * 3
#
#
# lambda a: a * 3
#
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# results =  [i for i in a if i < 5 ]
# print(results)

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# print(my_dict.get('f'))


a = 1