# Python Data Types
# HackerRank Challenges|
# Domain:Python|
# Sub Domain:Basic Data Types


# list_comprehension|

	 List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one.
   The simplest form of a list comprehension is:
   [ expression-involving-loop-variable for loop-variable in sequence ]
   This will step over every element in a sequence, successively setting the loop-variable equal to every element one at a time. It will then build up a list by evaluating the expression-involving-loop-variable for each one. This eliminates the need to use lambda forms and generally produces a much more readable code than using map() and a more compact code than using a for loop. 
   
   >> ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
   >> ListOfNumbers
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

   You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
  Print a list of all possible coordinates given by (i,j,k) on a 3d grid where the sum of i+j+k is not equal to n.
  
   Example:
	x = 1, y= 1, z = 2, n = 3
    All Permutations of |i,j,k| are:
  	[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2]]
    Print an array of the elements that do not sum to n = 3
	[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]

# nested_lists|

 	A nested list is a list that contains another list (i.e.: a list of lists). It is also referred to as a multi-diminsional array. For example, a 2 dimensional array is used below:
    nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']] 
    print len(nested_list)
    # prints 3
    print nested_list[1]
    # prints ['red', 'black']
    print nested_list[1][0]
    # prints red

    To go through every element in this list, use a nested for loop.
    >>> nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
    >>> for inner in nested_list:
    ...     for value in inner:
    ...         print value
    ... 
	blue
	green
	red
	black
	blue
	white

# finding_the_percentage|

	A dictionary is a data type which stores values in pairs. For each element in the dictionary, there is a unique key that points to a value. A dictionary is mutable. It can be changed.
  For example:

   a_dict = {'one': 1} # Here 'one' is the key.  
   Note: The key of a dictionary is immutable. We cannot use a list as a key because a list is mutable. But we can make a tuple of list and use as key.

   a_dict['two'] = 2 # Adds key 'two' which points to 2
   print a_dict['one']
   #prints 1  
   if 'three' in a_dict:
	# To check whether a certain string exist as a key in the dictionary  
    	print a_dict['three']
    else:  
    	print "Three not there"
    # prints Three not there
    del a_dict['one']
    # Deletes index 'one' and the value associated with it  
    print a_dict
    # prints {'two': 2}
    Note: A dictionary is unordered. So, only use the keys to navigate through the dictionary.


# list|
	When we talk about storing multiple values in a container-like data structure, the first thing that comes to mind is a list.
	You can initialize a list as:
 arr = list()
 #or simply
 arr = []
 or with a few elements as:
 arr = [1,2,3]
 Elements can be accessed easily similar to most programming languages:
 print arr[0]
 #result is 1
 print arr[0] + arr[1] + arr[2]
 #result is 6

	Lists in Python are very versatile. You can add almost anything in a Python list.
   In Python, you can create a list of any objects: strings, integers, or even lists. You can even add multiple types in a single list!
 Let's look at some of the methods you can use on list.

	1.) append(x)
	   Adds a single element x to the end of a list.
	   arr.append(9)   
	   print arr  
           # prints [1, 2, 3, 9]

	2.) extend(L)
            Merges another list L to the end.
            arr.extend([10,11])
            print arr
            # prints [1, 2, 3, 9, 10, 11]

	3.) insert(i,x)
             Inserts element x at position i.
             arr.insert(3,7)
             print arr
             # prints [1, 2, 3, 7, 9, 10, 11]

	4.) remove(x)
             Removes the first occurrence of element x.
             arr.remove(10)  
             arr  
	     # prints [1, 2, 3, 7, 9, 11]

	5.) pop()
             Removes the last element of a list. If an argument is passed, that index item is popped out.
             temp = arr.pop()
              print temp 
             # prints 11

	6.) index(x)
	     Returns the first index of a value in the list. Throws an error if it's not found.
             temp = arr.index(3)
	     print temp
	     # prints 2

	7.) count(x)
	     Counts the number of occurrences of an element x.
  	     temp = arr.count(1)
	     print temp
	     # prints 1

	8.) sort()
	Sorts the list.
	arr.sort()
     	print arr
	# [1, 2, 3, 7, 9]

	9.) reverse()
	Reverses the list.
	arr.reverse()
	print arr
	# [9, 7, 3, 2, 1]


# tuples|
	Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot be modified once created). This restricts their use because we cannot add, remove, or assign values; however, it gives us an advantage in space and time complexities.
	A common tuple use is the swapping of 2 numbers:
	a, b = b, a
	Here a,b is a tuple, and it assigns itself the values of b,a.
	Another awesome use of tuples is as keys in a dictionary. In other words, tuples are hashab


# find_the_runner_up_score|
...
# Innominion_OCT_21_Internship
# Innomatics Research Labs
