#set


#set.isdisjoint(other) - истина, если set and other не имеют общих элементов
# a = {123,435} # Метод возвращает True , если множество sets не имеет общих элементов с итерируемым объектом other , если имеются общие элементы то вернет False
# print(a.isdisjoint({123})) # - False


#set==other # - все элементы set принадлежат other, все элементы other принадлежат set
# a = {123,321}
# b = {123,321}


#set.issubset(other) or set<= other # - все элементы принадлежал other
# myset = {1, 2, 3}
# myset.issubset([1, 2])  # False
# myset.issubset([1, 2, 3])  # True
# myset.issubset([1, 2, 3, 4])  # True


#set.issuperset(other) или set >= other # - аналогично только наоборот
# myset = {1, 2, 3}
# print(myset.issuperset([1, 2])) # - True


#set.union(other, ...) или set | other | # - объединение нескольких множеств
# a = {123}
# b = {345}
# v = {678}
# print(a.union(b,v)) # - {345, 123, 678}


#set.intersection(other , ... ) или set & other & ... # - пересечение
# my_list = [4]
# my_set_1 = set([1, 2, 3, 4, 5])
# my_set_2 = set([5, 6, 7, 8, 9])
# my_set_3 = set(my_list)
# my_set_1.intersection(my_set_2)  # {5}
# my_set_1 & my_set_2  # {5}
# my_set_1 & my_set_3  # {4}


#set.difference(other, ...) или set - other - ... # - множество из всех элементов set, не принадлежащие ни одному из othe
# a = {'a','b','v'}
# b = {'a','g','d'}
# print(a.difference(b)) # - {'b', 'v'}


#set.symmetric_difference(other); set ^ other # - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих
# A = {'a', 'b', 'c', 'd'}
# B = {'c', 'd', 'e' }
# C = {}
# print(A.symmetric_difference(B))#{'a', 'e', 'b'}
# print(B.symmetric_difference(A))#{'e', 'b', 'a'}
# print(A.symmetric_difference(C))#{'a', 'b', 'c', 'd'}
# print(B.symmetric_difference(C))#{'c', 'e', 'd'}


#set.copy # - copy
# a = {123,456}
# b = a.copy()
# print(b) # - {456, 123}


#set.update(other, .. )  set |= other |  ..  # - обьединение
# a = {123,456}
# b = {789,1011}
# p = {1213,1415}
# a.update(b,p)
# print(a) # - {1011, 789, 1415, 456, 123, 1213}

# a = {123,456}
# b = {789,1011}
# a |= b
# print(a)


#set.intersection_update(other, ...); set &= other & ... #- пересечение
# a = {123,456}
# b = {123,1011}
# p = {1213,123}
# a.intersection_update(b,p)
# print(a) # - {123} позволяет сохранить в множестве set только те элементы, которые присутствуют одновременно во всех объектах, участвующих в операции. Метод возвращает обновленное множество set с элементами, которые являются общими для множества set и всех итерируемых объектов *other

# a = {123,456}
# b = {123,1011}
# p = {1213,123}
# a &= b & p
# print(a)


#set.difference_update(other, ...); set -= other | ... # - вычитание
# a = {123,456}
# b = {123,789}
# p = {1213,123}
# a.difference_update(b,p)
# print(a) # - {456}


#set.symmetric_difference_update(other); set ^= other # - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих
# a = {123,456}
# b = {123,789}
# a.symmetric_difference_update(b)
# print(a) # - {456, 789}


#set.add(elem) # - добавляет элемент в множество
# a = {123,456}
# a.add(789)
# print(a) # - {456, 123, 789}


# set.remove(elem) # - удаляет элемент из множества. KeyError, если такого элемента не существует
# a = {123,456}
# a.remove(123)
# print(a) # - {456}


# set.discard(elem) #- удаляет элемент, если он находится в множестве
# a = {1,2,3,4,5}
# a.discard(2)
# print(a) #- {1, 3, 4, 5}


# set.pop() #- удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым
# a = {2,3,6,}
# a.pop()
# print(a) # - {3, 6}


# set.clear() #- очистка множества
# a = {123,456}
# a.clear()
# print(a)



