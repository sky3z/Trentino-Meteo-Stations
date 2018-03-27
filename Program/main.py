"""
Programma principale il quale richiama la funzione logBot() da Log_Bot_xls
"""
from Log_Bot_xls import *												# importazione di tutto da Log_Bot_xls
from crea__staz_inDir import *											# importazione da crea__staz_inDir													# import di datetime provvisorio

def main(oggi, data_iniziale):
        create_folder(data_iniziale)
        
