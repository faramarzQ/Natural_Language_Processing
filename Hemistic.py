import Word
from hazm import *

class Hemistic:

    normalizer = Normalizer()

    def __init__(self,doc_id,  hemistic_id, content, documents=None):
        self.hemistic_id = hemistic_id
        self.doc_id = doc_id
        self.content = []
        self.words = []
        self.content = self.filter(content)
        self.autoSetWords(self.content, documents)
    
    def autoSetWords(self, content, documents):
        for index, word in enumerate(content):
            word_obj = Word.Word(self.doc_id, self.hemistic_id, index, word, documents)
            self.words.append(word_obj)
        
        del self.content # to lower object size
    
    def filter(self, content):
        word = Hemistic.normalizer.normalize(content)
        return word_tokenize(word)

    def getWords(self):
        words = []
        for word in self.words:
            temp = word.get()
            if temp != None:
                words.append(temp)    
        
        return words
        