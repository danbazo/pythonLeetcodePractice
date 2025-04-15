def groupAnagrams(strs):
        anagrams=[]
        while strs:
            word=strs.pop()
            anagrams.append([word])
            wordCount={}
            for letter in word:
                if letter in wordCount:
                    wordCount[letter]+=1
                else:
                    wordCount[letter]=1

            for i in reversed(range(len(strs))):
                if len(strs[i])!=len(word):
                    continue
                wordCopy=wordCount.copy()
                broken=False
                for character in strs[i]:
                                   
                    if character in wordCopy and wordCopy[character]>0:
                        wordCopy[character]-=1
                    else:
                        broken=True
                        break
                   
                if broken: continue
                anagrams[-1].append(strs.pop(i))
        return anagrams
