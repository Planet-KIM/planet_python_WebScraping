from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='c://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options)

driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)

savedCookies = driver.get_cookies()
print('Saved Cookies : {}'.format(savedCookies))
print('\n\n')

driver2 = webdriver.Chrome(
    executable_path='c://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options)
driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
    #phantomjs driver을 사용하는 경우 주석을 해제합니다.
    #if not cookie['domain'].startswith('.'):
        #cookie['domain']='.{}',format(cookie['domain'])
    driver2.add_cookie(cookie)

driver2.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print('second cookies : {}'.format(driver2.get_cookies()))