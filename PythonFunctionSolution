def candy(ratings: List[int])
        """We initialize our variables
        candyCount will be our return variable, we will increase it on our iterations
        preRating will be the previous rating for our logic, and we start with negative one, so every children will have more than this.
        prevCandy will be the value to pass so we know how many candies the last child got.
        descentCount will keep the count of how many children are in a descent order at a time, so we can adjust some calculations further down without doing more passings.
        """
        candyCount=0
        prevRating=-1
        prevCandy=0
        descentCount=0
        """
        We make a single run through the list with a for loop, evaluating all items minus the last one, that will be checked outside the loop, as it has no following item to compare to.
        We will check if the previous item is less or greater than the current one (i will consider equality as being less than, as an equality basically breaks the list and we treat the subsequent elements as a new list, restarting the variables except the candyCount)
        """
        for i in range(len(ratings)-1):
            if prevRating<ratings[i]:
                if ratings[i]>ratings[i+1]:
                    prevCandy+=1
                    candyCount+=prevCandy
                    descentCount=1
                    prevRating=ratings[i]
                elif ratings[i]<ratings[i+1]:
                    prevCandy+=1
                    candyCount+=prevCandy
                    prevRating=ratings[i]
                else:
                    prevRating=-1
                    prevCandy+=1
                    candyCount+=prevCandy
                    prevCandy=0
            else:
                if ratings[i]>ratings[i+1]:
                    descentCount+=1
                    prevCandy-=1
                    candyCount+=prevCandy
                    prevRating=ratings[i]

                elif ratings[i]<ratings[i+1]:
                    descentCount+=1
                    prevCandy-=1
                    candyCount+=prevCandy
                    if prevCandy>1:
                        candyCount-=(descentCount-1)*(prevCandy-1)
                    elif prevCandy<1:
                        candyCount+=(descentCount)*(1-prevCandy)
                    descentCount=0
                    prevCandy=1
                    prevRating=ratings[i]
                else:
                    descentCount+=1
                    prevCandy-=1
                    candyCount+=prevCandy
                    if prevCandy>1:
                        candyCount-=(descentCount-1)*(prevCandy-1)
                    elif prevCandy<1:
                        candyCount+=(descentCount)*(1-prevCandy)
                    descentCount=0
                    prevCandy=0
                    prevRating=-1
        """
        After we are done, we evaluate the last item of the list, which was not checked in the loop.
        """
        if prevRating<ratings[-1]: candyCount+=(prevCandy+1)
        else: 
            descentCount+=1
            prevCandy-=1
            candyCount+=prevCandy
            if prevCandy>1:
                candyCount-=(descentCount-1)*(prevCandy-1)
            elif prevCandy<1:
                candyCount+=(descentCount)*(1-prevCandy)
        return candyCount
