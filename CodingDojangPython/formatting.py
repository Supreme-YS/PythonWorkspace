# formatting


formatting = 'Hello, {0}'.format('Python')

print(formatting)


formatting_method = 'Hello, {0} {2} {1}'.format('Python', 'Script', 3.85)

print(formatting_method)


multi =  '{0} {0} {1} {1}'.format('Python', 'Script')
print(multi)

multi2 = 'Hello, {} {} {}'.format('Python', 'Script', 3.8)
print(multi2)

multi3 = 'Hello, {language} {version}'.format(language='Python', version=3.8)
print(multi3)

language = 'Python'
version = 3.8

multi4 = f'Hello, {language} {version}'
print(multi4)
