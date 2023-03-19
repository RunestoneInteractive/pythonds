Exercises
=========

#. Where do skip lists get their name?

#. Compare the notion of a perfectly balanced binary search tree and a
   skip list. Can you draw pictures to describe these notions?

#. What would it mean if all towers in a skip list were one level high?

#. Given a set of 20 keys, is it possible that one of the towers could
   have a height of 20?

#. Run the octree quantization program on an image of your choice.
   Try some different settings for the maximum depth of the tree as well
   as the final number of colors.

#. Explain why the indices for an octree node are calculated
   starting with the most significant bit and going to the least
   significant bit.

#. Draw the nodes in an octree, down to level 5, after inserting
   the following two colors: (174, 145, 229) and (92, 145, 85).

#. Draw a DFA graph for the pattern ATC.

#. Compute the mismatched links for the pattern ATC.

#. Create a KMP graph for the pattern ATCCAT.

#. Implement the following methods for the ``ArrayList`` class and then
   analyze their performance.

   -  ``__delitem__``: Delete the item at the given index from the list.

   -  ``pop``: Implement the pop method with and without a positional
      parameter.

   -  ``index``: Search for a given value in the ``ArrayList``. Return
      its position in the list if it is found and -1 if the item is not
      present.

   -  ``__iter__``: Make the ``ArrayList`` iterable.

#. Modify ``encrypt`` method of the Caesar cipher (Listing `[lst_enc] <#lst_enc>`__) 
   to accept a parameter that specifies the encryption key.

#. The Python list supports both concatenation and repetition. Add
   support for the ``+`` and ``*`` operators to the ``ArrayList``.

#. Implement the ``delete`` method for a skip list. You can assume that
   the key is present.

#. Implement methods for a skip list that will allow the map to perform
   the following operations:

   -  ``__contains__()`` will return a boolean result as to whether a
      key is present in the map.

   -  ``keys()`` will return a list of keys in the map.

   -  ``values()`` will return a list of values in the map.

#. Implement the ``__getitem__()`` and the ``__setitem__()`` methods for a skip
   list.

#. Modify the ``Octree`` class to improve the performance of the
   ``reduce`` method by using a more efficient data structure for
   keeping track of the leaf nodes.

#. Add two methods to the ``Octree`` class, one to write a quantized
   image to a disk file and one to read a file of the same format you
   wrote.

#. Some versions of ``Octree`` quantization look at the total count for
   all the children of a node and use that information to decide which
   nodes to reduce. Modify the ``Octree`` implementation to use this
   method of node selection for reducing the tree.

#. Implement a version of the simple pattern-matcher that will locate
   all occurrences of the pattern in the text.

#. Modify the graph implementation from Chapter `[graphs] <#graphs>`__
   so that it can be used to represent KMP graphs. Using the
   ``mismatched_links`` method, write a method that will take a pattern
   and create the complete KMP graph. With the graph complete, write a
   program that will run an arbitrary text against the KMP graph and
   return whether a match exists.
