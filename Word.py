from hazm import *

class Word:

    stop_words = open("Stopwords" , "r").read().split('\n')
    stemmer = Stemmer()
    lemmatizer = Lemmatizer()

    def __init__(self, word_id, content):
        self.word_id = word_id
        self.content = ''
        self.stopped = False
        self.ifWordIsStopped(content)
        self.filter(content)

    def ifWordIsStopped(self, content):
        if content in Word.stop_words:
            self.stopped = True

    def get(self):
        return self.content

    def filter(self, content):
        stem = Word.stemmer.stem(content)
        self.content = Word.lemmatizer.lemmatize(stem)




