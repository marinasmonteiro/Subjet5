
def play():
    secret_color="green"
    secret_number=6

    guess_number=input("Chose a number between 1 and 20:")
    guess_color=input("chose a color:")


    if secret_number==int(guess_number) and secret_color==guess_color:
        print("you've found both the secret number and the secret color!")
    elif secret_number==int(guess_number) or secret_color==guess_color:
        print("You found at least one of the secrets!")
    else:
        print("You didnt find any of the secrets!")
        print("Better luck next time!")

    print("Try again!")

play()
