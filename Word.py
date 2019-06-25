from hazm import *
import math

class Word:

    stop_words = open("Stopwords" , "r").read().split('\n')
    stemmer = Stemmer()
    lemmatizer = Lemmatizer()

    def __init__(self, doc_id, hemistic_id, word_id, content, docs=None):
        self.doc_id = doc_id
        self.hemistic_id = hemistic_id
        self.word_id = word_id
        self.content = None
        self.tf = {}
        self.tf_idf_per_doc = {}
        self.idf = 0
        self.docs_contain_q = None
        self.stopped = False
        self.ifWordIsStopped(content)
        self.content = self.filter(content)
        if (docs != None) and (self.stopped == False):
            self.findTermFrequencyInDocs(docs)

    def ifWordIsStopped(self, content):
        if content in Word.stop_words:
            self.stopped = True

    def get(self):
        if self.stopped != True:
            return self.content

    def filter(self, content):
        temp = Word.stemmer.stem(content)
        return Word.lemmatizer.lemmatize(temp).split('#')[0]

    def findTermFrequencyInDocs(self, docs):
        q_word_tf = {}
        docs_with_q_init = set()
        IDF = 0
        similarity_IDF = 0

        for doc in docs:
            TF = 0
            similarity_TF = 0
            doc_words = doc.getWords()
            for d_word in doc_words:
                if self.content == d_word:
                    TF += 1
                    docs_with_q_init.add(doc.doc_id)
                else:
                    edited_distance = self.editDistance(self.content, d_word, len(self.content), len(d_word))
                    if len(self.content) >= len(d_word):
                        biggest = self.content 
                    else:
                        biggest = d_word

                    if (len(biggest) / 2) >= edited_distance:
                        similarity_TF += 1
                        docs_with_q_init.add(doc.doc_id)
        
            q_word_tf[doc.doc_id] = ((similarity_TF / 2) + TF) / len(doc_words)

        self.tf = q_word_tf
        self.docs_contain_q = docs_with_q_init
        if len(docs_with_q_init) != 0:
            DF = len(docs) / len(docs_with_q_init)
            IDF = math.log(DF,10)
        self.idf = IDF

    def editDistance(self, str1, str2, m , n): 
  
        # If first string is empty, the only option is to 
        # insert all characters of second string into first 
        if m==0: 
            return n 
    
        # If second string is empty, the only option is to 
        # remove all characters of first string 
        if n==0: 
            return m 
    
        # If last characters of two strings are same, nothing 
        # much to do. Ignore last characters and get count for 
        # remaining strings. 
        if str1[m-1]==str2[n-1]: 
            return self.editDistance(str1,str2,m-1,n-1) 
    
        # If last characters are not same, consider all three 
        # operations on last character of first string, recursively 
        # compute minimum cost for all three operations and take 
        # minimum of three values. 
        return 1 + min(self.editDistance(str1, str2, m, n-1),    # Insert 
                    self.editDistance(str1, str2, m-1, n),    # Remove 
                    self.editDistance(str1, str2, m-1, n-1)    # Replace 
                    )

    def getTfByDoc(self, doc_id):
        tf = self.tf.get(doc_id)
        if(tf != None):
            return tf
        else:
            return 0

    def setTFIDFPerDoc(self, tf_idf_per_doc):
        self.tf_idf_per_doc = tf_idf_per_doc
