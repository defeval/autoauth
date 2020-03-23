f = open('data.txt', 'a')
print(f.write('Hello\n'))
print(f.write('Python\n'))

f.close()

f = open('data.txt')
text = f.read()
print(text.split())
