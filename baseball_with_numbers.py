import random

while True:
    num_list = [n for n in range(1, 10)]
    answer = random.sample(num_list, 3)
    print(answer)

    print("숫자야구 게임을 시작합니다.")

    while True:
        user = input("숫자를 입력해주세요 : ")
        strike = 0
        ball = 0
        out = 0

        if len(user) != 3:
            print("3자리 숫자를 입력해주세요.")
        elif user[0] == user[1] or user[1] == user[2] or user[0] == user[2]:
            print("중복되지 않은 숫자를 입력해주세요.")
        elif user.isdigit() == False:
            print("정수만 입력해주세요.")
        else:
            user = list(map(int, user))

            for i in range(3):
                if user[i] in answer:
                    if user[i] == answer[i]:
                        strike += 1
                    else:
                        ball += 1
                else:
                    out += 1

            if strike == 3:
                print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
                break
            elif out == 3:
                print("OUT")
            else:
                print(f"{strike}S {ball}B")

    retry = input("게임을 다시 시작하려면 Y, 종료하려면 N를 입력하세요.")
    if retry == "N":
        break
