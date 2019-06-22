#!/usr/bin/python3

import NormalizePoem as NP
import NormalizeQuery as NQ
import Search

class Main:
    def __init__(self):

        documents = NP.normalize()
        queries = NQ.normalize()

        Search.findSimilarity(documents, queries)



        # str1 = "miss"
        # str2 = "mis"
        # print (Main.editDistance(str1, str2, len(str1), len(str2)) )
    


    def editDistance(str1, str2, m , n): 
  
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
            return Main.editDistance(str1,str2,m-1,n-1) 
    
        # If last characters are not same, consider all three 
        # operations on last character of first string, recursively 
        # compute minimum cost for all three operations and take 
        # minimum of three values. 
        return 1 + min(Main.editDistance(str1, str2, m, n-1),    # Insert 
                    Main.editDistance(str1, str2, m-1, n),    # Remove 
                    Main.editDistance(str1, str2, m-1, n-1)    # Replace 
                    ) 
        
Main()