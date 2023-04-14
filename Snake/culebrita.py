import turtle
#se importa para que se mueva cada x tiempo
import time
#para colocar la comida en lugares aleaotrios
import random

retraso = 0.1
marcador = 0
marcadorMaximo = 0




s = turtle.Screen()
#le da un tamaño en pixeles al screen
s.setup(650,650)
s.bgcolor("gray")
s.title("Nokia 1100")
s.tracer()



culebrita = turtle.Turtle()
culebrita.speed(1)
#cambiar la forma de la culebrita
culebrita.shape("square")
#quitar el rastro o pintura de la culebrita
culebrita.penup()
#colocacion del jugador
culebrita.goto(0,0)
#cuando el programa termine que se reinicie el programa pero que no se mueva mas?
#darle movimiento, el movimiento depende de esta variable
culebrita.direction = "stop"
culebrita.color("green")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("Black")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Marcador: 0 \t Marcador más alto: 0", align="center", font= ("verdana", 20, "normal"))



def arriba():
    culebrita.direction = "up"
    
def abajo():
    culebrita.direction = "down"
    
def derecha():
    culebrita.direction = "right"
    
def izquierda():
    culebrita.direction = "left"


#darle movimiento 
def movimiento():
    if culebrita.direction == "up":
        #es como el metodo pos pero solo devuelve la coordenada en y
        y = culebrita.ycor()
        #movimiento en eje y y designar movimiento hacia arriba
        culebrita.sety(y + 20)
    if culebrita.direction == "down":
        y = culebrita.ycor()
        culebrita.sety(y - 20)
    if culebrita.direction == "right":
        x = culebrita.xcor()
        culebrita.setx(x + 20)
    if culebrita.direction == "left":
        x = culebrita.xcor()
        culebrita.setx(x - 20)
#coloca la pantalla a esperar un estimulo de teclado       
s.listen()
#En mayuscula la primera porque hace referencia a la tecla 
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")





#darle movimiento 
#este es el loop
while True:
    #actualiza la pantalla
    s.update()
    
    if culebrita.xcor() > 300 or culebrita.xcor() < -300 or culebrita.ycor() > 300 or culebrita.ycor() < -300:
        #poner una pequeña pausa, luego el for recorre la lista y limpia para reiniciar
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            #ocultar culebrita
            i.hideturtle()
        culebrita.home()
        culebrita.direction = "stop"
        cuerpo.clear()
        
        
        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcadorMaximo), align="center", font= ("verdana", 20, "normal"))

    
    #20 porque ese es el tamaño de la culebrita
    if culebrita.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)
        
        agregarCuerpo = turtle.Turtle()
        agregarCuerpo.shape("square")
        agregarCuerpo.color("green")
        agregarCuerpo.penup()
        agregarCuerpo.goto(0,0)
        agregarCuerpo.speed(0)
        cuerpo.append(agregarCuerpo)
        
        marcador += 10
        if marcador > marcadorMaximo:
            marcadorMaximo = marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcadorMaximo), align="center", font= ("verdana", 20, "normal"))
        
    total = len(cuerpo)
        #inicia desde -1 porque los segmentos van a iniciar a la par de la serpiente, 
        # no hasta atras, 0 hace referencia a que no se cuenta, porque es la cabeza
        #y 1 va la cuenta de -1 en -1
    for index in range (total -1,0,-1):
        #i-1 porque no quiero que inicie en el 0
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        #enviar dicho cuerpo a la par de la culebrita
        cuerpo[index].goto(x,y)
            
        #si en la lista hay un cuerpo, enviar el cuerpo a la unicacion de la culebrita
        #para que siga la cabeza
    if total >0:
        x = culebrita.xcor()
        y = culebrita.ycor()
        cuerpo[0].goto(x,y)
            
            
            
            

    
    movimiento()
    
    for i in cuerpo:
        if i.distance(culebrita) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            culebrita.home()
            cuerpo.clear()
            culebrita.direction = "stop"
            
            marcador = 0
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcadorMaximo), align="center", font= ("verdana", 20, "normal"))

    #ponerle delay al movimiento de la culebrita
    time.sleep(retraso)
    
turtle.done()