import requests
from bs4 import BeautifulSoup






URL = "https://www.nature.com/news"

headers = {
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
	"Accept":"*/*"
}


row_html = requests.get(URL, headers=headers).text

with open("data/nature.html", "w") as file:
	file.write(row_html)

with open("data/nature.html", "r") as file:
	row = file.read()


soup = BeautifulSoup(row,'lxml')

all_titles = soup.find_all(class_="c-card__title u-serif u-text17 u-font-weight--regular")

print(all_titles)