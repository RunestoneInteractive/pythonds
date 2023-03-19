..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


The Binary Search
~~~~~~~~~~~~~~~~~

It is possible to take greater advantage of the ordered list if we are
clever with our comparisons. In the sequential search, when we compare
against the first item, there are at most :math:`n-1` more items to
look through if the first item is not what we are looking for. Instead
of searching the list in sequence, a **binary search** will start by
examining the middle item. If that item is the one we are searching for,
we are done. If it is not the correct item, we can use the ordered
nature of the list to eliminate half of the remaining items. If the item
we are searching for is greater than the middle item, we know that the
entire first (left) half of the list as well as the middle item can be
eliminated from further consideration. The item, if it is in the list,
must be in the second (right) half.

We can then repeat the process with the left half. Start at the middle
item and compare it against what we are looking for. Again, we either
find it or split the list in half, therefore eliminating another large
part of our possible search space. :ref:`Figure 3 <fig_binsearch>` shows how this
algorithm can quickly find the value 54. The complete function is shown
in :ref:`CodeLens 3 <lst_binarysearchpy>`.


.. _fig_binsearch:

.. figure:: Figures/binsearch.png
   :align: center

   Figure 3: Binary Search of an Ordered List of Integers


.. _lst_binarysearchpy:

.. codelens:: search3
    :caption: Binary Search of an Ordered List

    def binary_search(a_list, item):
        first = 0
        last = len(a_list) - 1

        while first <= last:
            midpoint = (first + last) // 2
            if a_list[midpoint] == item:
                return True
            elif item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

        return False


    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

    print(binary_search(test_list, 3))
    print(binary_search(test_list, 13))

Before we move on to the analysis, we should note that this algorithm is
a great example of a divide and conquer strategy. *Divide and conquer*
means that we divide the problem into smaller pieces, solve the smaller
pieces in some way, and then reassemble the whole problem to get the
result. When we perform a binary search of a list, we first check the
middle item. If the item we are searching for is less than the middle
item, we can simply perform a binary search of the left half of the
original list. Likewise, if the item is greater, we can perform a binary
search of the right half. Either way, this is a recursive call to the
binary search function passing a smaller list. :ref:`CodeLens 4 <lst_recbinarysearch>`
shows this recursive version.

.. _lst_recbinarysearch:

.. codelens:: search4
    :caption: A Binary Search--Recursive Version

    def binary_search_rec(a_list, item):
        if len(a_list) == 0:
            return False
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint + 1 :], item)


    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

    print(binary_search_rec(test_list, 3))
    print(binary_search_rec(test_list, 13))



Analysis of Binary Search
^^^^^^^^^^^^^^^^^^^^^^^^^

To analyze the binary search algorithm, we need to recall that each
comparison eliminates about half of the remaining items from
consideration. What is the maximum number of comparisons this algorithm
will require to check the entire list? If we start with :math:`n` items, about
:math:`\frac{n}{2}` items will be left after the first comparison.
After the second comparison, there will be about :math:`\frac{n}{4}`.
Then :math:`\frac{n}{8}`, :math:`\frac{n}{16}`, and so on. How many
times can we split the list? :ref:`Table 3 <tbl_binaryanalysis>` helps us to see the
answer.

.. _tbl_binaryanalysis:

.. table:: **Table 3: Tabular Analysis for a Binary Search**

    ======================== ====================================== 
             **Comparisons**   **Approximate Number of Items Left** 
    ======================== ====================================== 
                           1                   :math:`\frac {n}{2}` 
                           2                   :math:`\frac {n}{4}` 
                           3                   :math:`\frac {n}{8}` 
                         ...                                        
                   :math:`i`                 :math:`\frac {n}{2^i}` 
    ======================== ====================================== 


When we split the list enough times, we end up with a list that has just
one item. Either that is the item we are looking for or it is not.
Either way, we are done. The number of comparisons necessary to get to
this point is :math:`i` where :math:`\frac {n}{2^i} =1`. Solving for :math:`i`
gives us :math:`i=\log{n}`. The maximum number of comparisons is
logarithmic with respect to the number of items in the list. Therefore,
the binary search is :math:`O(\log{n})`.

One additional analysis issue needs to be addressed. In the recursive
solution shown above, the recursive call

``binary_search_rec(a_list[:midpoint], item)``

uses slicing operator to create the left half of the list that is then
passed to the next invocation (similarly for the right half as well).
The analysis that we did above assumed that slicing takes
constant time. However, we know that in Python it is
actually :math:`O(k)`. This means that the binary search using slicing will not
perform in strict logarithmic time. Luckily this can be remedied by
passing the list along with the starting and ending indices. The indices
can be calculated as we did in :ref:`Listing 3 <lst_binarysearchpy>`. We leave this
implementation as an exercise.

Even though a binary search is generally better than a sequential
search, it is important to note that for small values of :math:`n`, the
additional cost of sorting is probably not worth it. In fact, we should
always consider whether it is cost effective to take on the extra work
of sorting to gain searching benefits. If we can sort once and then
search many times, the cost of the sort is not so significant. However,
for large lists, sorting even once can be so expensive that simply
performing a sequential search from the start may be the best choice.

.. admonition:: Self Check

   .. mchoice:: BSRCH_1
      :correct: b
      :answer_a: 11, 5, 6, 8
      :answer_b: 12, 6, 11, 8
      :answer_c: 3, 5, 6, 8
      :answer_d: 18, 12, 6, 8
      :feedback_a:  Looks like you might be guilty of an off-by-one error.  Remember the first position is index 0.
      :feedback_b:  Binary search starts at the midpoint and halves the list each time.
      :feedback_c: Binary search does not start at the beginning and search sequentially, its starts in the middle and halves the list after each compare.
      :feedback_d: It appears that you are starting from the end and halving the list each time.

      Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the recursive binary search algorithm.  Which group of numbers correctly shows the sequence of comparisons used to find the key 8.

   .. mchoice:: BSRCH_2
      :correct: d
      :answer_a: 11, 14, 17
      :answer_b: 18, 17, 15
      :answer_c: 14, 17, 15
      :answer_d: 12, 17, 15
      :feedback_a:  Looks like you might be guilty of an off-by-one error.  Remember the first position is index 0.
      :feedback_b:  Remember binary search starts in the middle and halves the list.
      :feedback_c:  Looks like you might be off by one, be careful that you are calculating the midpont using integer arithmetic.
      :feedback_d: Binary search starts at the midpoint and halves the list each time. It is done when the list is empty.

      Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the recursive binary search algorithm.  Which group of numbers correctly shows the sequence of comparisons used to search for the key 16?

