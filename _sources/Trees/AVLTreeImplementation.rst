..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


AVL Tree Implementation
~~~~~~~~~~~~~~~~~~~~~~~


Now that we have demonstrated that keeping an AVL tree in balance is
going to be a big performance improvement, let's look at how we will
augment the procedure to insert a new key into the tree. Since all new
keys are inserted into the tree as leaf nodes and we know that the
balance factor for a new leaf is zero, there are no new requirements for
the node that has just been inserted. But once the new leaf is added, we must
update the balance factor of its parent. How this new leaf affects the
parent’s balance factor depends on whether the leaf node is a left child
or a right child. If the new node is a right child, the balance factor of
the parent will be reduced by one. If the new node is a left child, then
the balance factor of the parent will be increased by one. This rule
can be applied recursively to the grandparent of the new node, and
possibly to every ancestor, all the way up to the root of the tree. Since
this is a recursive procedure, let's examine the two base cases for
updating balance factors:

-  The recursive call has reached the root of the tree.

-  The balance factor of the parent has been adjusted to zero. You
   should convince yourself that once a subtree has a balance factor of
   zero, then the balance of its ancestor nodes does not change.

We will implement the AVL tree as a subclass of ``BinarySearchTree``. To
begin, we will override the ``_put`` method and write a new
``update_balance`` helper method. These methods are shown in
:ref:`Listing 1 <lst_updbal>`. You will notice that the definition for ``_put`` is
exactly the same as in simple binary search trees except for the addition of
the calls to ``update_balance`` on lines 9 and 17.


**Listing 1**

.. _lst_updbal:

.. code-block:: python
    
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.left_child)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)
    		    
    		    

The new ``update_balance`` method is where most of the work is done. This
implements the recursive procedure we just described. It first checks to see if the current node is out
of balance enough to require rebalancing (line 20). If that
is the case then the rebalancing is done and no further updating to
parents is required. If the current node does not require rebalancing
then the balance factor of the parent is adjusted. If the balance factor
of the parent is nonzero then the algorithm continues to work its way
up the tree toward the root by recursively calling ``update_balance`` on
the parent.

When a rebalancing of the tree is necessary, how do we do it? Efficient
rebalancing is the key to making the AVL Tree work well without
sacrificing performance. In order to bring an AVL Tree back into balance,
we will perform one or more **rotations** on the tree.

To understand what a rotation is, let's look at a very simple example.
Consider the tree in the left half of :ref:`Figure 3 <fig_unbalsimple>`. This tree
is out of balance with a balance factor of -2. To bring this tree into
balance we will use a left rotation around the subtree rooted at node A.

.. _fig_unbalsimple:

.. figure:: Figures/simpleunbalanced.png
   :align: center

   Figure 3: Transforming an Unbalanced Tree Using a Left Rotation
   

To perform a left rotation we essentially do the following:

#.  Promote the right child (B) to be the root of the subtree.

#.  Move the old root (A) to be the left child of the new root.

#.  If new root (B) already has a left child, then make it the right child
    of the new left child (A). Note: since the new root (B) was the right
    child of A, the right child of A is guaranteed to be empty at this
    point. This allows us to add a new node as the right child without
    any further consideration.


While this procedure is fairly easy in concept, the details of the code
are a bit tricky since we need to move things around in just the right
order so that all properties of a binary search tree are preserved.
Furthermore, we need to make sure to update all of the parent pointers
appropriately.

Let's look at a slightly more complicated tree to illustrate the right
rotation. The left side of :ref:`Figure 4 <fig_rightrot1>` shows a tree that is
left-heavy and with a balance factor of 2 at the root.


.. _fig_rightrot1:

.. figure:: Figures/rightrotate1.png
  :align: center

  Figure 4: Transforming an Unbalanced Tree Using a Right Rotation


To perform a right rotation we essentially do the following:

#.  Promote the left child (C) to be the root of the subtree.

