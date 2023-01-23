#S = 'str';- # литералы строк, строки в апострофах и в кавычках - одно и то же
# S = "str";
# S = '''str''';
# S = """str"""


# S = "s\np\ta\nbbb" - экранированные последовательности


# S = r"C:\temp\new" - неформатированные строки (подавляют экранирование)


# S = b"byte" - cтрока байтов


#S1 + S2 # - конкатерация
# a = 'asd' + 'ggwp'
# print(a)


#S1 * 3 # - повторение строки
# a = 'hiphop' * 3
# print(a)


#S[i] # - обращение по индексу
# a = 'asd'[2]
# print(a) # - запринтит букву d


#S[i:j:step] # - извлечение среза
# a = 'шласашапошоссеисосаласушку'[15:21]
# print(a) # запринтит сосала


# len(s) # - длинна строки
# a = 'qwerty'
# print(len(a)) # - 6


#S.find(str,start,end) # - поиск подстроки в строке. Возвращает номер первого вхождения или -1
# a = 'sadcool'
# b = a.find('sad',)
# print(b) # - 0


#S.rfind(str,start,end) # метод rfind() похож на find(), за исключением того, что поиск выполняется справа налево
# a = 'sadcoolsat'
# b = a.find('sat',)
# print(b) # - 7


# S.rindex(str,start,end) # - поиск подстроки в строке возвращает номер последнего вхождения или вызывает ValueError
# a = 'vindeto'
# b = a.rindex('to',1,7)
# print(b)


#S.replace(шаблон, замена , maxcount) # - замена шаблона на замену. maxcount ограничивает количество замен
# a = 'gitller'
# b = a.replace('gitller', 'putin')
# print(b) # putin


# a = 'gitller_its_gitller'
# b = a.replace('gitller', 'putin',1)
# print(b) # - putin_its_gitller


# s.split(символ) # - разбиение строки на подстроки
# a = 'pivacik'
# b = a.split("a")
# print(b)


# s.isdigit() #- состоит ли строка из цифр
# a = '123'
# b = a.isdigit()
# print(b)# - True


#s.isalpha() # - состоит ли строка из букв
# a = 'asd'
# b = a.isalpha()
# print(b) # - True


#s.isalnum() # - состоит ли строка из цифр и букв
# a = 'asd123'
# b = a.isalnum()
# print(b) # True


#s.islower() # - состоит ли строка из символов в нижнем регистре


#s.isupper() # - cостоит ли строка из символов в верхнем регистре


#s.isspace() # - Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
# a = 'asd'
# b = a.isspace()
# print(b)


#s.istitle() # - начинается ли лова в строке с заглавной буквы
# a = 'Kakish'
# b = a.istitle()
# print(b) # - True


# s.upper()	# - преобразование строки к верхнему регистру


# s.lower()	# - преобразование строки к нижнему регистру


#s.startswith(str) # - начинается ли строка S с шаблона str
# a = 'genna ahuevshi v krai'
# b = a.startswith("genna")
# print(b)# - True


#s.endswith(str) # - заканчивается ли строка S шаблоном str
# a = 'boom bim baam'
# b = a.endswith('baam')
# print(b)# - True


#s.join(список) # - сборка строки из под строк
# a = ['gg','wp']
# b = ",".join(a)
# print(b)# gg,wp


# a = ['g g','w p']
# b = " "
# c = b.join(a)
# print(c)# g g w p


#ord(символ) # - символ в его код ASCII


#chr(число) # - код ASCII в символ


#s.capitalize() #- переводит первый символ строки в верхний регистр, а все остальные в нижний


#s.center(width, fill) # - возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
# a = ' grinlich rewgerg ergerg    '
# b = a.center(1, 0)
# print(b)


#s.count(str,start,end)# - возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)
# a = 'asd asd asd '
# b = a.count('asd')
# print(b) # - 3


#s.expandtabs(tabsize)# -в озвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелами
# a = '\t1\t10\t100\t1000\t10000'
# b = a.expandtabs(8)
# print(b)# -         1       10      100     1000    10000


#s.lstrip(chars) # - удаление пробельных символов в начале строк
# a = '   gang'
# b = a.lstrip()
# print(b) # -"gang"


#s.rstrip(chars)# - удаление пробельных символов в конце строки
# a = 'asdasd      '
# b = a.rstrip()
# print(b) #'asdasd'


#s.strip(chars)# - удаление пробельных символов в начале и в конце строки
# a = '   asdasd     '
# b = a.strip()
# print(b)#'asdasd'


#s.partition(шаблон)# - возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки
# a = 'asd.asd'
# b = a.partition('.')
# print(b)# ('asd', '.', 'asd')

#s.rpartition(sep)# - тоже самое слева на право
# a = 'asd.ast.'
# b = a.rpartition('.')
# print(b)# ('asd.ast', '.', '')


#s.swapcase() # - переводит символы нижнего регистра в верхний, а верхнего – в нижний


#s.title() # - первую букву каждого слова переводит в верхний регистр, а все остальные в нижний


#s.zfill(width) # -	делает длину строки не меньшей width, по необходимости заполняя первые символы нулями
# a = 'qwerty'
# b = a.zfill(9)
# print(b) # 000qwerty


#s.ljust(width, fillchar=" ")# - делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar
# a = 'love'
# b = a.ljust(6,"6")
# print(b)# love66


#s.rjust(width, fillchar=" ")# - делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar
# a = '8'
# b = a.ljust(3,"22")
# print(b)# 228


#s.format(*args, **kwargs)# - форматирование строки
# a = '{nums}____{spaces}_____{smile}'
# b = a.format(smile = ':-D', nums = '1234', spaces = '    ')
# print(b)

