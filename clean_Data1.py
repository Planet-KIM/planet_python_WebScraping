import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string


#이를 이용하면 구문에서 깔끔하게 data만 뽑아올 수 있습니다.
#문장을 단어로 분할하고, 구두점과 공백을 제거하고, 한 글자로 이루어진 단어(I, a를 제외)를 제거
def cleanSentence(sentence):
    sentence = sentence.split(' ')
    # 구두점이라고 생각하는 모든 글자의 리스트와 공백문자를 단어 양 끝으로 다 제거 (하이픈이 들어간 단어는 바뀜x)
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or (word.lower() == 'a' or word.lower == 'i')]
    return sentence

#줄바꿈 문자와 인용 기호를 제거하고, 마침표 뒤에 공백이 나타나는 것을 기준으로 텍스트를 문장으로 분할하는 기능
def cleanInput(content):
    content = content.upper()
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, "UTF-8")
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

#n-그램을 만드는 것
#getNgrams에서 문장마다 호출. 이렇게 하여서 n-그램이 생성되는 일을 방지
def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

#진입점 역할
def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = []
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n))
    return(ngrams)

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is : ' + str(len(ngrams)))