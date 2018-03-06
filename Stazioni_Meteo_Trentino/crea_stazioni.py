import os
import csv
import sys

with open('stazioni_meteo.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row[1])
        newpath = row[1]
        if not os.path.exists(newpath):
            os.makedirs(newpath)
