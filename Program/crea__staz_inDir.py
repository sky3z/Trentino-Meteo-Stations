import os
import csv
from Log_Bot_xls import *
from main import *

def create_folder(data_iniziale):
	with open('Program/stazioni_meteo.csv') as csvDataFile:
		csvReader = csv.reader(csvDataFile)
		for row in csvReader:
			newstat = row[1]
			if not os.path.exists('Program/Stazioni_Meteo_Trentino/' + newstat):
				os.makedirs('Program/Stazioni_Meteo_Trentino/' + newstat)
			final_dir0 = os.path.join('Program/Stazioni_Meteo_Trentino', newstat, str(data_iniziale.year))
			if not os.path.exists(final_dir0):
				os.makedirs(final_dir0)
			final_dir2 = os.path.join('Program/Stazioni_Meteo_Trentino', newstat, str(data_iniziale.year), 'dati')
			if not os.path.exists(final_dir2):
				os.makedirs(final_dir2)
			final_dir3 = os.path.join('Program/Stazioni_Meteo_Trentino', newstat, str(data_iniziale.year), 'dati', 'csv')
			if not os.path.exists(final_dir3):
				os.makedirs(final_dir3)
			final_dir4 = os.path.join('Program/Stazioni_Meteo_Trentino', newstat, str(data_iniziale.year), 'dati', 'xls')
			if not os.path.exists(final_dir4):
				os.makedirs(final_dir4)
			final_dir5 = os.path.join('Program/Stazioni_Meteo_Trentino', newstat, str(data_iniziale.year), 'report')
			if not os.path.exists(final_dir5):
				os.makedirs(final_dir5)
