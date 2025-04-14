    def canConstruct(ransomNote, magazine):
      """
      Returns a boolean indicanting is ransomNote can be constructed using characters in magazine
    
      Keyword arguments:
      ransomNote a string
      magazine a string
      """
      
      # Create a dictionary to count occurrences of each character in magazine
        magazineDict={}
        for element in magazine:
            if element in magazineDict:
                magazineDict[element]+=1
            else: magazineDict[element]=1

      # Check if ransomNote can be constructed using magazine characters
        for letter in ransomNote:
            if letter not in magazineDict or  magazineDict[letter]==0: return False
            magazineDict[letter]-=1
        return True
