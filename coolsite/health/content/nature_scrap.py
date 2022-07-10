import requests
from bs4 import BeautifulSoup






URL = "https://www.nature.com/news"

headers = {
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
	"Accept":"*/*"
}


row_html = requests.get(URL, headers=headers).text

print(row_html)