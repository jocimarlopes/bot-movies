from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import random

print('''=====> MOVIES TORRENT DOWNLOAD

===> Non Complication
===> Non Adsense
===> Non need Adblock

===> Version 1.2
===> by Jocimar Lopes''')

movie = ''
path= 'C:\\bots\\geckodriver.exe'
#tagName = 'Baixa'
count = range(0, 8, 1)

while movie == '':
    movie = input('Movie name: ')
movie_search = movie + ' dublado download torrent'


driver = webdriver.Firefox(executable_path=path)
driver.maximize_window()
driver.get('https://google.com')

assert "Google" in driver.title

element = driver.find_element_by_name('q')
element.clear()
element.send_keys(movie_search)
element.send_keys(Keys.ENTER)

time.sleep(2.7)
atual_url = driver.current_url
driver.get(atual_url)

def goClientTorrent():
    keyboard.press_and_release('left')
    time.sleep(1)

    keyboard.press_and_release('enter')
    time.sleep(0.5)

    keyboard.press_and_release('tab')
    time.sleep(0.2)

    keyboard.press_and_release('tab')
    time.sleep(0.2)

    keyboard.press_and_release('tab')
    time.sleep(0.2)

    keyboard.press_and_release('enter')
    time.sleep(5)

    keyboard.press_and_release('enter')
    time.sleep(1)
    print('Download is Started')
    time.sleep(1)
    print('Thank You!')
    driver.close()
    exit()

def goPageDownload():
    current_url = driver.current_url
    source = "view-source:" + current_url

    driver.get(source)

    time.sleep(2)

    element = driver.find_element_by_tag_name("a[href*='magnet:']")
    time.sleep(1)
    element.click()
    time.sleep(2)
    goClientTorrent()

def goSearch(data):
    time.sleep(2.1)
    print('TagName: ', data)
    time.sleep(1)
    if data == 'Baixa':
        print('Select: ', data)
        findInSearch('Baixa', 'Download')
    if data == 'Download':
        print('Select: ', data)
        findInSearch('Download', 'Torrent')
    if data == 'Torrent' :
        print('Select: ', data)
        findInSearch('Torrent', 'Baixa')

def findInSearch(var, pos):
    print(var, pos)
    best = driver.find_element_by_xpath("//div[@class='yuRUbf']/a/h3/span").text
    returnURL = driver.current_url
    if var != pos:
        if best.find(var):
            print('Find by ', var)
            element = driver.find_element_by_xpath("//div[@class='yuRUbf']/a/h3/span")
            element.text
            print(element.text)
            if element.text.find(var):
                element = driver.find_elements_by_class_name("yuRUbf")
                print('Searching by word: ', var)
                tagName = pos
                element[random.randint(0, 9)].click()
                time.sleep(3.9)
                page_source = driver.page_source
                if 'magnet:' in page_source:
                    print('Magnet: TRUE')
                    time.sleep(1)
                    print('Go to Link Download')
                    goPageDownload()
                else:
                    print('Magnet: FALSE')
                    print(var, pos)
                    print(tagName)
                    time.sleep(1)
                    driver.get(returnURL)
                    time.sleep(1.8)
                    goSearch(pos)
        else:
            return
goSearch('Baixa')

