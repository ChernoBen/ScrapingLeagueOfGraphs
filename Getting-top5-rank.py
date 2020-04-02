# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:09:17 2020

@author: benja
"""


'''obetendo dados top 5 ranking from LeagueOfGrafs '''
'''
scraping lol stats from Top platinum PLayers
font LeagueOfStats 
'''
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
'''configurando e instanciando webdriver firefox '''
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')

'''abrindo lolGraphs com selenium'''
driver.get('https://www.leagueofgraphs.com/pt/rankings/records/kills')
time.sleep(10)

'''obtendo tabela por xpath'''
html_xpath = "//*[@id='mainContent']/div/div/div[1]/table"
element = driver.find_element_by_xpath(html_xpath)
conteudo_html = element.get_attribute('outerHTML')

''' tratando conteudo com beatiful soup'''
soup = BeautifulSoup(conteudo_html,'html.parser')
table = soup.findAll('table', class_= 'data_table specific_records_table')

'''tratando com pandas'''
df_full = pd.read_html(str(table))[0].head(4)

'''fechando navegador'''
driver.quit()








