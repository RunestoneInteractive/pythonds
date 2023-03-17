..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

:skipreading:`True`

Exercises
---------

#. Convert the following values to binary using the Divide by 2 algorithm. Show the
   stack of remainders.

   -  17

   -  45

   -  96

#. Convert the following infix expressions to prefix (use full
   parentheses):

   -  (A + B) · ( C + D) · (E + F)

   -  A + ((B + C) · (D + E))

   -  A · B · C · D + E + F

#. Convert the above infix expressions to postfix (use full
   parentheses).

#. Convert the above infix expressions to postfix using the direct
   conversion algorithm. Show the stack as the conversion takes place.

#. Evaluate the following postfix expressions. Show the stack as each
   operand and operator is processed.

   -  2 3 · 4 +

   -  1 2 + 3 + 4 + 5 +

   -  1 2 3 4 5 · + · +

#. The alternative implementation of the queue ADT is to use a list
   such that the rear of the queue is at the end of the list. What would
   this mean for Big-O performance?

#. What is the result of carrying out both steps of the linked list
   ``add`` method in reverse order? What kind of reference results? What
   types of problems may result?

#. Explain how the linked list ``remove`` method works when the item to
   be removed is in the last node.

#. Explain how the ``remove`` method works when the item is in the
   only node in the linked list.

#. Modify the infix-to-postfix algorithm so that it can handle errors.

#. Modify the postfix evaluation algorithm so that it can handle errors.

#. Implement a direct infix evaluator that combines the functionality of
   infix-to-postfix conversion and the postfix evaluation algorithm.
   Your evaluator should process infix tokens from left to right and use
   two stacks, one for operators and one for operands, to perform the
   evaluation.

#. Turn your direct infix evaluator from the previous problem into a
   calculator.

#. Implement the queue ADT, using a list such that the rear of the
   queue is at the end of the list.

#. Design and implement an experiment to do benchmark comparisons of the
   two queue implementations. What can you learn from such an
   experiment?

#. Modify the hot potato simulation to allow for a randomly chosen
   counting value so that each pass is not predictable from the previous
   one.

#. Consider a real life situation. Formulate a question and then design
   a simulation that can help to answer it. Possible situations include:

   -  Cars lined up at a car wash

   -  Customers at a grocery store check-out

   -  Airplanes taking off and landing on a runway

   -  A bank teller

   Be sure to state any assumptions that you make and provide any
   probabilistic data that must be considered as part of the scenario.

#. Implement a radix sorting machine. A radix sort for base 10 integers
   is a mechanical sorting technique that utilizes a collection of bins,
   one main bin and 10 digit bins. Each bin acts like a queue and
   maintains its values in the order that they arrive. The algorithm
   begins by placing each number in the main bin. Then it considers each
   value digit by digit. The first value is removed and placed in a
   digit bin corresponding to the digit being considered. For example,
   if the ones digit is being considered, 534 is placed in digit bin 4
   and 667 is placed in digit bin 7. Once all the values are placed in
   the corresponding digit bins, the values are collected from bin 0 to
   bin 9 and placed back in the main bin. The process continues with the
   tens digit, the hundreds, and so on. After the last digit is
   processed, the main bin contains the values in order.

#. Another example of the parentheses matching problem comes from
   Hypertext Markup Language (HTML). In HTML, tags exist in both opening
   and closing forms and must be balanced to properly describe a web
   document. This very simple HTML document:

   ::

       <html>
          <head>
             <title>
                Example
             </title>
          </head>

          <body>
             <h1>Hello, world</h1>
          </body>
       </html>

   is intended only to show the matching and nesting structure for tags
   in the language. Write a program that can check an HTML document for
   proper opening and closing tags.

#. Extend the program from Listing 3.15 to handle palindromes with
   spaces. For example, I PREFER PI is a palindrome that reads the same
   forward and backward if you ignore the blank characters.

#. To implement the ``size`` method, we counted the number of nodes in
   the list. An alternative strategy would be to store the number of
   nodes in the list as an additional piece of data in the head of the
   list. Modify the ``UnorderedList`` class to include this information
   and rewrite the ``size`` method.

#. Implement the ``remove`` method so that it works correctly in the
   case where the item is not in the list.

#. Modify the list classes to allow duplicates. Which methods will be
   impacted by this change?

#. Implement the ``__str__`` method in the ``UnorderedList`` class. What
   would be a good string representation for a list?

#. Implement the ``__str__`` method so that lists are displayed the
   Python way (with square brackets).

#. Implement the remaining operations defined in the unordered list ADT
   (``append``, ``index``, ``pop``, ``insert``).

#. Implement a ``slice`` method for the ``UnorderedList`` class. It should
   take two parameters, ``start`` and ``stop``, and return a copy of the
   list starting at the ``start`` position and going up to but not
   including the ``stop`` position.

#. Implement the remaining operations defined in the ordered list ADT.

#. Consider the relationship between unordered and ordered lists. Is it
   possible that inheritance could be used to build a more efficient
   implementation? Implement this inheritance hierarchy.

#. Implement a stack using linked lists.

#. Implement a queue using linked lists.

#. Implement a deque using linked lists.

#. Design and implement an experiment that will compare the performance
   of a Python list with a list implemented as a linked list.

#. Design and implement an experiment that will compare the performance
   of the Python list-based stack and queue with the linked list
   implementation.

#. The linked list implementation given above is called a *singly linked
   list* because each node has a single reference to the next node in the
   sequence. An alternative implementation is known as a *doubly linked
   list*. In this implementation, each node has a reference to the next
   node (commonly called *next*) as well as a reference to the preceding
   node (commonly called *back*). The head reference also contains two
   references, one to the first node in the linked list and one to the
   last. Code this implementation in Python.

#. Create an implementation of a queue that would have an average performance of
   :math:`O(1)` for ``enqueue`` and ``dequeue`` operations.

