import Word
from hazm import *

class Hemistic:
    def __init__(self, hemistic_id, content):
        self.hemistic_id = hemistic_id
        # normalized_content = self.normalizeHemestic(content)
        self.content = word_tokenize(content)
        self.words = []
        self.autoSetWords()
    
    def autoSetWords(self):
        for index, word in enumerate(self.content):
            word_obj = Word.Word(index, word)
            self.words.append(word_obj)
        
        del self.content # to lowe object size
    
    # def normalizeHemestic(self, content):
    #     normalizer = Normalizer()
    #     print(word_tokenize(content[::-1]))
        