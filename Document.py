import Hemistic
from hazm import *

class Document:

    def __init__(self, doc_id, content, documents=None):
        self.doc_id = doc_id 
        self.content = content.split('\n')
        self.hemistics = [] 
        self.autoSetHemistic(documents)
    
    def autoSetHemistic(self, documents):
        for index, hemistic in enumerate(self.content):
            hemistic_obj = Hemistic.Hemistic(self.doc_id, index, hemistic, documents)
            self.hemistics.append(hemistic_obj)
        
        del self.content # to lower object size
    
    def getWords(self):
        words = []
        for hemistic in self.hemistics:
            words.append(hemistic.getWords())
        
        words = sum(words, []) # change 2d to 1d
        return words
    
    def getWordsAsObjects(self):
        words = []
        for hemistic in self.hemistics:
            words.append(hemistic.words)
        
        words = sum(words, []) # change 2d to 1d
        return words
    
    def calculateTFIDFForQuery(self, documents):
        words = self.getWordsAsObjects()
        rank = {}
        for word in words:
            tf_idf_sum = {}
            for doc in documents:
                tf_idf = word.getTfByDoc(doc.doc_id) * word.idf
                if tf_idf != 0:
                    tf_idf_sum[doc.doc_id] = tf_idf
            word.setTFIDFPerDoc(tf_idf_sum)
            print(word.tf_idf_per_doc)
        print('_____________________________')