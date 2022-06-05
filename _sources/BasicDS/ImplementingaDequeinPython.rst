..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Implementing a Deque in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we have done in previous sections, we will create a new class for the
implementation of the abstract data type deque. Again, the Python list
will provide a very nice set of methods upon which to build the details
of the deque. Our implementation (:ref:`Listing 1 <lst_dequecode>`) will assume that
the rear of the deque is at position 0 in the list.

.. _lst_dequecode:

.. highlight:: python
   :linenothreshold: 5

**Listing 1**

::

    class Deque:
        """Deque implementation as a list"""

        def __init__(self):
            """Create new deque"""
            self._items = []

        def is_empty(self):
            """Check if the deque is empty"""
            return not bool(self._items)

        def add_front(self, item):
            """Add an item to the front of the deque"""
            self._items.append(item)

        def add_rear(self, item):
            """Add an item to the rear of the deque"""
            self._items.insert(0, item)

        def remove_front(self):
            """Remove an item from the front of the deque"""
            return self._items.pop()

        def remove_rear(self):
            """Remove an item from the rear of the deque"""
            return self._items.pop(0)

        def size(self):
            """Get the number of items in the deque"""
            return len(self._items)

.. highlight:: python
   :linenothreshold: 500

In ``remove_front`` we use the ``pop`` method to remove the last element
from the list. However, in ``remove_rear``, the ``pop(0)`` method must
remove the first element of the list. Likewise, we need to use the
``insert`` method (line 12) in ``add_rear`` since the ``append`` method
assumes the addition of a new element to the end of the list.

CodeLens 1 shows the ``Deque`` class in
action as we perform the sequence of operations from
:ref:`Table 1 <tbl_dequeoperations>`.

.. codelens:: deqtest
    :caption: Example Deque Operations

    class Deque:
        """Queue implementation as a list"""

        def __init__(self):
            """Create new deque"""
            self._items = []

        def is_empty(self):
            """Check if the deque is empty"""
            return not bool(self._items)

        def add_front(self, item):
            """Add an item to the front of the deque"""
            self._items.append(item)

        def add_rear(self, item):
            """Add an item to the rear of the deque"""
            self._items.insert(0, item)

        def remove_front(self):
            """Remove an item from the front of the deque"""
            return self._items.pop()

        def remove_rear(self):
            """Remove an item from the rear of the deque"""
            return self._items.pop(0)

        def size(self):
            """Get the number of items in the deque"""
            return len(self._items)

    d=Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())


You can see many similarities to Python code already described for
stacks and queues. You are also likely to observe that in this
implementation adding and removing items from the front is :math:`O(1)` whereas
adding and removing from the rear is :math:`O(n)`. This is to be expected given
the common operations that appear for adding and removing items. Again,
the important thing is to be certain that we know where the front and
rear are assigned in the implementation.

