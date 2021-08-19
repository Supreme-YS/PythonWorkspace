#사전 (딕셔너리)

# cabinet = {3:"유재석", 100:"김태호"} #dictionary = {key : value}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(100)

#주의사항 

#print(cabinet[5]) #오류 후 값 종료됨
# print(cabinet.get(5)) #오류 발생안하고 None이란 값으로 출력
# print(cabinet.get(5, "사용가능"))


# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


#새 손님

print(cabinet)
cabinet["A-3"] = "김종국" #유재석 값 빠지고 김종국 입력
cabinet["C-20"] = "조세호" #조세호 입력됨

print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)