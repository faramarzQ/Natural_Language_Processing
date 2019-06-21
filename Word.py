from hazm import *

class Word:

    stop_words = open("Stopwords" , "r").read().split('\n')
    stemmer = Stemmer()
    lemmatizer = Lemmatizer()

    def __init__(self, word_id, content):
        self.word_id = word_id
        self.content = content
        self.stopped = False
        self.ifWordIsStopped(content)
        self.setWordStem(content)
        self.setWordLemmatize(content)
    
    def ifWordIsStopped(self, content):
        if content in Word.stop_words:
            self.stopped = True
    
    def setWordStem(self, content):
        self.word_stem = Word.stemmer.stem(content)
    
    def setWordLemmatize(self, content):
        self.word_lemmatize = Word.lemmatizer.lemmatize(content)
    
    def get(self):
        return self.content



