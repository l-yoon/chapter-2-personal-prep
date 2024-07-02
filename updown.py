import random


def updown_game(highscore=0):
    attempts = 0
    random_number = random.randint(1, 100)
    if highscore != 0:
        print(f"최고점수:{highscore}")
        
    # loop
    while True:

        guess_number = int(input("1-100의 사이의 숫자를 입력하세요: "))
        attempts += 1
        # range
        if guess_number < 1 or guess_number > 100:
            print("1-100사의의 숫자를 입력하세요!")
        # up or down
        elif random_number < guess_number:
            print("다운")
        elif random_number > guess_number:
            print("업")
        else:
            print(f"정답! 시도한 횟수: {attempts}")
            if highscore == 0 or attempts < highscore:
                highscore = attempts
            break

    # restart
    while True:
        restart = input("게임을 다시 하시겠습니까? (y/n): ").lower()
        if restart == "y":
            updown_game(highscore)
        elif restart == "n":
            print(f"최고점수:{highscore}")
            print("END")
            break


updown_game()
