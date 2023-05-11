from tkinter import * 

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

# lineas
linea1 = c.create_line(10,10, base-10,10, fill="red")
linea2 = c.create_line(base-10,10,base-10, altura-10, fill="red")
linea3 = c.create_line(base-10,altura-10,10, altura-10, fill="red")
linea4 = c.create_line(10,altura-10,10,10, fill="red")
linea5 = c.create_line(10,10,base-10,altura-10, fill="red")
linea6 = c.create_line(base-10,10,10,altura-10, fill="red")
linea7 = c.create_line(base-10,10,altura-10,10, fill="green"   )



# desplegar ventana
ventana_principal.mainloop()






























