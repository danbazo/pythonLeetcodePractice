# leetcode135Candy

This is the solution for Leetcode Excercise #135. Candy.

The premise is at follows:
  There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
  
  You are giving candies to these children subjected to the following requirements:
  

-   Each child must have at least one candy.
-   Children with a higher rating get more candies than their neighbors.
-   Return the minimum number of candies you need to have to distribute the candies to the children.

This is a Linear solution, with a test runtime of 8ms, that beats 94.42% of accepted solutions on leetcode for that problem.

In this approach, I priotized an algorith with O(n) complexity, focusing on a for loop and a single run.
The logic for the calculations is the following:

- When we evaluate the current rating of a children, we compare it the the previous and following one to determine our actions.
- If the following rating is equal to our current one, we consider a "reset" of our initial variables,  the rest of the list can be treated as a new one, as the requierements of the problem dont consider equality, and so, consequtive children with the same rating dont have a rule that determine the relation between each other candies.
- Besides that, we have 4 cases:
- We are going up (previous rating is lower, next one is higher), and so the current kid will have one more candy than the previous one
- We hit a maximum (both previous and next rating are lower), that means we are starting to descend, and we will start a count of the children going down, and the current kid will have one more candy than the previous one.
- We hit are going down, we add a counter we started when we hit the maximum, and the current kid will have one less candy than the previous one.
- We hit a minimum (both previous and next rating are higher). We know this value should be 1, as is the minimum amount we can give a kid. So we will compare our current candy value to 1, and adjust backwards accordingly, starting on the previous Maximum when we started going down (Basically, we will add or subtract candies here by multyplying the going down counter we had by ehr difference of the current candy and 1, number that can be negative)

