import pytesseract
from PIL import Image
from pytesseract import Output
import numpy as np

#정리되지 않은 파일과, 그 파일에 필로 임계점 툴을 적용할 임계점 값을 받아 처리한 다음 필로 이미지 객체를 반환합니다.
def cleanFile(filePath, threshold):
    image = Image.open(filePath)
    #임계점을 설정하고 저장합니다.
    image = image.point(lambda x: 0 if x < threshold else 255)
    return image

#임계점 필터를 거친 필로 이미지 객체를 받아서 테서랙트를 실행합니다.
#인식된 각 문자열에 포함된 글자수를 기준으로 각 문자열의 신뢰도를 계산해서 인식된 글자 수와 함께 반환합니다.
def getConfidence(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    text = data['text']
    confidences = []
    numchars = []

    for i in range(len(text)):
        if int(data['conf'][i]) > -1:
            confidences.append(data['conf'][i])
            numchars.append(len(text[i]))

    return np.average(confidences, weights=numchars), sum(numchars)

filePath = './Img/test.png'

start  = 80
step = 5
end = 200

for threshold in range(start, end, step):
    image = cleanFile(filePath, threshold)
    scores = getConfidence(image)
    output = 'threshold : {}, confidence: {}, numChars : {}'
    output = output.format(str(threshold), str(scores[0]), str(scores[1]))
    print(output)