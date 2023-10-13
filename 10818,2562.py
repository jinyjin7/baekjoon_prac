#10818
#첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

n = int(input())
lst = list(map(int,input().split()))


print(min(lst),max(lst))


#2562번
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#로직만 생각햇을때_정답은 나오지만 너무 비효율적임
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# n5 = int(input())
# n6 = int(input())
# n7 = int(input())
# n8 = int(input())
# n9 = int(input())

# list2 = [n1,n2,n3,n4,n5,n6,n7,n8,n9]

# max1 = max(list2)

# print(max1)
# print(list2.index(max1)+1)

#수정한 로직
print(*max((int(input()),i+1)for i in range(9)))