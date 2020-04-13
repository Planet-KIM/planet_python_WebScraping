from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='C://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options)
driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')
print(driver.find_element_by_id('message').text)

element = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('div2')
actions = ActionChains(driver)
actions.drag_and_drop(element, target).perform()

print(driver.find_element_by_id('message').text)