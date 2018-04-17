import urllib2, csv
from bs4 import BeautifulSoup

#CSV stuff TK

url = 'https://www.mshp.dps.missouri.gov/HP71/SearchAction?searchDate=04/03/2015'
html = urllib2.urlopen(url).read() 

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'accidentOutput'})

rows = table.find_all('tr')

for row in rows: 
	cells = row.find_all('td')

	for cell in cells: 
		print cell.text
		