Coding Questions - BackTracking
===========================
**BackTracking** is a coding pattern to solve the combination and permuation problems.

I need a set of questions to understand the flow of this method::
    def perm(s):
        # this permutation can't handle duplicates
        if len(s)==1:
            return [s]
        res = []
        for i in range(len(s)):
            for tmp in perm(s[:i]+s[i+1:]):
                res.append(s[i]+tmp)
        return res


    def combine(s):
        if len(s)==1:
            return [s]
        res = []
        for i in range(len(s)):
            res.append(s[i])
            for tmp in combine(s[:i]+s[i+1:]):
                res.append(s[i]+tmp)
        return res



How do you implement the above method using stack?