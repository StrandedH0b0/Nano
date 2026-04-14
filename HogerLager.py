import random

def Logic(current, next_card, guess):
    
    if guess == "hoger":
        if next_card > current:
            messages(1, next_card)
            return True
        else:
            messages(2, next_card)
            return False

    if guess == "lager":
        if next_card < current:
            messages(1, next_card)
            return True
        else:
            messages(2, next_card)
            return False

    messages(3, next_card)
    return False


def messages(message, number):
    
    if message == 1:
        print(f"Goed! Het volgende getal was {number}")

    if message == 2:
        print(f"Fout! Het volgende getal was {number}")

    if message == 3:
        print("Typ 'hoger' of 'lager'!")

    if message == 4:
        print("=== HOGER / LAGER ===")

    if message == 5:
        print("Typ 'exit' om te stoppen")


def main():
    current = random.randint(1, 13)
    score = 0

    messages(4, 0)
    messages(5, 0)

    while True:
        print(f"\nHuidige kaart: {current}")

        guess = input("Hoger of lager?: ")

        if guess == "exit":
            print(f"Je score was: {score}")
            exit()

        next_card = random.randint(1, 13)

        win = Logic(current, next_card, guess)

        if win == True:
            score = score + 1
            current = next_card
        else:
            print(f"Game over! Score: {score}")
            exit()


main()