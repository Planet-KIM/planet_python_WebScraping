import csv
from io import StringIO
from urllib.request import urlopen

url = 'http://pythonscraping.com/files/MontyPythonAlbums.csv'
data = urlopen(url).read().decode('ascii', 'ignore')
dataFile = StringIO(data)
#csvReader = csv.reader(dataFile)

dictReader = csv.DictReader(dataFile)

#for row in csvReader:
#    #print(row)
#    print('The album = "{}" was released in {}'.format(row[0], str(row[1])))

for row in dictReader:
    print(row)
