def minWindow(s, t):
       """
        Returns a String of the smallest sub String of s, where all the characters from t are found, including repeating ones. 
        If it doesnt exist, returns an empty string

        Keyword arguments:
        s a string
        t a string
        """     
    #Initialize the result string   
    currentSubS=''
    #Get values of the length for both strings, for later use
    sLen=len(s)
    tLen=len(t)
    #Initialize the reference length of the answer string, as the length of s  plus one, as subsequent answers will be smaller, if they exist
    minLength=sLen+1
    #Initialize the start and end of the sliding window
    start=0
    end=0
    #turning string t to a frequency map of letters
    tDict={}
    for letter in t:
        if letter in tDict:
            tDict[letter]+=1
        else:
            tDict[letter]=1

    #Loop through the string s with the sliding window, until one of the criteria is broken
    #If we find a minLength equal to tLen, thats the smallest possible answer
    #If the start of our window reaches the end of s minus the lenght of t
    #If the end of the window reaches the end of s
    while minLength>tLen and start<=sLen-tLen and end<sLen:
        #check if the last letter of the window is in t and remove one from its value in tDict
        if s[end] in tDict:
            tDict[s[end]]-=1
          #Iterate over the tDict to check if all its values have reached 0, wich means we found and answer
            broke=False
            for key in tDict:
                if tDict[key]>0:
                    broke=True
                    break
            #if an answer is found, we will move the start of the window untill we reach a value from t that hasnt been over repeated, to minimeze the sizeof the window
            if not broke:
                while not (s[start] in tDict and tDict[s[start]]==0):
                    if s[start] in tDict:
                        tDict[s[start]]+=1
                    start+=1
                #The window string is compared to the current string answer, and the one with the smallest length returned
                possibleSubS=s[start:end+1]
                if len(possibleSubS)<=minLength:
                    minLength=len(possibleSubS)
                    currentSubS=possibleSubS
                #the move both the start and end of the window                  
                tDict[s[start]]+=1
                start+=1
                end+=1
                
                
            else:
                end+=1
        else:
            end+=1

    return currentSubS
