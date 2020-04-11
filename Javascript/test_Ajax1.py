from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver.exe', chrome_options=options)

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'
driver.get(url)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))
    
finally:
    print(driver.find_element_by_id('content').text)
    driver.close()