#directory=folder 
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

text_loader = DirectoryLoader(
    path="data",
    glob="**/*.txt",
    loader_cls=TextLoader,
)
pdf_loader = DirectoryLoader(
    path="data",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader,
)
documents = text_loader.load() + pdf_loader.load()
print(documents[1].page_content)
#all the pages in the directory are consider as a seprate doc each and listed continuously 
#time complexity is high as it processes all files in the directory





#LAZY LOADING