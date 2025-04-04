def isPalindrome(s):
        '''
        This code checks if a given string is a palindrome, removing all non alphanumeric characters and turning it into lowercase.
        It returns a boolean
        '''

        #First the strings uppercase letters are turnes into lowercase
        sLower=s.lower()
        #Then, we remove all non alphanumeric characters
        sLowerAlphaNum=''.join(x for x in sLower if x.isalnum())

        #lastly, we iterate simmetrically over the string with two pointers, to check if the characters are equal to their oppsite. If one is found that is not
        #the function will return False. If the iteration finish, it will return True
        for i in range(len(sLowerAlphaNum)//2):
            if not sLowerAlphaNum[i]==sLowerAlphaNum[-1-i]: return False
        return True 
