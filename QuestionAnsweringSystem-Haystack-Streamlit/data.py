import requests
import pdftotext

# book url
url = "https://apex.oracle.com/pls/apex/lonestar/r/files/static/v13Y/Think-And-Grow-Rich_2011-06.pdf"

# Downloading the pdf from the url
resp = requests.get(url)
with open('book.pdf', 'wb') as f:
    f.write(resp.content)
    
# Converting the pdf file into text document 'document.txt'
pdf = pdftotext.PDF(open("book.pdf", "rb")) # extracts text from the pdf pages
with open("document.txt",'w') as f:
    for page in pdf:
        f.writelines(page) # add each page content to the text document
