import os
import pytesseract
from PIL import Image
import pandas as pd 
import warnings
warnings.simplefilter("ignore")
from datetime import datetime


def ocrfile():
    # path Input File
    folderPath = r'inputFile'

    # ประกาศตัวแปร เพื่อเก็บ File
    rows = []

    # อ่านไฟล์ ภาพ นามสกุล png ทั้งหมดให้ Floder
    for filename in os.listdir(folderPath):
            filename = filename.lower()
            if filename.endswith('.jpg'):
                rows.append((filename))

    # อ่านไฟล์ ภาพ ทั้งหมด มาเก็บไว้
    dfimages = pd.DataFrame(rows, columns=['namefile'])

    for index, row in dfimages.iterrows():
        path = (row['namefile'])
        path = folderPath + '/' + path      
       
        rowsfile = []

        try:
            # อ่าน ไฟล์ .jpg 
            img = Image.open(path)

            # ocr ไฟล์ .jpg 
            # กำหนดให้อ่านภาษาไทย
            result = pytesseract.image_to_string(img, lang='tha+eng')      
            rowsfile.append((result))
            dffilesave = pd.DataFrame(rowsfile)

            #ตั้งชื่อไฟล์ สำหรับ Save 
            now = datetime.now()
            itime = now.strftime("%m/%d/%Y, %H:%M:%S")
            xnow = itime
            namefile = str(xnow)
            namefile = namefile.replace('/','-')
            namefile = namefile.replace(',','_')
            namefile = namefile.replace(':','-')
            namefile = namefile.replace(' ','')
            # Save File เป็น csv
            dffilesave.to_csv(r'outputFile/' + 'ocr-invoice-' + namefile +'.csv', encoding='utf-8', index=False)

        except:
            pass 


if __name__ == "__main__":
    # จุดเริมต้น Run โปรแกรม
    ocrfile()
