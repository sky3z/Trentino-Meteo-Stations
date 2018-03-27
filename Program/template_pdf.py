"""
Programma principale per la creazione del fil PDF basato sui valori in percentuale presi dai file .csv
"""
from reportlab.lib.pagesizes import letter										# moduli reportlab per creare pdf
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.lib import colors
from reportlab.lib.colors import PCMYKColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table, PageBreak
from reportlab.platypus.flowables import Flowable
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics import renderPDF
import os
																		# importazione modulo os

class PDFMaker(object):															# creazione classe PDFMaker
	""""""

	def __init__(self, pdf_file, namestation, id):								# funzione init per la classe PDFMaker
		self.c = canvas.Canvas(pdf_file, pagesize=letter)						# indica il foglio di lavoro
		self.styles = getSampleStyleSheet()										# indica lo stile del foglio
		self.width, self.height = letter										# larghezza e altezza hanno dimensioni lettera, formato preimpostato
		self.namestation = namestation											# indica il nome della stazione
		self.id = id															# indica l'id della stazione

	def createDocument(self):													# funzione che crea il documento
		""""""
		voffset = 65															# offset verticale

		# add a logo and size it
		logo = Image('Meta-logo.jpg')									# indica la path dell'immagine
		logo.drawHeight = 3*inch												# indica l'alteza dell'immagine
		logo.drawWidth = 3.5*inch												# indica la larghezza dell'immagine
		logo.wrapOn(self.c, self.width, self.height)							# indica l'impostazione dell'immagine nel foglio
		logo.drawOn(self.c, *self.coord(65, 80, mm))							# disegna la foto a coordinate fissate 65,80, mm

		address = """<font size="24">
		Stazione di %s%s</font>
        """ % (self.namestation, self.id)										# indica il nome della stazione corrente
		p = Paragraph(address, self.styles["Normal"])							# creazione di un paragrafo di testo
		p.wrapOn(self.c, self.width, self.height)
		try:								# importazione del testo nel foglio
			if len(self.namestation) == 6:											# if fatti per centrare il nome della stazione nel foglio
				self.X = 188
			elif len(self.namestation) == 3:
				self.X = 223
			elif len(self.namestation) == 4:
				self.X = 214
			elif len(self.namestation) == 5:
				self.X = 205
			elif len(self.namestation) == 7:
				self.X = 180
			elif len(self.namestation) == 8:
				self.X = 175
			elif len(self.namestation) == 9:
				self.X = 172
			elif len(self.namestation) == 10:
				self.X = 168
			elif len(self.namestation) == 11:
				self.X = 164
			elif len(self.namestation) == 12:
				self.X = 160
			elif len(self.namestation) == 13:
				self.X = 156
			elif len(self.namestation) == 14:
				self.X = 152
			elif len(self.namestation) == 15:
				self.X = 148
			elif len(self.namestation) == 16:
				self.X = 144
			elif len(self.namestation) == 17:
				self.X = 140
			elif len(self.namestation) == 18:
				self.X = 136
			elif len(self.namestation) == 19:
				self.X = 132
			elif len(self.namestation) == 20:
				self.X = 128
			elif len(self.namestation) == 21:
				self.X = 124
			elif len(self.namestation) == 22:
				self.X = 120
			elif len(self.namestation) == 23:
				self.X = 116
			p.drawOn(self.c, *self.coord(self.X, 195))								# diesgna il testo a coordinate...
		except AttributeError:
			print("Nell'anno %s la stazione di %s non era in funzione" %(d_ata,a))
		tMedia = """<font size="12">
		<b>Temperatura media</b></font>
		"""																		# paragrafo di testo
		self.createParagraph(tMedia, 18, voffset+25)							# creazione paragrafo
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresTMED,"%d" %(percTMED)+"%"]]						# dati per tabella
		table = Table(data, colWidths=2*inch)									# inizializzazione tabella
		table.setStyle([("VALIGN", (-1,-1), (-1,-1), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])				# stile tabella
		table.wrapOn(self.c, self.width, self.height)							# importazione nel foglio della tabella
		table.drawOn(self.c, *self.coord(18, 105, mm))							# disegno della tabella a coordinate...

		umid = """<font size="12">
		<b>Umidità</b></font>
		"""
		self.createParagraph(umid, 18, voffset + 50)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresUMID,"%d" %(percUMID)+"%"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,130, mm))

		piogg = """<font size="12">
		<b>Pioggia</b></font>
		"""
		self.createParagraph(piogg, 18, voffset + 75)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresPG,"%d" %(percPG)+"%"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,155, mm))

		bagnFogl = """<font size="12">
		<b>Bagnatura fogliare</b></font>
		"""
		self.createParagraph(bagnFogl, 18, voffset + 100)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresFB,"%d" %(percFB)+"%"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,180, mm))

		velVento = """<font size="12">
		<b>Velocità vento</b></font>
		"""
		self.createParagraph(velVento, 18, voffset + 125)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresVenVel,"%d" %(percVenVel)+"%"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,205, mm))

		radSolare = """<font size="12">
		<b>Radiazione solare</b></font>
		"""
		self.createParagraph(radSolare, 18, voffset + 150)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresRAD,"%d" %(percRAD)+"%"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,230, mm))

		self.c.showPage()														# per iniziare una nuova pagina

		self.drawing = Drawing(200, 400)										# disegna figura vuota
		self.drawing.rotate(-90)												# ruota figura vuota
		self.data = [(percRAD,percVenVel,percFB,percPG,percUMID,percTMED)]	#dati per il grafico
		self.names = ["Radiazione solare", "Velocità vento", "Bagnatura fogliare", "Pioggia", "Umidità", "Temperatura media"]	#nomi per grafico
		self.bc = HorizontalBarChart()											# inizializzazione grafico orizzontale
		self.bc.x = 20															# x del grafico
		self.bc.y = 50															# y del grafico
		self.bc.height = 400													# altezza del grafico
		self.bc.width = 600														# larghezza grafico
		self.bc.data = self.data												# dati del grafico sono uguali a data
		self.bc.strokeColor = colors.white										# colore del grafico
		self.bc.valueAxis.valueMin = 0											# valore minimo asse
		self.bc.valueAxis.valueMax = 100										# valore massimo asse
		self.bc.valueAxis.valueStep = 5											# step di 5 dell'asse
		self.bc.categoryAxis.labels.boxAnchor = 'ne'							# non importante
		self.bc.categoryAxis.labels.dx = -10									# etichettatura grafico
		self.bc.categoryAxis.labels.fontName = 'Helvetica'						# font garfico
		self.bc.categoryAxis.categoryNames = self.names							# asse dei nomi, quello sotto
		self.drawing.add(self.bc)												# aggiunta del grafico alla figura vuota
		renderPDF.draw(self.drawing, self.c, 40,700)							# disegmo del grafico sul pdf

		self.d = Drawing(0,0)
		self.d.rotate(-90)
		self.c.rotate(-90)
		self.c.setFont('Helvetica', 30)
		self.cb = self.c.drawString(-600,525,"Percentuale di funzionamento")	# creazione titolo per grafico ruotato di -90 gradi
		self.d.add(self.cb)														# la x è negativa perchè anche le coordinate cambiano in base al punto di orgine
		renderPDF.draw(self.d, self.c, 100,100)


	def coord(self, x, y, unit=1):												# funzione ripresa da internet per la collocazione in base alle coordinate
		"""
		# http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
    	Helper class to help position flowables in Canvas objects
    	"""
		x, y = x * unit, self.height - y * unit
		return x, y

	def createParagraph(self, ptext, x, y, style=None):							# funzione che crea un paragrafo
		""""""
		if not style:
			style = self.styles["Normal"]
			p = Paragraph(ptext, style=style)
			p.wrapOn(self.c, self.width, self.height)
			p.drawOn(self.c, *self.coord(x, y, mm))

	def savePDF(self):															# funzione che salva il pdf
		""""""
		self.c.save()


