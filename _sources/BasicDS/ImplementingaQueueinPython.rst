..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Implementing a Queue in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is again appropriate to create a new class for the implementation of
the abstract data type queue. As before, we will use the power and
simplicity of the list collection to build the internal representation
of the queue.

We need to decide which end of the list to use as the rear and which to
use as the front. The implementation shown in :ref:`Listing 1 <lst_queuecode>`
assumes that the rear is at position 0 in the list. This allows us to
use the ``insert`` function on lists to add new elements to the rear of
the queue. The ``pop`` operation can be used to remove the front element
(the last element of the list). Recall that this also means that ``enqueue``
will be :math:`O(n)` and ``dequeue`` will be :math:`O(1)`. 

.. _lst_queuecode:

**Listing 1**

::

    class Queue:
        """Queue implementation as a list"""

        def __init__(self):
            """Create new queue"""
            self._items = []

        def is_empty(self):
            """Check if the queue is empty"""
            return not bool(self._items)

        def enqueue(self, item):
            """Add an item to the queue"""
            self._items.insert(0, item)

        def dequeue(self):
            """Remove an item from the queue"""
            return self._items.pop()

        def size(self):
            """Get the number of items in the queue"""
            return len(self._items)

CodeLens 1 shows the ``Queue`` class in
action as we perform the sequence of operations from
:ref:`Table 1 <tbl_queueoperations>`.

.. codelens:: ququeuetest
    :caption: Example Queue Operations

    class Queue:
        """Queue implementation as a list"""

        def __init__(self):
            """Create new queue"""
            self._items = []

        def is_empty(self):
            """Check if the queue is empty"""
            return not bool(self._items)

        def enqueue(self, item):
            """Add an item to the queue"""
            self._items.insert(0, item)

        def dequeue(self):
            """Remove an item from the queue"""
            return self._items.pop()

        def size(self):
            """Get the number of items in the queue"""
            return len(self._items)

    q = Queue()
    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue(True)
    print(q.size())


Further manipulation of this queue would give the following results:


::

    >>> q.size()
    3
    >>> q.is_empty()
    False
    >>> q.enqueue(8.4)
    >>> q.dequeue()
    4
    >>> q.dequeue()
    'dog'
    >>> q.size()
    2

.. admonition:: Self Check

   .. mchoice:: queue_1
      :correct: b
      :answer_a: 'hello', 'dog'
      :answer_b: 'dog', 3
      :answer_c: 'hello', 3
      :answer_d: 'hello', 'dog', 3
      :feedback_a: Remember the first thing added to the queue is the first thing removed.  FIFO
      :feedback_b: Yes, first in first out means that hello is gone
      :feedback_c: Queues, and Stacks are both data structures where you can only access the first and the last thing.
      :feedback_d: Ooops, maybe you missed the dequeue call at the end?

      Suppose you have the following series of queue operations.

      ::

          q = Queue()
          q.enqueue("hello")
          q.enqueue("dog")
          q.enqueue(3)
          q.dequeue()

      What items are left on the queue?

