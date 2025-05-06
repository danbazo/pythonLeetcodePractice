def fullJustify(words, maxWidth):
        """
        returns a list of justified strings formed by the words in words to a given width

        Keyword arguments:
        words a list of words
        maxWidth an integer
        """
        #Initilize the variables to be used
        justifiedWords=[] # Final output list of justified lines
        currentLine=[words[0]] # Current line being built (starts with first word)
        currentLineStr='' # Temporary string for current justified line
        currentWidth=len(words[0]) # Current line width
        
        for i in range(1,len(words)):
                # Check if adding the next word (with a space) exceeds maxWidth
            if currentWidth+len(words[i])+1<=maxWidth:
                currentWidth+=(len(words[i])+1)
                currentLine.append(words[i])
            else:
                 # If only one word in the line, left-justify it
                if len(currentLine)==1:
                    currentLineStr+=currentLine[0]+(' '*(maxWidth-len(currentLine[0])))
                else:
                    totalSpace=maxWidth-currentWidth+len(currentLine)-1 # Total space to distribute
                    space=totalSpace//(len(currentLine)-1) # Evenly distributed space
                    remainder=totalSpace%(len(currentLine)-1) # Extra space to add from left to right
                  

                    for j in range(len(currentLine)):
                        if j>0:
                        # Add base space plus one extra if needed
                            currentLineStr+=' '*(space+(1 if remainder>0 else 0))
                            remainder-=1

                        currentLineStr+=currentLine[j]
                        
                justifiedWords.append(currentLineStr)
                # Reset for the next line
                currentLineStr=''
                currentWidth=len(words[i])
                currentLine=[words[i]]
        # Handle the last line: left-justified with single spaces
        for k in range(len(currentLine)):
            if k>0:
                currentLineStr+=' '
            currentLineStr+=currentLine[k]
        currentLineStr+=(' '*(maxWidth-len(currentLineStr)))  # Padding to the right
        justifiedWords.append(currentLineStr)
        return justifiedWords
#Example test
if __name__ == "__main__":
   print('Text Justification Test test. words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16')
   print('Returns: ', fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
