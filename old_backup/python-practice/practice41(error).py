#예외처리
#try 내부문장을 실행하다가 오류가 발생하면 Except 명령으로 넘어간다.
try:

    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(num[0] / num[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except:
    print("알 수 없는 에러가 발생하였습니다.")
    