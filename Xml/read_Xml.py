from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen

from bs4 import BeautifulSoup

wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
#print(xml_content.decode('utf-8')) #여기까지는 그냥 텍스트 파일을 제외한 메타 데이터만 출력

wordObj = BeautifulSoup(xml_content.decode('utf-8'))
text_Strings = wordObj.findAll("w:t")

for textElem in text_Strings:
    #print(textElem.text)
    #여기 까지하면 메타데이터 속의 텍스트를 읽어올 수 있습니다.
    closeTag = ""
    try:
        style = textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"] == 'Title':
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        #출력할 태그가 없습니다.
        pass
    print(textElem.text)
    print(closeTag)




