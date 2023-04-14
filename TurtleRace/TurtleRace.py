import turtle
import random


s = turtle.Screen()
s.title("Turtle Race")
s.bgcolor("#D7F2FC")

Tortuga1 = turtle.Turtle()
Tortuga2 = turtle.Turtle()



#Tortuga1.speed(100)
Tortuga1.hideturtle()
Tortuga1.shape("turtle")
Tortuga1.color("green", "green")
Tortuga1.shapesize(2,2,2)
Tortuga1.pensize(3)


#Tortuga2.speed(100)
Tortuga2.hideturtle()
Tortuga2.shape("turtle")
Tortuga2.color("blue", "blue")
Tortuga2.shapesize(2,2,2)
Tortuga2.pensize(3)




#creacion de la meta tortuga 1
Tortuga1.penup()
Tortuga1.goto(300,200)
Tortuga1.pendown()
Tortuga1.circle(40)
#colocar la tortuga 1en su punto de partida
Tortuga1.penup()
Tortuga1.goto(-300,235)
Tortuga1.showturtle()

#creacion de la meta tortuga 2
Tortuga2.penup()
Tortuga2.goto(300,-100)
Tortuga2.pendown()
Tortuga2.circle(40)
#colocar la tortuga 2 en su punto de partida
Tortuga2.penup()
Tortuga2.goto(-300,-60)
Tortuga2.showturtle()


dado = [1,2,3,4,5,6]




for i in range(20):
    if Tortuga1.pos() >= (300,200):
        print("La tortuga verde ganó")
        break
    elif Tortuga2.pos() >= (300,-100):
        print("La tortuga azul ganó")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar la tortuga verde.")
        turno1 = random.choice(dado)
        print("Tú numero es: ", turno1, "\nAvanzas: ",turno1*20)
        Tortuga1.pendown()
        Tortuga1.fd(20*turno1)
        
        turno2 = input("Presiona la tecla enter para avanzar la tortuga azul.")
        turno2 = random.choice(dado)
        print("Tú numero es: ", turno2, "\nAvanzas: ",turno2*20)
        Tortuga2.pendown()
        Tortuga2.fd(20*turno2)
        



turtle.done()