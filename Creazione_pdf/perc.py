import os

aa = ['Ala', 'Aldeno', 'Arco', 'Arsio', 'Avio', 'Banco_Casez', 'Baselga_di_Pine', 'Besagno', 'Besenello', 'Bezzecca', 'Bleggio_Superiore',
	'Borgo_Valsugana', 'Brancolino', 'Caldes', 'Caldonazzo','Cavedine', 'Cembra', 'Cles', 'Cognola', 'Coredo', 'Cunevo', 'Denno', 'Dercolo',
	'Dro', 'Faedo_Maso_Togn', 'Fondo', 'Gardolo', 'Giovo_Bosch', 'Lavaze', 'Lavis', 'Levico', 'Livo', 'Lomaso', 'Loppio', 'Malga_Flavona',
	'Mama_di_Avio', 'Marco', 'Maso_Callianer', 'Mezzocorona_Novali', 'Mezzocorona_Piovi_Veci', 'Mezzolombardo', 'Mori', 'Nago', 'Nanno',
	'Nave_San_Rocco', 'Nomi', 'Ospedaletto', 'Paneveggio', 'Passo_Vezzena', 'Pedersano', 'Pellizzano', 'Pergine', 'Pietramurata', 'Pinzolo_Pra_Rodont',
	'Polsa', 'Predazzo', 'Prezzano', 'Rabbi', 'Revo', 'Riva_del_Garda', 'Romagnano', 'Romeno', 'Ronzo_Chienis', 'Rovere_della_Luna', 'Rovereto',
	'S_Michele_a_A', 'S_Orsola', 'Sarche', 'Savignano', 'Segno', 'Serravalle', 'Spormaggiore', 'Stenico', 'Storo', 'Telve', 'Terlago', 'Terzolas',
	'Ton', 'Toss_Castello', 'Trento_Sud', 'Verla', 'Vigolo_Vattaro', 'Volano', 'Zambana', 'Zortea']
																										# lista di tutte le stazioni
for a in aa:
	pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Program/", "Stazioni_Meteo_Trentino", a, "2015", "dati", "csv"))			# pathname iniziale
	final_pathname = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Creazione_pdf/"))	#pathname finale
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
					if a == "Ala":
					    percTOTAla = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Aldeno':
					    percTOTAldeno = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Arco':
					    percTOTArco = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Arsio':
					    percTOTArsio = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Avio':
					    percTOTAvio = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Banco_Casez':
					    percTOTBanco_Casez = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Baselga_di_Pine':
					    percTOTBaselga_di_Pine = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Besagno':
					    percTOTBesagno = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Besenello':
					    percTOTBesenello = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Bezzecca':
					    percTOTBezzecca = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Bleggio_Superiore':
					    percTOTBleggio_Superiore = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Borgo_Valsugana':
					    percTOTBorgo_Valsugana = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Brancolino':
					    percTOTBrancolino = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Caldes':
					    percTOTCaldes = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Caldonazzo':
					    percTOTCaldonazzo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Cavedine':
					    percTOTCavedine = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Cembra':
					    percTOTCembra = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Cles':
					    percTOTCles = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Cognola':
					    percTOTCognola = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Coredo':
					    percTOTCoredo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Cunevo':
					    percTOTCunevo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Denno':
					    percTOTDenno = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Dercolo':
					    percTOTDercolo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Dro':
					    percTOTDro = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Faedo_Maso_Togn':
					    percTOTFaedo_Maso_Togn = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Fondo':
					    percTOTFondo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Gardolo':
					    percTOTGardolo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Giovo_Bosch':
					    percTOTGiovo_Bosch = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Lavaze':
					    percTOTLavaze = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Lavis':
					    percTOTLavis = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Levico':
					    percTOTLevico = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Livo':
					    percTOTLivo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Lomaso':
					    percTOTLomaso = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Loppio':
					    percTOTLoppio = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Malga_Flavona':
					    percTOTMalga_Flavona = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Mama_di_Avio':
					    percTOTMama_di_Avio = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Marco':
					    percTOTMarco = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Maso_Callianer':
					    percTOTMaso_Callianer = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Mezzocorona_Novali':
					    percTOTMezzocorona_Novali = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Mezzocorona_Piovi_Veci':
					    percTOTMezzocorona_Piovi_Veci = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Mezzolombardo':
					    percTOTMezzolombardo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Mori':
					    percTOTMori = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Nago':
					    percTOTNago = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Nanno':
					    percTOTNanno = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Nave_San_Rocco':
					    percTOTNave_San_Rocco = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Nomi':
					    percTOTNomi = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Ospedaletto':
					    percTOTOspedaletto = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Paneveggio':
					    percTOTPaneveggio = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Passo_Vezzena':
					    percTOTPasso_Vezzena = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Pedersano':
					    percTOTPedersano = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Pellizzano':
					    percTOTPellizzano = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Pergine':
					    percTOTPergine = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Pietramurata':
					    percTOTPietramurata = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Pinzolo_Pra_Rodont':
					    percTOTPinzolo_Pra_Rodont = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Polsa':
					    percTOTPolsa = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Predazzo':
					    percTOTPredazzo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Prezzano':
					    percTOTPrezzano = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Rabbi':
					    percTOTRabbi = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Revo':
					    percTOTRevo = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Riva_del_Garda':
					    percTOTRiva_del_Garda = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Romagnano':
					    percTOTRomagnano = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Romeno':
					    percTOTRomeno = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Ronzo_Chienis':
					    percTOTRonzo_Chienis = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Rovere_della_Luna':
					    percTOTRovere_della_Luna = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Rovereto':
					    percTOTRovereto = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'S_Michele_a_A':
					    percTOTS_Michele_a_A = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'S_Orsola':
					    percTOTS_Orsola = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Sarche':
					    percTOTSarche = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Savignano':
					    percTOTSavignano = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Segno':
					    percTOTSegno = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Serravalle':
					    percTOTSerravalle = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Spormaggiore':
					    percTOTSpormaggiore = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Stenico':
					    percTOTStenico = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Storo':
					    percTOTStoro = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Telve':
					    percTOTTelve = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Terlago':
					    percTOTTerlago = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Terzolas':
					    percTOTTerzolas = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Ton':
					    percTOTTon = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Toss_Castello':
					    percTOTToss_Castello = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Trento_Sud':
					    percTOTTrento_Sud = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Verla':
					    percTOTVerla = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Vigolo_Vattaro':
					    percTOTVigolo_Vattaro = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Volano':
					    percTOTVolano = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Zambana':
					    percTOTZambana = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
					if a == 'Zortea':
					    percTOTZortea = (percTMED + percUMID + percPG + percFB + percVenVel + percRAD) / 6
