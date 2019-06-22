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
        self.content = self.filter(content)

    def ifWordIsStopped(self, content):
        if content in Word.stop_words:
            self.stopped = True

    def get(self):
        if self.stopped != True:
            return self.content

    def filter(self, content):
        temp = Word.stemmer.stem(content)
        return Word.lemmatizer.lemmatize(temp).split('#')[0]




