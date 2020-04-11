from PIL import Image
import pytesseract
from pytesseract import Output

print(pytesseract.image_to_data(Image.open('Img/test.png'), output_type=Output.DICT))

print('\n\n')

print(pytesseract.image_to_string(Image.open('Img/test.png'), output_type=Output.BYTES))
