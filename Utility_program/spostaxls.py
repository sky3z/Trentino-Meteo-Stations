import os
import csv
aa = ['Ala', 'Aldeno', 'Arco', 'Arsio', 'Avio', 'Banco_Casez', 'Baselga_di_Pine', 'Besagno', 'Besenello', 'Bezzecca', 'Bleggio_Superiore',
	'Borgo_Valsugana', 'Brancolino', 'Caldes', 'Caldonazzo','Cavedine', 'Cembra', 'Cles', 'Cognola', 'Coredo', 'Cunevo', 'Denno', 'Dercolo',
	'Dro', 'Faedo_Maso_Togn', 'Fondo', 'Gardolo', 'Giovo_Bosch', 'Lavaze', 'Lavis', 'Levico', 'Livo', 'Lomaso', 'Loppio', 'Malga_Flavona',
	'Mama_di_Avio', 'Marco', 'Maso_Callianer', 'Mezzocorona_Novali', 'Mezzocorona_Piovi_Veci', 'Mezzolombardo', 'Mori', 'Nago', 'Nanno',
	'Nave_San_Rocco', 'Nomi', 'Ospedaletto', 'Paneveggio', 'Passo_Vezzena', 'Pedersano', 'Pellizzano', 'Pergine', 'Pietramurata', 'Pinzolo_Pra_Rodont',
	'Polsa', 'Predazzo', 'Prezzano', 'Rabbi', 'Revo', 'Riva_del_Garda', 'Romagnano', 'Romeno', 'Ronzo_Chienis', 'Rovere_della_Luna', 'Rovereto',
	'S_Michele_a_A', 'S_Orsola', 'Sarche', 'Savignano', 'Segno', 'Serravalle', 'Spormaggiore', 'Stenico', 'Storo', 'Telve', 'Terlago', 'Terzolas',
	'Ton', 'Toss_Castello', 'Trento_Sud', 'Verla', 'Vigolo_Vattaro', 'Volano', 'Zambana', 'Zortea']
data = "2016"

