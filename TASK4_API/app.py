from flask import Flask, render_template, request,jsonify
from io import StringIO
import os
import re
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/api1/', methods=['GET', 'POST'])
def index():
    return render_template('api1.html')

@app.route('/api1/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.files['file']
        path_file=os.path.join("uploads",file.filename)
        file.save(path_file)
        output_string = StringIO()
        with open(path_file, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        text=output_string.getvalue()
        final_txt=text.replace("\n"," ")    
        
            
        return jsonify({"Extracted Data":final_txt})

@app.route('/api2/', methods=['GET', 'POST'])
def index1():
    return render_template('api2.html')

@app.route('/api2/data', methods=['GET', 'POST'])
def data1():
    if request.method == 'POST':
        text = request.form['text']
        text = re.findall("[a-zA-Z]+",text )
        unwanted_words=set(stopwords.words('english'))
        text=[ele for ele in text if not ele in unwanted_words]
        extra_removal = {"www","I","com","gmail","Page"}
        text=[t for t in text if not t in extra_removal]
        Ctr=Counter(text)
        finaltext=" ".join(text)
        corpus=[]
        most_occur = Ctr.most_common(10) 
        with open('listfile.txt', 'r') as filehandle:
            for line in filehandle:
                documentfiles = line[:-1]
                corpus.append(documentfiles)
        corpus.append(finaltext)
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)
        X_as_array=X.toarray()
        for counter, doc in enumerate(X_as_array):
            tf_idf_tuples = list(zip(vectorizer.get_feature_names(), doc))
            one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['TERM', 'IDF_SCORE']).sort_values(by='IDF_SCORE', ascending=False).reset_index(drop=True)
        keywords=one_doc_as_df[:10]       
        final_keywords=keywords.values.tolist()
        
        return jsonify({"Count":most_occur,"Keywords":final_keywords})
        


if __name__ == '__main__':
    app.run(debug=True)


