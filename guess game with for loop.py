import random
a=random.randint(0,10)
chance=3
for i in range(100):
    print(f'you have {chance} chance left')
    user=int(input("num: "))
    if user==a:
        print('congratulation You Won')
        break
    elif user > a:
        print('your number is bigger than guess no')
    elif user < a:
        print('your number is lesser than guess no')
    else:
        print("try again")

    chance -= 1

    if chance ==0:
        print('sorry you lose')
        break