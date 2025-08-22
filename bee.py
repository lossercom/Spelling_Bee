Word = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(Word) > 0:
        print(f"{len(Word)} Left!")
        guess = input("Guess a Word: ")
        if guess == "GRAPHIC":
            Word.clear()
            print("You've won!")
        elif guess in Word.keys():
            Points = Word.pop(guess)
            print(f"Good job! Your scored {Points} Points.")
    print("That's the game!")

main()