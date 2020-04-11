from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe', chrome_options=options)

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'
driver.get(url)
time.sleep(3)
print(driver.find_element_by_id('content').text)
#print(driver.find_element_by_css_selector('#content').text)
#print(driver.find_element_by_css_selector('div').text)
driver.close()