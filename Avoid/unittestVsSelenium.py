from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import unittest

class TestAddition(unittest.TestCase):
    driver = None

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(
            executable_path='c://Temp/Python/python_Web_Scraping/Javascript/Drivers/chromedriver/chromedriver.exe',
            options=options
        )
        url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        self.driver.get(url)

    def testDown(self):
        print('Tearing down the test')

    def test_drag(self):
        element = self.driver.find_element_by_id("draggable")
        target = self.driver.find_element_by_id("div2")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element, target).perform()
        self.assertEqual("You are definitely not a bot!",
                         self.driver.find_element_by_id("message").text)


if __name__ == '__main__':
    unittest.main()
