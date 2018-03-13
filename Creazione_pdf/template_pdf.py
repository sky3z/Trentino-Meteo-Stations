from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
import os

class LetterMaker(object):
	""""""

	def __init__(self, pdf_file, org, seconds, namestation, id):
		self.c = canvas.Canvas(pdf_file, pagesize=letter)
		self.styles = getSampleStyleSheet()
		self.width, self.height = letter
		self.organization = org
		self.seconds = seconds
		self.namestation = namestation
		self.id = id

	def createDocument(self):
		""""""
		voffset = 65

		# add a logo and size it
		logo = Image('Metacortex_Posit.jpg')
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
				["0", "0", "0"]]
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
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
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
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
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
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
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
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
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
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,230, mm))


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

	def obtainsData(self):
		""""""
		self.pathname = os.path.abspath(os.path)

if __name__ == "__main__":
	doc = LetterMaker("example.pdf", "Metacortex", 10, "Paveneggo", "(30)")
	doc.createDocument()
	doc.savePDF()
