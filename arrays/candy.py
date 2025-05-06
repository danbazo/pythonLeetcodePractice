def candy(ratings):
        """
        returns an integer of the minimum number of candies to be distributed between children acording to the ratings list

        Keyword arguments:
        ratings a list of integers of a rating per each child
        """

        #Initilize variables to be used
        
        candyCount=0 # Total candies distributed
        prevRating=-1 # Previous rating for comparison
        prevCandy=0 # Candies given to the previous child
        descentCount=0 # Counter for consecutive descending ratings
        
     # Iterate through all children except the last, which is handled separately
        for i in range(len(ratings)-1):
            if prevRating<ratings[i]:
                # Ascending or start of peak
                if ratings[i]>ratings[i+1]:
                # Peak followed by a descent
                    prevCandy+=1
                    candyCount+=prevCandy
                    descentCount=1
                    prevRating=ratings[i]
                elif ratings[i]<ratings[i+1]:
                # Increasing trend
                    prevCandy+=1
                    candyCount+=prevCandy
                    prevRating=ratings[i]
                else:
                # Flat area after a climb
                    prevRating=-1
                    prevCandy+=1
                    candyCount+=prevCandy
                    prevCandy=0
            else:
                # Descending or equal trend
                if ratings[i]>ratings[i+1]:
                    descentCount+=1
                    prevCandy-=1
                    candyCount+=prevCandy
                    prevRating=ratings[i]

                elif ratings[i]<ratings[i+1]:
                 # End of descent, start climbing again
                    descentCount+=1
                    prevCandy-=1
                    candyCount+=prevCandy
                    if prevCandy>1:
                        # Adjust overcounting during descent
                        candyCount-=(descentCount-1)*(prevCandy-1)
                    elif prevCandy<1:
                        # Adjust undercounting: ensure all children get at least 1
                        candyCount+=(descentCount)*(1-prevCandy)
                    descentCount=0
                    prevCandy=1
                    prevRating=ratings[i]
                else:
                    # Flat after descent
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
        
        #Last item on the list is evaluated
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

#Example test
if __name__ == "__main__":
   print('Candy test. ratings = [1,2,2]')
   print('Returns: ', candy([1,2,2]))
