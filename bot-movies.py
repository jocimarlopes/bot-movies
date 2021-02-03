from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

print('''=====> MOVIES TORRENT DOWNLOAD

===> Non Complication
===> Non Adsense
===> Non need Adblock

===> Version 1.0
===> by Jocimar Lopes''')

movie = ''
while movie == '':
    movie = input('Movie name: ')
movie_search = movie + ' download torrent'

path= 'C:\\bots\\geckodriver.exe'

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

time.sleep(1.8)

best = driver.find_element_by_xpath("//div[@class='yuRUbf']/a/h3/span").text
print(best)

time.sleep(1)

if best.find('Torrent'):
    element = driver.find_element_by_partial_link_text('Torrent')
    print('Searching by word: Torrent')
elif best.find('Download'):
    element = driver.find_element_by_partial_link_text('Download')
    print('Searching by word: Download')
elif best.find('Baixa'):
    element = driver.find_element_by_partial_link_text('Baixa')
    print('Searching by word: Baixa')

element.click()
time.sleep(3.9)

current_url = driver.current_url
source = "view-source:" + current_url

driver.get(source)

time.sleep(2)

element = driver.find_element_by_tag_name("a[href*='magnet:']")
time.sleep(1)
element.click()
time.sleep(2.4)

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
time.sleep(4)

keyboard.press_and_release('enter')
time.sleep(1)
exit()
