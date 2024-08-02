import random
import time
tries = 1
def numberguesser(firstnumber, secondnumber):
    global tries
    n = random.randint(firstnumber, secondnumber)
    while True:
        guess = int(input("Enter A Guess Between The Numbers You Selected: "))
        if guess == n:
            print("Wow! You Got It In", tries, "Tries")
            break
        elif(guess > n + 50):
            print("Your Guess Is Way Larger Then The Number")
            tries += 1
        elif(guess > n and guess < n + 50):
            print("Your Guess Is Above The Number But, Not That Much")
            tries += 1
        elif(guess < n - 50):
            print("Your Guess Is Way Smaller Then The Number")
            tries += 1
        elif(guess < n and guess > n - 50):
            print("Your Guess Is Below The Number But, Not That Much")
            tries += 1
def askingnumbers():
    firstnum = (input("Tell the First (The Smaller Number): "))
    secondnum = (input(f"Tell The Second (The Larger Number) Then {firstnum}: "))
    if not str(firstnum.isdigit()):
        print(f"{firstnum} Is Not A Number")
        time.sleep(1)
        askingnumbers()
    elif not str(secondnum.isdigit()):
        print(f"{secondnum} Is Not A Number")
        time.sleep(1)
        askingnumbers()
    elif firstnum > secondnum:
        print(f"{firstnum} Is Greater Then {secondnum}")
        time.sleep(1)
        askingnumbers()
    else:
        firstnum = int(firstnum)
        secondnum = int(secondnum)
        numberguesser(firstnum, secondnum)
askingnumbers()
    