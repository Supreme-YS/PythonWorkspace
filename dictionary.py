#Dictionary
#딕셔너리 생성
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

#키 이름의 중복 #health가 두 개임.
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)

#딕셔너리의 자료형
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

#빈 딕셔너리
x = {}
y = dict()

#dict를 활용한 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)    # 키=값 형식으로 딕셔너리를 만듦
print(lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72])) #zip 함수로 키 리스트와 값 리스트를 묶음

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)]) # (키, 값) 형식의 튜플로 딕셔너리를 만듦

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}) #dict 안에서 중괄호로 딕셔너리를 만듦

#key에 접근하기
print(lux['health'])

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux    # 딕셔너리에 키를 지정하지 않으면 딕셔너리 전체를 뜻함

#key에 값 할당하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
lux['mana'] = 1184      # 키 'mana'의 값을 1184로 변경

#key가 없다면 ?
lux['mana_regen'] = 3.28    # 키 'mana_regen'을 추가하고 값 3.28 할당

#키가 딕셔너리에 있는지 확인하기

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

'health' in lux #True
'attack_speed' in lux #False

'attack_speed' not in lux #True
'health' not in lux #False

#키 갯수 구하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
len(lux) #4 출력
len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}) #4 출력

