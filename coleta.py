import requests
from bs4 import BeautifulSoup

url = ' site aqui '     #coloque o site para coleta ao lado
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar título das páginas
title = soup.title.string
print(title)

# Encontra todos links da página
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        links.append(href)
print(links)

# Encontra todos parágrafos na página
paragraphs = []
for paragraph in soup.find_all('p'):
    text = paragraph.get_text()
    if text:
        paragraphs.append(text)
print(paragraphs)
