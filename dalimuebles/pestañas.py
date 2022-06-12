from doctest import master
import tkinter as tk
from tkinter.messagebox import showinfo
import modelo_peewee
from tkinter import Label, Button, Entry, StringVar, DoubleVar, ttk
from tkinter import *


class Aplicacion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("520x400")
        self.master.configure(background="slate gray")
        self.master.configure(relief="sunken")
        self.pack(side="top")
        self.manejo_botones()
        self.objeto = modelo_peewee.Abmc

    def ventana_alta(self):
        self.master = Toplevel()
        self.master.title("Alta de registro")
        self.master.geometry("820x450")
        self.pack()
        self.master.configure(background="slate gray")

        # --Definimos el Treeview--#
        self.titulo = Label(
            self.master,
            text="ALTA DE REGISTROS.",
            font=("Bahnschrift", 16),
            bg="light goldenrod",
            fg="black",
        )

        self.titulo.place(x=100, y=20, width=600, height=30)
        self.titulo2 = Label(
            self.master,
            text="Ingrese los datos",
            font=("Bahnschrift", 14),
            bg="light goldenrod",
            fg="black",
        )
        self.titulo2.place(x=100, y=60, width=600, height=30)

        self.var_nombre = StringVar()
        self.var_medida = StringVar()
        self.var_descripcion = StringVar()
        self.var_precio = DoubleVar()

        # --Definimos el Treeview--#
        self.nombre = Label(
            self.master,
            text="Nombre (del mueble) ",
            font=("Bahnschrift", 11),
            bg="light goldenrod",
            borderwidth=2,
            fg="black",
        )
        self.nombre.place(x=100, y=100, width=200, height=30)

        self.medida = Label(
            self.master,
            text="Medidas",
            font=("Bahnschrift", 11),
            bg="light goldenrod",
        )
        self.medida.place(x=100, y=150, width=200, height=30)

        self.descripcion = Label(
            self.master,
            text="Detalle",
            font=("Bahnschrift", 11),
            bg="light goldenrod",
        )
        self.descripcion.place(x=100, y=200, width=200, height=30)

        self.precio = Label(
            self.master,
            text="Precio",
            font=("Bahnschrift", 11),
            bg="light goldenrod",
        )
        self.precio.place(x=100, y=250, width=200, height=30)

        """Capturando los datos"""

        self.entry_nombre = Entry(
            self.master,
            textvariable=self.var_nombre,
        )
        self.entry_nombre.place(x=300, y=100, width=400, height=30)

        self.entry_medida = Entry(self.master, textvariable=self.var_medida)
        self.entry_medida.place(x=300, y=150, width=400, height=30)

        self.entry_descripcion = Entry(self.master, textvariable=self.var_descripcion)
        self.entry_descripcion.place(x=300, y=200, width=400, height=30)

        self.entry_precio = Entry(self.master, textvariable=self.var_precio)
        self.entry_precio.place(x=300, y=250, width=400, height=30)

        """Botonera"""
        ###--Boton guardar
        self.boton_guardar = Button(
            self.master,
            text="Guardar",
            command=lambda: self.objeto.funcion_g(
                self,
                self.var_nombre,
                self.var_medida,
                self.var_descripcion,
                self.var_precio,
            ),
            activebackground="light goldenrod",
            foreground="black",
            height=2,
            width=9,
            font=("Bahnschrift", 13),
        )
        self.boton_guardar.place(x=250, y=300, width=300, height=40)

    def ver_productos(self):
        self.master = Toplevel()
        self.master.title("Lista de productos")
        self.master.geometry("820x550")
        self.master.configure(background="slate gray")

        # --Definimos el Treeview--#
        self.titulo = Label(
            self.master,
            text="Arrancá con fuerza.",
            font=("Bahnschrift", 14),
            bg="light goldenrod",
            fg="black",
        )
        self.titulo.place(x=200, y=20, width=400, height=30)
        self.titulo2 = Label(
            self.master,
            text="Lista de productos.",
            font=("Bahnschrift", 16),
            bg="light goldenrod",
            fg="black",
        )
        self.titulo2.place(x=200, y=60, width=400, height=30)

        self.tree_principal = ttk.Treeview(self.master)

        self.tree_principal["columns"] = ("nombre", "med", "desc", "precio")

        self.tree_principal.place(x=10, y=130, width=800, height=250)

        self.tree_principal.column("#0", width=50, minwidth=50, anchor=CENTER)
        self.tree_principal.column("nombre", width=240, minwidth=200)
        self.tree_principal.column("med", width=100, minwidth=50, anchor=W)
        self.tree_principal.column("desc", width=270, minwidth=200)
        self.tree_principal.column("precio", width=80, minwidth=50)

        self.tree_principal.heading("#0", text="ID")
        self.tree_principal.heading("nombre", text="Nombre del mueble", anchor=W)
        self.tree_principal.heading("med", text="Medida")
        self.tree_principal.heading("desc", text="Descripción", anchor=W)
        self.tree_principal.heading("precio", text="Precio", anchor=W)
        self.objeto.actualizar_treeview(self, self.tree_principal)

        """Boton borrar"""
        self.boton_borrar = Button(
            self.master,
            text="Borrar",
            command=lambda: self.objeto.funcion_b(self, self.tree_principal),
            activebackground="red",
            foreground="black",
            activeforeground="#CCDDFD",
            height=2,
            width=9,
            font=("Bahnschrift", 12),
        )
        self.boton_borrar.place(x=20, y=400, width=100, height=40)

        """Boton abrir ventana"""
        self.boton_abrir_formu = Button(
            self.master,
            text="Modificar",
            command=lambda: self.window_datos(),
            activebackground="blue",
            foreground="black",
            activeforeground="white",
            height=2,
            width=9,
            font=("Bahnschrift", 12),
        )
        self.boton_abrir_formu.place(x=150, y=400, width=100, height=40)
        """Boton refresh ventana"""
        self.boton_actualiza = Button(
            self.master,
            text="Actualizar",
            command=lambda: self.objeto.actualizar_treeview(self, self.tree_principal),
            activebackground="SpringGreen2",
            foreground="black",
            activeforeground="white",
            height=2,
            width=9,
            font=("Bahnschrift", 12),
        )
        self.boton_actualiza.place(x=290, y=400, width=100, height=40)


    def window_datos(self):
        self.master = Toplevel()
        self.label = Label(self.master, text="Ingrese nuevo nombre: ")
        self.label.pack(fill="x", padx=100, pady=5)
        self.nuevo_nombre = StringVar()
        self.entry = Entry(self.master, textvariable=self.nuevo_nombre)
        self.entry.pack(fill="x", padx=50, pady=5)

        self.label2 = Label(self.master, text="Ingrese nueva medida: ")
        self.label2.pack(fill="x", padx=50, pady=5)
        self.nuevo_medida = StringVar()
        self.entry2 = Entry(self.master, textvariable=self.nuevo_medida)
        self.entry2.pack(fill="x", padx=50, pady=5)

        self.label3 = Label(self.master, text="Ingrese nueva descripción: ")
        self.label3.pack(fill="x", padx=50, pady=5)
        self.nuevo_descripcion = StringVar()
        self.entry3 = Entry(self.master, textvariable=self.nuevo_descripcion)
        self.entry3.pack(fill="x", padx=50, pady=5)

        self.label4 = Label(self.master, text="Ingrese nuevo precio: ")
        self.label4.pack(fill="x", padx=50, pady=5)
        self.nuevo_precio = IntVar()
        self.entry4 = Entry(self.master, textvariable=self.nuevo_precio)
        self.entry4.pack(fill="x", padx=50, pady=5)
        """Boton modificar"""
        self.boton_modificar = Button(
            self.master,
            text="Confirmar los cambios",
            command=lambda: self.objeto.funcion_m(
                self,
                self.tree_principal,
                self.nuevo_nombre,
                self.nuevo_medida,
                self.nuevo_descripcion,
                self.nuevo_precio,
            ),
            activebackground="light salmon",
            foreground="black",
            activeforeground="white",
            height=2,
            width=9,
            font=("Bahnschrift", 12),
        )
        self.boton_modificar.pack(fill="x")
        self.objeto.actualizar_treeview(self, self.tree_principal)

    def manejo_botones(self):
        self.titulo2 = Label(
            self.master,
            text="Bienvenid@s a Dalimuebles.",
            font=("Bahnschrift", 16),
            bg="light goldenrod",
            fg="black",
        )
        self.titulo2.place(x=10, y=10, width=500, height=50)
        self.boton1 = tk.Button(
            self.master,
            text="INTEGRANTES DEL GRUPO",
            font=("Bahnschrift", 10),
            width=25,
            borderwidth=2,
            bg="alice blue",
            activebackground="light goldenrod",
            command=self.hago_algo,
        )
        self.boton1.place(x=10, y=70, width=500, height=40)
        self.boton2 = tk.Button(
            self.master,
            text="ALTA DE PRODUCTO",
            font=("Bahnschrift", 10),
            width=25,
            borderwidth=2,
            bg="alice blue",
            activebackground="light goldenrod",
            command=self.ventana_alta,
        )
        self.boton2.place(x=10, y=130, width=500, height=40)

        self.boton3 = tk.Button(
            self.master,
            text="VER PRODUCTOS",
            font=("Bahnschrift", 10),
            width=25,
            borderwidth=2,
            bg="alice blue",
            activebackground="light goldenrod",
            command=self.ver_productos,
        )
        self.boton3.place(x=10, y=190, width=500, height=40)
        self.salir = tk.Button(
            self.master,
            text="SALIR",
            font=("Bahnschrift", 10),
            activebackground="light goldenrod",
            width=25,
            bg="alice blue",
            borderwidth=2,
            command=self.master.destroy,
        )
        self.salir.place(x=10, y=250, width=500, height=40)

    def hago_algo(self):
        showinfo(
            "INFO", "Trabajo realizado por Gaston Cipolla, Pablo Délia y Lucas Cipolla"
        )
