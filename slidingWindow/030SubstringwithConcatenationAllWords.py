def findSubstring(s, words):
        """
        returns a list with the starting positions of all substrings of s of all words concatenated, in any order, without repeating (Unless the word is repeated in words).

        Keyword arguments:
        s a string
        words a list of strings, all the same length
        """
        #Initialize result List
        confirmedSubStrings=[]
        #Length the words and quantity of words
        wordLength=len(words[0])
        wordAmount=len(words)

        #Build a frequency map of words
        wordDict={}
        for word in words:
            if word in wordDict:
                wordDict[word]+=1
            else:
                wordDict[word]=1

        #Offset the answer to create windows that will move wordLength, and to avoid missing potencial answers
        for offset in range(wordLength):

            #Initialize the window and the pointer    
            start=offset
            i=start
            #Assign a copy of wordDict to a counter, to keep track of the words through the loop     
            remainingWords=wordDict.copy()
            #Loop through the string with a window, untill we reach the end    
            while start+wordLength*wordAmount<=len(s):
                #on each iteration we will define the word we are working with    
                currentWord=s[i:i+wordLength]
                #if the word is in wordDict, is a valid word a we will proceed, else its not, and we will move the window    
                if currentWord in wordDict:
                    #If the word in remaining words still has counts, a count will be removed     
                    if remainingWords[currentWord]>0:
                        remainingWords[currentWord]-=1
                        #after a count is removed, if we already opened the window to a length of wordLength*wordAmount, we will save the start as an answer, and move the start of the window one word
                        if i-start==wordLength*(wordAmount-1):

                            confirmedSubStrings.append(start)
                            remainingWords[s[start:start+wordLength]]+=1
                            start+=wordLength
                    
                #if there are no counts available in remainingWords, there are one too many of the same word in our window, and it should slide the start untill thats not the case anymore
                    else:
                        while currentWord!=s[start:start+wordLength]:
                            remainingWords[s[start:start+wordLength]]+=1
                            start+=wordLength
                        
                        start+=wordLength
                    #after we check the valid word, we advance to the next one     
                    i+=wordLength
                #If the word is not valid, the start will me moved after this word, and the window will restart as well
                else:
                    start=i+wordLength
                    i=start
                    remainingWords=wordDict.copy()
           
        return confirmedSubStrings
