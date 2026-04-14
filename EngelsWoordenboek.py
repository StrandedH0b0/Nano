import requests

def Logic(word):
    url = f"https://freedictionaryapi.com/api/v1/entries/en/{word}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            messages(2, word, "")
            return

        data = response.json()

        # eerste betekenis pakken
        definition = data["entries"][0]["senses"][0]["definition"]

        messages(1, word, definition)

    except:
        messages(3, word, "")


def messages(message, word, definition):
    
    if message == 1:
        print(f"\nWoord: {word}")
        print(f"Betekenis: {definition}")

    if message == 2:
        print("Woord niet gevonden.")

    if message == 3:
        print("Fout bij ophalen van data.")

    if message == 4:
        print("=== WOORDENBOEK ===")

    if message == 5:
        print("Typ een Engels woord of 'exit' om te stoppen")


def main():
    messages(4, "", "")
    messages(5, "", "")

    while True:
        word = input("\nVoer woord in: ")

        if word == "exit":
            exit()

        if word.isalpha():
            Logic(word)
        else:
            print("Alleen letters invoeren!")


main()