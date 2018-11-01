Coding Questions - Dynamic Programming
=========================================
General DP solution steps:
1. Think in a divide and conquer way
2. Each sub-step should have overlap between each other
3. Build an eqaution between current step's optimum solution and prev's solution

**solution have optimal substructure and overlapped subproblems**


#. Wild Card Match
    *. Recursive Thinking
        Base Case
        ? Case
        * Case which needs to build solution recursively

    *. Once you have Recursive Solution, you can either
        Use memoization to improve time complexity
        Use DP to imporove time complexity

    *. T(n) = T(n-1) + T(n-2) --> O(2**n)

    We can reduce the time complexity to polynomial time O(mn)!
#. Frog Jump
    Same as above solution, you can build recursive solution first!
#. Unique Ways
    *. DP: Build one DP and find the relationship between last step and last-1 step
    *. Combination: There're M+N steps, and we know we will get to the final states, as long as we perform M right move and N down move.
                    Then we can use combination to solve the problem.

#. House Robber
    Solution::
            # Recursive
            class Solution(object):
                def rob(self, nums):
                    """
                    :type nums: List[int]
                    :rtype: int
                    """
                    self.money = 0
                    
                    def helper(idx, nums, curr, robbed):
                        if idx == len(nums):
                            self.money = max(self.money, curr)
                            return
                        if not robbed:
                            helper(idx+1, nums, curr+nums[idx], True)
                            helper(idx+1, nums, curr, False)
                        else:
                            helper(idx+1, nums, curr, False)
                    
                    helper(0, nums, 0, True)
                    helper(0, nums, 0, False)
                    return self.money

                # DP
                def rob(self, nums):
                    """
                    :type nums: List[int]
                    :rtype: int
                    """
                    dp = [0]*(len(nums)+1)
                    for i in range(1, len(nums)+1):
                        dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
                    
                    return dp[-1]

    Robber II:
        max(rob_line(nums[:-1]), rob_line(nums[1:]))





#. Win or Lose
#. Longest Subsequence
    *. Find the recursive structure first
    *. Convert it into dynamic programming paradigm

#. Panlindromic string
    When it comes to panlindromic string, think in a recursive way, you can check it layer by layer.
    And when build the DP solution, inner loop is from bottom to the top because of DP[i+1][j-1]

#. Buy and Sell Stocks
    *. If you get a diff array, that's maxium sub-array problem which can be solved in DP or Divide and Conquer
    *. We can build a 2 Dimensional DP, trick is we don't know how's 1st transaction like thus we need to have additional for loop to check this::
            # This is also a great example to reduce time complexity.
            class Solution(object):
                def maxProfit(self, prices):
                    k = 2 # at most 2 transactions
                    dp = [[0]*(len(prices)+1) for _ in range(k+1)]

                    for i in range(1, k+1):
                        for j in range(1, len(prices)+1):
                            tmpProfit = 0
                            for pos in range(1, j):
                                tmpProfit = max(tmpProfit, prices[j-1]-prices[pos-1]+dp[i-1][pos])
                            dp[i][j] = max(dp[i][j-1], tmpProfit)
                    return dp[-1][-1]
#. Maximum subarray problem

#. Knapsack problem
#. Build Stairs
#. Fibonacci



LeetCode 691. Stickers to Spell Word
-------------------------------------------
    * First thought should be how to solve it using navie method

    * 2nd thought should be able to find some recusion pattern

    * 3rd thought should be able to come up with DP optimization


solution::
    
    #hello world




Knapsack problem - 0/1 Knapsack
-----------------------------------

You are the owner of a local store and you have a budget of N to spend on purchasing goods, different suppliers have different bundle options with different prices. You can buy **only one bundle** from each supplier untill the budget is used off. What's your max units you can get using N budget?


This is 0/1 knapsack because you either choose or not.


* 可以利用一维的**滚动**数组模拟二维数据
    
    另外由于这里由i−1的前面的解j−c[i]推导出i后面的解j，也就是利用一维的数据的话，旧解为前面的解，新解为后面的．
    那么就应该让j从大到小进行循环遍历，因为这样第一次接触的到为旧解i−1，新出来的新解j在此次遍历也不会再用到．

* 另一个小的常数时间优化

    在利用dfs递归求解时，先将物品按照单位价格排好序，单位价格高的靠前，这样如果某个物品超载时，没必要再累积其后面物品的价格， 而是按照该物品的单位价格乘以剩余容量，这样算出的总价格虽然比实际装载的总价格略高些，如果这样略高于实际值的解还低于当前的最优解，则可对后面剪枝，避免多余的计算．


