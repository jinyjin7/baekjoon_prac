#11022
#첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)


n = int(input())


for i in range(1, n+1):
    A, B = map(int,input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')

#10699
#오늘날짜 출력

import datetime
print(datetime.date.today())