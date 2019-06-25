#!/usr/bin/python3

import NormalizePoem as NP
import NormalizeQuery as NQ
import Search
import RankDocuments

class Main:
    def __init__(self):

        documents = NP.normalize()
        queries = NQ.normalize(documents)

        for query in queries:
            query.calculateTFIDFForQuery(documents)
        
Main()