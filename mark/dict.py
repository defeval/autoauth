d = {'a': 1, 'c': 2, 'b': 3}
print(help(d))

# сортировка по ключу в разборе
key = list(d.keys())  # unsort list keys
print(key)

key.sort()
print(key)

for i in key:
    print(i, '=>', d[i])

# сортировка по ключу более простая
for i in sorted(d):
    print(i, '=>', d[i])

print(sorted(d))

if 'f' not in d:
    print('f is not in d')

d['f'] = 99
print(sorted(d))

if 'f' in d:
    print('f in d')

# get key
value = d.get('a', 0)
print(value)
value = d.get('h', 0)
print(value)



