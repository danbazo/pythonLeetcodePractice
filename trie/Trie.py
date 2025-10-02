class Trie:

    def __init__(self):
        self.trieDict={}

    def insert(self, word):
        currentLevel=self.trieDict
        for letter in word:
            if letter in currentLevel:
                currentLevel=currentLevel[letter]
            else:
                currentLevel[letter]={}
                currentLevel=currentLevel[letter]
        currentLevel[""]=""

    def search(self, word):
        currentLevel=self.trieDict
        for letter in word:
            if letter in currentLevel:
                currentLevel=currentLevel[letter]
            else:
                return False
        return "" in currentLevel


    def startsWith(self, prefix):
        currentLevel=self.trieDict
        for letter in prefix:
            if letter in currentLevel:
                currentLevel=currentLevel[letter]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
