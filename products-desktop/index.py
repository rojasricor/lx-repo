from tkinter import ttk
from tkinter import *

# import sqlite3
import pymysql

obtener_conexion = lambda: pymysql.connect(host = 'localhost', user = 'admin', password = 'admin', db = 'productos')

class Productos:

	# nombre_base_de_datos = 'productos.db'

	def __init__(self, ventana):
		self.app = ventana
		self.app.title('Aplicacion de Productos')

		# Creamos un frame contenedor
		frame = LabelFrame(self.app, text = 'Registrar un nuevo producto')
		frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

		# Input del nombre
		Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
		self.nombre = Entry(frame)
		self.nombre.focus()
		self.nombre.grid(row = 1, column = 1)

		# Input del precio
		Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
		self.precio = Entry(frame)
		self.precio.grid(row = 2, column = 1)

		# Boton para agregar productos
		ttk.Button(frame, text = 'Guardar Producto', command = self.agregar_producto).grid(row = 3, columnspan = 2, sticky = W + E)

		# Label para mostrar mensajes de exito o informacion
		self.mensaje = Label(text = '', fg = 'red')
		self.mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

		# Tabla
		self.tabla = ttk.Treeview(height = 10, columns = 2)
		self.tabla.grid(row = 4, column = 0, columnspan = 2)
		self.tabla.heading('#0', text = 'Producto', anchor = CENTER)
		self.tabla.heading('#1', text = 'Precio USD', anchor = CENTER)

		# Botones para editar y eliminar
		ttk.Button(text = 'ELIMINAR', command = self.eliminar_producto).grid(row = 5, column = 0, sticky =  W + E)
		ttk.Button(text = 'EDITAR', command = self.editar_producto).grid(row = 5, column = 1, sticky =  W + E)

		# Obtiene y llena los productos de la base de datos a la aplicacion
		self.obtener_productos()

	def ejecutar_consulta(self, consulta, parametros = ()):
		with obtener_conexion() as conexion:
			cursor = conexion.cursor()
			cursor.execute(consulta, parametros)
			resultado = cursor.fetchall()
			conexion.commit()
		return resultado

	def obtener_productos(self):
		# Limpiar la tabla
		filas = self.tabla.get_children()
		for fila in filas:
			self.tabla.delete(fila)

		# Consultando los productos
		consulta = 'SELECT * FROM productos ORDER BY nombre DESC'
		productos = self.ejecutar_consulta(consulta)

		# Insertando los productos a la tabla
		for row in productos:
			self.tabla.insert('', 0, text = row[1], values = row[2])

	def estos_input_no_estan_vacios(self, entry):
		return len(entry[0].get()) != 0 and len(entry[1].get()) != 0

	def agregar_producto(self):
		if self.estos_input_no_estan_vacios((self.nombre, self.precio)):
			consulta = 'INSERT INTO productos VALUES(NULL, %s, %s)'
			parametros = (self.nombre.get(), self.precio.get())
			self.ejecutar_consulta(consulta, parametros)
			self.obtener_productos()
			self.mensaje['text'] = 'Producto: {} guardado exitosamente'.format(self.nombre.get())
			self.nombre.delete(0, END)
			self.precio.delete(0, END)
			self.nombre.focus()
		else:
			self.mensaje['text'] = 'El nombre y el precio es requerido'

	def eliminar_producto(self):
		nombre_producto = self.tabla.item(self.tabla.selection())['text']
		if not nombre_producto:
			self.mensaje['text'] = 'Por favor selecciona un registro de la tabla'
			return
		else:
			consulta = 'DELETE FROM productos WHERE nombre = %s'
			self.ejecutar_consulta(consulta, (nombre_producto,))
			self.mensaje['text'] = 'El producto {} ha sido eliminado'.format(nombre_producto)
			self.obtener_productos()

	def actualizar_producto(self, nuevo_nombre_producto, nuevo_precio_producto, nombre_producto, precio_producto):
		if self.estos_input_no_estan_vacios((nuevo_nombre_producto, nuevo_precio_producto)):
			consulta = 'UPDATE productos SET nombre = %s, precio = %s WHERE nombre = %s AND precio = %s'
			parametros = (nuevo_nombre_producto.get(), nuevo_precio_producto.get(), nombre_producto, precio_producto)
			self.ejecutar_consulta(consulta, parametros)
			self.mensaje['text'] = 'El producto {} ha sido modificado'.format(nombre_producto)
			self.ventana_editar.destroy()
			self.obtener_productos()
		else:
			self.mensaje['text'] = 'Complete los nuevos campos'

	def editar_producto(self):
		nombre_producto = self.tabla.item(self.tabla.selection())['text']
		precio_producto = self.tabla.item(self.tabla.selection())['values']
		if not nombre_producto or not precio_producto:
			self.mensaje['text'] = 'Por favor selecciona un registro de la tabla'
			return
		else:
			self.ventana_editar = Toplevel()
			self.ventana_editar.title = 'Editar producto'

			# Nombre anterior
			Label(self.ventana_editar, text = 'Nombre antiguo: ').grid(row = 0, column = 0)
			Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = nombre_producto), state = 'readonly').grid(row = 0, column = 1)

			# Nuevo nombre
			Label(self.ventana_editar, text = 'Nuevo nombre: ').grid(row = 1, column = 0)
			nuevo_nombre_producto = Entry(self.ventana_editar)
			nuevo_nombre_producto.focus()
			nuevo_nombre_producto.grid(row = 1 , column = 1)

			# Precio anterior
			Label(self.ventana_editar, text = 'Precio antiguo: ').grid(row = 2, column = 0)
			Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value = precio_producto[0]), state = 'readonly').grid(row = 2, column = 1)

			# Nuevo precio
			Label(self.ventana_editar, text = 'Nuevo precio: ').grid(row = 3, column = 0)
			nuevo_precio_producto = Entry(self.ventana_editar)
			nuevo_precio_producto.grid(row = 3, column = 1)

			# Boton para guardar cambios
			Button(self.ventana_editar, text = 'Actualizar', command = lambda: self.actualizar_producto(nuevo_nombre_producto, nuevo_precio_producto, nombre_producto, precio_producto)).grid(row = 4, columnspan = 2, sticky =  W + E)

if __name__ == '__main__':
	ventana = Tk()
	aplicacion = Productos(ventana)
	ventana.mainloop()
