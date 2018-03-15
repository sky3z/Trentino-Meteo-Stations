from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table, PageBreak
from reportlab.lib import colors
from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics import renderPDF
from reportlab.platypus.flowables import Flowable
import os

class PDFMaker(object):
	""""""

	def __init__(self, pdf_file, namestation, id):
		self.c = canvas.Canvas(pdf_file, pagesize=letter)
		self.styles = getSampleStyleSheet()
		self.width, self.height = letter
		self.namestation = namestation
		self.id = id

	def createDocument(self):
		""""""
		voffset = 65

		# add a logo and size it
		logo = Image('Image_pdf/Meta-logo.jpg')
		logo.drawHeight = 3*inch
		logo.drawWidth = 3.5*inch
		logo.wrapOn(self.c, self.width, self.height)
		logo.drawOn(self.c, *self.coord(65, 80, mm))

		address = """<font size="24">
		Stazione di %s%s</font>
        """ % (self.namestation, self.id)
		p = Paragraph(address, self.styles["Normal"])
		p.wrapOn(self.c, self.width, self.height)
		if len(self.namestation) == 6:
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
		p.drawOn(self.c, *self.coord(self.X, 195))

		tMedia = """<font size="12">
		<b>Temperatura media</b></font>
		"""
		self.createParagraph(tMedia, 18, voffset+25)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				[valTot, valPresTMED,"%d" %(percTMED)+"%"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (-1,-1), (-1,-1), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18, 105, mm))

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

		self.c.showPage()

		self.drawing = Drawing(200, 400)
		self.drawing.rotate(-90)
		self.data = [(percRAD,percVenVel,percFB,percPG,percUMID,percTMED)]
		self.names = ["Radiazione solare", "Velocità vento", "Bagnatura fogliare", "Pioggia", "Umidità", "Temperatura media"]
		self.bc = HorizontalBarChart()
		self.bc.x = 20
		self.bc.y = 50
		self.bc.height = 400
		self.bc.width = 600
		self.bc.data = self.data
		self.bc.strokeColor = colors.white
		self.bc.valueAxis.valueMin = 0
		self.bc.valueAxis.valueMax = 100
		self.bc.valueAxis.valueStep = 5
		self.bc.categoryAxis.labels.boxAnchor = 'ne'
		self.bc.categoryAxis.labels.dx = -10
		self.bc.categoryAxis.labels.fontName = 'Helvetica'
		self.bc.categoryAxis.categoryNames = self.names
		self.drawing.add(self.bc)
		renderPDF.draw(self.drawing, self.c, 40,700)

		self.d = Drawing(0,0)
		self.d.rotate(-90)
		self.c.rotate(-90)
		self.c.setFont('Helvetica', 30)
		self.cb = self.c.drawString(-600,525,"Percentuale di funzionamento")
		self.d.add(self.cb)
		renderPDF.draw(self.d, self.c, 100,100)


	def coord(self, x, y, unit=1):
		"""
		# http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
    	Helper class to help position flowables in Canvas objects
    	"""
		x, y = x * unit, self.height - y * unit
		return x, y

	def createParagraph(self, ptext, x, y, style=None):
		""""""
		if not style:
			style = self.styles["Normal"]
			p = Paragraph(ptext, style=style)
			p.wrapOn(self.c, self.width, self.height)
			p.drawOn(self.c, *self.coord(x, y, mm))
			
	def savePDF(self):
		""""""
		self.c.save()


if __name__ == "__main__":
	aa = ['Ala', 'Aldeno', 'Arco', 'Arsio', 'Avio', 'Banco_Casez', 'Baselga_di_Pine', 'Besagno', 'Besenello', 'Bezzecca', 'Bleggio_Superiore',
		'Borgo_Valsugana', 'Brancolino', 'Caldes', 'Caldonazzo','Cavedine', 'Cembra', 'Cles', 'Cognola', 'Coredo', 'Cunevo', 'Denno', 'Dercolo',
		'Dro', 'Faedo_Maso_Togn', 'Fondo', 'Gardolo', 'Giovo_Bosch', 'Lavaze', 'Lavis', 'Levico', 'Livo', 'Lomaso', 'Loppio', 'Malga_Flavona',
		'Mama_di_Avio', 'Marco', 'Maso_Callianer', 'Mezzocorona_Novali', 'Mezzocorona_Piovi_Veci', 'Mezzolombardo', 'Mori', 'Nago', 'Nanno',
		'Nave_San_Rocco', 'Nomi', 'Ospedaletto', 'Paneveggio', 'Passo_Vezzena', 'Pedersano', 'Pellizzano', 'Pergine', 'Pietramurata', 'Pinzolo_Pra_Rodont',
		'Polsa', 'Predazzo', 'Prezzano', 'Rabbi', 'Revo', 'Riva_del_Garda', 'Romagnano', 'Romeno', 'Ronzo_Chienis', 'Rovere_della_Luna', 'Rovereto',
		'S_Michele_a_A', 'S_Orsola', 'Sarche', 'Savignano', 'Segno', 'Serravalle', 'Spormaggiore', 'Stenico', 'Storo', 'Telve', 'Terlago', 'Terzolas',
		'Ton', 'Toss_Castello', 'Trento_Sud', 'Verla', 'Vigolo_Vattaro', 'Volano', 'Zambana', 'Zortea']

	for a in aa:
		pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Stazioni_Meteo_Trentino", a, "2016", "dati", "csv"))
		final_pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Stazioni_Meteo_Trentino/", a, "2016/", "report", a))
		for filename in os.listdir(pathname):
			with open(pathname + "/" + filename) as handle:
				try:
					next(handle)
					next(handle)
				except Exception:
					continue

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
				doc = PDFMaker(final_pathname + "_report" + ".pdf", nomeStat, "("+idStat+")")
				doc.createDocument()
				doc.savePDF()
