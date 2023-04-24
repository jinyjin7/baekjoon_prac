#업다운게임
import random

answer = random.randint(10, 100)

while True:
    user_input = int(input())
    if user_input == answer:
        break
    elif user_input > answer:
        print("down")
    elif user_input < answer:
        print("up")
    else:
        break
print("게임이 끝났습니다.")



#11021번
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. (for문)
T = int(input())

for i in range(T):
    A, B = map(int,input().split())
    i += 1
    print(f"Case #{i}: {A+B}")

#10952번
#입력은 여러 개의 테스트 케이스로 이루어져 있다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#입력의 마지막에는 0 두 개가 들어온다. (while문)


while True:
    A, B = map(int,input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
    

    


