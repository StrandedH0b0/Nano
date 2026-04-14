import subprocess
import sys


def main_menu():
    while True:
        print("\n=== Nano hoofdmenu ===")
        print("1. Raad het nummer")
        print("2. Galgje")
        print("3. Word Scramble")
        print("4. Hoger Lager")        
        print("5. Woordenboek")
        print("6. Afsluiten")

        keuze = input("Maak een keuze (1-6): ")

        if keuze == "1":
            print("\nStart Raad het nummer...\n")
            subprocess.run([sys.executable, "RaadHetNummer.py"])

        elif keuze == "2":
            print("\nStart Galgje...\n")
            subprocess.run([sys.executable, "Galgje.py"])

        elif keuze == "3":
            print("\nWord Scramble...\n")
            subprocess.run([sys.executable, "WordScramble.py"])    

        elif keuze == "4":
            print("\nHoger Lager...\n")
            subprocess.run([sys.executable, "HogerLager.py"])    

        elif keuze == "5":
            print("\nWoordenboek...\n")
            subprocess.run([sys.executable, "EngelsWoordenboek.py"])
        elif keuze == "6":
            print("Programma wordt afgesloten.")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main_menu()