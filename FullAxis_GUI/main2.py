#Librerias Necesarias
#Tkinter para dibujar el Gui, PIL para trabajar con img
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog

#Librerias para trabajr numeros y datos importados
import numpy as np
import csv 
import pandas

#Libreria para utilizar parametros especificos del sistema
import sys
import setproctitle
sys.path.insert(1, 'config/') #se señala carpeta donde se encuentran librerias propias

#Librerias propias para manejar componentes externos, principalmente configuraciones
import languaje as lang
import setting as stt

#Libreria para controlar gráficos, es necesario analisar si se puede enviar a libreria propia 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Ellipse
import matplotlib.animation as animation
from matplotlib.text import OffsetFrom
from matplotlib.gridspec import GridSpec

#Librerias para comunicación Serial y su uso 
import serial
import serial.tools.list_ports
import time



#Establece nombre en gestor de procesos
setproctitle.setproctitle('FullAxis')





LANG=0


class Lelitxipawe():
	'''
	Clase principal de la Ventana
	'''
	def __init__(self, master=None): #Se inicia la ventana con sus caracteristicas predeterminadas
		self.root = master
		self.root.config(background='white')#Color de fondo
		self.root.update_idletasks()
		#self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
		self.w,self.h = 1280,720
		self.root.geometry("%dx%d+0+0" % (self.w, self.h))
		self.root.minsize(self.w, self.h)#Tamaño minimo de la ventana
		#self.root.maxsize(self.w, self.h)#Tamaño minimo de la ventana
		self.root.attributes('-zoomed', True)
