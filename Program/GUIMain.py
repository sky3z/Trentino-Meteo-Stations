import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Log_Bot_xls import *
from crea__staz_inDir import *
from main import *


class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("Stazioni Meteo Trentino")
		self.pack(fill=BOTH, expand=1)
		menu = Menu(self.master)
		self.master.config(menu=menu)
		file=Menu(menu)
		file.add_command(label="Exit", command=self.client_exit)
		menu.add_cascade(label="File", menu=file)
		inserisci = Menu(menu)
		inserisci.add_command(label="Data", command=self.inserisci_data)
		menu.add_cascade(label="Inserisci", menu=inserisci)
		help = Menu(menu)
		help.add_command(label="Show Guide", command=self.showGuide)
		menu.add_cascade(label="Help", menu=help)
		text = Label(self, font= 18,text="Programma con GUI per l'avvio del codice \n in modo grafico, questa GUI è ancora minimale, in \nfuturo verrà aggiornata con ulteriori funzioni")
		text.place(x=20, y= 30)
		b1 = Button(self, font= 20, text="Avvia Programma", width= 20, height=3, background="green", command=self.b1_press)
		b1.place(x=100, y=150)
		b1.bind("<Return>", self.b1_press_a)
		b1.focus_force()

	def client_exit(self):
		exit()

	def showGuide(self):
		messagebox.showinfo("Help", """             	 Help of Stazioni Meteo Trentino\n
							        Questa è l'interfaccia grafica del programma\n
							    	          'Le Stazioni del Trentino'""")

	def b1_press(self):
		oggi = dt.datetime(2013,12,31,23)
		data_iniziale = oggi - dt.timedelta(hours = 8759)
		create_folder(data_iniziale)
		logBot(oggi, data_iniziale)

	def b1_press_a(self):
		b1_press()

	def inserisci_data(self):
		window = tk.Toplevel(self)
		window.geometry("300x200")
		textBox = Text(window, height=2, width=10)
		textBox.pack()
		bdata= Button(window, font=20, text="OK", command=self.newwindow_destroy)
		bdata.pack()

	def newwindow_destroy(self):
		window.quit()

radice = tk.Tk()
radice.geometry("400x300")
app = Window(radice)
radice.mainloop()
