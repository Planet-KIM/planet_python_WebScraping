import time
from urllib.request import urlretrieve
from PIL import Image
import pytesseract
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe', chrome_options=options)
url = 'https://www.amazon.com/Death-Ivan-Ilyich-Nikolayevich-Tolstoy/'
url += 'dp/1427027277'
driver.get(url)
time.sleep(2)

#미리보기 버튼을 클릭합니다.
driver.find_element_by_id('imgBlkFront').click()
imageList = []

# 페이지를 불러올 떄까지 기다립니다.
time.sleep(5)

while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    #오른쪽 화살표를 누를 수 있다면 페이지를 계속 넘깁니다.
    driver.find_element_by_id('sitbReaderRightPageTurner').click() #여기서 오류가 발생합니다. 이유를 파악하지 못함.
    time.sleep(2)
    #새 페이즈를 모두 가져옵니다. 동시에 여러 페이지를 가져올 수 있지만,
    # 세트에는 중복이 저장되지 않습니다.
    pages = driver.find_elements_by_xpath('//div[@class=\'pageImage\']/div/img')
    if not len(pages):
        print('No pages found')
    for page in pages:
        image = page.get_attribute('src')
        print('Found image : {}'.format(image))
        if image not in imageList:
            urlretrieve(image, 'page.jpg')
            imageList.append(image)
            print(pytesseract.image_to_string(Image.open('page.jpg')))


driver.quit()



