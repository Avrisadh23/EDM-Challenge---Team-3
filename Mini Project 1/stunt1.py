import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.ridvanmau.com/tabel-tumbuh-kembang-anak/#google_vignette"
page = requests.get(URL)

content = page.text
#print (content)

bs4 = BeautifulSoup(content, 'html.parser')


tabelStunting = bs4.find_all('h3' > 'table' , id = 'tabel-tumbuh-kembang-anak-usia-0-24-bulan')

list_rt = bs4.find_all("tr")


headers = ['Usia' , 'Motorik' , 'Bahasa', 'Emosi']

writer = csv.writer(open('Data.csv', 'w', newline=''))
writer.writerow(headers)

for tr in list_rt:
    data = []
    
    list_td = tr.find_all('td')
    for td in list_td:
        data.append(td.text)
        
    writer.writerow(data)
        
 