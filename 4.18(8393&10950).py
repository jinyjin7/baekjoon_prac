#8393 : 합 구하기
n = int(input())
s = 0
for i in range(n+1):
    s += i
    print(s)





#10950 : A+B n번
T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    print(a+b)