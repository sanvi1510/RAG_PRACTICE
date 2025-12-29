#1 page = 1 doc object
from langchain_community.document_loaders import PyPDFLoader #import the pdf loader class from langchain community doc loaders

loader=PyPDFLoader("data/testpdf.pdf") 

documents=loader.load()

print(documents[1])