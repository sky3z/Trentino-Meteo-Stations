"""
Script Python creato per comodità nel scrivere il programma idd_down e idd_str,
questo "programma" scrive in un file chiamato ciclo_stazioni delle righe di codice
che poi verranno utilizzate.
"""

import os      # importazione modulo os
import csv		# importazione modulo csv per operare su file csv

with open('stazioni_meteo.csv') as csvDataFile:		# apre il file stazioni_meteo.csv
    csvReader = csv.reader(csvDataFile)				# legge il file
    file = open("ciclo_stazioni.txt", "w")			# apre un nuovo file chiamato ciclo_stazioni.txt con permessi di scrittura
    for row in csvReader:							# per ogni riga nel file csv
        print(row[1], row[2])						# stampa ogni riga in posizione 1 e 2
        file.write("elif ide_str == str(%s):\n"		# testo da stampare nel file ciclo_stazioni.txt
            "   pat_str = '%s/'\n" %(int(row[2]), row[1]))
    file.close()									# chiude il file e finisce la scrittura
