import random
import time

def main():
    # Domanda al giocatore per il tempo di gioco (30, 20, o 15 secondi)
    print("GLI AMICI DEL 10: indica il numero corretto:")
    
    while True:
        # Scegliere tra i tempi 30, 20, 15
        tempo_di_gioco = input("Quanti secondi vuoi giocare? (30, 20, 15 o 10): ")
        
        if tempo_di_gioco in ['30', '20', '15', '10']:
            break
        else:
            print("Scelta non valida. Scegli tra 30, 20, 15 o 10 secondi.")
    
    # Convertire la scelta in un intero per il calcolo del tempo
    tempo_di_gioco = int(tempo_di_gioco)
    
    # Inizializza il punteggio
    score = 0
    
    start_time = time.time()  # Registra l'ora di inizio del gioco
    used_numbers = []  # Lista per tenere traccia dei numeri già utilizzati
    
    while True:
        # Scegli un numero casuale tra 1 e 9 che non sia stato già usato
        while True:
            numero_scelto = random.randint(1, 9)
            if numero_scelto not in used_numbers:
                break
        
        used_numbers.append(numero_scelto)  # Aggiungi il numero alla lista dei numeri utilizzati
        
        # Calcola il numero che quando sommato a `numero_scelto` dà 10
        numero_da_indovinare = 10 - numero_scelto
        
        print(f"{numero_scelto}")
        
        try:
            # Richiedi all'utente di inserire il suo numero
            guess = int(input(""))
            
            if guess == numero_da_indovinare:
                print(f"Ottimo!")
                
                # Incrementa il punteggio se l'utente ha indovinato correttamente
                score += 1
            else:
                print("Purtroppo non hai indovinato il numero. Prova ancora!\n")
                while guess != numero_da_indovinare:
                    print(f"Qual'è l'amico del 10 di {numero_scelto} ? (Risposta precedente: {guess})")
                    guess = int(input("Inserisci il tuo numero: "))
        
        except ValueError:
            print("Inserisci un numero valido tra 1 e 9.\n")
        
        # Controlla se il tempo è scaduto
        elapsed_time = time.time() - start_time
        
        if len(used_numbers) == 9 or elapsed_time >= tempo_di_gioco:  # Esci dal ciclo se i numeri sono stati usati o il tempo è scaduto
            break
    
    # Mostra il punteggio totale alla fine del gioco
    print(f"Tempo di gioco terminato. Punteggio totale: {score}")

if __name__ == "__main__":
    main()