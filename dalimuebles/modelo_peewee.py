import re
from peewee import *
from tkinter.messagebox import *

"""Instancia el objeto database, creando la base o conectándose"""
db = SqliteDatabase("muebles.db")

"""Aca se declara con que tabla se trabaja"""


class BaseModel(Model):
    class Meta:
        database = db


"""Aca definimos la tabla con las columnas que va a tener"""


class Muebles(BaseModel):
    nombre = CharField(unique=True)
    medida = CharField()
    descripcion = CharField()
    precio = BitField()


db.connect()
db.create_tables([Muebles])


class Abmc:
    def __init__(
        self,
    ):
        pass

    """Función alta"""

    def funcion_g(self, var_nombre, var_medida, var_descripcion, var_precio):

        try:
            """La REGEX con la validación de sólo letras -- ^[A-Za-zñÑáéíóúÁÉÍÓÚüÜ]*$"""
            patron = "^[A-Za-zñÑáéíóúÁÉÍÓÚüÜ]*$"
            patron_nombre = var_nombre.get()
            if re.match(patron, patron_nombre):
                mueble = Muebles()
                mueble.nombre = patron_nombre
                mueble.medida = var_medida.get()
                mueble.descripcion = var_descripcion.get()
                mueble.precio = var_precio.get()
                mueble.save()
                showinfo("Alta", "Registro Ok!")
            else:
                showerror("Error validadción", "Recuerde que el nombre es sólo letras.")

        except Exception as error1:
            print(error1)

    """Función actualizar"""

    def actualizar_treeview(self, tree_principal):

        records = tree_principal.get_children()
        for element in records:
            tree_principal.delete(element)

        for fila in Muebles.select():
            tree_principal.insert(
                "",
                0,
                text=fila.id,
                values=(fila.nombre, fila.medida, fila.descripcion, fila.precio),
            )

    """Definimos la funcion borrar"""

    def funcion_b(self, tree_principal):
        records = tree_principal.get_children()
        if askyesno("Borrar", "Está chequeado que vas a borrar este registro?"):
            item_seleccionado = tree_principal.focus()
            valor_id = tree_principal.item(item_seleccionado)
            borrar = Muebles.get(Muebles.id == valor_id["text"])
            borrar.delete_instance()
            showinfo("Borrar", "Borrado exitosamente")

        else:
            showinfo("Borrar", "No pudo ser eliminado")

        for element in records:
            tree_principal.delete(element)

        for fila in Muebles.select():
            tree_principal.insert(
                "",
                0,
                text=fila.id,
                values=(fila.nombre, fila.medida, fila.descripcion, fila.precio),
            )

    """Funcion modificar"""

    def funcion_m(
        self,
        tree_principal,
        nuevo_nombre,
        nuevo_medida,
        nuevo_descripcion,
        nuevo_precio,
    ):
        item_seleccionado = tree_principal.focus()
        valor_id = tree_principal.item(item_seleccionado)
        try:
            patron = "^[A-Za-zñÑáéíóúÁÉÍÓÚüÜ]*$"
            patron_nombre = nuevo_nombre.get()
            if re.match(patron, patron_nombre):
                actualizar = Muebles.update(
                    nombre=patron_nombre,
                    medida=nuevo_medida.get(),
                    descripcion=nuevo_descripcion.get(),
                    precio=nuevo_precio.get(),
                ).where(Muebles.id == valor_id["text"])
                actualizar.execute()
                showinfo("Modificacion", "Modificado con éxito")
            else:
                showerror("ERROR DE VALIDACION", "El atributo nombre es sólo letras")
        except Exception as error2:
            print(error2)
