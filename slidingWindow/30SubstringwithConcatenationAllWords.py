def findSubstring(s, words):
        
        confirmedSubStrings=[]
        wordLength=len(words[0])
        wordAmount=len(words)
        wordDict={}
        for word in words:
            if word in wordDict:
                wordDict[word]+=1
            else:
                wordDict[word]=1
        for offset in range(wordLength):
            start=offset
            i=start
            remainingWords=wordDict.copy()
            while start+wordLength*wordAmount<=len(s):
                
                if s[i:i+wordLength] in wordDict:
                    if remainingWords[s[i:i+wordLength]]>0:
                        remainingWords[s[i:i+wordLength]]-=1
                        if i-start==wordLength*(wordAmount-1):

                            confirmedSubStrings.append(start)
                            remainingWords[s[start:start+wordLength]]+=1
                            start+=wordLength
                    else:
                        while s[i:i+wordLength]!=s[start:start+wordLength]:
                            remainingWords[s[start:start+wordLength]]+=1
                            start+=wordLength
                        
                        start+=wordLength
                        print(start)
                        print(i)
                        print(remainingWords)
                    i+=wordLength
                else:
                    start=i+wordLength
                    i=start
                    remainingWords=wordDict.copy()
           
        return confirmedSubStrings
