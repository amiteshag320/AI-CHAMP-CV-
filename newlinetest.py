from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
output_string = StringIO()
with open('profile (1).pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    
text=output_string.getvalue()    
final=text.replace("\n"," ")

if __name__ == '__main__':
    for i in range(1,51):
        str_path = 'Profile ({}).pdf'.format(i)
        data_forcsv=extract_text_from_pdf(str_path)
        data_forcsv = re.findall("[a-zA-Z]+",data_forcsv )
        #replaced_data = data_forcsv.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        #lst_data= word_tokenize(data_forcsv)
        #lst_data=replaced_data.split(" ")
        unwanted_words=set(stopwords.words('english'))
        lst_data=[ele for ele in data_forcsv if not ele in unwanted_words]
        #lst_data = [item for item in lst_data if not item.isdigit()]
        print(lst_data)