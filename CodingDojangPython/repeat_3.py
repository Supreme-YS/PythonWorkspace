a, b, c, d = map(int, input().split())

checkpoint = a >= 90 and b > 80 and c > 85 and d >= 80

if checkpoint == True:
    
    print('합격')
    
else:
    print('불합격')
