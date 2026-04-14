import random

def Logic(number, guess):
    if guess > 100 :
        messages(1)
        WinCon = False
        return WinCon
    
    if guess < 0 :
        messages(2)
        WinCon = False
        return WinCon
    
    if number == guess:
        messages(3)
        WinCon = True
        return WinCon

    if number < guess:
        messages(4)
        WinCon = False
        return WinCon

    if number > guess:
        messages(5)
        WinCon = False
        return WinCon

def messages(message):
    if message == 1:
        print("Het getal is altijd onder de 100.")

    if message == 2:
        print("Het getal kan niet minder zijn dan 0.")

    if message == 3:
        print("goed geraden!!!")

    if message == 4:
        print("Het nummer die je zoekt is lager!")

    if message == 5:
        print("Het nummer die je zoekt is hoger!")
    
    if message == 6:
        print("Raad het nummer tussen 0 en 100")

    if message == 7:
        print("Je kan altijd exit invoeren om terug te gaan naar het hoofd scherm")

def main():
    number = random.randint(0,100)
    WinCon = False

    messages(6)
    messages(7)


    while WinCon == False :
        
        guess= input("Voer jouw gok in: ")

        if guess.isnumeric():
            guess= int(guess)
            WinCon = Logic(number, guess)
            continue
            
        if guess.isalpha:
            if guess == str("exit"):
                print(f"het antwoord was {number}")
                exit()
            else:
                print("Je mag geen woorden raden... Dat is galgje!")
                continue



main()