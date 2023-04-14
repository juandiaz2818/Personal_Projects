import tkinter as tk    #esta libreria es la que crea una ventana para hacer los botones y todo lo de adivinar la palabra
import turtle    #esta libreria es usada para Dibujamos el ahorcado
import random   #con esta libreria puedes elegir una palabra random en el arreglo "palabras"
from tkinter import messagebox  #con esta libreria puedes abrir una ventana de alerta como la de  el juego se termino 
# Palabaras para adivinar
palabras = ["python", "java", "html", "devoloper", "enginieer", "code", "desktop", "software"]
palabra = random.choice(palabras)


# Inicializa las letras adivinadas
letras_encontradas = set()

# Iniciar contador de fallos
fallos = 0


#estas son las coordenadas utilizadas para  guiar a la "tortuga" a los puntos donde debe ir para así Dibujamos  correctamente
punto_base = (-100, -100)
punto_mensaje = (-120, 80)
punto_palo = (60, -100)
punto_travesano = (60, 100)
punto_cuerda = (-39,100)
punto_cabeza = (-38, 31)
punto_cuerpo = (-38, 31)
punto_brazo_izquierdo = (-38, 25)
punto_brazo_derecho = (-38, 25)
punto_pierna_izquierda = (-38, -49)
punto_pierna_derecha = (-38, -49)


def dibujar_ahorcado():

    # Dibujamos la base, escondemos el lapiz y aumentamos la velocidad
    turtle.hideturtle()
    turtle.pensize(3)
    turtle.speed(100)
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_base)
    turtle.pendown()
    turtle.forward(200)

    #Dibujamos el poste principal
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_palo)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(200)
    # Dibujamos el poste  donde ira colgado  Alex
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_travesano)
    turtle.pendown()
    turtle.left(180)
    turtle.forward(100)
    
def draw_head():
    
    #Dibujamos la cuerda
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_cuerda)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(30)
    
    # Dibujamos cabeza
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_cabeza)
    turtle.pendown()
    turtle.circle(20)
    
   
    # Dibujamos el ojo de la izquierda
    turtle.penup()
    turtle.goto(-51,62)
    turtle.pendown()
    turtle.goto(-44,54)
    turtle.penup()
    turtle.goto(-51,54)
    turtle.pendown()
    turtle.goto(-44,62)

     # Dibujamos el ojo de la derecha
    turtle.penup()
    turtle.goto(-32,61)
    turtle.pendown()
    turtle.goto(-26,54)
    turtle.penup()
    turtle.goto(-32,54)
    turtle.pendown()
    turtle.goto(-26,61)
    #Dibujamos la boca
    turtle.penup()
    turtle.goto(-45,41)
    turtle.pendown()
    turtle.setheading(50)
    turtle.circle(-10, 110)
    
    #Escribimos  el mensaje, ademas  cambiamos el color de la tortuga a azul  para el mensaje y a negro para segir dibujando 
    
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_mensaje)
    turtle.pendown()
    turtle.color("blue")
    turtle.write("Él es Alex, sálvalo por favor :/", align="center", font = ("Comic Sans MS", 16 , "bold")  )
    turtle.color("black")
    

def draw_body():
    # Dibujamos cuerpo
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_cuerpo)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(80)

   
    
def draw_arms():
    # Dibujamos brazo izquierdo
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_brazo_izquierdo)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(40)
    #Dibujamos el brazo derecho
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_brazo_derecho)
    turtle.pendown()
    turtle.left(225)
    turtle.forward(40)


def draw_legs():
    #Dibujamos la pierna izquierda
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_pierna_izquierda)
    turtle.pendown()
    turtle.right(60)
    turtle.forward(45)
    #Dibujamos la pierna derecha 
    turtle.penup()
    turtle.home()
    turtle.setpos(punto_pierna_derecha)
    turtle.pendown()
    turtle.left(240)
    turtle.forward(45)


# Función para actualizar la pantalla en funcion de los intentos 
def actualizar_pantalla():
   
    # Dibujamos ahorcado
    if fallos > 0:
        dibujar_ahorcado()
        if fallos > 1:
            draw_head()
            if fallos > 2:
                draw_body()
                if fallos > 3:
                    draw_arms()
                    if fallos > 4: 
                         draw_legs()
                         #Imprimimos un mensaje en pantalla para darle una ltima posibilidad de sobrevivir a alex
                         messagebox.showinfo("Ultima oportunidad", "Te regalo un ultimo intento para que no muera Alex")
                        
        
    # Crear string de letras encontradas y no encontradas
    letras = ""
    for letra in palabra:
        if letra in letras_encontradas:
            letras += letra
        else:
            letras += "_ "

    # Actualizar etiqueta
    etiqueta.config(text=letras)

# Función para manejar el botón
def boton_presionado():
    # Obtener letra ingresada
    letra = entrada.get()

    # Verificar si la letra está en la palabra
    if letra in palabra:
        letras_encontradas.add(letra)
        Fin_del_juego()
    else:
        global fallos
        fallos += 1
    #Verifica si el numero de intentos es mayor o iguala 6 si es true el juego imprime un mensaje de advertencia de que perdiste, ademas cierra la ventana
    #de tkinter y de la libreria turtle    
    if fallos >= 6:
        messagebox.showerror("PERDISTE! :(", "Alex múrio, le llevaremos la noticia a su familia")
        ventana.destroy()
        turtle.bye()
        
    else:
        # Actualizar pantalla
        actualizar_pantalla()

    # Limpiar entrada
    entrada.delete(0, tk.END)
def Fin_del_juego():
    if set(palabra) == letras_encontradas:
        messagebox.showinfo("Felicidades", "Salvaste la vida de Alex, un criminal...")
        ventana.destroy()
        turtle.bye()

    

# Crear ventana de tkinter
ventana = tk.Tk()
ventana.title("Ahorcado")

# Crear etiqueta para mostrar las letras encontradas
etiqueta = tk.Label(ventana, font=("Comic Sans MS", 24))
etiqueta.pack()

# Crear entrada para ingresar letras
entrada = tk.Entry(ventana, font=("Comic Sans MS", 24))
entrada.pack()

# Crear botón para enviar letra
boton = tk.Button(ventana, text="Probar suerte", command=boton_presionado)
boton.pack()

# Crear pantalla de turtle dentro de la ventana de tkinter
pantalla_turtle = turtle.Screen()
pantalla_turtle.screensize(400, 400)
pantalla_turtle.setworldcoordinates(-200, -200, 200, 200)

# Actualizar pantalla por primera vez
actualizar_pantalla()

# Iniciar loop de tkinter
ventana.mainloop()
