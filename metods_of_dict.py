# a = {'ggwp': 5, 12:6}
# метод dict.clear() - очищает словарь
#  a.clear()
#  print(a)


# dict.copy() - возвращает копию словаря , которая является новым обьектом отличающаемся от копируемого
# a = {'123':4, 45:4}
# b = a.copy()  - два разных обьекта
# a[3] = 5
# b[4] = 6
# print(a)
# print(b)

# a = {'123':4, 45:4} # одна ссылка
# b = a
# a[3] = 5
# b[4] = 6
# print(a)
# print(b)


#dict.fromkeys(seq,value) cоздает словарь с ключами из seq и значением value (поумолчанию None)
#seq - итерируемый обьект
#метод fromkeys мы можем использовать только от dict , не можем использовать его от уже созданного словаря
#a = ['lol', 'bot', 'bet', 'nigga', 'chill']
# x = dict.fromkeys(a)
# print(x)
# x = dict.fromkeys(a,10)
# print(x)


#dict.get(ket,defaultvalue) - возвращает значение ключа , но если его нет бросает исключение , а возвращает default (по умолчанию None)
# a = {'trigger':1, 'jopa':4, 'mama':8}
# b = a.get("jopa")
# c = a.get('asd')
# v = a.get('asd','такого ключа нет')
# print(b)
# print(v)
# print(c)

#dict.items() - возвращает все пары ключ значений
# a = {'cicka':5, 'picka':25}
# b = a.items()
# print(b)# возвращает обьект dict_items который является списком из кортежей в котором первый элемент ключ второй значение
# for key,value in b:
#     print(key,value)


#dict.keys() - возвращает все ключи словаря
# a = {'qwe':34,'hlp':23}
# print(a.keys())

#dict.pop(key,defauilt) - удаляет key и возвращает значение , если к4люча нет возвращает default (по умолчанию бросает исключение)
# a = {'gang':21, 'giga':45}
# b = a.pop('gang')
# print(b)
# print(a)

# a = {'hill':123, 'bib':456}
# b = a.pop('asd')


# a = {'reg':123,'ewr':546}
# b = a.pop('asd','я дефолт котрый не возвращает исключения а возвращаюсь я')
# print(a)
# print(b)


#dict.popitem() - удаляет и возвращает пару ключ значение если исключение бросает исключение
# a = {'dfg':34, 'fuck':45}
# b = a.popitem()
# print(b)
# print(a)


# a = {}
# b = a.popitem()


#dict.setdefauilt(key,default)  - возвращает значение ключа, но если него нет , не бросает  исключение , а создает ключ со значением default ( по умолчанию None)
# a = {'rip':45,'bip':78}
# b = a.setdefault('rip')
# print(a)
# print(b)

# a = {'hip':12,'hop':56}
# b = a.setdefault('asd')
# print(a)
# print(b)

# a = {'zip':45, "zap":56}
# b = a.setdefault('asd',55)
# print(a)
# print(b)


#dict.update(other) -обновляет словарь , добавляя пары ( ключ, значение ) Существующие ключи перезаписываются . Возвращают None (не новый словарь )
#other - другой словарь
# a = {'lol':34,'hihi':67}
# b = {'metod':78, 'zalypa':89}
# c = a.update(b) - не обязательно писать переменную , a.update(other)
# print(a)
# print(b)
# print(c)


#dict.values() - возвращает значения в словаре.
# a = {'fgh':67,'dfgh':89}
# b = a.values()
# print(b)


# a = {'get':67, 'values':87}
# b = a['get'] # получение значения по ключу , если ключа нет исключение
# a[7]=56 # запись в словарь