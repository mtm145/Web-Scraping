
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# definindo servidor do Chrome
service = Service("F:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Url do web Scraping
driver.get("https://www.nfl.com/stats/player-stats/")
time.sleep(1)

''' localização da tag no html da página pelo XPATH,
    clicando na tag correspondente a quantidade de Touchdowns a[contains(text(),'TD')]'''
driver.find_element(
    By.XPATH, "//thead//tr//th//a[contains(text(),'TD')]").click()
element = driver.find_element(
    By.XPATH, "//tbody"
)

# transformando os dados em HTML legível
dadosHtml = element.get_attribute('outerHTML')
soup = BeautifulSoup(dadosHtml, 'html.parser')


# localizando as tags necessárias
listData = soup.find(name='tbody')
lineData = listData.find_all(name='td')
columnData = listData.find_all(name='tr')


# formatação dos dados
top10players = []
for c in range(0, 150, 16):
    top10players.append(lineData[c].text)

for c in range(6, 157, 16):
    top10players.append(lineData[c].text)

for index in range(0, 10):
    print(
        f"Position: {index+1}º, "
        f"player {top10players[index]} "
        f"with: {top10players[(index+10)]} touchdowns.")

driver.quit()