print(percTOTAla,
percTOTAldeno,
percTOTArco,
percTOTArsio,
percTOTAvio,
percTOTBanco_Casez,
percTOTBaselga_di_Pine,
percTOTBesagno,
percTOTBesenello,
percTOTBezzecca,
percTOTBleggio_Superiore,
percTOTBorgo_Valsugana,
percTOTBrancolino,
percTOTCaldes,
percTOTCaldonazzo,
percTOTCavedine,
percTOTCembra,
percTOTCles,
percTOTCognola,
percTOTCoredo,
percTOTCunevo,
percTOTDenno,
percTOTDercolo,
percTOTDro,
percTOTFaedo_Maso_Togn,
percTOTFondo,
percTOTGardolo,
percTOTGiovo_Bosch,
percTOTLavaze,
percTOTLavis,
percTOTLevico,
percTOTLivo,
percTOTLomaso,
percTOTLoppio,
percTOTMalga_Flavona,
percTOTMama_di_Avio,
percTOTMarco,
percTOTMaso_Callianer,
percTOTMezzocorona_Novali,
percTOTMezzocorona_Piovi_Veci,
percTOTMezzolombardo,
percTOTMori,
percTOTNago,
percTOTNanno,
percTOTNave_San_Rocco,
percTOTNomi,
percTOTOspedaletto,
percTOTPaneveggio,
percTOTPasso_Vezzena,
percTOTPedersano,
percTOTPellizzano,
percTOTPergine,
percTOTPietramurata,
percTOTPinzolo_Pra_Rodont,
percTOTPolsa,
percTOTPredazzo,
percTOTPrezzano,
percTOTRabbi,
percTOTRevo,
percTOTRiva_del_Garda,
percTOTRomagnano,
percTOTRomeno,
percTOTRonzo_Chienis,
percTOTRovere_della_Luna,
percTOTRovereto,
percTOTS_Michele_a_A,
percTOTS_Orsola,
percTOTSarche,
percTOTSavignano,
percTOTSegno,
percTOTSerravalle,
percTOTSpormaggiore,
percTOTStenico,
percTOTStoro,
percTOTTelve,
percTOTTerlago,
percTOTTerzolas,
percTOTTon,
percTOTToss_Castello,
percTOTTrento_Sud,
percTOTVerla,
percTOTVigolo_Vattaro,
percTOTVolano,
percTOTZambana,
percTOTZortea)
