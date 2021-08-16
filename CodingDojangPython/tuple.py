#Tuple
a = (1, 2, 3, 4, 5)
b = 1, 2, 3, 4, 5

print(a, b, sep='\n')

#Tuple_feature
person = ('Jacob', 29, 173, True)
print(person)

#one_factor_tuple
c = (27, )
d = 27,
print(c, d, sep='\n')

#range_tuple
e = tuple(range(10))
f = tuple(range(1, 10))
g = tuple(range(1, 10, 2))

print(e, f, g, sep='\n')

#from_list_to_tuple
ab = [1, 2, 3]
tuple(ab)
print(tuple(ab))

#from_tuple_to_list

cd = (4, 5, 6)
list(cd)
print(list(cd))

#string in list
string_list = list('hello')
print(string_list)

#string in tuple
string_tuple = tuple('Python')
print(string_tuple)

#make_multi_variable
z, x, c = [1, 2, 3]
print(z, x, c)

t, y, u = (4, 5, 6)
print(t, y, u)

