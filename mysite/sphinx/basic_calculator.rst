LeetCode 150. Evaluate Reverse Polish Notation
-----------------------------------------------------
In order to apply the recursive solution:
    1. Find the pattern that's repeative
    2. Think about the return type (return value or update a global variable)
    3. Come up with the Base case
    4. Add more conditions to the base case

Recursive::
        
        def evalRPN(self, tokens):
            if not tokens:
                return 0

            def helper(tokens):
                if tokens and tokens[-1] not in ('+', '-', '/', '*'):
                    return int(tokens.pop())
                else:
                    op = tokens.pop()
                    right = helper(tokens)
                    left = helper(tokens)

                    if op == '+':
                        return left + right
                    elif op == '-':
                        return left - right
                    elif op == '*':
                        return left*right
                    elif op == '/':
                        return int(float(left)/right)

            return helper(tokens)

Stack solution
Link__ http://scriptasylum.com/tutorials/infix_postfix/algorithms/postfix-evaluation/
::    
        def evalRPN(self, tokens):
            stack = []
            for t in tokens:
                if t not in ["+", "-", "*", "/"]:
                    stack.append(int(t))
                else:
                    r, l = stack.pop(), stack.pop()
                    if t == "+":
                        stack.append(l+r)
                    elif t == "-":
                        stack.append(l-r)
                    elif t == "*":
                        stack.append(l*r)
                    else:
                        # here take care of the case like "1/-22",
                        # in Python 2.x, it returns -1, while in
                        # Leetcode it should return 0
                        stack.append(int(float(l)/r))
            return stack.pop()


LeetCode 241. Different Ways to Add Parentheses
-------------------------------------------------

Recursive::
        
        def diffWaysToCompute(self, input):
            """
            :type input: str
            :rtype: List[int]
            """
            if input.isdigit():
                return [int(input)]
            res = []
            for i in range(len(input)):
                op = input[i]
                if op in ('+', '-', '*'):
                    left = self.diffWaysToCompute(input[:i])
                    right = self.diffWaysToCompute(input[i+1:])

                    for i in left:
                        for j in right:
                            res.append(self.ops[op](i, j))
            return res


LeetCode 224. Basic Calculator I II III IV
-------------------------------------------------------

#. Parenthesis would make everything more complex
#. Without Parenthesis, the basic operator can be handled in one stack or one call with prev&curr variables
#. Parenthesis can be treated using Stack or Recusion call
#. We can use 2 stack solution to cover all possible cases!    


Recursive::

        def calculate(self, s):
            def helper(s, curr_pos):
                # we need 2 values before and after the Operator
                # we also need one variable to record the curr idx
                res = 0
                curr = 0
                op = 1
                i = curr_pos
                # since i is changing between different levels, we will use while instead of for
                while i < len(s):
                    if s[i].isdigit():
                        curr = curr*10 + int(s[i])
                    elif s[i] == '+':
                        res += op*curr
                        op = 1
                        curr = 0
                    elif s[i] == '-':
                        res += op*curr
                        op = -1
                        curr = 0
                    elif s[i] == '(':
                        val, i = helper(s, i + 1)
                        res += op*val
                        op = 1
                    elif s[i] == ')':
                        res += op*curr
                        curr_pos = i
                        break
                    i += 1
                return res, curr_pos

            return helper('(' + s + ')', 0)[0]



https://en.wikipedia.org/wiki/Shunting-yard_algorithm

