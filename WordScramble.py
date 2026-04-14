import random

woorden = ["python", "computer", "school", "programmeren", "toetsenbord"]

def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def Logic(word, guess):
    if guess == word:
        messages(1)
        return True
    else:
        messages(2)
        return False

def messages(message):
    if message == 1:
        print("Goed geraden!!!")

    if message == 2:
        print("Fout geraden!")

    if message == 3:
        print("Raad het woord:")

    if message == 4:
        print("Typ 'exit' om terug te gaan")

def main():
    messages(4)
    punten = 0

    while True:
    
        word = random.choice(woorden)
        scrambled = shuffle_word(word)

        print(f"Je hebt nu {punten} punten!!")
        messages(3)
        print(scrambled)

        guess = input("Jouw antwoord: ")

        if guess == "exit":
            print(f"Het woord was {word}")
            exit()

        if Logic(word, guess) == True:
            punten = punten + 1


main()