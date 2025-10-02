def letterCombinations(digits):
  numToLetters={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
  if not digits: return []
  n=len(digits)
  combinations=[]
  def helper(word,i):
      if i<n:
          for letter in numToLetters[digits[i]]:
              helper(word+letter,i+1)
      else:
          combinations.append(word)

  helper("",0)
  return combinations
