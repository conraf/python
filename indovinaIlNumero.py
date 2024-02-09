import random

def play_game():
    """
    Un gioco dove devi indovinare un numero tra 1 e 100.
    """
    secret_number = random.randint(1, 100)
    print("Indovina il numero che sto pensando!")
    print("E' un numero compreso tra 1 e 100...")

    for _ in range(10): # Limita il numero di tentativi a 10, modifica il valore tra parentesi se vuoi.
        guess = int(input("Scrivilo qui: "))
        if guess < secret_number:
            print("Troppo basso! Prova ancora.")
        elif guess > secret_number:
            print("Troppo alto! Prova ancora.")
        else:
            print("Congratulazioni! Hai indovinato il numero in {} tentativi.".format(_+1))
            break

    if _ >= 7:
        print("Peccato, non hai indovinato il numero nei tentativi previsti. Il numero era: {}".format(secret_number))

if __name__ == "__main__":
    play_game()