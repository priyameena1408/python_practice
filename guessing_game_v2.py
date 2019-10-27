import random
repeat = True
x = random.randint(1, 10)
while repeat:
    guess = int(input("Enter a number between 1 to 10: "))
    while guess != x:
        if guess < x:
            print("Too Low! Try again...")
        else:
            print("Too High! Try again...")
        guess = int(input("Try Again: "))
    print("YOU GUESSED IT!!!")
    a = input("Do you want to continue? (Y/N) ")
    if a == "N" or a == "n":
        repeat = False
        print("Bye!! Miss you...")
