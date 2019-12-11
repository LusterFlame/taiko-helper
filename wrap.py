from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re

def wrapWikiInfo():
    url = "https://www.wikihouse.com/taiko/index.php?%C2%C0%B8%DD%A4%CE%C3%A3%BF%CD%20%BF%B7%E3%FE%C2%CE%A1%CA%A5%A2%A5%B8%A5%A2%C8%C7%A1%CB%A4%CE%BC%FD%CF%BF%B6%CA"
    client = urlopen(url)

    html = client.read().decode(client.headers.get_content_charset(), errors = "ignore")

    page_soup = soup(html, "html.parser")
    client.close()

    containers = page_soup.findAll('table')[1].findAll('tr')

    MInfoList = []
    MusicInfo = []

    f = open("containers.txt", "w+", encoding = "UTF-8", errors = "replace")
    for x in containers:
        cell = x.findAll("td")
        if len(cell) > 8:
            for count, y in enumerate(cell[:]):
                if count >= 2:
                    # Set difficulty cells as a list to store urls
                    MusicInfo.append([y.text])
                    if count == 2:
                        MusicInfo[0] = MusicInfo[0][0].rsplit(u'\u3000')[0]
                if count >= 4:
                    # make difficulty into only numbers
                    temp = MusicInfo[count - 2][0].rsplit(u'\u00D7')
                    if len(temp) > 1:
                        MusicInfo[count - 2] = [MusicInfo[count - 2][0].rsplit(u'\u00D7')[1]]
                    else:
                        MusicInfo[count - 2] = "no_exist"
                    # Get and store url if exists
                    a = y.findAll('a')
                    if len(a) > 0:
                        href = a[0].get('href')
                        MusicInfo[count - 2].append(href)
            MInfoList.append(MusicInfo[:])
            MusicInfo.clear()

    for item in MInfoList:
        f.write("[\n")
        for element in item:
            f.write("\t%s\n" % element)
        f.write("[\n")
    f.close()

    return MInfoList

def wrapImage(url, getUra):
    client = urlopen(url)
    html = client.read().decode(client.headers.get_content_charset(), errors = "ignore")
    page_soup = soup(html, "html.parser")
    client.close()

    img = page_soup.findAll('img')

    for i in img:
        print(i['src'])

    if getUra == True:
        return "https://www.wikihouse.com/taiko/" + img[1]['src']
    else:
        return "https://www.wikihouse.com/taiko/" + img[0]['src']

