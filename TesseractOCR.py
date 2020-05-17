import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'

def image():
    im = Image.open(a)
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text)

def pdf():
    pdf = wi(filename = a, resolution = 300)
    pdfImage = pdf.convert('jpeg')   
    imageBlobs = []

    for img in pdfImage.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob()) 

    recogText=[]

    for imgBlob in imageBlobs:
        im = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(im, lang = 'eng')
        recogText.append(text)
    
    print(recogText[1])

a = input("Enter file location : ")

ext=[]
ext = a.split('.')

if(ext[1]=='pdf'):
    pdf()
elif(ext[1]=='jpg' or ext[1]=='jpeg'):
    image()
else:
    pass