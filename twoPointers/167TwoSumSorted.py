def twoSum(numbers, target):
        """
        Returns a list with the 1 indexed positions of the two values inside numbers that sum the target value

        Keyword arguments:
        numbers: a List of integers, sorted in increasing order
        target: an integer

        """
        lower=0
        upper=len(numbers)-1
        while True:
            if numbers[lower]+numbers[upper]<target:
                lower+=1
            elif numbers[lower]+numbers[upper]>target:
                upper-=1
            else:
                return [lower+1,upper+1]
