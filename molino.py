from tkinter import * 
import random
# variables globales
base = 460
altura = 240
radio = 50
angulo2 = 90
# funcion para modificar arco
def modificar(angulo):
    c.itemconfig(arco,extent=angulo)
    c.itemconfig(arco,start=angulo)
    c.itemconfig(arco2,start=angulo)
    c.itemconfig(arco3,start=angulo)


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
c.config(bg="cyan")
c.place(x=10,y=10)

# arco
arco = c.create_arc(base/2-radio,altura/2-radio,base/2+radio,altura/2+radio, start=0, extent=45, fill="red4")
arco1 = c.create_arc(base/2-radio,altura/2-radio,base/2+radio,altura/2+radio, start=90, extent=45, fill="green4")
arco2 = c.create_arc(base/2-radio,altura/2-radio,base/2+radio,altura/2+radio, start=180, extent=45, fill="yellow2")
arco3 = c.create_arc(base/2-radio,altura/2-radio,base/2+radio,altura/2+radio, start=240, extent=45, fill="green4")
base = c.create_polygon(base/2,altura/2,base/3,altura-10,base/1.5,altura-10, fill="black", outline="green")

# frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="black", width=480, height=240)
frame_controles.place(x=10,y=260)

# barra de deslizamiento
barra_deslizamiento = Scale(frame_controles,label="Angulo", from_=0, to=360, orient="horizontal", length=455, tickinterval=90, command=modificar)
barra_deslizamiento.place(x=10,y=10)



# desplegar ventana
ventana_principal.mainloop()