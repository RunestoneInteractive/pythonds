..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Implementing a Stack in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have clearly defined the stack as an abstract data type, we
will turn our attention to using Python to implement the stack. Recall
that when we give an abstract data type a physical implementation, we
refer to the implementation as a *data structure*.

As we described in Chapter 1, in Python, as in any object-oriented
programming language, the implementation of choice for an abstract data
type such as a stack is the creation of a new class. The stack
operations are implemented as methods. Further, to implement a stack,
which is a collection of elements, it makes sense to utilize the power
and simplicity of the primitive collections provided by Python. We will
use a list.

Recall that the list class in Python provides an ordered collection
mechanism and a set of methods. For example, if we have the list
[2, 5, 3, 6, 7, 4], we need only to decide which end of the list will be
considered the top of the stack and which will be the base. Once that
decision is made, the operations can be implemented using the list
methods such as ``append`` and ``pop``.

The following stack implementation (:ref:`ActiveCode 1 <lst_stackcode1>`) assumes that
the end of the list will hold the top element of the stack. As the stack
grows (as ``push`` operations occur), new items will be added on the end
of the list. ``pop`` operations will manipulate that same end.

.. _lst_stackcode1:


.. activecode:: stack_1ac
    :caption: Implementing a Stack class using Python lists
    :nocodelens:

    class Stack:
        """Stack implementation as a list"""

        def __init__(self):
            """Create new stack"""
            self._items = []

        def is_empty(self):
            """Check if the stack is empty"""
            return not bool(self._items)

        def push(self, item):
            """Add an item to the stack"""
            self._items.append(item)

        def pop(self):
            """Remove an item from the stack"""
            return self._items.pop()

        def peek(self):
            """Get the value of the top item in the stack"""
            return self._items[-1]

        def size(self):
            """Get the number of items in the stack"""
            return len(self._items)

Remember that nothing happens when we click the ``run`` button other than the
definition of the class.  We must create a ``Stack`` object and then use it.
:ref:`ActiveCode 2 <lst_stackcode1>` shows the ``Stack`` class in
action as we perform the sequence of operations from
:ref:`Table 1 <tbl_stackops>`.  Notice that the definition of the ``Stack`` class is
imported from the ``pythonds3`` module  that is included with the materials for this book
or can be downloaded from the `Python Package Index <https://pypi.org/>`_.

.. note::
    The ``pythonds3`` module contains implementations of all data structures discussed in this book.
    It is structured according to the sections: basic, trees, and graphs.
    The module can be downloaded from `GitHub <https://github.com/psads/pythonds3>`_
    or installed from the command line as follows:
    
    ``python3 -m pip install -U pythonds3``


.. activecode:: stack_ex_1
    :nocodelens:

    from pythonds3.basic import Stack

    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())



It is important to note that we could have chosen to implement the stack
using a list where the top is at the beginning instead of at the end. In
this case, the previous ``pop`` and ``append`` methods would no longer
work and we would have to index position 0 (the first item in the list)
explicitly using ``pop`` and ``insert``. The implementation is shown in
:ref:`CodeLens 1 <lst_stackcode2>`.

.. _lst_stackcode2:

.. codelens:: stack_cl_1
    :caption: Alternative Implementation of the Stack class

    class Stack:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def push(self, item):
            self.items.insert(0, item)

        def pop(self):
            return self.items.pop(0)

        def peek(self):
            return self.items[0]

        def size(self):
            return len(self.items)

    s = Stack()
    s.push("hello")
    s.push("true")
    print(s.pop())


This ability to change the physical implementation of an abstract data
type while maintaining the logical characteristics is an example of
abstraction at work. However, even though the stack will work either
way, if we consider the performance of the two implementations, there is
definitely a difference. Recall that the ``append()`` and ``pop()``
operations were both :math:`O(1)`. This means that the first implementation will
perform ``push`` and ``pop`` in constant time no matter how many items are on
the stack. The performance of the second implementation suffers in that
the ``insert(0)`` and ``pop(0)`` operations will both require :math:`O(n)` for a
stack of size ``n``. Clearly, even though the implementations are logically
equivalent, they would have very different timings when performing
benchmark testing.

.. admonition:: Self Check

   .. mchoice:: stack_1
      :answer_a: "x"
      :answer_b: "y"
      :answer_c: "z"
      :answer_d: The stack is empty
      :correct: c
      :feedback_a: Remember that a stack is built from the bottom up.
      :feedback_b: Remember that a stack is built from the bottom up.
      :feedback_c: Good job.
      :feedback_d: Remember that a stack is built from the bottom up.

      Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?

      .. code-block:: python

       m = Stack()
       m.push("x")
       m.push("y")
       m.pop()
       m.push("z")
       m.peek()

   .. mchoice:: stack_2
      :answer_a: "x"
      :answer_b: the stack is empty
      :answer_c: an error will occur
      :answer_d: "z"
      :correct: c
      :feedback_a: You may want to check out the docs for isEmpty
      :feedback_b: There is an odd number of things on the stack but each time through the loop 2 things are popped.
      :feedback_c: Good Job.
      :feedback_d: You may want to check out the docs for isEmpty

      Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?

      .. code-block:: python

        m = Stack()
        m.push("x")
        m.push("y")
        m.push("z")
        while not m.is_empty():
           m.pop()
           m.pop()

   Write a function `rev_string(my_str)` that uses a stack to reverse the
   characters in a string.

   .. actex:: stack_stringrev
      :nocodelens:

      from test import testEqual
      from pythonds3.basic import Stack

      def rev_string(my_str):
          # your code here

      testEqual(rev_string("apple"), "elppa")
      testEqual(rev_string("x"), "x")
      testEqual(rev_string("1234567890"), "0987654321")

.. youtube:: fZtLSM7k_54
    :divid: stack1_video
    :height: 315
    :width: 560
    :align: left

