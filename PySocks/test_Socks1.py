from selenium import webdriver

service_args = ['--proxy=localhost:9150', '--proxy-type=socks5',]
driver = webdriver.Chrome(
    executable_path='c://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    service_args=service_args
)
driver.get("http://icanhazip.com")
driver.close()
print(driver.page_source)