from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='C://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options
)
driver.get('http://pythonscraping.com/')
driver.get_screenshot_as_file('./pythonscraping.png')