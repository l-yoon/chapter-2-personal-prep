import random


def rpc_game():
    options = ['가위', '바위', '보']
    win_count = 0
    lose_count = 0
    draw_count = 0

    # loop
    while True:
        user_choice = input("가위,바위,보 중에 하나를 입력하세요:")
        comp_choice = random.choice(options)
        # error value
        if user_choice not in options:
            print("옮바른 값을 입력하세요!")

        # draw
        elif user_choice == comp_choice:
            print("비김")
            print(f"사용자:{user_choice},컴퓨터:{comp_choice}")
            draw_count += 1

        # lose
        elif user_choice == "가위" and comp_choice == "바위" or\
                user_choice == "바위" and comp_choice == "보" or\
                user_choice == "보" and comp_choice == "가위":
            print("컴퓨터 승")
            print(f"사용자:{user_choice},컴퓨터:{comp_choice}")
            lose_count += 1

        # win
        else:
            print("사용자 승")
            print(f"사용자:{user_choice},컴퓨터:{comp_choice}")
            win_count += 1

        # restart
        while True:
            restart = input("게임을 다시 하시겠습니까? (y/n):").lower()
            if restart == "y":
                break
            elif restart == "n":
                print(f"승:{win_count},패:{lose_count},무승부:{draw_count}")
                print("END")
                return
            else:
                print("y/n을 입력해주세요")


rpc_game()
