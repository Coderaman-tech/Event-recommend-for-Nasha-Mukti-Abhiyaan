from bs4 import BeautifulSoup
import requests
from csv import writer

state=input("Enter the state: ")
district=input("Enter the district: ")



html_text=requests.get("https://nmba.dosje.gov.in/photo-gallery-dashboard.php?state="+state+"&district="+district+"&filter=#").text


soup=BeautifulSoup(html_text,'lxml')
lists=soup.find_all('div',class_='h600')
fh=open('data.txt','w',encoding="utf-8")

for l in lists:
    # fh.write(l.text)
    s=l.text
    fh.write(s)
