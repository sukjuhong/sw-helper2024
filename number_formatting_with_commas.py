cnt = 0

while True:
    if cnt == 3:
        print("3회 이상 잘못된 입력을 하셨습니다. 프로그램을 종료합니다.")
        break
    else:
        n = input("숫자를 입력하세요: ")
        minus = False

        if n[0] == "-":
            minus = True
            n = n[1:]

        if n.isdigit() == False:
            print("정수만 입력해주세요.")
            cnt += 1
        elif len(n) > 20:
            print("20자리 이하의 숫자를 입력해주세요.")
            cnt += 1
        else:
            if minus:
                n = "-" + n

            n = int(n)
            print("{:,}".format(n))
            break
