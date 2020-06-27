Key Terms
=========

======================== ====================================
amortized analysis       deterministic finite automaton (DFA)
DFA graph                dictionary
dithering                DNA string
greedy method            KMP graph
Knuth-Morris-Pratt (KMP) level
map                      octtree
pixel                    public key encryption
quantization             RSA algorithm
skip list                substring
tower                    
======================== ====================================

Discussion Questions
====================

#. Where do skip lists get their name?

#. Compare the notion of a perfectly balanced binary search tree and a
   skip list. Can you draw pictures to describe these notions?

#. What would it mean if all towers in a skip list were one level high?

#. Given a set of 20 keys, is it possible that one of the towers could
   have a height of 20?

#. Run the ``OctTree`` quantization program on an image of your choice.
   Try some different settings for the maximum depth of the tree as well
   as the final number of colors.

#. Explain why the indices for an ``OctTree`` node are calculated
   starting with the most significant bit and going to the least
   significant bit.

#. Draw the nodes in an ``OctTree``, down to level 5, after inserting
   the following two colors: (174, 145, 229) and (92, 145, 85).

#. Draw a DFA graph for the pattern ATC.

#. Compute the mismatch links for the pattern ATC.

#. Create a KMP graph for the pattern ATCCAT.

Programming Exercises
=====================

#. Implement the following methods for the ``ArayList`` class and then
   analyze their performance.

   -  ``del``, delete the item at the given index from the list.

   -  verb|pop|, implement the pop method with and without a positional
      parameter.

   -  ``index`` search for a given value in the ``ArrayList``. Return
      its position in the list if it is found and -1 if the item is not
      present.

   -  Make the ArrayList iterable.

#. The Python list supports both concatenation and repetition. Add
   support for the ``+`` and ``*`` operators to the ``ArrayList``.

#. Implement the ``delete`` method for a skip list. You can assume that
   the key is present.

#. Implement methods for skip list that will allow the map to perform
   the following operations:

   -  ``__contains__()`` will return a boolean result as to whether a
      key is present in the map

   -  ``keys()`` will return a list of keys in the map

   -  ``values()`` will return a list of values in the map

#. Implement ``__getItem__()`` and ``__setItem__()`` methods for skip
   lists.

#. Modify the ``OctTree`` class to improve the performance of the
   ``reduce`` method by using a more efficient data structure for
   keeping track of the leaf nodes.

#. Add two methods to the ``OctTree`` class, one to write a quantized
   image to a disk file and one to read a file of the same format you
   wrote.

#. Some versions of ``OctTree`` quantization look at the total count for
   all the children of a node and use that information to decide which
   nodes to reduce. Modify the ``OctTree`` implementation to use this
   method of node selection for reducing the tree.

#. Implement a version of the simple pattern-matcher that will locate
   *all* occurrences of the pattern in the text.

#. Modify the graph implementation from Chapter `[graphs] <#graphs>`__
   so that it can be used to represent KMP graphs. Using the
   ``mismatch_links`` method, write a method that will take a pattern
   and create the complete KMP graph. With the graph complete, write a
   program that will run an arbitrary text against the KMP graph and
   return whether a match exists.
