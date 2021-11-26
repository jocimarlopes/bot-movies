from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import platform

i = 0
path = 'geckodriver'
if 'Linux' in platform.system():
    path = './geckodriver'
if 'Windows' in platform.system():
    path = 'geckodriver.exe'


class Bot:

    def init(args):

        movie_search = args.m + ' dublado download hd torrent'

        driver = webdriver.Firefox(executable_path=path)
        driver.maximize_window()
        driver.get('https://google.com')

        assert "Google" in driver.title

        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(movie_search)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        atual_url = driver.current_url
        driver.get(atual_url)
        Bot.goSearch('\nFilme: ' + args.m, driver)

    def goSearch(data, driver):
        time.sleep(2.1)
        print('\n\nWait.. ')
        time.sleep(1)
        print('Searching Torrent in Google Search... ', data)
        Bot.findInSearch('Torrent', 'Download', driver)

    def findInSearch(var, pos, driver):
        returnURL = driver.current_url
        time.sleep(1)
        print('Find the Movie, wait..')
        array = driver.find_elements_by_class_name("g")
        list = len(array)
        global i
        if i < list:
            element = driver.find_elements_by_class_name("yuRUbf")
            element[i].click()
            time.sleep(4)
            i = i + 1
            Bot.verifyLinkInPage(driver, returnURL, pos)
        else:
            print('\n\nSearch finished with 0 results')

    def verifyLinkInPage(driver, url, p):
        page_source = driver.page_source
        if 'magnet:' in page_source:
            print('Torrent: TRUE')
            time.sleep(1)
            print('Go to Link Download\n')
            Bot.goPageDownload(driver)
        else:
            print('Torrent: FALSE')
            time.sleep(1)
            print('Return to Google Search')
            driver.get(url)
            time.sleep(2)
            print('and Research in List\n\n')
            Bot.goSearch(p, driver)

    def goPageDownload(driver):
        current_url = driver.current_url
        source = "view-source:" + current_url

        driver.get(source)
        time.sleep(2)

        element = driver.find_element_by_tag_name("a[href*='magnet:']")
        time.sleep(1)
        print('\n')
        print(element.get_attribute('href'))