if __name__ == '__main__':
	d_ata = input("Inserisci data: ")
	aa = ['Ala', 'Aldeno', 'Arco', 'Arsio', 'Avio', 'Banco_Casez', 'Baselga_di_Pine', 'Besagno', 'Besenello', 'Bezzecca', 'Bleggio_Superiore',
		'Borgo_Valsugana', 'Brancolino', 'Caldes', 'Caldonazzo','Cavedine', 'Cembra', 'Cles', 'Cognola', 'Coredo', 'Cunevo', 'Denno', 'Dercolo',
		'Dro', 'Faedo_Maso_Togn', 'Fondo', 'Gardolo', 'Giovo_Bosch', 'Lavaze', 'Lavis', 'Levico', 'Livo', 'Lomaso', 'Loppio', 'Malga_Flavona',
		'Mama_di_Avio', 'Marco', 'Maso_Callianer', 'Mezzocorona_Novali', 'Mezzocorona_Piovi_Veci', 'Mezzolombardo', 'Mori', 'Nago', 'Nanno',
		'Nave_San_Rocco', 'Nomi', 'Ospedaletto', 'Paneveggio', 'Passo_Vezzena', 'Pedersano', 'Pellizzano', 'Pergine', 'Pietramurata', 'Pinzolo_Pra_Rodont',
		'Polsa', 'Predazzo', 'Prezzano', 'Rabbi', 'Revo', 'Riva_del_Garda', 'Romagnano', 'Romeno', 'Ronzo_Chienis', 'Rovere_della_Luna', 'Rovereto',
		'S_Michele_a_A', 'S_Orsola', 'Sarche', 'Savignano', 'Segno', 'Serravalle', 'Spormaggiore', 'Stenico', 'Storo', 'Telve', 'Terlago', 'Terzolas',
		'Ton', 'Toss_Castello', 'Trento_Sud', 'Verla', 'Vigolo_Vattaro', 'Volano', 'Zambana', 'Zortea']
																											# lista di tutte le stazioni
	for a in aa:
		pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Program/", "Stazioni_Meteo_Trentino", a, d_ata, "dati", "csv"))			# pathname iniziale
		final_pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Program/", "Stazioni_Meteo_Trentino/", a, d_ata, "report", a))	#pathname finale
		for filename in os.listdir(pathname):								# per filename in tutte le directory della pathname
			with open(pathname + "/" + filename) as handle:					# apri file in pathname
				try:
					next(handle)											# prova prima riga vuota
					next(handle)											# prova seconda riga vuota
				except Exception:											# se ritorna eccezione
					continue												# esci e continua

				VALORE_ASSENTE = "--"
				valTot = 0;			#valori totali
				valAssTMED = 0;		#valori assenti temperatura
				valAssUMID = 0;		#valori assenti umidità
				valAssPG   = 0;		#valori assenti pioggia
				valAssFB   = 0;		#valori assenti bagnatura fogliare
				valAssVenVel = 0;	#valori assenti	velocità vento
				valAssRAD  = 0;		#valori assenti	radiazione solare
				boot = 1;			#operazioni da eseguire una volta sola
				nomeStat = "";		#nome stazione	[da prendere una sola volta per stazione]
				idStat = "";		#id stazione	[da prendere una sola volta per stazione]

				for riga in handle:						#cicla tutte le righe del file corrente
					if riga.strip():		#se la riga non è vuota [?????non dovrebbero esserci linee vuote, però non so perche ne compaiono?????]
						valTot = valTot + 1				#incrementa i valori totali
						riga = riga.replace("\"", "")	#rimuori i doppi apici
						comp = riga.split(",")			#separa i vari componenti (0 -> NUMERO, 1 -> ID, 2 -> NOME, 3 -> DATA, 4 -> T MED, 5 -> UMID, 6 -> PG, 7 -> FB, 8 -> VEN-VEL, 9 -> RAD)

						#recupero dati per nome file [da fare una volta sola per stazione]
						if boot == 1:
							boot = -1			#non ripetere
							idStat = comp[1]	#prendi l'id della stazione
							nomeStat = comp[2]	#prendi il nome della stazione


						#controlla i vari componenti e se corrispondono a "VALORE_ASSENTE" incrementa la variabile associata
						if comp[4] == VALORE_ASSENTE:	#temperatura
							valAssTMED = valAssTMED + 1

						if comp[5] == VALORE_ASSENTE:	#temperatura
							valAssUMID = valAssUMID + 1

						if comp[6] == VALORE_ASSENTE:	#temperatura
							valAssPG = valAssPG + 1

						if comp[7] == VALORE_ASSENTE:	#temperatura
							valAssFB = valAssFB + 1

						if comp[8] == VALORE_ASSENTE:	#temperatura
							valAssVenVel = valAssVenVel + 1

						if comp[9] == VALORE_ASSENTE:	#temperatura
							valAssRAD = valAssRAD + 1

						valPresTMED = valTot - valAssTMED
						percTMED = (valPresTMED * 100) / valTot

						valPresUMID = valTot - valAssUMID
						percUMID = (valPresUMID * 100) / valTot

						valPresPG = valTot - valAssPG
						percPG = (valPresPG * 100) / valTot

						valPresFB = valTot - valAssFB
						percFB = (valPresFB * 100) / valTot

						valPresVenVel = valTot - valAssVenVel
						percVenVel = (valPresVenVel * 100) / valTot

						valPresRAD = valTot - valAssRAD
						percRAD = (valPresRAD * 100) / valTot
				doc = PDFMaker(final_pathname + "_report" + ".pdf", nomeStat, "("+idStat+")")		# creazione del pdf con parametri
				doc.createDocument()																# creazione
				doc.savePDF()																		# salvataggio