#		self.root.overrideredirect(True)
		self.root.call('wm', 'iconphoto', self.root._w, ImageTk.PhotoImage(Image.open('resources/icon.ico')))#Icono de la ventana
		self.app()


	def app(self): #Estructura de la ventana
		self.txokiñ()
		self.ñizol()
		self.wirin()
		self.wirin_epu()

	def ñizol(self): #Menú principal
		menu = Menu(self.root)
		self.root.config(menu=menu)
		file = Menu(menu, tearoff=0)
		file.add_command(label="Abrir usuario")
		file.add_command(label="Importar usuario", command=self.abrir)
		file.add_command(label="Nuevo usuario", command=self.we_kakon)
		file.add_command(label="Cerrar usuario")
		file.add_separator()
		file.add_command(label="Salir",command=root.quit)
		menu.add_cascade(label="Archivo", menu=file)
		edit = Menu(menu, tearoff=0)
		edit.add_command(label="Nueva Prueba")
		edit.add_command(label="Borrar Prueba")
		edit.add_separator()
		edit.add_command(label="Abrir prueba suelta")
		menu.add_cascade(label="Editar", menu=edit)
		help = Menu(menu, tearoff=0)
		help.add_command(label="Ayuda")
		help.add_separator()
		help.add_command(label="Acerca de nosotros",)
		menu.add_cascade(label="Ayuda", menu=help)

	def txokiñ(self):#Marcos y estructura
		#Configuración de los Frames, proporciones en setting.py variable size_frame
		size_frame=stt.size_screen(self.w,self.h)

		self.frame_quick = Frame(bd=1,relief="sunken") ##crea la caja superior
		self.frame_contenido = Frame(bd=1, bg="white",relief="sunken") ##crea la caja derecha
		self.frame_info = Frame(bd=1,relief="sunken") ##crea la caja inferior
		self.frame_command = Frame(bd=1,relief="sunken") ##crea la caja izquierda
		#se ubican los frames en la ventana principal
		self.frame_quick.place(	relx=size_frame['up'][0], rely=size_frame['up'][1], 
								relwidth=size_frame['up'][2], relheight=size_frame['up'][3])
		self.frame_contenido.place(	relx=size_frame['der'][0], rely=size_frame['der'][1], 
									relwidth=size_frame['der'][2], relheight=size_frame['der'][3])
		self.frame_command.place(	relx=size_frame['izq'][0], rely=size_frame['izq'][1], 
									relwidth=size_frame['izq'][2], relheight=size_frame['izq'][3])
		self.frame_info.place(	relx=size_frame['down'][0], rely=size_frame['down'][1], 
								relwidth=size_frame['down'][2], relheight=size_frame['down'][3])


		self.frame_data = Frame(self.frame_command, bg="red")
		self.frame_registros = Frame(self.frame_command, bg="green")
		self.frame_curva = Frame(self.frame_command, bg="white")
		self.frame_data.place(relwidth=1, relheight=1/3)
		self.frame_registros.place(rely =1/3, relwidth=1, relheight=1/3)
		self.frame_curva.place(rely = 2*(1/3), relwidth=1, relheight=1/3)


	def wirin(self):#se dibujan los gráficos
		fig = self.wirikan()
		self.graphy = FigureCanvasTkAgg(fig, master=self.frame_contenido)
		self.graphy.get_tk_widget().pack(side="top",fill='both',expand=True)

	def wirin_epu(self):
		fig = self.wirikan_select()
		self.graphy2 = FigureCanvasTkAgg(fig, master=self.frame_curva)
		self.graphy2.get_tk_widget().pack(side="top", fill="both", expand=True)

	def wirikan(self): #Graficos principales
		fig = plt.figure(figsize=(20,15))
		gs1 = GridSpec(7, 1)
		gs1.update(left=0.05, right=0.95, wspace=0.5, hspace=0.3, top=0.98, bottom=0.08)

		ax1 = plt.subplot(gs1[0:2,:])
		ax1.grid()
		ax1.set_ylabel('Roll',fontsize=8)
		ax1.xaxis.set_tick_params(labelsize=7)
		ax1.yaxis.set_tick_params(labelsize=7)

		ax2 = plt.subplot(gs1[2:4,:])
		ax2.grid()
		ax2.set_ylabel('Pitch',fontsize=8)
		ax2.xaxis.set_tick_params(labelsize=7)
		ax2.yaxis.set_tick_params(labelsize=7)

		ax3 = plt.subplot(gs1[4:6,:])
		ax3.grid()
		ax3.set_ylabel('Yaw',fontsize=8)
		ax3.xaxis.set_tick_params(labelsize=7)
		ax3.yaxis.set_tick_params(labelsize=7)

		ax4 = plt.subplot(gs1[6,:])
		ax4.grid()
		ax4.set_ylabel('Mark',fontsize=8)
		ax4.xaxis.set_tick_params(labelsize=7)
		ax4.yaxis.set_tick_params(labelsize=7)

		return fig

	def wirikan_select(self):
		fig = plt.figure(figsize=(10,10))
		gs1 = GridSpec(1, 1)
		
		ax1 = plt.subplot(gs1[0:2,:])
		ax1.grid()
		plt.xticks(fontsize=6, rotation=90)
		plt.yticks(fontsize=6, rotation=90)
		
		return fig

	def wirikan_2(x_vec,y1_data,line1,identifier='',pause_time=0.01):
		if line1==[]:
			plt.ion()
			#fig = plt.figure(figsize=(13,6))
			#ax = fig.add_subplot(111)
			#line1, = ax.plot(x_vec,y1_data)
			line1, = self.ax3.plot(x_vec,y1_data)

			plt.show()
			#self.graphy.draw()

		#line1.set_data(x_vec,y1_data)

		plt.pause(pause_time)

		return line1

	def we_kakon(self):
		self.kakon = Toplevel(takefocus=True)
		self.kakon.focus_force()
		self.kakon.attributes("-topmost", True)
		self.kakon.title("Nuevo registro")
		self.kakon.bind("<FocusOut>",self.focus_kakon)
		frame_data = Frame(self.kakon)
		label = Label(frame_data, text="ID :").grid(column=0 , row=1, sticky="w")
		label = Label(frame_data, text="Nombre :").grid(column=0,row=2,sticky="w")
		label = Label(frame_data, text="Apellidos :").grid(column=0 , row=3,sticky="w")
		label = Label(frame_data, text="Nacimiento :").grid(column=0 , row=4,sticky="w")
		entry_ID = Entry(frame_data, width=10).grid(column=1, row=1)
		entry_name = Entry(frame_data, width=10).grid(column=1, row=2)
		entry_name.focus_set()
		entry_lastName = Entry(frame_data, width=10).grid(column=1, row=3)
		entry_edad = Entry(frame_data, width=10).grid(column=1, row=4)
		frame_button = Frame(self.kakon)
		btn_cancelar = Button(frame_button, text="Cancelar").pack( side = LEFT)
		btn_crear = Button(frame_button, text="Crear").pack( side = LEFT)
		frame_data.pack()
		frame_button.pack()


	def focus_kakon(self,event):
		self.kakon.focus_force()

	def abrir(self):
		#dd = filedialog()
		#dd.askopenfile(mode="r", **options)
		file = filedialog.askopenfilename(parent=self.root, initialdir = "~/",
										  title = "Seleccione el archivo",
										  filetypes = [("tar.gz","*.tar.gz")
										 			  ,("all files","*.*")])
		return(file)

if __name__ == '__main__':

    root = Tk()
    my_gui = Lelitxipawe(master=root)
    my_gui.root.wm_title("FullAxis V.4")
    root.mainloop()