from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(
    executable_path='c://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
    options=options)
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

'''
# Solution 1 #
firstnameField.send_keys('Ryan')
lastnameField.send_keys('Mitchell')
submitButton.click()
#############
'''
# Solution 2 #
actions = ActionChains(driver)\
    .click(firstnameField).send_keys('Ryan')\
    .click(lastnameField).send_keys('Mitchell')\
    .send_keys(Keys.RETURN)
actions.perform()
##############

print(driver.find_element_by_tag_name('body').text)

driver.close()
