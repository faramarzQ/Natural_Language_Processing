import glob
import Document
import Word

def normalize():

    queries_name = []
    for query in glob.glob("*.persian_query"):
        queries_name.append(query)

    queries_content = []
    for query in queries_name:
        raw_input = open(query , "r").read()
        queries_content.append(raw_input)
    
    queries = []
    for index, query in enumerate(queries_name):
        query_obj = Document.Document(query, queries_content[index])
        queries.append(query_obj)

    return queries

