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
import os																		# importazione modulo os

class PDFMaker(object):															# creazione classe PDFMaker
	""""""

	def __init__(self, pdf_file, namestation):								# funzione init per la classe PDFMaker
		self.c = canvas.Canvas(pdf_file, pagesize=letter)						# indica il foglio di lavoro
		self.styles = getSampleStyleSheet()										# indica lo stile del foglio
		self.width, self.height = letter										# larghezza e altezza hanno dimensioni lettera, formato preimpostato
		self.namestation = namestation											# indica il nome della stazione

	def createDocument(self):													# funzione che crea il documento
		""""""
		voffset = 65															# offset verticale

		# add a logo and size it
		logo = Image('Image_pdf/Meta-logo.jpg')									# indica la path dell'immagine
		logo.drawHeight = 3*inch												# indica l'alteza dell'immagine
		logo.drawWidth = 3.5*inch												# indica la larghezza dell'immagine
		logo.wrapOn(self.c, self.width, self.height)							# indica l'impostazione dell'immagine nel foglio
		logo.drawOn(self.c, *self.coord(65, 80, mm))
																				# disegna la foto a coordinate fissate 65,80, mm
		tMedia = """<font size="12">
		<b>Data riferimento: 01/01/2017 a 31/12/2017</b></font>
		"""																		# paragrafo di testo
		self.createParagraph(tMedia, 18, voffset+10)
		data = [["Nome stazione", "Temperatura media", "Umidità", "Pioggia", "Bagnatura fogliare", "Velocità vento", "Radiazione solare"],
				[bb[0], bb[1], bb[2], bb[3], bb[4], bb[5], bb[6]],
				[bb[7], bb[8], bb[9], bb[10], bb[11], bb[12], bb[13]],
				[bb[14], bb[15], bb[16], bb[17], bb[18], bb[19], bb[20]],
				[bb[21], bb[22], bb[23], bb[24], bb[25], bb[26], bb[27]],
				[bb[28], bb[29], bb[30], bb[31], bb[32], bb[33], bb[34]],
				[bb[35], bb[36], bb[37], bb[38], bb[39], bb[40], bb[41]],
				[bb[42], bb[43], bb[44], bb[45], bb[46], bb[47], bb[48]],
				[bb[49], bb[50], bb[51], bb[52], bb[53], bb[54], bb[55]],
				[bb[56], bb[57], bb[58], bb[59], bb[60], bb[61], bb[62]],
				[bb[63], bb[64], bb[65], bb[66], bb[67], bb[68], bb[69]],
				[bb[70], bb[71], bb[72], bb[73], bb[74], bb[75], bb[76]],
				[bb[77], bb[78], bb[79], bb[80], bb[81], bb[82], bb[83]],
				[bb[84], bb[85], bb[86], bb[87], bb[88], bb[89], bb[90]],
				[bb[91], bb[92], bb[93], bb[94], bb[95], bb[96], bb[97]],
				[bb[98], bb[99], bb[100], bb[101], bb[102], bb[103], bb[104]],
				["Caldonazzo Brina", "0", "0", "0", "0", "0", "0"],
				[bb[112], bb[113], bb[114], bb[115], bb[116], bb[117], bb[118]],
				[bb[119], bb[120], bb[121], bb[122], bb[123], bb[124], bb[125]],
				[bb[126], bb[127], bb[128], bb[129], bb[130], bb[131], bb[132]],
				[bb[133], bb[134], bb[135], bb[136], bb[137], bb[138], bb[139]],
				[bb[140], bb[141], bb[142], bb[143], bb[144], bb[145], bb[146]],
				[bb[147], bb[148], bb[149], bb[150], bb[151], bb[152], bb[153]],
				[bb[154], bb[155], bb[156], bb[157], bb[158], bb[159], bb[160]],
				[bb[161], bb[162], bb[163], bb[164], bb[165], bb[166], bb[167]],
				[bb[168], bb[169], bb[170], bb[171], bb[172], bb[173], bb[174]],
				[bb[175], bb[176], bb[177], bb[178], bb[179], bb[180], bb[181]]]						# dati per tabella
		table = Table(data, colWidths=inch)									# inizializzazione tabella
		table.setStyle([("VALIGN", (-1,-1), (-1,-1), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black),
						("FONTSIZE", (0,0), (-1,-1), 7),
						("ALIGN", (0,0), (-1,-1), "CENTER")])				# stile tabella
		table.wrapOn(self.c, self.width, self.height)							# importazione nel foglio della tabella
		table.drawOn(self.c, *self.coord(18, 250, mm))							# disegno della tabella a coordinate...

		self.c.showPage()

		data1 = [["Nome stazione", "Temperatura media", "Umidità", "Pioggia", "Bagnatura fogliare", "Velocità vento", "Radiazione solare"],
				[bb[182], bb[183], bb[184], bb[185], bb[186], bb[187], bb[188]],
				[bb[189], bb[190], bb[191], bb[192], bb[193], bb[194], bb[195]],
				[bb[196], bb[197], bb[198], bb[199], bb[200], bb[201], bb[202]],
				[bb[203], bb[204], bb[205], bb[206], bb[207], bb[208], bb[209]],
				[bb[210], bb[211], bb[212], bb[213], bb[214], bb[215], bb[216]],
				[bb[217], bb[218], bb[219], bb[220], bb[221], bb[222], bb[223]],
				[bb[224], bb[225], bb[226], bb[227], bb[228], bb[229], bb[230]],
				[bb[231], bb[232], bb[233], bb[234], bb[235], bb[236], bb[237]],
				[bb[238], bb[239], bb[240], bb[241], bb[242], bb[243], bb[244]],
				[bb[245], bb[246], bb[247], bb[248], bb[249], bb[250], bb[251]],
				[bb[252], bb[253], bb[254], bb[255], bb[256], bb[257], bb[258]],
				[bb[259], bb[260], bb[261], bb[262], bb[263], bb[264], bb[265]],
				[bb[266], bb[267], bb[268], bb[269], bb[270], bb[271], bb[272]],
				[bb[273], bb[274], bb[275], bb[276], bb[277], bb[278], bb[279]],
				["Mezzocorona Piovi", bb[281], bb[282], bb[283], bb[284], bb[285], bb[286]],
				[bb[287], bb[288], bb[289], bb[290], bb[291], bb[292], bb[293]],
				[bb[294], bb[295], bb[296], bb[297], bb[298], bb[299], bb[300]],
				[bb[301], bb[302], bb[303], bb[304], bb[305], bb[306], bb[307]],
				[bb[308], bb[309], bb[310], bb[311], bb[312], bb[313], bb[314]],
				[bb[315], bb[316], bb[317], bb[318], bb[319], bb[320], bb[321]],
				[bb[322], bb[323], bb[324], bb[325], bb[326], bb[327], bb[328]],
				[bb[329], bb[330], bb[331], bb[332], bb[333], bb[334], bb[335]],
				[bb[336], bb[337], bb[338], bb[339], bb[340], bb[341], bb[342]],
				[bb[343], bb[344], bb[345], bb[346], bb[347], bb[348], bb[349]],
				[bb[350], bb[351], bb[352], bb[353], bb[354], bb[355], bb[356]],
				[bb[357], bb[358], bb[359], bb[360], bb[361], bb[362], bb[363]],
				[bb[364], bb[365], bb[366], bb[367], bb[368], bb[369], bb[370]],
				[bb[371], bb[372], bb[373], bb[374], bb[375], bb[376], bb[377]],
				[bb[378], bb[379], bb[380], bb[381], bb[382], bb[383], bb[384]],
				[bb[385], bb[386], bb[387], bb[388], bb[389], bb[390], bb[391]],
				[bb[392], bb[393], bb[394], bb[395], bb[396], bb[397], bb[398]],
				[bb[399], bb[400], bb[401], bb[402], bb[403], bb[404], bb[405]],
				[bb[406], bb[407], bb[408], bb[409], bb[410], bb[411], bb[412]],
				[bb[413], bb[414], bb[415], bb[416], bb[417], bb[418], bb[419]]]
		table1 = Table(data1, colWidths=inch)									# inizializzazione tabella
		table1.setStyle([("VALIGN", (-1,-1), (-1,-1), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black),
						("FONTSIZE", (0,0), (-1,-1), 7),
						("ALIGN", (0,0), (-1,-1), "CENTER")])				# stile tabella
		table1.wrapOn(self.c, self.width, self.height)							# importazione nel foglio della tabella
		table1.drawOn(self.c, *self.coord(18, 250, mm))							# disegno della tabella a coordinate...

		self.c.showPage()
		data2 = [["Nome stazione", "Temperatura media", "Umidità", "Pioggia", "Bagnatura fogliare", "Velocità vento", "Radiazione solare"],
				[bb[420], bb[421], bb[422], bb[423], bb[424], bb[425], bb[426]],
				[bb[427], bb[428], bb[429], bb[430], bb[431], bb[432], bb[433]],
				[bb[434], bb[435], bb[436], bb[437], bb[438], bb[439], bb[440]],
				[bb[441], bb[442], bb[443], bb[444], bb[445], bb[446], bb[447]],
				[bb[448], bb[449], bb[450], bb[451], bb[452], bb[453], bb[454]],
				[bb[455], bb[456], bb[457], bb[458], bb[459], bb[460], bb[461]],
				[bb[462], bb[463], bb[464], bb[465], bb[466], bb[467], bb[468]],
				[bb[469], bb[470], bb[471], bb[472], bb[473], bb[474], bb[475]],
				[bb[476], bb[477], bb[478], bb[479], bb[480], bb[481], bb[482]],
				[bb[483], bb[484], bb[485], bb[486], bb[487], bb[488], bb[489]],
				[bb[490], bb[491], bb[492], bb[493], bb[494], bb[495], bb[496]],
				[bb[497], bb[498], bb[499], bb[500], bb[501], bb[502], bb[503]],
				[bb[504], bb[505], bb[506], bb[507], bb[508], bb[509], bb[510]],
				[bb[511], bb[512], bb[513], bb[514], bb[515], bb[516], bb[517]],
				[bb[518], bb[519], bb[520], bb[521], bb[522], bb[523], bb[524]],
				[bb[525], bb[526], bb[527], bb[528], bb[529], bb[530], bb[531]],
				[bb[532], bb[533], bb[534], bb[535], bb[536], bb[537], bb[538]],
				[bb[539], bb[540], bb[541], bb[542], bb[543], bb[544], bb[545]],
				[bb[546], bb[547], bb[548], bb[549], bb[550], bb[551], bb[552]],
				[bb[553], bb[554], bb[555], bb[556], bb[557], bb[558], bb[559]],
				[bb[560], bb[561], bb[562], bb[563], bb[564], bb[565], bb[566]],
				[bb[567], bb[568], bb[569], bb[570], bb[571], bb[572], bb[573]],
				[bb[574], bb[575], bb[576], bb[577], bb[578], bb[579], bb[580]],
				[bb[581], bb[582], bb[583], bb[584], bb[585], bb[586], bb[587]],
				[bb[588], bb[589], bb[590], bb[591], bb[592], bb[593], bb[594]],
				[bb[595], bb[596], bb[597], bb[598], bb[599], bb[600], bb[601]],]
		table2 = Table(data2, colWidths=inch)									# inizializzazione tabella
		table2.setStyle([("VALIGN", (-1,-1), (-1,-1), "TOP"),
						("GRID", (0,0), (-1,-1), 1, colors.black),
						("GRID", (0,0), (-1,0), 1, colors.black),
						("FONTSIZE", (0,0), (-1,-1), 7),
						("ALIGN", (0,0), (-1,-1), "CENTER")])				# stile tabella
		table2.wrapOn(self.c, self.width, self.height)							# importazione nel foglio della tabella
		table2.drawOn(self.c, *self.coord(18, 200, mm))							# disegno della tabella a coordinate...


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
	aa = ['Ala', 'Aldeno', 'Arco', 'Arsio', 'Avio', 'Banco_Casez', 'Baselga_di_Pine', 'Besagno', 'Besenello', 'Bezzecca', 'Bleggio_Superiore',
		'Borgo_Valsugana', 'Brancolino', 'Caldes', 'Caldonazzo','Caldonazzo_Brina','Cavedine', 'Cembra', 'Cles', 'Cognola', 'Coredo', 'Cunevo', 'Denno', 'Dercolo',
		'Dro', 'Faedo_Maso_Togn', 'Fondo', 'Gardolo', 'Giovo_Bosch', 'Lavaze', 'Lavis', 'Levico', 'Livo', 'Lomaso', 'Loppio', 'Malga_Flavona',
		'Mama_di_Avio', 'Marco', 'Maso_Callianer', 'Mezzocorona_Novali', 'Mezzocorona_Piovi_Veci', 'Mezzolombardo', 'Mori', 'Nago', 'Nanno',
		'Nave_San_Rocco', 'Nomi', 'Ospedaletto', 'Paneveggio', 'Passo_Vezzena', 'Pedersano', 'Pellizzano', 'Pergine', 'Pietramurata', 'Pinzolo_Pra_Rodont',
		'Polsa', 'Predazzo', 'Prezzano', 'Rabbi', 'Revo', 'Riva_del_Garda', 'Romagnano', 'Romeno', 'Ronzo_Chienis', 'Rovere_della_Luna', 'Rovereto',
		'S_Michele_a_A', 'S_Orsola', 'Sarche', 'Savignano', 'Segno', 'Serravalle', 'Spormaggiore', 'Stenico', 'Storo', 'Telve', 'Terlago', 'Terzolas',
		'Ton', 'Toss_Castello', 'Trento_Sud', 'Verla', 'Vigolo_Vattaro', 'Volano', 'Zambana', 'Zortea']
	bb = list()
	ban = 0
	data = "2017"																						# lista di tutte le stazioni
	for a in aa:
		pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Program/", "Stazioni_Meteo_Trentino", a, data, "dati", "csv"))			# pathname iniziale
		final_pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Program/","report/", "report"))	#pathname finale
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

				ban = ban+1
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
				row = nomeStat,'%d' %(percTMED), '%d' %(percUMID), '%d' %(percPG), '%d' %(percFB), '%d' %(percVenVel), '%d' %(percRAD)
				bb.extend(row)
	doc = PDFMaker(final_pathname + data + ".pdf", nomeStat)		# creazione del pdf con parametri
	doc.createDocument()																# creazione
	doc.savePDF()
