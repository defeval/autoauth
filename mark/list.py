my_list = [12, 14, 1.25]

my_list.append(0.5)
print(my_list)

my_list.pop(0)  # удаление элемента
print(my_list)

my_list.sort()  # удаление элемента
print(my_list)

my_list.reverse()  # удаление элемента
print(my_list)

# генераторы списков
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

cols2 = [row[1] ** 2 for row in m if row[1] % 2 == 0]
print(cols2)

diag = [m[i][i] for i in [2, 1, 0]]
print(diag)

triple = [int(c * 3) for c in '123z0.5' if c.isnumeric()]
print(triple)

g = [sum(row) for row in m]
print(g)

# Тоже генератор списка
squares = [x ** 2 for x in range(1, 6)]
print(squares)