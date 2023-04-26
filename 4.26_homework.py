#가위바위보 게임
import random
option = ['가위','바위','보']
#리스트내 값들을 랜덤으로 가져올 수 있음
C_choice = random.choice(option)
while True:
    user_input = input("가위,바위,보 중에 골라주세요.\n")
    if user_input in option:
        if user_input == C_choice:
            print("당신과 컴퓨터는 비겼습니다.")
            break
        elif user_input != C_choice:
            if user_input=='가위' and C_choice=='바위':
                print("컴퓨터가 이겼습니다!")
                break
            elif user_input=='바위' and C_choice=='보':
                print("컴퓨터가 이겼습니다!")
                break
            elif user_input=='보' and C_choice=='가위':
                print("컴퓨터가 이겼습니다!")
                break
            else:
                print("당신이 이겼습니다!")
                break

print(f"당신은 {user_input}을(를) 냈습니다!")
print(f"컴퓨터는 {C_choice}을(를) 냈습니다!")


#25304번 백준문제
#첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
#둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
#이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

#총 금액
X = int(input())
#물품 종류의 수
N = int(input())
#영수증의 금액
sum = 0

for i in range(1,N+1):
    a,b = map(int,input().split())
    i = (a*b)
    sum += i
if X == sum:
    print("Yes")
else:
    print("No")



