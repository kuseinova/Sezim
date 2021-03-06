# 1. Даны два множества. С помощью определенных методов (операторов) найдите:
# пересечение множеств, разницу множеств, объединение множеств.
# Пример:
# Ввод: a = {1, 6, 4, 0, 34, 17, 100, -45}
# b = {22, 0, 3, 100, 4}
# Вывод: {0, 4, 100}
# {1, 6, 34, 17, -45}
# {1, 6, 4, 0, 34, 17, 100, -45, 22, 3}

# a = {1, 6, 4, 0, 34, 17, 100, -45}
# b = {22, 0, 3, 100, 4} 
# c = a & b
# x = a - b
# s = a | b
# print(c)
# print(x)
# print(s)

# 2. Команда Makers собралась на обед. Но они не могут решить, где им пообедать, так
# как у каждого свои вкусовые предпочтения. Помогите найти им выход в данной
# ситуации.
# Данные: Айбек хочет покушать в Dodo или в ImperiaPizza, на крайняк FreshBox.
# Айдай хочет покушать шашлык в OchakKebab или рамен в FreshBox.
# Азат очень хочет вафли с FreshBox либо KFC.
# Гульзана хочет всё.
# Напишите код, который сможет определить, в какое место им лучше пойти.

# Aibek = {'dodo', 'imperia', 'freshbox'}
# aidai = {'ochak', 'freshbox'}
# azat = {'freshbox', 'kfc'}
# gulzana = {'dodo', 'imperia', 'freshbox', 'ochak', 'kfc'}
# x = Aibek & aidai & azat & gulzana
# print(x)

# 3. Джон загадал пять чисел от 1 до 30. Определите, кто из перечисленных ниже
# людей угадал хотя бы одно число из загаданных Джоном.
# Джон загадал: 5, 7, 11, 10, 28
# Рейчел: 29, 2, 6, 12, 3
# Кэтрин: 1, 5, 14, 8, 22
# Сэм: 19, 20, 3, 11, 10

# john = {5, 7, 11, 10, 28}
# reichel = {29, 2, 6, 12, 3}
# ketrin = {1, 5, 14, 8, 22}
# sem = {19, 20, 3, 11, 10}

# x = john & reichel
# print(x)
# y = john & ketrin
# print(y)
# z = john & sem
# print(z)

# 4. Имеется пицца, ингридиенты которой помещены во множество. Используйте
# определенные методы, чтобы проделать следующие действия.
# Ингридиенты: {сыр чеддар, грибы, соус, шпинат}
# Действия: 1. Добавьте помидоры.
# 2. Уберите из пиццы колбасу(если она есть)
# 3. Уберите из пиццы шпинат, вместо него добавьте базилик
# 4. Замените сыр чеддар сыром моцарелла.
# Какая пицца у вас получилась?

# ingrid = {'syr chedder', 'griby', 'sous', 'shpinat'}
# ingrid.add('pomidor')
# print('kolbaca' in ingrid)
# ingrid.discard('shpinat')
# ingrid.add('basilic')
# ingrid.discard('syr chedder')
# ingrid.add('syr macorella')
# print(ingrid)
