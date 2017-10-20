Python Tips
===========
That has a paragraph about a main subject and is set when the '='
is at least the same length of the title itself.
 
Enumerate
---------

Enum object is really useful when you have a list of concept defination and those concept is consisted 
by other data structures(list, set, dict).

The benefits of Enum is:
 * Import the object and you have a config libs.
 * Members will display all the concepts the object hold.
 * Fit the *Group/Desk* defination in work.
 
Bit Operation
-------------

 * 2**i can be replaced by 1<<i; and + can be replaced by |
 * m/2 can be replaced by m>>1
 

Char
-------------
 * char * (-1) = ''::
    >>> 'a'*-1
    ''

Understanding the map function
--------------------------------------


Maximum recursion depth exceeded 
-------------------------------------

It is a guard against a stack overflow, yes. Python (or rather, the CPython implementation) doesn't optimize tail recursion, and unbridled recursion causes stack overflows. You can change the recursion limit with sys.setrecursionlimit, but doing so is dangerous -- the standard limit is a little conservative, but Python stackframes can be quite big.

Python isn't a functional language and tail recursion is not a particularly efficient technique. **Rewriting the algorithm iteratively**, if possible, is generally a better idea.

<https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it>


Division
-------------
Python's default division of integers is return the floor (towards negative infinity) with no ability to change that. You can read the BDFL's reason why.

To do 'round up' division, you would use::

    >>> a=1
    >>> b=2
    >>> (a+(-a%b))//b
    1
    >>> a,b=-1,2
    >>> (a+(-a%b))//b
    0

To do truncation towards zero, and maintain integer division, you use (a+(-a%b))//b if either a or b are negative and the default division if both are positive.

This will do integer division and always round towards zero::

    >>> a=1
    >>> b=2
    >>> a//b if a*b>0 else (a+(-a%b))//b
    0
    >>> a=-1
    >>> b=2
    >>> a//b if a*b>0 else (a+(-a%b))//b
    0
    >>> a,b=-3,2
    >>> a//b if a*b>0 else (a+(-a%b))//b
    -1
    >>> a,b=3,2
    >>> a//b if a*b>0 else (a+(-a%b))//b
    1


List
---------------

    * nums[::-1] is creating new list!!!


Built-In
-----------------
    
    * sorted::
        sorted(iterable[, cmp[, key[, reverse]]])

    * defaultdict
        Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists::

            >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
            >>> d = defaultdict(list)
            >>> for k, v in s:
            ...     d[k].append(v)
            ...
            >>> d.items()
            [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


https://docs.python.org/2/library/functions.html#sorted