http://www.hawstein.com/posts/dp-knapsack.html
http://blog.csdn.net/u010106759/article/details/77984537


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


        # Below solution is wrong because i didn't consider the ordering!
        def knapsack_new(self, n, bundles, costs):
            dp =[(0, 0) for i in range(len(bundles)+1)]

            for i in range(1, len(bundles)+1):
                if n-dp[i-1][1] >= costs[i-1]:
                    dp[i] = (dp[i-1][0]+bundles[i-1], dp[i-1][1]+costs[i-1]) if dp[i-1][0]+bundles[i-1] > dp[i-1][0] else dp[i-1]
                else:
                    dp[i] = dp[i-1]
            return dp[-1][0]


Knapsack problem - Unbounded Knapsack
--------------------------------------------


You are the owner of a local store and you have a budget of N to spend on purchasing goods.
Different suppliers have different bundle options with different prices. You can buy **as many as 
bundles** from each supplier untill the budget is used off. What's your max units you can get using
N budget?


Notation:
    |   Budget          : N = 50  
    |   BundleUnits     : B = [5, 15, 20]  
    |   BundlePrice     : P = [5, 10, 15]  
    |   MaxUnit         : t = (50/10)*15=75  


Thoughts:

0/1背包只考虑放与不放进去两种情况，而完全背包要考虑 放0,放1, ···, 放j/w[i] 的情况.

The unbonded problem can be converted to 0/1 knapsack problem::
        
        for i in range(1, len(bundles)+1):
            for j in range(n, -1, -1):
                tmp = 0
                for k in range(1, j/costs[i-1]+1):
                    tmp = max(tmp, dp[i-1][j-k*costs[i-1]] + bundles[i-1]*k)
                dp[i][j] = max(tmp, dp[i-1][j])

Above solution's time complexity is O(N*len(B)*sum(k)) which is a little high.

* A simple optimiazation is to add one more check: if costs[i] < costs[i+1] and bundles[i]>bundles[i+1], then we can skip i+1 case.

* Another optimiazation is to divide last item to 0/1 problem using 2 as the base, then the loop goes to O(log(k)) instead of k.
    这是二进制的思想. 因为, 不管最优策略选几件第 i 种物品, 其件数写成二进制后, 总可以表示成若干个 2^k 件物品的和.


In fact, this problem can be coverted to O(N*len(B)), the only difference is::
    
        dp[i][j] = max(dp[i-1][j], dp[i][j-costs[i-1]]+bundles[i-1])

Instead of dp[i-1], dp[i] will contain all the possible solutions at i-1 (i'm still confused about this form and haven't found a good way to explain)

Try to understand this, i think it makes sense:
    dp[i][j-1]+v[i]代表至少放了一个第i种物品, 当然它的前提是能放进去（j>=w[i]）, 所以dp[i][j]=max{dp[i-1][j],dp[i][j-w[i] ]+v[i]}已经涵盖了一个都不放与至少放一个第i种物品的情况了.

http://blog.csdn.net/qq379666774/article/details/17581377



LeetCode 121. Best Time to Buy and Sell Stock
-------------------------------------------------
If you were only permitted to complete at most one transaction::
        # you can get max profix using one transaction in O(n)
        class Solution(object):
            def maxProfit(self, prices):
                buy = float('inf')
                sell = 0
                for i in range(len(prices)):
                    buy = min(buy, prices[i])
                    sell = max(sell, prices[i]-buy)
                return sell
                    



LeetCode 122. Best Time to Buy and Sell Stock II
-------------------------------------------------------
You may complete as many transactions as you like::

        class Solution(object):
            def maxProfit(self, prices):
                # the idea is to capture every profit.
                # you can sell and buy immediately at the same day
                profit = 0
                for i in range(1, len(prices)):
                    if prices[i]>prices[i-1]:
                        profit += prices[i]-prices[i-1]
                
                return profit



LeetCode 123. Best Time to Buy and Sell Stock III and IV
------------------------------------------------------------

This is a standard DP solution, i think the hardest part to come up with the DP helper array,

**DP[i][j] means the profit you have at j with i transactions**

