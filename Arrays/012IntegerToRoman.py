def intToRoman(num):
        romanValues='IVXLCDM'
        numRoman=''
        
        for h in range(4,0,-1):
            digit=(num%(10**h))//(10**(h-1))
            ref=(h-1)*2
            if digit<4:
                for i in range(digit):
                    numRoman+=romanValues[ref]
            elif digit==4:
                numRoman+=romanValues[ref:ref+2]
            elif digit<9:
                numRoman+=romanValues[ref+1]
                for j in range(digit-5):
                    numRoman+=romanValues[ref]
            else:
                numRoman+=romanValues[ref]
                numRoman+=romanValues[ref+2]

        
           
        return numRoman
