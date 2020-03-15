from urllib.request import urlopen
from urllib.request import HTTPError #예외처리를 하기 위한 에러제크.
from urllib.error import URLError #서버가 다운되었을 때 에러체크

from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    #bs = BeautifulSoup(html.read(), 'html.parser')

except HTTPError as e:
    print(e)
    # null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용

except URLError as e:
    print('The server could not be found!!')

else:
    #프로그램을 계속 실행합니다. except절에서 return 이나 break을 사용했다면
    #이 else절은 필요 없습니다.
    print('It Worked!')

    #태그에 오류가 있어도 체크를 해줍니다.
    #단점은 속도가 약간 느립니다.
    #bs = BeautifulSoup(html.read(), 'lxml') #atom으로 실행할 경우 lxml라이브러리를 인식을 하지 못함.
    bs = BeautifulSoup(html.read(), 'html.parser')

    print(bs.h1)

    try:
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        print("Tag was not found")
    else:
        if badContent == None:
            print("Tag was not found")
        else:
            print(badContent)
