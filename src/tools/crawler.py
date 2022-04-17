import requests
from bs4 import BeautifulSoup


def get_html(url):
    return requests.get(url).text


def get_audios(html):
    soup = BeautifulSoup(html, 'html.parser')
    audios = soup.find_all("div", {"class": "artikel"})
    result = []
    for audio in audios:
        links = audio.next()
        for link in links:
            mp3 = link.get('href')
            result.append(mp3)
    return result


def save_html(html):
    file = open('tests/unit/word_found.html', "w")
    file.write(html)
    file.close()
