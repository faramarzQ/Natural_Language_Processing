import glob
import Document

def normalize():
    docs_name = []
    for doc in glob.glob("*.persian_poem"):
        docs_name.append(doc)

    docs_content = []
    for doc in docs_name:
        raw_input = open(doc , "r").read()
        docs_content.append(raw_input)
    
    docs = []
    for index, doc in enumerate(docs_name):
        doc_obj = Document.Document(doc, docs_content[index])
        docs.append(doc_obj)
    
    return docs
