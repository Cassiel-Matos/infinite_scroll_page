import os
import time
import webbrowser
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import strftime
from datetime import datetime
from datetime import date
import datetime
from selenium.webdriver.support.ui import Select

#webdriver​
driver = webdriver.Chrome()

#link do site que deseja abrir
driver.get("https://www.facebook.com​")
#tempo só para esperar carregar no navegador
time.sleep(2)

#usuario e senha
us = '@@@@'
pas = '@@@'

time.sleep(1)

#busca os campos de emeil e senha então passa o us e pas nesses campos e da enter
caixabusca = driver.find_element_by_name("email")
caixabusca.send_keys(us)
caixabusca = driver.find_element_by_name("pass")
caixabusca.send_keys(pas)
caixabusca.submit()

#tempo do scroll
SCROLL_PAUSE_TIME = 0.5
Y = 400
# Get scroll height
# Obter altura de rolagem
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    Y = Y + 400
    # Scroll down to bottom
    # Role para baixo 
    driver.execute_script("window.scrollTo(0, window.scrollY + 200);")
    # Wait to load page
    # Espere para carregar a página
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    # Calcule a nova altura de rolagem e compare com a última altura de rolagem
    new_height = driver.execute_script("return document.body.scrollHeight")

    # if new_height == last_height:
    #     break
    # last_height = new_height

    