ide_str = 0
for a in aa:
	bc = str(a)
	if bc == 'Ala':
		ide_str = "30"
	if bc == 'Aldeno':
		ide_str = "59"
	if bc == 'Arco':
		ide_str = '29'
	if bc == 'Arsio':
	 	ide_str = '43'
	if bc == 'Avio':
	 	ide_str = '51'
	if bc == 'Banco_Casez':
	 	ide_str = '39'
	if bc == 'Baselga_di_Pine':
	 	ide_str = '24'
	if bc == 'Besagno':
	 	ide_str = '50'
	if bc == 'Besenello':
	 	ide_str = '77'
	if bc == 'Bezzecca':
	 	ide_str = '85'
	if bc == 'Bleggio_Superiore':
	 	ide_str = '80'
	if bc == 'Borgo_Valsugana':
	 	ide_str = '28'
	if bc == 'Brancolino':
	 	ide_str = '78'
	if bc == 'Caldes':
	 	ide_str = '88'
	if bc == 'Caldonazzo':
	 	ide_str = '66'
	if bc == 'Caldonazzo_Brina':
	 	ide_str = '166'
	if bc == 'Cavedine':
	 	ide_str = '83'
	if bc == 'Cembra':
	 	ide_str = '44'
	if bc == 'Cles':
	 	ide_str = '31'
	if bc == 'Cognola':
	 	ide_str = '46'
	if bc == 'Coredo':
	 	ide_str = '37'
	if bc == 'Cunevo':
	 	ide_str = '36'
	if bc == 'Denno':
	 	ide_str = '25'
	if bc == 'Dercolo':
	 	ide_str = '34'
	if bc == 'Dro':
	 	ide_str = '54'
	if bc == 'Faedo_Maso_Togn':
	 	ide_str = '22'
	if bc == 'Fondo':
	 	ide_str = '84'
	if bc == 'Gardolo':
	 	ide_str = '76'
	if bc == 'Giovo_Bosch':
	 	ide_str = '94'
	if bc == 'Lavaze':
	 	ide_str = '19'
	if bc == 'Lavis':
	 	ide_str = '97'
	if bc == 'Levico':
	 	ide_str = '52'
	if bc == 'Livo':
	 	ide_str = '79'
	if bc == 'Lomaso':
	 	ide_str = '23'
	if bc == 'Loppio':
	 	ide_str = '62'
	if bc == 'Malga_Flavona':
	 	ide_str = '89'
	if bc == 'Mama_di_Avio':
	 	ide_str = '65'
	if bc == 'Marco':
	 	ide_str = '64'
	if bc == 'Maso_Callianer':
	 	ide_str = '92'
	if bc == 'Mezzocorona_Novali':
	 	ide_str = '45'
	if bc == 'Mezzocorona_Piovi_Veci':
	 	ide_str = '72'
	if bc == 'Mezzolombardo':
	 	ide_str = '58'
	if bc == 'Mori':
	 	ide_str = '49'
	if bc == 'Nago':
	 	ide_str = '55'
	if bc == 'Nanno':
	 	ide_str = '38'
	if bc == 'Nave_San_Rocco':
	 	ide_str = '71'
	if bc == 'Nomi':
	 	ide_str = '60'
	if bc == 'Ospedaletto':
	 	ide_str = '68'
	if bc == 'Paneveggio':
	 	ide_str = '8'
	if bc == 'Passo_Vezzena':
	 	ide_str = '12'
	if bc == 'Pedersano':
	 	ide_str = '48'
	if bc == 'Pellizzano':
	 	ide_str = '73'
	if bc == 'Pergine':
	 	ide_str = '67'
	if bc == 'Pietramurata':
	 	ide_str = '69'
	if bc == 'Pinzolo_Pra_Rodont':
	 	ide_str = '11'
	if bc == 'Polsa':
	 	ide_str = '13'
	if bc == 'Predazzo':
	 	ide_str = '87'
	if bc == 'Prezzano':
	 	ide_str = '96'
	if bc == 'Rabbi':
	 	ide_str = '14'
	if bc == 'Revo':
	 	ide_str = '41'
	if bc == 'Riva_del_Garda':
	 	ide_str = '15'
	if bc == 'Romagnano':
	 	ide_str = '47'
	if bc == 'Romeno':
	 	ide_str = '74'
	if bc == 'Ronzo_Chienis':
	 	ide_str = '21'
	if bc == 'Rovere_della_Luna':
	 	ide_str = '57'
	if bc == 'Rovereto':
	 	ide_str = '26'
	if bc == 'S_Michele_a_A':
	 	ide_str = '27'
	if bc == 'S_Orsola':
	 	ide_str = '53'
	if bc == 'Sarche':
	 	ide_str = '91'
	if bc == 'Savignano':
	 	ide_str = '18'
	if bc == 'Segno':
	 	ide_str = '40'
	if bc == 'Serravalle':
	 	ide_str = '63'
	if bc == 'Spormaggiore':
	 	ide_str = '35'
	if bc == 'Stenico':
	 	ide_str = '90'
	if bc == 'Storo':
	 	ide_str = '82'
	if bc == 'Telve':
	 	ide_str = '81'
	if bc == 'Terlago':
	 	ide_str = '70'
	if bc == 'Terzolas':
	 	ide_str = '93'
	if bc == 'Ton':
	 	ide_str = '33'
	if bc == 'Toss_Castello':
	 	ide_str = '95'
	if bc == 'Trento_Sud':
	 	ide_str = '32'
	if bc == 'Verla':
	 	ide_str = '20'
	if bc == 'Vigolo_Vattaro':
	 	ide_str = '86'
	if bc == 'Volano':
	 	ide_str = '61'
	if bc == 'Zambana':
	 	ide_str = '56'
	if bc == 'Zortea':
	 	ide_str = '75'
	ini_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "Database_Trentino_FMACH_xls", a, a + "_" + data+".xls"))
	final_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Program", "Stazioni_Meteo_Trentino", a, data, "dati/", "xls/"))
	print(ide_str)
	os.rename(ini_path, final_path +"\\"+ ide_str + ".xls")
