from tkinter import * 
import random
# variables globales
base = 460
altura = 240
ventana_principal = Tk()

ventana_principal.title("Graficador 2D - Lineas Rectas")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False, False)

ventana_principal.config(bg="black")

# frame graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=250)
frame_graficacion.place(x=10,y=10)

# creacion canva
c = Canvas(frame_graficacion, width=base, height=altura)
c.config(bg="yellow")
c.place(x=10,y=10)

# graficacion

for i in range(100):
   x = random.randint(0,base-20)
   y = random.randint(0,altura-20)
   color = "#"
   for j in range(6):
     color = color + random.choice("0123456789abcdef")
   circulo = c.create_oval(x,y,x + 20,y + 20, fill=color)
   



# desplegar ventana
ventana_principal.mainloop()