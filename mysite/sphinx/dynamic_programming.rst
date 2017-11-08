Coding Questions - Dynamic Programming
=========================================

LeetCode 691. Stickers to Spell Word
-------------------------------------------
    * First thought should be how to solve it using navie method

    * 2nd thought should be able to find some recusion pattern

    * 3rd thought should be able to come up with DP optimization


solution::
    
    #hello world




Knapsack problem
--------------------

You are the owner of a local store and you have a budget of N to spend on purchasing goods.
Different suppliers have different bundle options with different prices. You can buy as many as 
bundles from each supplier untill the budget is used off. What's your max units you can get using
N budget?


Notation:
    |   Budget          : N = 50  
    |   BundleUnits     : B = [5, 15, 20]  
    |   BundlePrice     : P = [5, 10, 15]  
    |   MaxUnit         : t = (50/10)*15=75  


Thoughts:

#. Find the variable:
        
    For any supplier i, the unit number is **(N_remain/P[i])*B[i]**; the goal is to find **max(sum((N_remain/P[i])*B[i]))**.
    From above statement, we can see it's a linear programming problem which can be solved by dynamic programming.

#. Find the last step:
    
    |   with last supplier:     Find the max units with N budget and i suppliers
    |   without last supplier:  Find the max units with N-P[i] budget and i-1 suppliers

#. Build the relationship:
    |   DP[i][N]
    |   DP[i][j] = max(
                        1. (j/P[i-1])*B[i-1]  
                        2. DP[i-1][j-P[i-1]] + B[i-1]  
                        )


Sourcecode::


