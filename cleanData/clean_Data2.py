from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    print(wordList.items)
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

# 인터넷에서 가져온 텍스트 문자열을 받아서 따옴표를 제거하고, 따옴표를 제외한 다른 구두점 주위에 공백을 넣어서 단어로 취급하게 합니다.
# 그리고 2차원 딕셔너리, 즉 다음형태를 가진 딕셔너리의 딕셔너리를 만듭니다.
def buildWordDict(text):
    #줄바꿈 문자와 따옴표를 제거합니다.
    text = text.replace('\n', ' ');
    text = text.replace('"', '');

    #구두점 역시 단어로 취급해서 마르코프 체인에 들어가도록 합니다.
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' {} '.format(symbol));

    words = text.split(' ')
    #빈 단어를 제거합니다.
    words = [word for word in words if word != '']

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #이 단어에 필요한 새 딕셔너리를 만듭니다.
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1
    return wordDict

speech = 'http://pythonscraping.com/files/inaugurationSpeech.txt'
text = str(urlopen(speech).read(), 'utf-8')
wordDict = buildWordDict(text)

#길이가 100인 마르코프 체인을 생성합니다.
length = 100
chain = ['I']

for i in range(0, length):
    newWord = retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)

print(' '.join(chain))