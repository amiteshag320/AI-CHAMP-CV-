import re
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from io import StringIO
from collections import Counter 
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
    corpus=[]
    cnt_lst=[]
    while i<=50:

        str_path = 'Profile ({}).pdf'.format(i)
        data_forcsv=extract_text_from_pdf(str_path)
        data_forcsv = re.findall("[a-zA-Z]+",data_forcsv )
        i+=1
        unwanted_words=set(stopwords.words('english'))
        lst_data=[ele for ele in data_forcsv if not ele in unwanted_words]
        extra_removal = {"www","I","com","gmail","Page",}
        lst_data=[t for t in lst_data if not t in extra_removal]
        string_td = " ".join(lst_data)
        corpus.append(string_td)
        Ctr=Counter(lst_data)
        most_occur = Ctr.most_common(10) 
        freq_pd = pd.DataFrame.from_records(most_occur, columns=['WORD','COUNT'])
        cnt_lst.append(freq_pd)
    result_cnt =pd.concat(cnt_lst,axis=1)
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    X_as_array=X.toarray()
    final_lst=[]
    
    for counter, doc in enumerate(X_as_array):
        tf_idf_tuples = list(zip(vectorizer.get_feature_names(), doc))
        one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['TERM', 'IDF_SCORE']).sort_values(by='IDF_SCORE', ascending=False).reset_index(drop=True)
        final_lst.append(one_doc_as_df)
    result=pd.concat(final_lst,axis=1)
    result=result[:10]
    
    
   
    result.to_csv('Keywords.csv',index=True,header= ['PROFILE(1)', 'IDF_VAL', 'PROFILE(2)', 'IDF_VAL', 'PROFILE(3)', 'IDF_VAL', 'PROFILE(4)', 'IDF_VAL', 'PROFILE(5)', 'IDF_VAL', 'PROFILE(6)', 'IDF_VAL', 'PROFILE(7)', 'IDF_VAL', 'PROFILE(8)', 'IDF_VAL', 'PROFILE(9)', 'IDF_VAL', 'PROFILE(10)', 'IDF_VAL', 'PROFILE(11)', 'IDF_VAL', 'PROFILE(12)', 'IDF_VAL', 'PROFILE(13)', 'IDF_VAL', 'PROFILE(14)', 'IDF_VAL', 'PROFILE(15)', 'IDF_VAL', 'PROFILE(16)', 'IDF_VAL', 'PROFILE(17)', 'IDF_VAL', 'PROFILE(18)', 'IDF_VAL', 'PROFILE(19)', 'IDF_VAL', 'PROFILE(20)', 'IDF_VAL', 'PROFILE(21)', 'IDF_VAL', 'PROFILE(22)', 'IDF_VAL', 'PROFILE(23)', 'IDF_VAL', 'PROFILE(24)', 'IDF_VAL', 'PROFILE(25)', 'IDF_VAL', 'PROFILE(26)', 'IDF_VAL', 'PROFILE(27)', 'IDF_VAL', 'PROFILE(28)', 'IDF_VAL', 'PROFILE(29)', 'IDF_VAL', 'PROFILE(30)', 'IDF_VAL', 'PROFILE(31)', 'IDF_VAL', 'PROFILE(32)', 'IDF_VAL', 'PROFILE(33)', 'IDF_VAL', 'PROFILE(34)', 'IDF_VAL', 'PROFILE(35)', 'IDF_VAL', 'PROFILE(36)', 'IDF_VAL', 'PROFILE(37)', 'IDF_VAL', 'PROFILE(38)', 'IDF_VAL', 'PROFILE(39)', 'IDF_VAL', 'PROFILE(40)', 'IDF_VAL', 'PROFILE(41)', 'IDF_VAL', 'PROFILE(42)', 'IDF_VAL', 'PROFILE(43)', 'IDF_VAL', 'PROFILE(44)', 'IDF_VAL', 'PROFILE(45)', 'IDF_VAL', 'PROFILE(46)', 'IDF_VAL', 'PROFILE(47)', 'IDF_VAL', 'PROFILE(48)', 'IDF_VAL', 'PROFILE(49)', 'IDF_VAL', 'PROFILE(50)', 'IDF_VAL'])
    result_cnt.to_csv('frequency.csv',index=True,header= ['PROFILE(1)', 'COUNT', 'PROFILE(2)', 'COUNT', 'PROFILE(3)', 'COUNT', 'PROFILE(4)', 'COUNT', 'PROFILE(5)', 'COUNT', 'PROFILE(6)', 'COUNT', 'PROFILE(7)', 'COUNT', 'PROFILE(8)', 'COUNT', 'PROFILE(9)', 'COUNT', 'PROFILE(10)', 'COUNT', 'PROFILE(11)', 'COUNT', 'PROFILE(12)', 'COUNT', 'PROFILE(13)', 'COUNT', 'PROFILE(14)', 'COUNT', 'PROFILE(15)', 'COUNT', 'PROFILE(16)', 'COUNT', 'PROFILE(17)', 'COUNT', 'PROFILE(18)', 'COUNT', 'PROFILE(19)', 'COUNT', 'PROFILE(20)', 'COUNT', 'PROFILE(21)', 'COUNT', 'PROFILE(22)', 'COUNT', 'PROFILE(23)', 'COUNT', 'PROFILE(24)', 'COUNT', 'PROFILE(25)', 'COUNT', 'PROFILE(26)', 'COUNT', 'PROFILE(27)', 'COUNT', 'PROFILE(28)', 'COUNT', 'PROFILE(29)', 'COUNT', 'PROFILE(30)', 'COUNT', 'PROFILE(31)', 'COUNT', 'PROFILE(32)', 'COUNT', 'PROFILE(33)', 'COUNT', 'PROFILE(34)', 'COUNT', 'PROFILE(35)', 'COUNT', 'PROFILE(36)', 'COUNT', 'PROFILE(37)', 'COUNT', 'PROFILE(38)', 'COUNT', 'PROFILE(39)', 'COUNT', 'PROFILE(40)', 'COUNT', 'PROFILE(41)', 'COUNT', 'PROFILE(42)', 'COUNT', 'PROFILE(43)', 'COUNT', 'PROFILE(44)', 'COUNT', 'PROFILE(45)', 'COUNT', 'PROFILE(46)', 'COUNT', 'PROFILE(47)', 'COUNT', 'PROFILE(48)', 'COUNT', 'PROFILE(49)', 'COUNT', 'PROFILE(50)', 'COUNT'])
    print("TASK3completed")  
        