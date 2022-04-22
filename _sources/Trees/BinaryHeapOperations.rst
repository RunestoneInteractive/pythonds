..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Binary Heap Operations
~~~~~~~~~~~~~~~~~~~~~~

The basic operations we will implement for our binary heap are as
follows:

-  ``BinaryHeap()`` creates a new empty binary heap.

-  ``insert(k)`` adds a new item to the heap.

-  ``get_min()`` returns the item with the minimum key value, leaving
   the item in the heap.

-  ``delete()`` returns the item with the minimum key value, removing
   the item from the heap.

-  ``is_empty()`` returns ``True`` if the heap is empty, ``False`` otherwise.

-  ``size()`` returns the number of items in the heap.

-  ``heapify(list)`` builds a new heap from a list of keys.

:ref:`ActiveCode 1 <lst_heap1>` demonstrates the use of some of the binary
heap methods.  Notice that no matter what order we add items to the heap, the smallest
is removed each time.

.. _lst_heap1:


.. activecode:: heap1
    :caption: Using the Binary Heap
    :nocodelens:

    from pythonds3.trees import BinaryHeap

    my_heap = BinaryHeap()
    my_heap.insert(5)
    my_heap.insert(7)
    my_heap.insert(3)
    my_heap.insert(11)

    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
