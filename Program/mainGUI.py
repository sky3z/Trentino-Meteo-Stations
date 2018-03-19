from tkinter import *
from Log_Bot_xls import *
from main import *

class MiaApp():
	def __init__(self, genitore):
		# ----- costanti per la disposizione pulsanti
		larghezza_pulsanti = 8
		imb_pulsantex = "2m"
		imb_pulsantey = "1m"
		imb_quadro_pulsantix = "3m"
		imb_quadro_pulsantiy = "2m"
		imb_int_quadro_pulsantix = "3m"
		imb_int_quadro_pulsantiy = "1m"
		# ----------- fine costanti ----------------

		self.mioGenitore = genitore
		self.mioContenitore1 = Frame(genitore)
		self.mioContenitore1.pack()
		self.mioGenitore.title("Stazioni Meteo trentino")

		self.quadro_pulsanti = Frame(self.mioContenitore1)
		self.quadro_pulsanti.pack(side=TOP, ipadx=imb_int_quadro_pulsantix, ipady=imb_int_quadro_pulsantiy, padx=imb_quadro_pulsantix, pady=imb_quadro_pulsantiy)

		self.quadro_alto = Frame(self.mioContenitore1)
		self.quadro_alto.pack(side=TOP, fill=BOTH, expand=YES)

		self.quadro_basso = Frame(self.mioContenitore1, borderwidth=5, relief=RIDGE, height=50, background="white")
		self.quadro_basso.pack(side=TOP, fill=BOTH, expand=YES)

		self.quadro_sinistra = Frame(self.quadro_alto, background="red", borderwidth=5, relief=RIDGE, height=250, width=50)
		self.quadro_sinistra.pack(side=LEFT, fill=BOTH, expand=YES)

		self.quadro_destra = Frame(self.quadro_alto, background="tan", borderwidth=5, relief=RIDGE, width=250)
		self.quadro_destra.pack(side=RIGHT, fill=BOTH, expand=YES)

		self.pulsante1 = Button(self.quadro_pulsanti, command=self.pulsante1Premuto)
		self.pulsante1.configure(text="Conferma", background="green")
		self.pulsante1.focus_force()
		self.pulsante1.configure(width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
		self.pulsante1.pack(side=LEFT)
		self.pulsante1.bind("<Return>", self.pulsante1Premuto_a)

		self.pulsante2 = Button(self.quadro_pulsanti, command=self.pulsante2Premuto)
		self.pulsante2.configure(text="Annulla", background="red")
		self.pulsante2.configure(width=larghezza_pulsanti, padx=imb_pulsantex, pady=imb_pulsantey)
		self.pulsante2.pack(side=RIGHT)
		self.pulsante2.bind("<Return>", self.pulsante2Premuto_a)

		self.testo1 = Label(self.quadro_basso, text="prova testo")
		self.testo1.pack()

	def pulsante1Premuto(self):
		if self.pulsante1["background"] == "green":
			self.pulsante1["background"] = "yellow"
		elif self.pulsante1["background"] == "yellow":
			self.pulsante1["background"] = "cyan"
			oggi = dt.datetime(2015,12,31,23)
			data_iniziale = oggi - dt.timedelta(hours = 8759)
			logBot(oggi, data_iniziale)
		else:
			self.pulsante1["background"] = "green"

	def pulsante2Premuto(self):
		self.mioGenitore.destroy()

	def pulsante1Premuto_a(self):
		self.pulsante1Premuto()

	def pulsante2Premuto_a(self):
		self.pulsante2Premuto()

radice = Tk()
miaApp = MiaApp(radice)
radice.mainloop()