The state function is simple and you need to use the temp variable to reduce complexity::

        class Solution(object):
            def maxProfit(self, prices):
                if len(prices) < 2:
                    return 0
                # the 3rd inner loop to check each position and find max profit is unnecessary
                # we can try to use a tmp variable to reduce the time complexity
                k = 2
                if len(prices) < 2:
            return 0
                # k is big enougth to cover all ramps.
                if k >= len(prices) / 2:
                    return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
                dp = [[0] * (len(prices) + 1) for _ in range(k + 1)] # this means the max profit with k transctions.
                for i in range(1, k+1):
                    # initial
                    tmpMaxProfit = dp[i - 1][0] - prices[0] # use this varaible to get the profit at each transctions
                    for j in range(1, len(prices)+1):
                        # dp[i][j]  1> dp[i][j-1]
                        #           2> for m in range(j-1]:
                        #                   prices[j-1] + dp[i-1][m] - prices[m]
                        # Explaination: 1> we used up all transactions before last stock
                                        2> we leave the last transaction to j-1, we need to find the max profit we can make within (1, j-1]

                        # Since we are already checking all positions and 2> can be transformed to prices[j-1] + {dp[i-1] - prices[m]} for m in range(1, j)
                        # Then we can reduce the for loop to one variable.
                        
                        # Trick is, the prev buy choice could be any price before j-1, thus you have to check or find the max local
                        # and that would be your new value, then use tmpMaxProfit
                        # tmpMaxProfit = dp[i-1][j-1] - prices[j-1]: use one variable to reduce the loop
                        dp[i][j] = max(dp[i][j - 1],  tmpMaxProfit + prices[j-1])
                        tmpMaxProfit = max(tmpMaxProfit, dp[i - 1][j-1] - prices[j-1]) # initial for next level
                return dp[-1][-1]


LeetCode 309. Best Time to Buy and Sell Stock with Cooldown
--------------------------------------------------------------------

Don't worry, you can try to use the Brute Force to solve it first::

        class Solution(object):
            def maxProfit(self, prices):
                # Solution 1:
                # enumerate all the possible solutions and check for the max value
                # Each position has 3 ways to do: O(3**n)
                
                # Solution 2:
                # Record max PROFIT value for each state
                # hold[i] = max(hold[i-1], res[i-1]-prices[i]) - hold previous or buy current
                # sold[i] = hold[i-1] + prices[i] - sell current
                # rest[i] = max(res[i-1], sold[i-1])
                # return max(sold[i], rest[i])
                sold = 0
                rest = 0        
                hold = float('-inf')
                for price in prices:
                    prev = sold
                    hold = max(hold, rest-price)
                    sold = hold + price
                    rest = max(rest, prev)
                return max(rest, sold)
                # Solution 3:
                # Record max PROFIT value for each state
                # sell[i] - PROFIT when sell at day i
                # cooldown[i] - PROFIT when day i is cooldown
                if not prices or len(prices)<2:
                    return 0
                
                n = len(prices)
                sell = [0]*n
                cool = [0]*n
                sell[1] = prices[1]-prices[0]
                for i in range(2, n):
                    cool[i] = max(sell[i-1], cool[i-1])
                    sell[i] = prices[i] - prices[i-1] + max(sell[i-1], cool[i-2])
                return max(sell[-1], cool[-1])



LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
-----------------------------------------------------------------------
Solution::

        class Solution(object):
            def maxProfit(self, prices, fee):
                # Solution 1:
                # enumerate all the possible solutions and check for the max value
                # Each position has 2 ways to do: O(2**n)
                
                # Solution 2:
                # Similar to with cooldown problem, we can use 2 arrays to record the state.
                # buy[i] - PROFIT when we buy at day i BUY or NOT
                # sell[i] - PROFIT when we sell at day i SELL or NOT
                
                buy = [0] * len(prices)
                sell = [0] * len(prices)
                
                buy[0] = - prices[0]
                sell[0] = 0
                
                for i in range(1, len(prices)):
                    buy[i] = max(sell[i-1]-prices[i], buy[i-1]) # you have to sell before buy
                    sell[i] = max(buy[i-1]+prices[i]-fee, sell[i-1])
                return sell[-1]

Leetcode 53. Maximum Subarray            
------------------------------------

This is a very basic problem which can be used to help you understand the following concepts:
    # Divide and Conquer
    # DP solution
    # DP solution with minimum space complexity


DP Solution::
        
        dp = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-1]+nums[i-1]) 
        return dp[-1]

This is my initial thought, however, this equation doesn't meet the requirement of continous subarray.
Keeping the condition in mind then we can reformat the condition a little bit:
    | DP[i] means the maximum subarray that **ends at position i**

The code should look like this::
    
        def maxSubArray(self, nums):
            dp = [float('-inf')]*(len(nums)+1)
            for i in range(1, len(nums)+1):
                dp[i] = max(nums[i-1], dp[i-1]+nums[i-1]) 
            return max(dp)

If you want to reduce the space complexity, you can replace the DP array with 2 variables.
Optimized DP solution::

        def maxSubArray(self, nums):
            maxEnding = float('-inf')
            globalMax = float('-inf')
            for i in range(len(nums)):
                maxEnding = max(nums[i], maxEnding+nums[i])
                globalMax = max(globalMax, maxEnding)
            return globalMax


https://discuss.leetcode.com/topic/6413/dp-solution-some-thoughts
https://discuss.leetcode.com/topic/4175/share-my-solutions-both-greedy-and-divide-and-conquer





