class WordDictionary:

    def __init__(self):
        self.wordDict={}

    def addWord(self, word):
        currentDict=self.wordDict
        for letter in word:
            if letter in currentDict:
                currentDict=currentDict[letter]
            else:
                currentDict[letter]={}
                currentDict=currentDict[letter]
        currentDict['#']={}

                    

    def search(self, word):
        def helper(currentDict,word):
            if not word:
                if "#" in currentDict: return True
                else: return False
            if word[0]==".":
                for subDict in currentDict:
                    if helper(currentDict[subDict], word[1:]): return True
                
                return False
            elif word[0] in currentDict:
                return helper(currentDict[word[0]],word[1:])
            else: return False
        return helper(self.wordDict,word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
