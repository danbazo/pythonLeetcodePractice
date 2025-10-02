def permute(nums):
      permutations=[]
      permutation=[]
      usedList=[False]*len(nums)
      

      def helper():
          if len(permutation)==len(nums):
              permutations.append(permutation.copy())
              return
          for i in range(len(nums)):
              if not usedList[i]:
                  permutation.append(nums[i])
                  usedList[i]=True
                  helper()
                  permutation.pop()
                  usedList[i]=False
      helper()

      return permutations
