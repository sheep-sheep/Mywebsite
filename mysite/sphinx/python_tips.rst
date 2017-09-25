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
