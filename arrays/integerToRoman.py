def intToRoman(num):
        """
        returns a string of the correspondent roman number form of the integer num.
        
        Keyword arguments:
        num an integer up to 3999
        """

        # Roman numeral symbols in increasing order of value
        romanValues='IVXLCDM'
        #Initialize the answer string
        numRoman=''
        
        # Process each digit from thousands (10^3) to units (10^0)
        for h in range(4,0,-1):
            digit=(num%(10**h))//(10**(h-1)) # Extract digit at current place
            ref=(h-1)*2 # Index in romanValues string corresponding to current place
            if digit<4:
                # Repeat the base symbol (e.g., 'III')
                for i in range(digit):
                    numRoman+=romanValues[ref]
            elif digit==4:
                # Special case for 4 (e.g., 'IV')
                numRoman+=romanValues[ref:ref+2]
            elif digit<9:
                # 5-8: add 5 symbol and repeat base (e.g., 'VII')
                numRoman+=romanValues[ref+1]
                for j in range(digit-5):
                    numRoman+=romanValues[ref]
            else:
                # Special case for 9 (e.g., 'IX')
                numRoman+=romanValues[ref]+romanValues[ref+2]
                        
        return numRoman

if __name__ == "__main__":
  print('Integer to Roman test. num=3749')
  print('Returns: ', intToRoman(3749))
