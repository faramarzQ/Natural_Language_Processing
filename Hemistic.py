import Word
from hazm import *

class Hemistic:

    normalizer = Normalizer()

    def __init__(self, hemistic_id, content):
        self.hemistic_id = hemistic_id
        self.content = []
        self.words = []
        self.filter(content)
        self.autoSetWords(self.content)
    
    def autoSetWords(self, content):
        for index, word in enumerate(content):
            word_obj = Word.Word(index, word)
            self.words.append(word_obj)
        
        del self.content # to lowe object size
    
    def filter(self, content):
        word = Hemistic.normalizer.normalize(content)
        self.content = word_tokenize(word)        
        