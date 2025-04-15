def groupAnagrams(strs):
        """
        returns a list os list of grouped strings from strs that are anagrams of eachother.

        Keyword arguments:
        strs a list of strings
        """
        #Initialize the answer list
        anagrams=[]
        
        #Create a list of the strings in strs with sorted characters
        strsSorted=["".join(sorted(word)) for word in strs]
        
        #Zip both lists strsSorted and strs, sort them and unzip them
        SortedStrsSorted, sortedStrs =zip(*sorted(zip(strsSorted,strs)))
        
        #Loop through the new sorted lists (Touples really) and check if they are anagrams to group them inside the anagrams list
        currentWord=None
        for i in range(len(SortedStrsSorted)):
            if SortedStrsSorted[i]==currentWord:
                anagrams[-1].append(sortedStrs[i])
            else:
                currentWord=SortedStrsSorted[i]
                anagrams.append([sortedStrs[i]])
                    
        return anagrams
