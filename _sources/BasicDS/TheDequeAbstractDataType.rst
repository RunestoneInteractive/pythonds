..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


The Deque Abstract Data Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The deque abstract data type is defined by the following structure and
operations. A deque is structured, as described above, as an ordered
collection of items where items are added and removed from either end,
either front or rear. The deque operations are given below.

-  ``Deque()`` creates a new deque that is empty. It needs no parameters
   and returns an empty deque.

-  ``add_front(item)`` adds a new item to the front of the deque. It
   needs the item and returns nothing.

-  ``add_rear(item)`` adds a new item to the rear of the deque. It needs
   the item and returns nothing.

-  ``remove_front()`` removes the front item from the deque. It needs no
   parameters and returns the item. The deque is modified.

-  ``remove_rear()`` removes the rear item from the deque. It needs no
   parameters and returns the item. The deque is modified.

-  ``is_empty()`` tests to see whether the deque is empty. It needs no
   parameters and returns a boolean value.

-  ``size()`` returns the number of items in the deque. It needs no
   parameters and returns an integer.

As an example, if we assume that ``d`` is a deque that has been created
and is currently empty, then :ref:`Table 6 <tbl_dequeoperations>` shows the results
of a sequence of deque operations. Note that the contents in front are
listed on the right. It is very important to keep track of the front and
the rear as you move items in and out of the collection as things can
get a bit confusing.

.. _tbl_dequeoperations:

.. table:: **Table 6: Examples of Deque Operations**

    ============================= =============================== ==================
            **Deque Operation**              **Deque Contents**     **Return Value**
    ============================= =============================== ==================
                 ``d.is_empty()``                          ``[]``           ``True``
                ``d.add_rear(4)``                         ``[4]``                   
            ``d.add_rear("dog")``                  ``['dog', 4]``                   
           ``d.add_front("cat")``           ``['dog', 4, 'cat']``                   
            ``d.add_front(True)``     ``['dog', 4, 'cat', True]``                   
                     ``d.size()``     ``['dog', 4, 'cat', True]``              ``4``
                 ``d.is_empty()``     ``['dog', 4, 'cat', True]``          ``False``
              ``d.add_rear(8.4)`` ``[8.4,'dog', 4, 'cat', True]``                   
              ``d.remove_rear()``     ``['dog', 4, 'cat', True]``            ``8.4``
             ``d.remove_front()``           ``['dog', 4, 'cat']``           ``True``
    ============================= =============================== ==================


