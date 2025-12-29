#1 page = 1 doc object
#PyPDFLoader for the textual pdfs only 
from langchain_community.document_loaders import PyPDFLoader #import the pdf loader class from langchain community doc loaders

loader=PyPDFLoader("data/testpdf.pdf") 

documents=loader.load()

print(documents[1])
#uses pypdfinternally to extract text from pdfs
#can't be used on complex pdfs with images/tables etc. as Pypdf only reads text 
print(len(documents))#no of pages 
 