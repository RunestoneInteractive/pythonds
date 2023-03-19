..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Calculating the Sum of a List of Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will begin our investigation with a simple problem that you already
know how to solve without using recursion. Suppose that you want to
calculate the sum of a list of numbers such as:
:math:`[1, 3, 5, 7, 9]`. An iterative function that computes the sum
is shown in :ref:`ActiveCode 4.3.1 <lst_itsum>`. The function uses an accumulator variable
(``the_sum``) to compute a running total of all the numbers in the list
by starting with :math:`0` and adding each number in the list.


.. activecode:: lst_itsum
    :caption: Iterative Summation

    def list_sum(num_list):
        the_sum = 0
        for i in num_list:
            the_sum = the_sum + i
        return the_sum
        
    print(list_sum([1, 3, 5, 7, 9]))

Pretend for a minute that you do not have ``while`` loops or ``for``
loops. How would you compute the sum of a list of numbers? If you were a
mathematician you might start by recalling that addition is a function
that is defined for two parameters, a pair of numbers. To redefine the
problem from adding a list to adding pairs of numbers, we could rewrite
the list as a fully parenthesized expression. Such an expression looks
like this: 

.. math::

    ((((1 + 3) + 5) + 7) + 9)
    
We can also parenthesize
the expression the other way around,

.. math::

     (1 + (3 + (5 + (7 + 9)))) 

Notice that the innermost set of
parentheses, :math:`(7 + 9)`, is a problem that we can solve without a
loop or any special constructs. In fact, we can use the following
sequence of simplifications to compute a final sum.

.. math::

    total = \  (1 + (3 + (5 + (7 + 9)))) \\
    total = \  (1 + (3 + (5 + 16))) \\
    total = \  (1 + (3 + 21)) \\
    total = \  (1 + 24) \\
    total = \  25


How can we take this idea and turn it into a Python program? First,
let’s restate the sum problem in terms of Python lists. We might say
the sum of the list ``num_list`` is the sum of the first element of the
list (``num_list[0]``) and the sum of the numbers in the rest of the
list (``num_list[1:]``). To state it in a functional form:

.. math::

    list\_sum(num\_list) = first(num\_list) + list\_sum(rest(num\_list))
    \label{eqn:list_sum}



In this equation :math:`first(num\_list)` returns the first element of
the list and :math:`rest(num\_list)` returns a list of everything but
the first element. This is easily expressed in Python as shown in
:ref:`ActiveCode 4.3.2 <lst_recsum>`.


.. activecode:: lst_recsum
    :caption: Recursive Summation

    def list_sum(num_list):
        if len(num_list) == 1:
            return num_list[0]
        else:
            return num_list[0] + list_sum(num_list[1:])

    print(list_sum([1, 3, 5, 7, 9]))

There are a few key ideas in this listing to look at. First, on line 2 we are checking to see if the list is one element long. This
check is crucial and is our escape clause from the function. The sum of
a list of length 1 is trivial; it is just the number in the list.
Second, on line 5 our function calls itself! This is the
reason that we call the ``list_sum`` algorithm recursive. A recursive
function is a function that calls itself.

:ref:`Figure 4.1 <fig_recsumin>` shows the series of **recursive calls** that are
needed to sum the list :math:`[1, 3, 5, 7, 9]`. You should think of
this series of calls as a series of simplifications. Each time we make a
recursive call we are solving a smaller problem, until we reach the
point where the problem cannot get any smaller.

.. _fig_recsumin:

**Figure 4.1:** Series of Recursive Calls Adding a List of Numbers

.. figure:: Figures/sumlistIn.png
   :align: center
   :alt: image


When we reach the point where the problem is as simple as it can get, we
begin to piece together the solutions of each of the small problems
until the initial problem is solved. :ref:`Figure 4.2 <fig_recsumout>` shows the
additions that are performed as ``list_sum`` works its way backward
through the series of calls. When ``list_sum`` returns from the topmost
problem, we have the solution to the whole problem.

.. _fig_recsumout:

**Figure 4.2:** Series of Recursive Returns from Adding a List of Numbers

.. figure:: Figures/sumlistOut.png
   :align: center
   :alt: image

