import turtle, random
from random import randint
turtle.Screen().bgcolor("lightblue")	# Imposto il colore di sfondo
turtle.hideturtle()						# Nascondo turtle

# Creo il mio dizionario: a ogni lettera corrisponde un'inclinazione in gradi.
# Le lettere sono separate una dall'altra da 7 gradi di inclinazione.
lettere={'a':7,'b':14,'c':21,'d':28,'e':35,'è':35,'é':35,'f':42,'g':49,'h':56,'i':63,'j':70,'k':77,'l':84,'m':91,'n':98,'o':105,'p':112,'q':119,'r':126,'s':133,'t':140,'u':147,'v':154,'w':161,'x':168,'y':175,'z':182}

# Disegno il vaso dell'albero
turtle.penup()
turtle.goto(-100,-300)
turtle.color("brown")
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.forward(200)
turtle.right(135)
turtle.forward(100)
turtle.right(45)
turtle.forward(50)
turtle.end_fill()

for i in range(14):
    # Chiedo agli studenti di inserire il proprio pensiero, uno dopo l'altro.
    pensiero=input("Scrivi qui il tuo pensiero: ")
    # Separo la frase in singole parole.
    lista=pensiero.lower().split()	# Oltre a splittare la frase, il metodo lower la trasforma tutta in minuscolo
    print(lista)
    L=len(lista)
    # Sposto Turtle nella posizione iniziale senza disegnare nulla e orientandola correttamente.
    turtle.penup()
    turtle.goto(0,-300)
    # Chiedo a Turtle di scegliere un colore random.
    colors=["magenta","red","green","blue","orange","purple","yellow","indigo","beige","brown","black","white","pink"]
    color=random.choice(colors)
    turtle.color(color)
    # Imposto la larghezza del tratto
    turtle.pensize(8)
    # Preparazione del disegno della singola frase
    for i in range(L):
        x=lista[i]					# La lista delle parole diventa x
        iniziale=x[0]				# Considero solamente la lettera iniziale di ogni parola
        y=lettere[iniziale]			# Questa lettera diventa y
        # Ora dsegno materialmente la singola frase
        turtle.pendown()			# Giù la penna per scrivere
        turtle.right(y)				# Inclino di y gradi a seconda della corrispondenza indicata nel dizionario tra lettere e gradi
        turtle.forward(len(x)*10)	# Disegno il segmento-parola per una lunghezza pari a 10 volte il numero di lettere di quella parola
        turtle.left(y)				# Resetto l'inclinazione di turtle ruotandola in senso opposto degli stessi y gradi 

# DECORAZIONI: Scritta centrale e fiocchi di neve

# Aumento la velocità di turtle per fare prima
turtle.speed(10000)
turtle.pensize(4)

# Definisco una funzione per settare il colore, le coordinate e le dimensioni dei fiocchi di neve
def fiocco(color,x,y,size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.left(90)

# Inizio del loop per creare le forme dei fiocchi di neve
    for i in range(0,branches):
        # creo le forme dei fiocchi di neve
        turtle.forward(100*size/100)
        turtle.backward(40*size/100)
        turtle.left(40)
        turtle.forward(30*size/100)
        turtle.backward(30*size/100)
        turtle.right(80)
        turtle.forward(30*size/100)
        turtle.backward(30*size/100)
        turtle.left(40)
        turtle.backward(40*size/100)
        turtle.left(40)
        turtle.forward(30*size/100)
        turtle.backward(30*size/100)
        turtle.right(80)
        turtle.forward(30 * size / 100)
        turtle.backward(30 * size / 100)
        turtle.left(40)
        turtle.backward(20*size/100)
        turtle.right(360/branches)

# Scritta centrale
turtle.color("green")
style=('Times',40,'italic')
turtle.write('Vi auguriamo\nBuone Feste!', font=style,align='center')

# Disegno 10 fiocchi di neve decorativi
for i in range(0,10):
    randomX = randint(-350,350)
    randomY = randint(-350,350)
    randomSize = randint(20,60)
    branches=randint(5,8)
    fiocco("white",randomX,randomY,randomSize)
turtle.done()