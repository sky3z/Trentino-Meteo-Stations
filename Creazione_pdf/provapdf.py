from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors

class LetterMaker(object):
	""""""

	def __init__(self, pdf_file, org, seconds, namestation):
		self.c = canvas.Canvas(pdf_file, pagesize=letter)
		self.styles = getSampleStyleSheet()
		self.width, self.height = letter
		self.organization = org
		self.seconds = seconds
		self.namestation = namestation

	def createDocument(self):
		""""""
		voffset = 65

		# add a logo and size it
		logo = Image("meta_logo.jpg")
		logo.drawHeight = 3*inch
		logo.drawWidth = 3.5*inch
		logo.wrapOn(self.c, self.width, self.height)
		logo.drawOn(self.c, *self.coord(65, 80, mm))

		address = """<font size="32">
		Stazione di %s</font>
        """ % (self.namestation)
		p = Paragraph(address, self.styles["Normal"])
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord("CENTER", 180))

		tMedia = """<font size="12">
		<b>Temperatura media</b></font>
		"""
		self.createParagraph(tMedia, 18, voffset+15)
		data = [["Dati attesi", "Dati effettivi", "Percentuale di funzionamento"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (-1,-1), (-1,-1), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1.5, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,95, mm))

		umid = """<font size="12">
		<b>Umidità</b></font>
		"""
		self.createParagraph(umid, 18, voffset + 40)
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1.5, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,120, mm))

		piogg = """<font size="12">
		<b>Pioggia</b></font>
		"""
		self.createParagraph(piogg, 18, voffset + 65)
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1.5, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,145, mm))

		bagnFogl = """<font size="12">
		<b>Bagnatura fogliare</b></font>
		"""
		self.createParagraph(bagnFogl, 18, voffset + 90)
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1.5, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,170, mm))

		velVento = """<font size="12">
		<b>Velocità vento</b></font>
		"""
		self.createParagraph(velVento, 18, voffset + 115)
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1.5, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,195, mm))

		radSolare = """<font size="12">
		<b>Radiazione solare</b></font>
		"""
		self.createParagraph(radSolare, 18, voffset + 140)
		data = [["Dati attesi", "Dati effettivi", "Percentuale"],
				["0", "0", "0"]]
		table = Table(data, colWidths=2*inch)
		table.setStyle([("VALIGN", (0,0), (0,0), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1.5, colors.black)])
		table.wrapOn(self.c, self.width, self.height)
		table.drawOn(self.c, *self.coord(18,220, mm))


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
	doc = LetterMaker("example.pdf", "Metacortex", 10, "Ala")
	doc.createDocument()
	doc.savePDF()
