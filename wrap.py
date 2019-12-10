from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = "https://www.wikihouse.com/taiko/index.php?%C2%C0%B8%DD%A4%CE%C3%A3%BF%CD%20%BF%B7%E3%FE%C2%CE%A1%CA%A5%A2%A5%B8%A5%A2%C8%C7%A1%CB%A4%CE%BC%FD%CF%BF%B6%CA"
client = urlopen(url)

html = client.read().decode(client.headers.get_content_charset(), errors = "ignore")

page_soup = soup(html, "html.parser")
client.close()

containers = page_soup.findAll('table')[1].findAll('tr')

f = open("containers.txt", "w+", encoding = "UTF-8", errors = "replace")
for x in containers:
    f.write(str(x))
f.close()