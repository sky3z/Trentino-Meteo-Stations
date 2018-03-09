"""
Programma creato per creare le cartelle di tutte le stazioni in Stazioni_Meteo_Trentino/
Anche questo programma è stato creato per utilità nel creare le cartelle automaticamente
e non fare tutto manualmente
"""

import os			# importazione del modulo os per operare sul sistema
import csv			# importazione del modulo csv per operare su file csv

with open('stazioni_meteo.csv') as csvDataFile:		# apre il file csv stazioni_meteo.csv come csvDataFile
    csvReader = csv.reader(csvDataFile)				# legge il file csv
    for row in csvReader:							# per ogni riga nel file csv
        print(row[1])								# stampa ogni riga in posizione 1
        newpath = row[1]							# la variabile newpath è uguale a row[1]
        if not os.path.exists(newpath):				# se non esiste già una cartelle chiamata come la variabile newpath
            os.makedirs(newpath)					# allora creala con il nome newpath
													# attenzione! newpath corrisponde alla posizione 1 di ogni riga nel file csv
