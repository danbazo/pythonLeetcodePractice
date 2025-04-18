def romanToInt(s):
        """
        returns an integer value equivalent for the roman number of th string s

        Keyword arguments:
        s a string of a Roman Number
        """
        #Initialize a dictionary for equivalence of values for Roman Numbers
        romanValues={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #Initilize the answer value
        total=0
        #Initialize a previous value, to check if it has to be subtrated or added
        previous=0
        #iterate over the string s in reverse order
        for i in reversed(s):
            current=romanValues[i]
        #If the current Value is smaller than the previous one, it is subtracting
            if current<previous:
                total-=current
        #Else is adding
            else:
                total+=current
            previous=current
        return total
#Example test
if __name__ == "__main__":
  print('Roman to Integer test. s=MCMXCIV')
  print('Returns: ', romanToInt('MCMXCIV'))
