from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='c://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options)
driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')
for link in links:
    if not link.is_displayed():
        print('The Link {} is a trap'.format(link.get_attribute('href')))

fields = driver.find_elements_by_tag_name('input')

for field in fields:
    if not field.is_displayed():
        print('Do not change value of {}'.format(field.get_attribute('name')))