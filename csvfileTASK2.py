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

        str_path = 'Profile ({}).pdf'.format(i)
        data_forcsv=extract_text_from_pdf(str_path)
        #data_forcsv = re.findall("[a-zA-Z]+",data_forcsv )
        i+=1
        #lst_data= word_tokenize(data_forcsv)
        #lst_data=replaced_data.split(" ") '
        #unwanted_words=set(stopwords.words('english'))
        #lst_data=[ele for ele in data_forcsv if not ele in unwanted_words]
        #lst_data = [item for item in lst_data if not item.isdigit()]
        rows.append(data_forcsv)
        
    df =pd.DataFrame(rows)
    print(df.head())
    df.to_csv ('testingforcsv.csv', index = True, header=False,index_label = 'profile')


    '''import csv

        file =open('csvfile.csv','w+',newline='')

        with file:
            write =csv.writer(file)
            write.writerows(data_forcsv)'''
