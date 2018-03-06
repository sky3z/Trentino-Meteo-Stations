#bot che deve connettersi al sito http://meteo.fmach.it con le credenziali
#'USER': 	"nicola.laporta@fmach.it"
#'PWD': 	"venturia"

#import dei vari moduli necessari===============================================
import glob				#per poter ricercare i file con le regular expression
import os
import time				#per poter eseguire una pausa in secondi, per date
import xlrd				#per poter operare su file .xls

import selenium			#per poter navigare in internet in modo automatico
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import csv				#per poter salvare i dati in formato csv

from winreg import *	#per soprire l'indirizzo assoluto della cartella di download
#===============================================================================

def main():

	#ricerca la cartella di dovnload
	with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
	    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]	#path della cartella di downoad

	#Apri il file relativo alla prima stazione controllata
	# oggi = dt.datetime.today()							#data di oggi (contiene anche l'ora)
	# data_iniziale = oggi - dt.timedelta(hours = 8760)	    #un anno prima
	oggi = "2018-01-01 00:00:00"
	data_iniziale ="2017-01-01 00:00:00"

	PAUSA = 4;		#pausa in secondi da eseguire dopo ogni download

	#componenti necessari a selezionare il periodo di riferimento
	comp = ["gg_in", "mm_in", "aa_in", "hh_in", "gg_fi", "mm_fi", "aa_fi", "hh_fi"]

	#dati che si devono prelevare (temperatura, umidità, pioggia, bagnatura
	#							   fogliare, velocità del vento e radiazione solare)
	dati_prel =["DATA", "T MED [°C]", "UMID [ %]", "PG [mm]", "FB [min]", "VEN-VEL n[m/s]", "RAD [MJ/mq]"]

	usernameStr = "nicola.laporta@fmach.it"		#nome utente
	passwordStr = "venturia"					#password utente

	#cartella personalizzata di download
	cartella = "Xls_download/"


	#connessione al sito http://www.fmach.it/user/login ============================
	browser = selenium.webdriver.Chrome()		#creazione oggetto
	browser.get("http://www.fmach.it/user/login")


	#ricerca campi di inserimento username, password================================
	username = browser.find_element_by_id("inputEmail")  	#barra nome utente
	password = browser.find_element_by_id("inputPassword") 	#barra password
	accedi = browser.find_element_by_name("LoginButton")	#ricerca pulsante conferma


	#inserimento nome utente e password ============================================
	username.send_keys(usernameStr)		#invio nome utente
	password.send_keys(passwordStr)		#invio password
	accedi.click()						#pressione pulsante conferma


	#Accesso alla pagina con le tabelle da controllare =============================
	meteo = browser.find_element_by_link_text("Meteo")				#ricerca pulsante "Meteo"
	meteo.click()													#pressione pulsante "Meteo"
	dati = browser.find_element_by_link_text("DATI")				#ricerca pulsante "Dati"
	dati.click()													#pressione pulsante "Dati"
	tabelle = browser.find_element_by_link_text("Tabelle Pronte")	#ricerca pulsante "Tabelle pronte"
	tabelle.click()													#pressione pulsante "Tabelle pronte"

	#Al momento vengono scaricati solo i dati relativi all'ora corrente
	dati_stazioni = []		#lista di dati scaricati

	num = 0

	while True:
		#try:
		num = num + 1
		num_str = str(num)

		#località stazione meteo
		loc = browser.find_element_by_xpath('//*[@id="articolo"]/form/select[1]/option[' + num_str + ']')

		#estrazione dati utili
		nam = loc.text
		nam = nam.strip()
		nam_str,  ide_str= nam.split("(")
		ide_str = ide_str.replace(")", "")
		ide_str = ide_str.strip()	#id stazione
		nam_str = nam_str.strip()	#nome stazione

		loc.click()			#selezione località meteo

		#modalità di ricerca dei dati (orario con selezione di data)
		mod = browser.find_element_by_xpath('//*[@id="articolo"]/form/select[2]/option[5]')
		mod.click()			#selezione modalità di ricerca

		#orario effettivo da ricercare
		orario = [data_iniziale.day, data_iniziale.month, data_iniziale.year,
					data_iniziale.hour, oggi.day, oggi.month, oggi.year, oggi.hour]

		#inserimento orario
		for i in range(8):
			campo = browser.find_element_by_name(comp[i])	#trova la casella
			campo.send_keys(Keys.CONTROL + "a")				#selezionane il testo
			campo.send_keys(Keys.DELETE)					#rimuovilo
			campo.send_keys(orario[i])						#sostituiscilo

		#ricerca il pulsante "Invia" per confermare la selezione
		invia = browser.find_element_by_xpath('//*[@id="articolo"]/form/input[9]')
		invia.click()		#pressione pulsante "Invia"

		#trova il pulsante per scaricare il file in formato xls
		download = browser.find_element_by_xpath('//*[@id="articolo"]/form[2]/button')
		download.click()

		while True:
			lista = glob.glob(Downloads + "\\*.xls")	#lista di tutti i file ".xls" presenti all'interno della cartella di download
			if(len(lista) == 0):	#continua a controllare e se nella cartella download non ci sono file ".xls"
				time.sleep(PAUSA)	#aspetta <PAUSA> secondi e poi
				pass				#continua a controllare
			else:					#altrimenti
				time.sleep(PAUSA)	#aspetta <PAUSA> secondi e poi
				break				#prosegui

		#trova il nome del file appena scaricato ===================================
		#cerca nella tabella di download tutti i file .xls
		path_file_nuovo = max(lista, key=os.path.getctime)			#cerca il file più recente
		path_file_nuovo = str(path_file_nuovo)						#trasforma il suo path in una stringa
		nome_file_nuovo = path_file_nuovo.split("\\")[-1]			#trova il suo nome

		try:
			os.remove(cartella + ide_str + ".xls")		#se il file finale esiste già nella cartella di default, rimuovilo
		except FileNotFoundError:
			pass										#se il file non eseiste, invece, non fare nulla

		os.rename(path_file_nuovo, cartella + ide_str + ".xls")			#sposta il file finale nella cartella di default

		#preparati per scrivere sul file csv =======================================
		with open("Stazioni_Meteo_Trentino/" + ide_str + ".csv", "w") as myfile:		#crea i nuovi file all'interno della cartella "Stazioni_Meteo_Trentino"
			wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)			#inizializzo subito il writer csv, in modo tale da poter scriver deirettamente su un nuovo file csv
			#inserisci i riferimenti all'interno del file csv finale
			wr.writerow(["NUMERO", "ID", "NOME", "DATA", "T MED", "UMID", "PG", "FB", "VEN-VEL", "RAD"])

		#apertura file e controllo dei suoi dati ===================================

			file_xls = xlrd.open_workbook(cartella + ide_str + ".xls")		#apri il file appena salvato
			sheet = file_xls.sheet_by_index(0)								#seleziona il foglio di lavoro

			for riga in range(sheet.nrows):					#cicla su ogni riga
				if(riga == 0):
					continue								#la riga contiene riferimenti che non servono, allora va saltata

				dati = []									#blocco di dati che va scritto poi nel file .csv
				dati.append(num_str.strip())				#aggiungi il numero della stazione
				dati.append(ide_str.strip())				#aggiungi l'id della stazione
				dati.append(nam_str.strip())				#aggiungi il nome della stazione
				dati.append(sheet.cell_value(riga, 0))		#aggiungi la data
				dati.append(sheet.cell_value(riga, 1))		#aggiungi la temperatura media
				dati.append(sheet.cell_value(riga, 2))		#aggiungi l'umidità
				dati.append(sheet.cell_value(riga, 3))		#aggiungi la pioggia
				dati.append(sheet.cell_value(riga, 5))		#aggiungi la bagnatura fogliare
				dati.append(sheet.cell_value(riga, 7))		#aggiungi la velocità del vento
				dati.append(sheet.cell_value(riga, 8))		#aggiungi la radiazione solare

				wr.writerow(dati)							#scrivi i dati appena raccolti nel file csv

			myfile.close()									#chiudi il file csv per poterne aprire un altro

	#ritorna nella pagina prima e ripeti la procedura ==============================
		#ricerca il pulsante per tornare indietro
		ritorna = browser.find_element_by_xpath('//*[@id="articolo"]/form[1]/button')
		ritorna.click()		#premi il pulsante per tornare indietro

		#except Exception :
			#print("Lista di stazioni terminata, programa terminato")
			#break

	browser.close()			#finita tutta la procedura, chiudi la connessione
	sys.exit("Programma terminato;")	#termina l'esecuzione

if __name__ == '__main__':		#se il programma è eseguito manualmente
	main()						#richiama la funzione
