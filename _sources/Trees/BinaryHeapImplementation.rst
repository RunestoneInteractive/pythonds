..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Binary Heap Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Structure Property
^^^^^^^^^^^^^^^^^^^^^^

In order to make our heap work efficiently, we will take advantage of
the logarithmic nature of the binary tree to represent our heap. In order to guarantee logarithmic
performance, we must keep our tree balanced. A balanced binary tree has
roughly the same number of nodes in the left and right subtrees of the
root. In our heap implementation we keep the tree balanced by creating a
**complete binary tree**. A complete binary tree is a tree in which each
level has all of its nodes. The exception to this is the bottom level of
the tree, which we fill in from left to right. :ref:`Figure 1 <fig_comptree>`
shows an example of a complete binary tree.

.. _fig_comptree:

.. figure:: Figures/compTree.png
   :align: center
   :alt: image

   Figure 1: A Complete Binary Tree

Another interesting property of a complete tree is that we can represent
it using a single list. We do not need to use nodes and references or
even lists of lists. Because the tree is complete, the left child of a
parent (at position :math:`p`) is the node that is found in position
:math:`2p + 1` in the list. Similarly, the right child of the parent is at
position :math:`2p + 2` in the list. To find the parent of any node in
the tree, we can simply use Python’s integer division. Given that a node
is at position :math:`n` in the list, the parent is at position
:math:`(n - 1) // 2`. :ref:`Figure 2 <fig_heapOrder>` shows a complete binary tree
and also gives the list representation of the tree.  Note the :math:`2p + 1` and :math:`2p + 2` relationship between
parent and children. The list
representation of the tree, along with the full structure property,
allows us to efficiently traverse a complete binary tree using only a
few simple mathematical operations. We will see that this also leads to
an efficient implementation of our binary heap.

The Heap Order Property
^^^^^^^^^^^^^^^^^^^^^^^

The method that we will use to store items in a heap relies on
maintaining the heap order property. The **heap order property** is as
follows: in a heap, for every node :math:`x` with parent :math:`p`,
the key in :math:`p` is smaller than or equal to the key in
:math:`x`. :ref:`Figure 2 <fig_heapOrder>` also illustrates a complete binary
tree that has the heap order property.

.. _fig_heapOrder:

.. figure:: Figures/heapOrder.png
   :align: center
   :alt: image

   Figure 2: A Complete Binary Tree, along with Its List Representation


Heap Operations
^^^^^^^^^^^^^^^

We will begin our implementation of a binary heap with the constructor.
Since the entire binary heap can be represented by a single list, all
the constructor will do is initialize the list.
:ref:`Listing 1 <lst_heap1a>` shows the Python code for the constructor.

.. _lst_heap1a:


**Listing 1**

::

    class BinaryHeap:
        def __init__(self):
            self._heap = []

The next method we will implement is ``insert``. The easiest, and most
efficient, way to add an item to a list is to simply append the item to
the end of the list. The good news about appending is that it guarantees
that we will maintain the complete tree property. The bad news about
appending is that we will very likely violate the heap structure
property. However, it is possible to write a method that will allow us
to regain the heap structure property by comparing the newly added item
with its parent. If the newly added item is less than its parent, then
we can swap the item with its parent. :ref:`Figure 2 <fig_percUp>` shows the
series of swaps needed to percolate the newly added item up to its
proper position in the tree.

.. _fig_percUp:

.. figure:: Figures/percUp.png
   :align: center
   :alt: image

   Figure 2: Percolate the New Node up to Its Proper Position

Notice that when we percolate an item up, we are restoring the heap
property between the newly added item and the parent. We are also
preserving the heap property for any siblings. Of course, if the newly
added item is very small, we may still need to swap it up another level.
In fact, we may need to keep swapping until we get to the top of the
tree. :ref:`Listing 2 <lst_heap2>` shows the ``_perc_up`` method, which
percolates a new item as far up in the tree as it needs to go to
maintain the heap property. We used a leading underscore (``_``) in 
the name of the method as it is an internal operation.
The parent of the current node
can be computed by subtracting 1 from the index of the current node and dividing the result by 2.

We are now ready to write the ``insert`` method (see :ref:`Listing 3 <lst_heap3>`). Most of the work in the
``insert`` method is really done by ``_perc_up``. Once a new item is
appended to the tree, ``_perc_up`` takes over and positions the new item
properly.

.. _lst_heap2:

**Listing 2**

::

    def _perc_up(self, i):
        while (i - 1) // 2 >= 0:
            parent_idx = (i - 1) // 2
            if self._heap[i] < self._heap[parent_idx]:
                self._heap[i], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[i],
                )
            i = parent_idx


.. _lst_heap3:

**Listing 3**

::

    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)



With the ``insert`` method properly defined, we can now look at the
``delete`` method. Since the heap property requires that the root of the
tree be the smallest item in the tree, finding the minimum item is easy.
The hard part of ``delete`` is restoring full compliance with the heap
structure and heap order properties after the root has been removed. We
can restore our heap in two steps. First, we will restore the root item
by taking the last item in the list and moving it to the root position.
Moving the last item maintains our heap structure property. However, we
have probably destroyed the heap order property of our binary heap.
Second, we will restore the heap order property by pushing the new root
node down the tree to its proper position. :ref:`Figure 3 <fig_perc_down>` shows
the series of swaps needed to move the new root node to its proper
position in the heap.

.. _fig_perc_down:

.. figure:: Figures/percDown.png
   :align: center
   :alt: image

   Figure 3: Percolating the Root Node down the Tree

In order to maintain the heap order property, all we need to do is swap
the root with its smaller child that is less than the root. After the initial
swap, we may repeat the swapping process with a node and its children
until the node is swapped into a position on the tree where it is
already less than both children. The code for percolating a node down
the tree is found in the ``_perc_down`` and ``_get_min_child`` methods in
:ref:`Listing 4 <lst_heap4>`.

