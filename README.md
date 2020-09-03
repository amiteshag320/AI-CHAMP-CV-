# AI-CHAMP-CV-
Natural Language Preprocessing steps

## TASK 1
(Downloading...)
* Downloaded 50 profiles in Pdf format from  `LINKEDIN`.

## TASK 2
(Extracting...)
* I used ' PDFminer ' to Extract Data from All pdfs using a while loop
* And converted the extacted text to Pandas `DataFrame `
* And after that I converted the DataFrame to `finalCSVtask2.csv `

## TASK 3
(frequency and keywords...)
* I used the extracted text and removed the stopwords using `NLTK` libraray and also some words which were irrelevant.
* And also removed all the special characters and numbers .
* Then I used `Counter` and found out the 10 most `Frequent` words.
* Calculated the idf value of each word of the document using `Sklearn.tfidfvectorizer`.
* And then made two DataFrames one for **FREQUENCY** and **KEYWORDS**.
* Converted them to two csv files `frequency.csv` and `Keywords.csv`.

## TASK 4
(Two API's)
for `SECONDAPI` you need to run a command in command prompt for downloading nltk.stopwords , command is " python -m nltk.downloader stopwords"

I have used `flask` for making APIs , to use my API you should go through `TASK4 API` folder.The first API first downloads the pdffile in an `uploads` folder after then it extarcts the text part and gives output in JSON format.
* There is a folder `template` which consists of two templates one is  api1.html and api2.html
* So the folders **uploads**, **template/api1.html**,`FIRSTAPI.py` are important for successfull running of my first API.
The second API takes text data as input and gives the **10 most Frequent words** the text data and also **10 most essential words** in the text data it also outputs in `JSON` format.
* I have used `Counter` and `IDF` value for calculating the frequency and keywords .
* A text file named `listfile ` consists of all the text of 50 documents used in `SECONDAPI` to evaluate the IDF values of words.
* So the folders **listfile**, **template/api2.html**,`SECONDAPI.py` are important for successfull running of my second API.
* Also added one file anmed `app.py` which have both the APIs in it and can be accessed with routenames `/ap1/` and `/api2/` .
* **NOTE** : The IDF valus of keywords are according to the text present in 50 pdf files present in folder ` ALL 50 pdf's `.


Also you can access these api in my website 

https://pfdtotext01.herokuapp.com/api1/

https://pfdtotext01.herokuapp.com/api2/

