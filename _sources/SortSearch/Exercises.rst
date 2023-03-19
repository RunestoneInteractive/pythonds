..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

:skipreading:`True`

Exercises
---------

#. Using the hash table performance formulas given in the chapter,
   compute the average number of comparisons necessary when the table is

   -  10% full

   -  25% full

   -  50% full

   -  75% full

   -  90% full

   -  99% full

   At what point do you think the hash table is too small? Explain.

#. Modify the hash function for strings to use positional weightings.

#. We used a hash function for strings that weighted the characters by
   position. Devise an alternative weighting scheme. What are the biases
   that exist with these functions?

#. Research perfect hash functions. Using a list of names (classmates,
   family members, etc.), generate the hash values using the perfect
   hash algorithm.

#. Generate a random list of integers. Show how this list is sorted by
   the following algorithms:

   -  bubble sort

   -  selection sort

   -  insertion sort

   -  Shell sort (you decide on the increments)

   -  merge sort

   -  quicksort (you decide on the pivot value)

#. Consider the following list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Show
   how this list is sorted by the following algorithms:

   -  bubble sort

   -  selection sort

   -  insertion sort

   -  Shell sort (you decide on the increments)

   -  merge sort

   -  quicksort (you decide on the pivot value)

#. Consider the following list of integers: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]. Show
   how this list is sorted by the following algorithms:

   -  bubble sort

   -  selection sort

   -  insertion sort

   -  Shell sort (you decide on the increments)

   -  merge sort

   -  quicksort (you decide on the pivot value)

#. Consider the list of characters: [``"P", "Y", "T", "H", "O", "N"``]. Show
   how this list is sorted using the following algorithms:

   -  bubble sort

   -  selection sort

   -  insertion sort

   -  Shell sort (you decide on the increments)

   -  merge sort

   -  quicksort (you decide on the pivot value)

#. Devise alternative strategies for choosing the pivot value in a quicksort.
   For example, pick the middle item. Reimplement the algorithm
   and then execute it on random data sets. Under what criteria does
   your new strategy perform better or worse than the strategy from this
   chapter?

#. Set up a random experiment to test the difference between a
   sequential search and a binary search on a list of integers.

#. Use the binary search functions given in the text (recursive and
   iterative). Generate a random, ordered list of integers and do a
   benchmark analysis for each one. What are your results? Can you
   explain them?

#. Implement the binary search using recursion without the slice
   operator. Recall that you will need to pass the list along with the
   starting and ending index values for the sublist. Generate a random,
   ordered list of integers and do a benchmark analysis.

#. Implement the ``len`` method (``__len__``) for the hash table Map ADT
   implementation.

#. Implement the ``in`` method (``__contains__``) for the hash table Map
   ADT implementation.

#. How can you delete items from a hash table that uses chaining for
   collision resolution? How about if open addressing is used? What are
   the special circumstances that must be handled? Implement the ``del``
   method for the ``HashTable`` class.

#. In the hash table map implementation, the hash table size was chosen
   to be 101. If the table gets full, this needs to be increased.
   Re-implement the ``put`` method so that the table will automatically
   resize itself when the loading factor reaches a predetermined value
   (you can decide the value based on your assessment of load versus
   performance).

#. Implement quadratic probing as a rehash technique.

#. Using a random number generator, create a list of 500 integers.
   Perform a benchmark analysis using some of the sorting algorithms
   from this chapter. What is the difference in execution speed?

#. A bubble sort can be modified to “bubble” in both directions. The
   first pass moves “up” the list, and the second pass moves “down.”
   This alternating pattern continues until no more passes are
   necessary. Implement this variation and describe under what
   circumstances it might be appropriate.

#. Perform a benchmark analysis for a shell sort, using different
   increment sets on the same list.

#. Implement the ``merge_sort`` function without using the slice
   operator.

#. One way to improve the quicksort is to use an insertion sort on
   lists that have a short length (call it the “partition limit”). Why
   does this make sense? Reimplement the quicksort and use it to sort
   a random list of integers. Perform an analysis using different list
   sizes for the partition limit.

#. Implement the median of three method for selecting a pivot value as a
   modification to ``quick_sort``. Run an experiment to compare the two
   techniques.
