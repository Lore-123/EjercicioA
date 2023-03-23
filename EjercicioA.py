#LORENZO HERNANDEZ HERNANDEZ 41 S 
#MARIA JENNIFER CARBAJAL MARTINEZ 41 S
#EJERCICIO A  REGISTRO PRODUCTOS 
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
root = Tk()

ventanaPrincipal = Frame(root, bg="#0099FF")
ventanaPrincipal.grid()
ventanaPrincipal = Frame(root,bg="#a0a0a0").grid()
Regris = Label(ventanaPrincipal, text="REGISTRO DE PRODUCTOS", bg="#CCCCCC", font=("Roboto",10)).grid(row=3,column=2)

imge = Image.open("C:\\Users\\nisha\\OneDrive\\Escritorio\\TECNOLOGICO\\4to Semestre\\PROGRA VIS\\res.jpg")
imagens = imge.resize((50,50))
imagenA = ImageTk.PhotoImage(imagens)
Ponerimagen = Label(ventanaPrincipal, image=imagenA).grid(row=5,column=2,columnspan=1,rowspan=2)

Prod = Label(ventanaPrincipal, text="Producto:", bg="#CCCCCC", font=("Roboto",10)).grid(row=10,column=1)
Sku = Label(ventanaPrincipal, text="SKU:", bg="#CCCCCC", font=("Roboto",10)).grid(row=11,column=1)
registro = Entry(ventanaPrincipal, bg="#CCCCCC", font=("Roboto",10)).grid(row=10,column=2, padx=1,pady=5)
productos = Entry(ventanaPrincipal, bg="#CCCCCC", font=("Roboto",10)).grid(row=11,column=2, padx=1,pady=5)
depto = Label(ventanaPrincipal, bg="#CCCCCC", text=("Depto:"),font=("Roboto",10)).grid(row=13,column=1)
Ba = tk.Checkbutton(ventanaPrincipal, text="A", bg="#CCCCCC", font=("Roboto",10)).grid(row=15,column=1)
Bb = tk.Checkbutton(ventanaPrincipal, text="B",bg="#CCCCCC", font=("Roboto",10)).grid(row=15,column=2)
Bc = tk.Checkbutton(ventanaPrincipal, text="C", bg="#CCCCCC",font=("Roboto",10)).grid(row=15,column=3)

provedor = Label(ventanaPrincipal, bg="#CCCCCC",text="Proveedor:", font=("Roboto",10)).grid(row=16,column=1)
lista_desplegable = ttk.Combobox(ventanaPrincipal,width=17)
lista_desplegable.grid(row=16,column=2)
opciones = ["Ni entiendo", "Poli estacion", "Xboss"]
lista_desplegable['values']=opciones
  
idioma = Label(ventanaPrincipal, bg="#CCCCCC",text="Idioma:", font=("Roboto",10)).grid(row=17,column=1)
Be = tk.Checkbutton(ventanaPrincipal, bg="#CCCCCC", text="EN",font=("Roboto",10)).grid(row=18,column=1)
Bs = tk.Checkbutton(ventanaPrincipal, bg="#CCCCCC", text="ESP",font=("Roboto",10)).grid(row=18,column=2)

registrar = Button(ventanaPrincipal, text=("Registrar"), font=("Roboto",10),width=20,height=1).grid(row=25,column=2,padx=1,pady=5)


root.mainloop()