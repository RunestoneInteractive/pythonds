..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Implementation
--------------

Keeping in mind the definitions from the previous section,
we can use the following functions to create and manipulate a binary tree:

-  ``BinaryTree()`` creates a new instance of a binary tree.

-  ``get_root_val()`` returns the object stored in the current node.

-  ``set_root_val(val)`` stores the object in parameter ``val`` in the current node.

-  ``get_left_child()`` returns the binary tree corresponding to the left child of the current node.

-  ``get_right_child()`` returns the binary tree corresponding to the right child of the current node.

-  ``insert_left(val)`` creates a new binary tree and installs it as the left child of the current node.

-  ``insert_right(val)`` creates a new binary tree and installs it as the right child of the current node.
        

The key decision in implementing a tree is choosing a good internal storage technique.
Python allows us two very interesting possibilities, and we will examine both
before choosing one.  We call them *list of lists* and *nodes and references*.