For general purpose, just convert all the operators into Reversive Polish Notation::

        class Solution(object):
            def evalRPN(self, tokens):
                if not tokens:
                    return 0

                def helper(tokens):
                    if tokens and tokens[-1] not in ('+', '-', '/', '*'):
                        return int(tokens.pop())
                    else:
                        op = tokens.pop()
                        right = helper(tokens)
                        left = helper(tokens)

                        if op == '+':
                            return left + right
                        elif op == '-':
                            return left - right
                        elif op == '*':
                            return left*right
                        elif op == '/':
                            return int(float(left)/right)

                return helper(tokens)

            def calculate(self, s):
                """
                :type s: str
                :rtype: int
                """
                def rank(op):
                    if op == '+':
                        return 1
                    elif op == '-':
                        return 1
                    elif op == '*':
                        return 2
                    elif op == '/':
                        return 2
                    else:
                        return 0

                def convertRPN(s):
                    output = [] # output queue
                    stack = [] # operator stack
                    i = 0
                    while i < len(s):
                        char = s[i]
                        if char.isdigit():
                            j = i+1
                            while j < len(s) and s[j].isdigit():
                                j += 1
                            num = s[i:j]
                            output.append(num)
                            i = j
                        elif char == ' ':
                            i += 1
                        elif char == '(':
                            stack.append('(')
                            i += 1
                        elif char == ')':
                            # keep pushing the stack
                            while stack and stack[-1] != '(':
                                output.append(stack.pop())
                            stack.pop() # remove '('
                            i += 1
                        else:
                            op = s[i]
                            while stack and rank(op) <= rank(stack[-1]):
                                output.append(stack.pop())
                            stack.append(op)
                            i += 1

                    while stack:
                        output.append(stack.pop())

                    return output

                return self.evalRPN(convertRPN(s))


LeetCode 282. Expression Add Operators
------------------------------------------------------------

Similar to Basic calculator, you need to construct a recursive call to construct all path from top to bottom::

        class Solution(object):
            def addOperators(self, num, target):
                """
                :type num: str
                :type target: int
                :rtype: List[str]
                """

                def helper(nums, path, prev, sofar, target, res):
                    if not nums and sofar == target:
                        res.append(path)
                        return
                    
                    for i in range(1, len(nums)+1):
                        val = nums[:i]
                        if i == 1 or (i > 1 and nums[0] != "0"):
                            helper(nums[i:], path + '+' + val, int(val), sofar + int(val), target, res)
                            helper(nums[i:], path + '-' + val, -int(val), sofar - int(val), target, res)
                            helper(nums[i:], path + '*' + val, prev*int(val), sofar - prev + prev*int(val), target, res)
                
                res = []
                for i in range(1, len(num)+1):
                    if len(num[:i]) != len(str(int(num[:i]))):
                        continue
                    helper(num[i:], num[:i], int(num[:i]), int(num[:i]), target, res)
                    
                return res
        
                
                
LeetCode 679. 24 Game
-------------------------------------

My own solution::

        class Solution(object):
            def judgePoint24(self, nums):
                """
                :type nums: List[int]
                :rtype: bool
                """

                def dfs(nums, path):
                    if len(nums) == 1 and nums[0] == 24:
                        res.append(path[-1])
                        return
                    for i in range(len(nums)):
                        remaining = nums[:i] + nums[i+1:]
                        remaining_path = path[:i] + path[i+1:]
                        for j in range(len(remaining)):
                            dfs(remaining[:j] + remaining[j + 1:] + [nums[i] + remaining[j]], remaining_path[:j] + remaining_path[j+1:] + ['('+str(path[i]) + '+'+str(remaining_path[j]) + ')'])
                            dfs(remaining[:j] + remaining[j + 1:] + [nums[i] * remaining[j]], remaining_path[:j] + remaining_path[j+1:] + [str(path[i]) + '*'+str(remaining_path[j])])
                            dfs(remaining[:j] + remaining[j + 1:] + [nums[i] - remaining[j]], remaining_path[:j] + remaining_path[j+1:] + ['('+str(path[i]) + '-'+str(remaining_path[j]) + ')'])
                            if float(remaining[j]) == 0:
                                continue
                            dfs(remaining[:j] + remaining[j + 1:] + [float(nums[i]) / float(remaining[j])], remaining_path[:j] + remaining_path[j+1:] + [str(path[i]) + '/'+str(remaining_path[j])])

                res = []
                path = [str(num) for num in nums]
                dfs(nums, path)
                return res
