from flask import Flask, render_template, request,jsonify
from io import StringIO
import os
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('api1.html')

@app.route('/data', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(debug=True)


