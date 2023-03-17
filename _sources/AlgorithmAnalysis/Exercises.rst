..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

:skipreading:`True`

Exercises
---------


#. Give the Big O performance of the following code fragment:

   ::

       for i in range(n):
          for j in range(n):
             k = 2 + 2

#. Give the Big O performance of the following code fragment:

   ::

       for i in range(n):
            k = 2 + 2

#. Give the Big O performance of the following code fragment:

   ::

       i = n
       while i > 0:
          k = 2 + 2
          i = i // 2

#. Give the Big O performance of the following code fragment:

   ::

       for i in range(n):
          for j in range(n):
             for k in range(n):
                k = 2 + 2

#. Give the Big O performance of the following code fragment:

   ::

       for i in range(n):
          k = 2 + 2
       for j in range(n):
          k = 2 + 2
       for k in range(n):
          k = 2 + 2

#. Devise an experiment to verify that the ``list index`` operator is
   :math:`O(1)`.

#. Devise an experiment to verify that ``get item`` and ``set item`` are
   :math:`O(1)` for dictionaries.

#. Devise an experiment that compares the performance of the ``del``
   operator on lists and dictionaries.

#. Given a list of numbers in random order, write an algorithm that works in :math:`O(n\log(n))`
   to find the :math:`k`\ th smallest number in the list.

#. Can you improve the algorithm from the previous problem to be linear? Explain.



