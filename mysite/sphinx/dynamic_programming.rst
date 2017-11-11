Coding Questions - Dynamic Programming
=========================================

LeetCode 691. Stickers to Spell Word
-------------------------------------------
    * First thought should be how to solve it using navie method

    * 2nd thought should be able to find some recusion pattern

    * 3rd thought should be able to come up with DP optimization


solution::
    
    #hello world




Knapsack problem - 0/1 Knapsack
-----------------------------------

You are the owner of a local store and you have a budget of N to spend on purchasing goods.
Different suppliers have different bundle options with different prices. You can buy **only one bundle**from each supplier untill 
the budget is used off. What's your max units you can get using N budget?

This is 0/1 knapsack because you either choose or not.

Solution and Explaination::
        
        class Solution(object):
            def knapsack(self, n, bundles, costs):
                # this is a 0/1 knapsack problem, we can only choose True/False once for each position.
                # dp[i][j] means the max bundles when we have i choices with j costs.
                dp = [[0]*(n+1) for _ in range(len(bundles)+1)]

                for i in range(1, len(bundles)+1):
                    for j in range(1, n+1):
                        if j >= costs[i-1]:
                            dp[i][j] = max(dp[i-1][j], dp[i-1][j-costs[i-1]]+bundles[i-1])
                print dp
                return dp[-1][-1]

            # although we can compress the space complexity but the time complexity keeps the same
            # therefore we still have 2 loops.
            def knapsack_1(self, n, bundles, costs):
                # dp[j] means the max bundles when we have i choices with j costs.
                dp = [0]*(n+1)

                for i in range(1, len(bundles)+1):
                    # each time when we have dp, it keeps last states which is i-1
                    # Since we have dp[j-costs[i-1]] part, i-1 status will be lost if we update it first,
                    # we need to do it from the end to the front.
                    for j in range(n, -1, -1):
                        if j >= costs[i-1]:
                            dp[j] = max(dp[j], dp[j-costs[i-1]]+bundles[i-1])
                return dp[-1]

        def beautiful_print(data):
            if type(data) is list and type(data[0]):
                for value in data:
                    print value

        print Solution().knapsack_1(38, [3, 5, 4], [10, 20, 16])




Knapsack problem - 0/1 Knapsack
-----------------------------------

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


