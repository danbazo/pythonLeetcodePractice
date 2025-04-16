def longestConsecutive(nums):
    """
    returns a the length of the longest consecutive sequence of numbers in nums.
    
    Keyword arguments:
    nums a list of integers, unordered
    
    """
    
    #turn nums into a set for a faster lookup
    numsSet=set(nums)
    #Initialize the answer value as 0
    longest=0
    #Iterate over the whole set
    for element in numsSet:
        #if the previous number is in the set, its not the start of the sequence, so we continue     
        if element-1 in numsSet:
            continue
        #Initilize the current number value and the currentLength    
        currentNum=element
        currentLength=1

        #Check if next number is in set, and increase both length and number until next is not found
        while currentNum+1 in numsSet:
            currentNum+=1
            currentLength+=1
        #check which is longest between the current length and the longest yet    
        longest=max(longest,currentLength)
       
    return longest
