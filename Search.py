
def findSimilarity(documents, queries):

    print(documents[0].getWords())
    #edit distance
    #if has # or @
    #else tf-idf
    for query in queries:
        for doc in documents:
            d_words = doc.getWords()
            q_words = query.getWords()
            