.. _lst_heap4:

**Listing 4**


::

    def _perc_down(self, i):
        while 2 * i + 1 < len(self._heap):
            sm_child = self._get_min_child(i)
            if self._heap[i] > self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = (
                    self._heap[sm_child],
                    self._heap[i],
                )
            else:
                break
            i = sm_child

    def _get_min_child(self, i):
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] < self._heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2

The code for the ``delete`` operation is in :ref:`Listing 5 <lst_heap5>`. Note
that once again the hard work is handled by a helper function, in this
case ``_perc_down``.

.. _lst_heap5:

**Listing 5**

::

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

To finish our discussion of binary heaps, we will look at a method to
build an entire heap from a list of keys. The first method you might
think of may be like the following. Given a list of keys, you could
easily build a heap by inserting each key one at a time. Since you are
starting with an empy list, it is sorted and you could use
binary search to find the right position to insert the next key at a
cost of approximately :math:`O(\log{n})` operations. However, remember
that inserting an item in the middle of the list may require
:math:`O(n)` operations to shift the rest of the list over to make
room for the new key. Therefore, to insert :math:`n` keys into the
heap would require a total of :math:`O(n \log{n})` operations.
However, if we start with an entire list then we can build the whole
heap in :math:`O(n)` operations. :ref:`Listing 6 <lst_heap6>` shows the code
to build the entire heap.

.. _lst_heap6:

**Listing 6**

::

    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        i = len(self._heap) // 2 - 1
        while i >= 0:
            self._perc_down(cuir_idx)
            i = i - 1


.. _fig_buildheap:

.. figure:: Figures/buildheap.png
   :align: center
   :alt: image

   Figure 4: Building a Heap from the List [9, 6, 5, 2, 3]

:ref:`Figure 4 <fig_buildheap>` shows the swaps that the ``hepify`` method
makes as it moves the nodes in an initial tree of [9, 6, 5, 2, 3] into
their proper positions. Although we start out in the middle of the tree
and work our way back toward the root, the ``_perc_down`` method ensures
that the largest child is always moved down the tree. Because the heap is a
complete binary tree, any nodes past the halfway point will be leaves
and therefore have no children. Notice that when ``i = 0``, we are
percolating down from the root of the tree, so this may require multiple
swaps. As you can see in the rightmost two trees of
:ref:`Figure 4 <fig_buildheap>`, first the 9 is moved out of the root position,
but after 9 is moved down one level in the tree, ``_perc_down`` ensures
that we check the next set of children farther down in the tree to
ensure that it is pushed as low as it can go. In this case it results in
a second swap with 3. Now that 9 has been moved to the lowest level of
the tree, no further swapping can be done. It is useful to compare the
list representation of this series of swaps with the tree representation
shown in :ref:`Figure 4 <fig_buildheap>`

::

          start  [9, 6, 5, 2, 3]
          i = 1  [9, 2, 5, 6, 3]
          i = 0  [2, 3, 5, 6, 9]


The complete binary heap implementation can be seen in ActiveCode 1.



.. activecode:: completeheap
    :caption: The Complete Binary Heap Example
    :hidecode:

    class BinaryHeap:
        def __init__(self):
            self._heap = []

        def _perc_up(self, cur_idx):
            while (cur_idx - 1) // 2 >= 0:
                parent_idx = (cur_idx - 1) // 2
                if self._heap[cur_idx] < self._heap[parent_idx]:
                    self._heap[cur_idx], self._heap[parent_idx] = (
                        self._heap[parent_idx],
                        self._heap[cur_idx],
                    )
                cur_idx = parent_idx

        def _perc_down(self, cur_idx):
            while 2 * cur_idx + 1 < len(self._heap):
                min_child_idx = self._get_min_child(cur_idx)
                if self._heap[cur_idx] > self._heap[min_child_idx]:
                    self._heap[cur_idx], self._heap[min_child_idx] = (
                        self._heap[min_child_idx],
                        self._heap[cur_idx],
                    )
                else:
                    return
                cur_idx = min_child_idx

        def _get_min_child(self, parent_idx):
            if 2 * parent_idx + 2 > len(self._heap) - 1:
                return 2 * parent_idx + 1
            if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
                return 2 * parent_idx + 1
            return 2 * parent_idx + 2

        def heapify(self, not_a_heap):
            self._heap = not_a_heap[:]
            cur_idx = len(self._heap) // 2 - 1
            while cur_idx >= 0:
                self._perc_down(cur_idx)
                cur_idx = cur_idx - 1

        def get_min(self):
            return self._heap[0]

        def insert(self, item):
            self._heap.append(item)
            self._perc_up(len(self._heap) - 1)

        def delete(self):
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            result = self._heap.pop()
            self._perc_down(0)
            return result

        def is_empty(self):
            return not bool(self._heap)

        def __len__(self):
            return len(self._heap)

        def __str__(self):
            return str(self._heap)

    a_heap = BinaryHeap()
    a_heap.heapify([9, 5, 6, 2, 3])

    while not a_heap.is_empty():
        print(a_heap.delete())


The assertion that we can build the heap in :math:`O(n)` may seem a
bit mysterious at first, and a proof is beyond the scope of this book.
However, the key to understanding that you can build the heap in
:math:`O(n)` is to remember that the :math:`\log{n}` factor is
derived from the height of the tree. For most of the work in
``heapify``, the tree is shorter than :math:`\log{n}`.

Using the fact that you can build a heap from a list in :math:`O(n)`
time, you will construct a sorting algorithm that uses a heap and sorts
a list in :math:`O(n\log{n})` as an exercise at the end of this
chapter.
