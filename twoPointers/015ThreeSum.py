def threeSum(nums):
     """
        Returns a list of lists with all the possible 3 number combination from nums that sum 0, without repeting tripplets

        Keyword arguments:
        nums: a List of integers, not sorted


        """         
      #firt we sort the list nums
      nums.sort()
      #we initialize tripplets, our variable to be returned at the end, and some useful variables to keep track
      triplets=[]
      counter=1
      current=nums[-1]
      #we remove all triple numbers, as we cannot have more than 2 of the same digit in our answer unless its zero
      for i in reversed(range(len(nums)-1)):
          if nums[i]==current:
              counter+=1
              if (counter>2 and nums[i]) or counter>3:
                  del nums[i]
          else:
              counter=1
              current=nums[i]
       #we iterate over all the numbers on the list but the last two, and do a two sum method on the rest for each number. This gives us O(n**2) time complexity 
      #We also keep track to avoid adding the same answer list twice
      current=None
      for i in range(len(nums)-2):
          upper=len(nums)-1
          lower=i+1
          if nums[i]==current: continue
          current=nums[i]
          while upper>lower:
              
              testSum=nums[i]+nums[lower]+nums[upper]
              if testSum>0:
                  if testSum>(nums[upper]-nums[lower+1]): break
                  if nums[upper-1]==nums[upper]:upper-=2
                  else:upper-=1
              elif testSum<0:
                  if testSum<(nums[lower]-nums[upper-1]): break
                  if nums[lower+1]==nums[lower]:lower+=2
                  else: lower+=1
                  
              else:
                  triplet=[nums[i],nums[lower],nums[upper]]
                  triplets.append(triplet)
                  if nums[upper-1]==nums[upper]:upper-=2
                  else:upper-=1
                  if nums[lower+1]==nums[lower]:lower+=2
                  else: lower+=1
      return triplets
