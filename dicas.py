# encoding: utf-8
import os 
from bs4 import BeautifulSoup
from random import randint
import time

soup = BeautifulSoup(open('./dicas.html'), 'html.parser')

def print_tip():    
    tipIndex = randint(0, 65)
    text = soup.find_all('li')[tipIndex].text
    os.system('zenity --error --title="Dica {}" --text="{}" '.format(tipIndex, text))
    time.sleep(10)

while True:
    print_tip()