jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("년도 : " + jumin[0:2]) #실제 자리보다 하나 더 0부터 1까지라는 뜻
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지

print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) #특정부분부터 끝까지

print("뒤 7자리 (뒤에부터) :" + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지