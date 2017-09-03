Coding Questions - Numbers
===========================
This page will collect all the number related questions.
 
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


Inline Markup
-------------
Words can have *emphasis in italics* or be **bold** and you can define
code samples with back quotes, like when you talk about a command: ``sudo`` 
gives you super user powers!