#.  Move the old root (E) to be the right child of the new root.

#.  If the new root (C) already has a right child (D) then make it the
    left child of the new right child (E). Note: since the new root (C)
    was the left child of E, the left child of E is guaranteed to be
    empty at this point. This allows us to add a new node as the left
    child without any further consideration.

Now that you have seen the rotations and have the basic idea of how a
rotation works let us look at the code. :ref:`Listing 2 <lst_bothrotations>` shows the
code for the left rotation (the
``rotate_right`` method is symmetrical to ``rotate_left`` so we will leave
it to you to study the code for ``rotate_right``). In line 2
we create a temporary variable to keep track of the new root of the
subtree. As we said before, the new root is the right child of the
previous root. Now that a reference to the right child has been stored
in this temporary variable, we replace the right child of the old root
with the left child of the new.

The next step is to adjust the parent pointers of the two nodes. If
``new_root`` has a left child then the new parent of the left child
becomes the old root. The parent of the new root is set to the parent of
the old root. If the old root was the root of the entire tree then we
must set the root of the tree to point to this new root. Otherwise, if
the old root is a left child then we change the parent of the left child
to point to the new root; otherwise we change the parent of the right
child to point to the new root. (lines 10-13).
Finally we set the parent of the old root to be the new root. This is a
lot of complicated bookkeeping, so we encourage you to trace through
this function while looking at :ref:`Figure 3 <fig_unbalsimple>`.

.. _lst_bothrotations:

**Listing 2**

.. code-block:: python

    def rotate_left(self, rotation_root):
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)
        )		      
			      
.. highlight:: python
  :linenothreshold: 500

Finally, lines 16-21 require some explanation. In
these lines we update the balance factors of the old and the new
root. Since all the other moves involve moving entire subtrees, the
balance factors of all other nodes are unaffected by the rotation. But
how can we update the balance factors without completely recalculating
the heights of the new subtrees? :ref:`Figure 5 <fig_bfderive>` and the
following derivation should convince you that these lines are correct.

.. _fig_bfderive:

.. figure:: Figures/bfderive.png
   :align: center

   Figure 5: A Left Rotation


:ref:`Figure 5 <fig_bfderive>` shows a left rotation. B and D are the pivotal
nodes and A, C, E are their subtrees. Let :math:`h_x` denote the
height of a particular subtree rooted at node :math:`x`. By definition
we know the following:

.. math::

  new\_bal(B) = h_A - h_C \\
  old\_bal(B) = h_A - h_D


But we know that the old height of D can also be given by :math:`1 + max(h_C, h_E)`,
that is, the height of D is one more than the maximum
height of its two children. Remember that :math:`h_C` and
:math:`h_E` have not changed. So, let us substitute that in to the
second equation, which gives us 

:math:`old\_bal(B) = h_A - (1 + max(h_C,h_E))` 

and then subtract the two equations. The following steps
do the subtraction and use some algebra to simplify the equation for
:math:`new\_bal(B)`.

.. math::

   new\_bal(B) - old\_bal(B) = h_A - h_C - (h_A - (1 + max(h_C,h_E))) \\
   new\_bal(B) - old\_bal(B) = h_A - h_C - h_A + (1 + max(h_C,h_E)) \\
   new\_bal(B) - old\_bal(B) = h_A  - h_A + 1 + max(h_C,h_E) - h_C  \\
   new\_bal(B) - old\_bal(B) =  1 + max(h_C,h_E) - h_C 


Next we will move :math:`old\_bal(B)` to the right-hand side of the
equation and make use of the fact that
:math:`max(a,b)-c = max(a-c, b-c)`.

.. math::

   new\_bal(B) = old\_bal(B) + 1 + max(h_C - h_C ,h_E - h_C) \\


But :math:`h_E - h_C` is the same as :math:`-old\_bal(D)`. So we can
use another identity that says :math:`max(-a,-b) = -min(a,b)`. So we
can finish our derivation of :math:`new\_bal(B)` with the following
steps:

