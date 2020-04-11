#pillow 라이브러리는 이밎를 깔끔하게 다듬고 필터링하는 작업을 잘 처리합니다.

from PIL import Image, ImageFilter

kitten = Image.open('Img/test.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('./test_blurred.jpg')
blurryKitten.show()