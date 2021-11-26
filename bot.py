from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import platform
import subprocess
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

i = 0
path = 'geckodriver'
if 'Linux' in platform.system():
    path = './geckodriver'
if 'Windows' in platform.system():
    path = 'geckodriver.exe'


class Bot:

    def init(args):

        movie_search = args.m + ' dublado download hd torrent'
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=path)
        driver.maximize_window()
        driver.get('https://google.com')

        assert "Google" in driver.title

        element = driver.find_element_by_name('q')
        element.clear()
        print('Searching movie..')
        element.send_keys(movie_search)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        print('Start search in Google List')
        atual_url = driver.current_url
        driver.get(atual_url)
        Bot.goSearch('\nMovie: ' + args.m, driver)

    def goSearch(data, driver):
        print('Searching Torrent in Google Search... ', data)
        time.sleep(2.5)
        Bot.findInSearch('Torrent', 'Download', driver)

    def findInSearch(var, pos, driver):
        returnURL = driver.current_url
        time.sleep(0.5)
        array = driver.find_elements_by_class_name("g")
        list = len(array)
        global i
        if i < list:
            element = driver.find_elements_by_class_name("yuRUbf")
            print((i + 1), 'º Item in List')
            element[i].click()
            time.sleep(4)
            i = i + 1
            Bot.verifyLinkInPage(driver, returnURL, pos)
        else:
            print('\n\nSearch finished with 0 results')

    def verifyLinkInPage(driver, url, p):
        page_source = driver.page_source
        if 'magnet:' in page_source:
            print('Torrent Found: TRUE')
            time.sleep(0.5)
            print('Getting Magnet Link from Source\n')
            Bot.goPageDownload(driver)
        else:
            print('Torrent Found: FALSE')
            time.sleep(1)
            print('Return to Google Search List')
            driver.get(url)
            time.sleep(2.5)
            print('Research in List..\n\n')
            Bot.goSearch(p, driver)

    def goPageDownload(driver):
        current_url = driver.current_url
        source = "view-source:" + current_url
        driver.get(source)
        time.sleep(2)
        element = driver.find_element_by_tag_name("a[href*='magnet:']")
        time.sleep(1)
        print('\nInitializing Transmission-cli')
        try:
            subprocess.run([
                "transmission-cli",
                "--no-downlimit",
                "--finish exit",
                element.get_attribute('href')
            ])
        except NameError:
            print('Erro ao Abrir transmission-cli. Verifique se ele está instalado')
