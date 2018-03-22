import urllib2, csv
#imported urllib2 library
from bs4 import BeautifulSoup
#imported Beautiful Soup library from bs4 
outfile = open('jaildata.csv', 'w')
#creates a file that links python to my computer's file system
#names the file jaildata.csv and indicates that I will be writing to the file
writer = csv.writer(outfile)
#Tells python that writer = writing a CSV file and naming it csv.writer?
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#specifies the URL where data will be scraped from; sets it equal to the function variable URL
html = urllib2.urlopen(url).read()
#uses urllib2 to get the HTML page of the URL declared, sets it equal to the variable html
soup = BeautifulSoup(html, "html.parser")
#parses the html using Beautiful Soup and stores the result in the variable soup

tbody = soup.find('tbody', {'class': 'stripe'})
#find the class named stripe and get tis value, store it in the variable tbody
rows = tbody.find_all('tr')
#gets all the rows with stripe?
for row in rows:
#for each row in the results found from the above code
    cells = row.find_all('td')
#each row is set equal to the value "cell"
    data = []
#anything inside [] is set equal to data
    for cell in cells:
    	#for each cell in the new value cells, which actually is a row?
        data.append(cell.text)
        #append data to the text in that cell
    writer.writerow(data)
    #write the row with the new result