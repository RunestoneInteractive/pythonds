..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Discussion Questions
--------------------

1. Draw the graph corresponding to the following adjacency matrix.

.. figure:: Figures/adjMatEX.png
   :align: center


2. Draw the graph corresponding to the following list of edges.

   .. table:: 

           +--------+------+--------+
           | from   | to   | cost   |
           +========+======+========+
           | 1      | 2    | 10     |
           +--------+------+--------+
           | 1      | 3    | 15     |
           +--------+------+--------+
           | 1      | 6    | 5      |
           +--------+------+--------+
           | 2      | 3    | 7      |
           +--------+------+--------+
           | 3      | 4    | 7      |
           +--------+------+--------+
           | 3      | 6    | 10     |
           +--------+------+--------+
           | 4      | 5    | 7      |
           +--------+------+--------+
           | 6      | 4    | 5      |
           +--------+------+--------+
           | 5      | 6    | 13     |
           +--------+------+--------+

3. Ignoring the weights, perform a breadth first search on the graph
   from the previous question.
   
.. mchoice:: question1_1
   :answer_a: O(n)
   :answer_b: O(n<sup>2</sup>)
   :answer_c: O(1)
   :answer_d: O(n<sup>3</sup>)
   :correct: b
   :feedback_a: O(n) would suggest that there is no nesting. There are several nested for loops.
   :feedback_b: Correct. The two consecutively nested for loops would dictate that this is in the realm of O(n<sup>2</sup>).
   :feedback_c: O(1) would suggest that the function is constant. Since there are multiple for loops intertwined, it is not in constant time.
   :feedback_d: O(n<sup>3</sup>) would suggest that there are three consecutively nested for loops. There are only two.
   
   4. What is the Big-O running time of the ``buildGraph`` function?

.. shortanswer:: BigO

   5. Derive the Big-O running time for the topological sort algorithm.

.. shortanswer:: BigOTwo

   6. Derive the Big-O running time for the strongly connected components
   algorithm.

7. Show each step in applying Dijkstra’s algorithm to the graph shown above.

8. Using Prim’s algorithm, find the minimum weight spanning tree for the
   graph shown above.

9. Draw a dependency graph illustrating the steps needed to send an
   email. Perform a topological sort on your graph.

10. Derive an expression for the base of the exponent used in expressing the 
    running time of the knights tour.
    
.. shortanswer:: DFS

   11. Explain why the general DFS algorithm is not suitable for solving 
    the knights tour problem.

12. What is the Big-O running time for Prim’s minimum 
    spanning tree algorithm?

