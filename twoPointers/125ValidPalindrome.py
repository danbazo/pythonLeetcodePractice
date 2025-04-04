def isPalindrome(s):
        sLower=s.lower()
        sLowerAlphaNum=''.join(x for x in sLower if x.isalnum())
        
        for i in range(len(sLowerAlphaNum)//2):
            if not sLowerAlphaNum[i]==sLowerAlphaNum[-1-i]: return False
        return True 
