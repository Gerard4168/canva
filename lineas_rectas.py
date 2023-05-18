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
'''''linea1 = c.create_line(10,10, base-10,10, fill="red", width=5)
linea2 = c.create_line(base-10,10,base-10, altura-10, fill="red", width=5)
linea3 = c.create_line(base-10,altura-10,10, altura-10, fill="red", width=5)
linea4 = c.create_line(10,altura-10,10,10, fill="red", width=5)
linea5 = c.create_line(10,10,base-10,altura-10,fill="red4")
linea6 = c.create_line(10,altura-10, base-10,10, fill="red4")'''

# texto
''''texto1 = c.create_text(base/2,altura/2, text="SISTEMAS UIS SOCORRO", anchor="w", font=("Arial", "20", "bold"), fill="green2", activefill="white")'''

# cuadrados y rectangulos
''''rect1 = c.create_rectangle(20,20, 120,120, fill="blue", outline="red2", width="3")'''


# poligonos
mi_color = "#FF5733"
poligono1 = c.create_polygon((base/2)/2,0,base/2,(altura/2)/2,(base/2)/2,altura/2,0,(altura/2)/2, fill="cyan", outline="green")
poligono1 = c.create_polygon((base/2)*1.5,0,base,(altura/2)/2,(base/2)*1.5,altura/2,base/2,(altura/2)/2, fill="cyan", outline="green")
poligono1 = c.create_polygon((base/2)/2,altura/2,base/2,(altura/2)*1.5,(base/2)/2,altura,0,(altura/2)*1.5, fill="cyan", outline="green")
poligono1 = c.create_polygon((base/2)*1.5,altura/2,base,(altura/2)*1.5,(base/2)*1.5,altura,base/2,(altura/2)*1.5, fill="cyan", outline="green")

# ovalo - circulo
elip1 = c.create_oval( (base/4)-30,(altura/4)-30,(base/4)+30,(altura/4)+30, fill="orange")
elip2 = c.create_oval( (base/4.2)-5,(altura/4.2)-5,(base/4.3)+5,(altura/4.3)+5, fill="black")
elip1 = c.create_oval( (base/1.33)-30,(altura/1.33)-30,(base/1.33)+30,(altura/1.33)+30, fill="orange")
elip2 = c.create_oval( (base/1.36)-5,(altura/1.36)-5,(base/1.36)+5,(altura/1.36)+5, fill="black")
elip1 = c.create_oval( (base/4)-30,(altura/1.33)-30,(base/4)+30,(altura/1.33)+30, fill="orange")
elip1 = c.create_oval( (base/4)-5,(altura/1.4)-5,(base/4)+5,(altura/1.4)+5, fill="black")
elip1 = c.create_oval( (base/1.33)-30,(altura/4)-30,(base/1.33)+30,(altura/4)+30, fill="orange") 
elip1 = c.create_oval( (base/1.35)-5,(altura/4.2)-5,(base/1.35)+5,(altura/4.2)+5, fill="black")
# arcos
arc1 = c.create_arc( (base/4)-30,(altura/4)-30,(base/4)+30,(altura/4)+30, start=330, extent=40, fill="white")
arc1 = c.create_arc( (base/1.33)-30,(altura/1.33)-30,(base/1.33)+30,(altura/1.33)+30, start=330, extent=40, fill="white")
arc1 = c.create_arc( (base/4)-30,(altura/1.33)-30,(base/4)+30,(altura/1.33)+30, start=330, extent=40, fill="white")
arc1 = c.create_arc( (base/1.33)-30,(altura/4)-30,(base/1.33)+30,(altura/4)+30, start=330, extent=40, fill="white")

# desplegar ventana
ventana_principal.mainloop()






























