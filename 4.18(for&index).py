# a, b, c, d, e를 프린트해주세요
# c, d, e, f 를 프린트해주세요
# d, c, b를 프린트해주세요
# a,c,e를 프린트해주세요

my_list = ['a','b','c','d','e','f']

for a in range(0, 5):
    print(my_list[a])

for i in range(2, 6):
    print(my_list[i])

for b in range(3, 0, -1):
    print(my_list[b])

for b in range(0, 5, 2):
    print(my_list[b])