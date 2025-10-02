def combine(n, k):
      combinations=[]
      combination=[]

      def helper(i):
          l=len(combination)
          if l==k:                
              combinations.append(combination.copy())
          
          
          else:
              for number in range(i,n - (k - l) + 2):
                  combination.append(number)
                  helper(number+1)
                  combination.pop()
      helper(1)
      return combinations
