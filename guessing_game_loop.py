repeat = True
while repeat:
    guess = int(input("Enter a number between 1 to 10: "))
    while guess != 5:
        if guess < 5:
            print("Too Low! Try again...")
        else:
            print("Too High! Try again...")
        guess = int(input("Try Again: "))
    print("YOU GUESSED IT!!!")
    a = input("Do you want to continue? (Y/N) ")
    if a == "N" or a == "n":
        repeat = False
        print("Bye!! Miss you...")
