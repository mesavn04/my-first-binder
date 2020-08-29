from io import BytesIO
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

rsrcmgr = PDFResourceManager()
sio = BytesIO()
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

fp = open('D:\\Software\\ocr-table-master\\AR19_DKSH_internet_en (1).pdf', 'rb')
for page in PDFPage.get_pages(fp):
    interpreter.process_page(page)
fp.close()
text = sio.getvalue()
#text=text.replace(chr(272)," ")
print(type(text))
f = open('D:\\Software\\ocr-table-master\\DKSH.txt','wb')
f.write(text)

print("hello")