def romanToInt(s):
        romanValues={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total=0
        previous=0
        for i in reversed(s):
            current=romanValues[i]
            if current<previous:
                total-=current
            else:
                total+=current
            previous=current
        return total
