import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
def extract_text_from_pdf(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    text=output_string.getvalue()
    final_txt=text.replace("\n"," ")

    return final_txt

if __name__ == '__main__':
    i=1
    rows=[]
    while i<=50:

        str_path = "./ALL_50_pdf's/Profile ({}).pdf".format(i)
        data_forcsv=extract_text_from_pdf(str_path)
        i+=1
        rows.append(data_forcsv)
        
    df =pd.DataFrame(rows)
    df.to_csv ('finalCSVtask2.csv', index = True, header=False,index_label = 'profile')
    print('task2completed')