import random as rd
chances=3
while True:
        a=rd.randint(0,10)
        b=rd.randint(0,10)
        print(F'{a} X {b}= ')
        d=a*b
        print(f"{chances} chances left")
        c=int(input('Enter solution: '))
        user=d
        if user==c:
            print('You won')
        elif chances ==0:
            print('You lose')
            break
        else:
             print("youlose")
             chances -=1