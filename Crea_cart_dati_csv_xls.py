"""
Programma che crea le sottocartelle csv e xls, in tutte le cartelle delle stazioni meteo,
questo programma "sfrutta" il modulo os per poter creare le cartelle e conoscere la path dove
poterla creare. Logicamente se questa non esiste già, come dice il comando if not os.path.exists(nome).
"""

import os                              # importazione del modulo os

           # lista di tutte le stazioni ottenuta dal file csv tramite uno script
aa = ['Ala','Aldeno','Arco','Arsio','Avio','Banco_Casez','Baselga_di_Pine','Besagno','Besenello','Bezzecca','Bleggio_Superiore',
'Borgo_Valsugana','Brancolino','Caldes','Caldonazzo','Cavedine','Cembra','Cles','Cognola','Coredo','Cunevo','Denno','Dercolo',
'Dro','Faedo_Maso_Togn','Fondo','Gardolo','Giovo_Bosch','Lavaze','Lavis','Levico','Livo','Lomaso','Loppio','Malga_Flavona',
'Mama_di_Avio','Marco','Maso_Callianer','Mezzocorona_Novali','Mezzocorona_Piovi_Veci','Mezzolombardo','Mori','Nago','Nanno',
'Nave_San_Rocco','Nomi','Ospedaletto','Paneveggio','Passo_Vezzena','Pedersano','Pellizzano','Pergine','Pietramurata','Pinzolo_Pra_Rodont',
'Polsa','Predazzo','Prezzano','Rabbi','Revo','Riva_del_Garda','Romagnano','Romeno','Ronzo_Chienis','Rovere_della_Luna','Rovereto',
'S_Michele_a_A','S_Orsola','Sarche','Savignano','Segno','Serravalle','Spormaggiore','Stenico','Storo','Telve','Terlago','Terzolas',
'Ton','Toss_Castello','Trento_Sud','Verla','Vigolo_Vattaro','Volano','Zambana','Zortea']

for a in aa:                          # per a in tutte le posizioni della lista
	curr_dir = os.getcwd()            # si prende la directory corrente
	final_dir = os.path.join(curr_dir, 'Stazioni_Meteo_Trentino', a, '2017','dati',' ' )#aggiungere 'csv' o 'xls' in base a quale cartella si vuole creare
	if not os.path.exists(final_dir): # se la cartella 'csv' o 'xls' non esiste già
		os.makedirs(final_dir)        # crea la cartella con la path di final_dir
