from langchain_community.document_loaders import TextLoader #import the text loader class from langchain community doc loaders

loader=TextLoader("data/test_file.txt", encoding="utf-8") #loader=TextLoader

documents=loader.load()# load the documents from the text file using the load method

print((type(documents)))# documents is a list of Document objects
print(len(documents))#no of documents loaded

# print(documents[0].page_content)#print the content of the first document

#DOCUMENT HAS MAINLY TWO ATTRIBUTES
#1. page_content : contains the actual text content of the document 
#2. metadata : contains metadata information about the document such as source, author, etc.

print(documents[0])