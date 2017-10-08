Coding Questions - Numbers
===========================
This page will collect all the number related questions.

Bit Operations
-----------------------
Given a positive integer, check whether it has alternating bits or not::
		class Solution(object):
		    def hasAlternatingBits(self, n):
		        first = n%2
		        n /= 2
		        while n:
		            if first == n%2:
		                return False
		            else:
		                first = n%2
		            n /=2
		        return True

		def convertBinary(n):
		    res = []
		    while n:
		        res.append('1' if n%2 else '0')
		        n >>= 1
		    return ''.join(res[::-1])

		def dfsConvert(n):
		    if n==1:
		        return '1'
		    elif n == 0:
		        return 0
		    else:
		        return dfsConvert(n/2) + '1' if n%2 else dfsConvert(n/2) + '0'

Find all divisors of a natural number
----------------------------------------

I was trying to find an efficient way to display all dividors of a natuaral number::

    def find_all_dividors(self, n):
        import math
        res_0 = []
        res_1 = []
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0:
                res_0.append(i)
                if n/i != i:
                    res_1.append(n/i)
        return res_0 + res_1[::-1]

	# Notice that all the divisors can appear in pairs, we can add
	# them by pair too.


LeetCode 227. Basic Calculator II
---------------------------------------
This question is so annoying and if you are using python, you have to be careful about 
the rounding directions difference between positive and negative numbers

For this question, if you can always work on positive nubmers, then you don't need to consider the rounding issue::

	class Solution(object):
	    def calculate(self, s):
	        """
	        :type s: str
	        :rtype: int
	        """
	        if not s or len(s)==0:
	            return 0

	        stack = []

	        num = 0
	        sign = '+'

	        for c in s:
	            if c.isdigit():
	                num = num*10 + (ord(c) - ord('0'))
	            if not c.isdigit() and c != ' ':
	                # when we check the sign again, we have right number and the left number in the stack
	                if sign=='-':
	                    stack.append(-num)
	                elif sign=='+':
	                    stack.append(num)
	                elif sign=='*':
	                    stack.append(num*stack.pop(-1))
	                elif sign =='/':
	                    tmp = stack.pop(-1)
	                    stack.append(((tmp + (-tmp % num)) // num) if num < 0 or tmp <0 else tmp//num)
	                sign = c # when this is sign, we have the number at the left
	                num = 0
	        # this extra step is for the end of the loop, because when we have the right numer
	        # the loop has ended, we need one more check for the last element.
	        if sign == '-':
	            stack.append(-num)
	        elif sign == '+':
	            stack.append(num)
	        elif sign == '*':
	            stack.append(num * stack.pop(-1))
	        elif sign == '/':
	            tmp = stack.pop(-1)
	            stack.append(((tmp + (-tmp % num)) // num) if num < 0 or tmp < 0 else tmp // num)
	        return sum(stack)