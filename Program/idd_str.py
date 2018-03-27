"""
Programma che viene richiamato nel file main "Log_Bot_xls.py", questa è una funzione che indica,
in base a quale valore assume ide_str che è l'ID di ogni stazione a quale cartella deve "andare"
il file csv
"""
from Log_Bot_xls import *			# importazione da Log_Bot_xls di tutto
import os							# importazione del modulo os


def trova_path(ide_str, data_iniziale):   # funzione trova_path()
	pat_ide = ide_str					  # la variabile pat_ide è uguale alla variabile ide_str
	if pat_ide == ide_str:    			  # Controllo inutile ma sempre funzionale, in quanto controlla che le due variabili siano uguali prima di proseguire
		if ide_str == str(30):			  # ciclo che se ide_str corrisponde alla determinata stringa, fa diventare la variabile pat_ide uaguale al nome della stazione assegnatale
			pat_ide = "Ala/"
		elif ide_str == str(59):
			pat_ide = "Aldeno/"
		elif ide_str == str(29):
			pat_ide = "Arco/"
		elif ide_str == str(43):
			pat_ide = "Arsio/"
		elif ide_str == str(51):
			pat_ide = "Avio/"
		elif ide_str == str(39):
			pat_ide = "Banco_Casez/"
		elif ide_str == str(24):
			pat_ide = "Baselga_di_Pine/"
		elif ide_str == str(50):
			pat_ide = "Besagno/"
		elif ide_str == str(77):
			pat_ide = "Besenello/"
		elif ide_str == str(85):
			pat_ide = "Bezzecca/"
		elif ide_str == str(80):
			pat_ide = "Bleggio_Superiore/"
		elif ide_str == str(28):
			pat_ide = "Borgo_Valsugana/"
		elif ide_str == str(78):
			pat_ide = "Brancolino/"
		elif ide_str == str(88):
			pat_ide = "Caldes/"
		elif ide_str == str(66):
			pat_ide = "Caldonazzo/"
		elif ide_str == str(166):
			pat_ide = "Caldonazzo_Brina/"
		elif ide_str == str(83):
			pat_ide = "Cavedine/"
		elif ide_str == str(44):
			pat_ide = "Cembra/"
		elif ide_str == str(31):
			pat_ide = "Cles/"
		elif ide_str == str(46):
			pat_ide = "Cognola/"
		elif ide_str == str(37):
			pat_ide = "Coredo/"
		elif ide_str == str(36):
			pat_ide = "Cunevo/"
		elif ide_str == str(25):
			pat_ide = "Denno/"
		elif ide_str == str(34):
			pat_ide = "Dercolo/"
		elif ide_str == str(54):
			pat_ide = "Dro/"
		elif ide_str == str(22):
			pat_ide = "Faedo_Maso_Togn/"
		elif ide_str == str(84):
			pat_ide = "Fondo/"
		elif ide_str == str(76):
			pat_ide = "Gardolo/"
		elif ide_str == str(94):
			pat_ide = "Giovo_Bosch/"
		elif ide_str == str(19):
			pat_ide = "Lavaze/"
		elif ide_str == str(97):
			pat_ide = "Lavis/"
		elif ide_str == str(52):
			pat_ide = "Levico/"
		elif ide_str == str(79):
			pat_ide = "Livo/"
		elif ide_str == str(23):
			pat_ide = "Lomaso/"
		elif ide_str == str(62):
			pat_ide = "Loppio/"
		elif ide_str == str(89):
			pat_ide = "Malga_Flavona/"
		elif ide_str == str(65):
			pat_ide = "Mama_di_Avio/"
		elif ide_str == str(64):
			pat_ide = "Marco/"
		elif ide_str == str(92):
			pat_ide = "Maso_Callianer/"
		elif ide_str == str(45):
			pat_ide = "Mezzocorona_Novali/"
		elif ide_str == str(72):
			pat_ide = "Mezzocorona_Piovi_Veci/"
		elif ide_str == str(58):
			pat_ide = "Mezzolombardo/"
		elif ide_str == str(49):
			pat_ide = "Mori/"
		elif ide_str == str(55):
			pat_ide = "Nago/"
		elif ide_str == str(38):
			pat_ide = "Nanno/"
		elif ide_str == str(71):
			pat_ide = "Nave_San_Rocco/"
		elif ide_str == str(60):
			pat_ide = "Nomi/"
		elif ide_str == str(68):
			pat_ide = "Ospedaletto/"
		elif ide_str == str(8):
			pat_ide = "Paneveggio/"
		elif ide_str == str(12):
			pat_ide = "Passo_Vezzena/"
		elif ide_str == str(48):
			pat_ide = "Pedersano/"
		elif ide_str == str(73):
			pat_ide = "Pellizzano/"
		elif ide_str == str(67):
			pat_ide = "Pergine/"
		elif ide_str == str(69):
			pat_ide = "Pietramurata/"
		elif ide_str == str(11):
			pat_ide = "Pinzolo_Pra_Rodont/"
		elif ide_str == str(13):
			pat_ide = "Polsa/"
		elif ide_str == str(87):
			pat_ide = "Predazzo/"
		elif ide_str == str(96):
			pat_ide = "Prezzano/"
		elif ide_str == str(14):
			pat_ide = "Rabbi/"
		elif ide_str == str(41):
			pat_ide = "Revo/"
		elif ide_str == str(15):
			pat_ide = "Riva_del_Garda/"
		elif ide_str == str(47):
			pat_ide = "Romagnano/"
		elif ide_str == str(74):
			pat_ide = "Romeno/"
		elif ide_str == str(21):
			pat_ide = "Ronzo_Chienis/"
		elif ide_str == str(57):
			pat_ide = "Rovere_della_Luna/"
		elif ide_str == str(26):
			pat_ide = "Rovereto/"
		elif ide_str == str(27):
			pat_ide = "S_Michele_a_A/"
		elif ide_str == str(53):
			pat_ide = "S_Orsola/"
		elif ide_str == str(91):
			pat_ide = "Sarche/"
		elif ide_str == str(18):
			pat_ide = "Savignano/"
		elif ide_str == str(40):
			pat_ide = "Segno/"
		elif ide_str == str(63):
			pat_ide = "Serravalle/"
		elif ide_str == str(35):
			pat_ide = "Spormaggiore/"
		elif ide_str == str(90):
			pat_ide = "Stenico/"
		elif ide_str == str(82):
			pat_ide = "Storo/"
		elif ide_str == str(81):
			pat_ide = "Telve/"
		elif ide_str == str(70):
			pat_ide = "Terlago/"
		elif ide_str == str(93):
			pat_ide = "Terzolas/"
		elif ide_str == str(33):
			pat_ide = "Ton/"
		elif ide_str == str(95):
			pat_ide = "Toss_Castello/"
		elif ide_str == str(32):
			pat_ide = "Trento_Sud/"
		elif ide_str == str(20):
			pat_ide = "Verla/"
		elif ide_str == str(86):
			pat_ide = "Vigolo_Vattaro/"
		elif ide_str == str(61):
			pat_ide = "Volano/"
		elif ide_str == str(56):
			pat_ide = "Zambana/"
		elif ide_str == str(75):
			pat_ide = "Zortea/"
		else:						# altrimenti
			print("ERROR: The program can't associate the file to a folder")	 # stampa il testo
	k = dict(IP="Stazioni_Meteo_Trentino/", ID=pat_ide)			# creazione di un dizionario con chiave IP e valore ID che corrisponde a pat_ide
	return(k["IP"] + k["ID"] + str(data_iniziale.year)+ "/" + "dati/" + "csv/")		# ritorna al programma Log_Bot_xls la path
