from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./Drivers/chromedriver/chromedriver.exe', chrome_options=options)
url = 'http://pythonscraping.com/pages/javascript/redirectDemo1.html'
driver.get(url)
try:
    bodyElement = WebDriverWait(driver, 15).until(EC.presence_of_element_located((
        By.XPATH, '//body[contains(text(), "This is the page you are looking for!")]')))
    print(bodyElement.text)
except TimeoutException as e:
    print('Did not find the element')
    print(e)
