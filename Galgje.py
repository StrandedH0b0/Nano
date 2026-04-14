import random
from collections import Counter

def wordpicker():
    WordList = ['oosters', 'handboei', 'beroep', 'branding', 'portemonnee']
    Rc = random.randint(0,4)
    Word = WordList[Rc]

    return Word

def guessed(Word, lettersGuessed):
    # Voor elke letter in het woord: toon de letter als die al geraden is, anders een '_'
    for letter in Word:
        if letter in lettersGuessed:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()  # Nieuwe lijn aan het einde voor duidelijkheid


def messages(message, Word):
    if message == 1:
        print("welkom bij galgje. Raad het woord in 10 pogingen!!")
        print("Je kan altijd exit invoeren om terug te gaan naar het hoofd scherm")
        print("Raad een letter of het gehele woord!")
    
    if message == 2:
        print("Je mag alleen maar letters gebruiken")
    
    if message == 3:
        print(f"het antwoord was {Word}")

    if message == 4:
        print(f"CORRECT HET WOORD WAS INDERDAAD {Word}")
        exit()
        
    if message == 5:
        print(f"Je bent helaas af. Het woord was {Word}")
        exit()
    

def main():
    i = False
    Pogingen = 10

    Word = wordpicker()
    messages(1, Word)
    LettersGuessed = ""  # <-- toegevoegd om fout te voorkomen: variabele bestond nog niet

    while i == False:
        try:
            Guess = str(input("Geef letter: "))
        except:
            messages(2, Word)

        LettersGuessed = LettersGuessed + Guess  # letters worden bijgehouden

        guessed(Word, LettersGuessed)  # toont de stand met underscores en goed-geraden letters

        if Guess.isnumeric():
            messages(2, Word)
            continue

        if Guess == "exit":
            messages(3, Word)
            exit()

        if Guess == Word:
            messages(4, Word)
            continue

        if len(Guess) > 1:
            print(f'Het woord dat je hebt geraden is fout. je krijgt {len(Guess)} minder pogingen')
            Pogingen -= len(Guess)

            if Pogingen == 0:
                messages(5, Word)
                exit()

            print(f'Je hebt nog {Pogingen} pogingen')
        
        if len(Guess) == 1:
            if Guess in Word:
                print(f'De letter {Guess} zit in het word.')
                guessed(Word, LettersGuessed)  # update weergave
            else:
                Pogingen -= 1
                print(f"Dat is incorrect! Je hebt nog {Pogingen} pogingen.")

        if Pogingen < 0:
                    messages(5, Word)
                    i = True
                    break        

                   
main()
