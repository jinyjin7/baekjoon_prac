#시험성적
a = int(input())
if a > 89:
    print("A")
elif 90> a >79:
    print("B")
elif 80> a >69:
    print("C")
elif 70> a >59:
    print("D")
else:
    print("F")

#for문 연습하기
my_list = [ {"이름":"권기현", "나이":32},  {"이름":"홍서연", "나이":20},  
{"이름":"박소진", "나이":20}, {"이름":"이미진", "나이":19}, 
 {"이름":"이정현", "나이":18}, {"이름":"연제건", "나이":17}, 
 {"이름":"강유지", "나이":16}, {"이름":"김태연", "나이":15}, 
 {"이름":"김주영", "나이":14}]

#나를 제외한 한명씩 나이먹기
# for person in my_list:
#     if person['이름'] != '박소진':
#         person['나이']+=1

# print(my_list)
#or
for person in my_list:
    if person['이름']=='권기현'or person['이름']=='박소진':
        person['나이']-=1
    else:
        person['나이']+=1
print(my_list)


#처음작성한 답안,왜 권기현튜터님 나이는-2를 해야하나 싶었는데, else문 때문이였다.
# (나이가빠졌다가,else문에서 다시 +1이되버림)
# for person in my_list:
#     if person['이름']=='권기현':
#         person['나이']-=2
#     if person['이름']=='박소진':
#         person['나이']-=1
#     else:
#         person['나이']+=1
# print(my_list)
