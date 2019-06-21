import Hemistic
from hazm import *

class Document:

    def __init__(self, doc_id, content):
        self.doc_id = doc_id 
        self.content = content.split('\n')
        self.hemistics = [] 
        self.autoSetHemistic()
    
    def autoSetHemistic(self):
        for index, hemistic in enumerate(self.content):
            hemistic_obj = Hemistic.Hemistic(index, hemistic)
            self.hemistics.append(hemistic_obj)
        
        del self.content # to lower object size