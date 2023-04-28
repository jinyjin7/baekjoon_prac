import random


def match_result(user_input, computer_choice):
    print(f"당신은 {user_input}을(를) 냈습니다!")
    print(f"컴퓨터는 {computer_choice}을(를) 냈습니다!")
    if user_input == '가위':
        if computer_choice == '가위':
            return "비겼다."
        elif computer_choice == '바위':
            return "졌다."
        else:
            return "이겼다."
    elif user_input == '바위':
        if computer_choice == '가위':
            return "이겼다."
        elif computer_choice == '바위':
            return "비겼다."
        else:
            return "졌다."
    else:
        if computer_choice == '가위':
            return "졌다."
        elif computer_choice == '바위':
            return "이겼다."
        else:
            return "비겼다."




options = ['가위', '바위', '보']
computer_choice = random.choice(options)
me_win = 0
computer_win = 0

while True:
    user_input = input("가위, 바위, 보 중에서 골라주세요: ")
    if user_input in options:
        result = match_result(user_input, computer_choice)
        if result == "이겼다.":
            me_win+=1
            print(f"당신은 {me_win}:컴퓨터는 {computer_win}")
            if me_win == 2:
                print(f"축하합니다! 당신의 승리")
                break
        elif result == "졌다.":
            computer_win+=1
            print(f"당신은 {me_win}:컴퓨터는 {computer_win}")
            if computer_win ==2:
                print(f"아쉽습니다 ! AI의 승리")
                break
        else:
                print("한판더")
                continue

            
    else:
        print("잘못 입력하셨습니다.")




