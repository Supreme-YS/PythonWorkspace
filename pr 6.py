path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

x = path.split('\\')
filename = x[-1]
#또는
x = path.split('\\')
x.reverse()
filename = x[0]
또는
filename = path[path.rfind('\\') + 1:]

print(filename)
