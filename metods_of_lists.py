#list.append(x) # - добавляет элемент в конец списка
# a = [1,2,3,4]
# a.append(5)
# print(a) # - [1, 2, 3, 4, 5]


#list.extend(l) # - расширяет список list добавляя в конец все элементы списка
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)# - [1, 2, 3, 4, 5, 6]


#list.insert(i,x) # - вставляет на i-ный ээлемент значени х
# a = [1,2,3]
# a.insert(1,2)
# print(a)# - [1, 2, 2, 3]


#list.remove(x) # - удаляет первый элемент в списке , имеющий значение х  исключение если такого элемента нет
# a = [5,6,7]
# a.remove(5)
# print(a)# - [6, 7]


#list.pop(i) # - удаляет i-ный элементи возвращает его если индекс не указан удаляет последний элемент
# a = [123,345,678]
# a.pop(-2) #/ 1
# print(a)# [123, 678]


#list.index(x,(start,end) # - вщзвращает положение первого элемента со значением х (поиску ведется от старт до енд)
# a = [123,456,789]
# a.index(123,0,1)
# print(a) # [123, 456, 789]


#list.count(x) # - возвращает количество элементов со значением х
# a = [4,4,3,5,6,7]
# print(a.count(4))# - 2


#list.sort(key=функция) # - сортирует список на основе функции
# a = [4,3,6,7,1,2,5]
# a.sort()
# print(a) # - [1, 2, 3, 4, 5, 6, 7]


# def custom_key(people): # key = функция
#     return people[1]
# persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 24, 'M'], ['Alexa', 23, 'F']]
# print(f'Before sorting: {persons}')
# persons.sort(key=custom_key)
# print(f'After sorting: {persons}')


#list.reverse() - разворачивает список
# a = [3,2,1]
# a.reverse()
# print(a) # - [1, 2, 3]


#list.copy() # - поверхностная копия списка
# a = [1,2,3]
# b = a.copy()
# print(b) # - [1, 2, 3]


#list.clear() # - clear
# a = [1,2,3]
# a.clear()
# print(a) # - []