.. math::

   new\_bal(B) = old\_bal(B) + 1 + max(0 , -old\_bal(D)) \\
   new\_bal(B) = old\_bal(B) + 1 - min(0 , old\_bal(D)) \\


Now we have all of the parts in terms that we readily know. If we
remember that B is ``rotation_root`` and D is ``new_root`` then we can see this
corresponds exactly to the statement on lines 16-18 in
:ref:`Listing 2 <lst_bothrotations>`, or:

::

    rotation_root.balance_factor = (
        rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
    )

A similar derivation gives us the equation for the updated node D as
well as the balance factors after a right rotation. We leave these as
an exercise for you.

Now you might think that we are done. We know how to do our left and
right rotations, and we know when we should do a left or right rotation. 
But take a look at :ref:`Figure 6 <fig_hardrotate>`. Since node A has a balance
factor of -2 we should do a left rotation. But what happens when we do
the left rotation around A?

.. _fig_hardrotate:

.. figure:: Figures/hardunbalanced.png
   :align: center

   Figure 6: An Unbalanced Tree that is More Difficult to Balance


:ref:`Figure 7 <fig_badrotate>` shows us that after the left rotation we are now
out of balance the other way. If we do a right rotation to correct the
situation we are right back where we started.

.. _fig_badrotate:

.. figure:: Figures/badrotate.png
   :align: center

   Figure 7: After a Left Rotation the Tree is Out of Balance in the Other Direction


To correct this problem we must use the following set of rules:

#.  If a subtree needs a left rotation to bring it into balance, first
    check the balance factor of the right child. If the right child is
    left-heavy, then do a right rotation on right child followed by the
    original left rotation.

#.  If a subtree needs a right rotation to bring it into balance, first
    check the balance factor of the left child. If the left child is
    right-heavy, then do a left rotation on the left child followed by
    the original right rotation.

:ref:`Figure 8 <fig_rotatelr>` shows how these rules solve the dilemma we
encountered in :ref:`Figure 6 <fig_hardrotate>` and :ref:`Figure 7 <fig_badrotate>`. Starting
with a right rotation around node C puts the tree in a position where
the left rotation around A brings the entire subtree back into balance.

.. _fig_rotatelr:

.. figure:: Figures/rotatelr.png
   :align: center

   Figure 8: A Right Rotation Followed by a Left Rotation


The code that implements these rules can be found in our ``rebalance``
method, which is shown in :ref:`Listing 3 <lst_rebalance>`. Rule number 1 from
above is implemented by the ``if`` statement starting on line 2.
Rule number 2 is implemented by the ``elif`` statement starting on
line 8.

.. _lst_rebalance:

**Listing 3**

.. highlight:: python
  :linenothreshold: 5

::

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)


.. highlight:: python
   :linenothreshold: 500

The :ref:`discussion questions <tree_discuss>` provide you the opportunity to rebalance a tree
that requires a left rotation followed by a right. In addition the
discussion questions provide you with the opportunity to rebalance some
trees that are a little more complex than the tree in
:ref:`Figure 8 <fig_rotatelr>`.

By keeping the tree in balance at all times, we can ensure that the
``get`` method will run in order :math:`O(log_2(n))` time. But the
question is at what cost to our ``put`` method? Let us break this down
into the operations performed by ``put``. Since a new node is inserted
as a leaf, updating the balance factors of all the parents will require
a maximum of :math:`log_2(n)` operations, one for each level of the
tree. If a subtree is found to be out of balance, a maximum of two
rotations are required to bring the tree back into balance. But each of
the rotations works in :math:`O(1)` time, so even our ``put``
operation remains :math:`O(log_2(n))`.

At this point we have implemented a functional AVL tree, unless you need
the ability to delete a node. We leave the deletion of the node and
subsequent updating and rebalancing as an exercise for you.

