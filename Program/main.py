"""
Programma principale il quale richiama la funzione logBot() da Log_Bot_xls
"""
from Log_Bot_xls import *												# importazione di tutto da Log_Bot_xls
from crea__staz_inDir import *											# importazione da crea__staz_inDir
import datetime as dt													# import di datetime provvisorio

def main():
	oggi = dt.datetime(2015,12,31,23)
	data_iniziale = oggi - dt.timedelta(hours = 8759)
	create_folder(data_iniziale)										# funzione main
	logBot(oggi, data_iniziale)											# richiama funzione logBot()


if __name__ == '__main__':												# se il file è avviato manualmente
	main()																# avvia main()
