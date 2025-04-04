def fullJustify(words, maxWidth):
        justifiedWords=[]
        currentLine=[words[0]]
        currentLineStr=''
        currentWidth=len(words[0])
        for i in range(1,len(words)):
            if currentWidth+len(words[i])+1<=maxWidth:
                currentWidth+=(len(words[i])+1)
                currentLine.append(words[i])
            else:
                if len(currentLine)==1:
                    currentLineStr+=currentLine[0]+(' '*(maxWidth-len(currentLine[0])))
                else:
                    totalSpace=maxWidth-currentWidth+len(currentLine)-1
                    space=totalSpace//(len(currentLine)-1)
                    remainder=totalSpace%(len(currentLine)-1)
                  

                    for j in range(len(currentLine)):
                        if j>0:
                            currentLineStr+=' '*(space+(1 if remainder>0 else 0))
                            remainder-=1

                        currentLineStr+=currentLine[j]
                        
                justifiedWords.append(currentLineStr)
                currentLineStr=''
                currentWidth=len(words[i])
                currentLine=[words[i]]
        for k in range(len(currentLine)):
            if k>0:
                currentLineStr+=' '
            currentLineStr+=currentLine[k]
        currentLineStr+=(' '*(maxWidth-len(currentLineStr)))
        justifiedWords.append(currentLineStr)
        return justifiedWords
