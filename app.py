import random
#NumberGuessingGame
n = 0
l = 3
while(n<3):
    password = input("Enter a password: ")
    n = n+1
    l = l-1
    if password == "123456":
        x = int(input("Enter starting number: "))
        y = int(input("Enter ending number: "))

        r = random.randint(x, y)
        i = 1
        while (i < 4):
            a = int(input(f"Enter {i}st guess: "))
            i = i + 1
            if a == r:
                print("You Win!")
                break
            if a != r and i == 4:
                print(f"Sorry, You lose! The correct number was {r}")
            else:
                continue
        break
    if password != "123456":
        if l>0:
            print(f"Wrong password! You have {l} chance")
        if l == 0:
            print(f"Wrong password! You have used all attempts")









