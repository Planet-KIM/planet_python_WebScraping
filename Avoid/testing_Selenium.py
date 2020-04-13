from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options)

driver.get('http://en.wikipedia.org/wiki/Monty_Python')
assert "Monty Python" in driver.title
driver.close()