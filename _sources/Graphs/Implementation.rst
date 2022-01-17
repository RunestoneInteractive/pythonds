..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Implementation
~~~~~~~~~~~~~~

Using dictionaries, it is easy to implement the adjacency list in
Python. In our implementation of the graph abstract data type we will
create two classes:
``Vertex``, which will represent each vertex in the graph 
(see :ref:`Listing 1 <lst_vertex>`) and
``Graph``, which holds the master list of vertices (see :ref:`Listing 2 <lst_graph>`).

Each ``Vertex`` uses a dictionary to keep track of the vertices to which
it is connected and the weight of each edge. This dictionary is called
``neighbors``. The listing below shows the code for the ``Vertex``
class. The constructor simply initializes the ``key``, which will
typically be a string, and the ``neighbors`` dictionary. The
``set_neighbor`` method is used to add a connection from this vertex to
another. The ``get_neighbors`` method returns all of the vertices in
the adjacency list, as represented by the ``neighbors`` instance
variable. The ``get_neighbor`` method returns the weight of the edge from
this vertex to the vertex passed as a parameter.

.. _lst_vertex:

**Listing 1**

::

    class Vertex:
        def __init__(self, key):
            self.key = key
            self.neighbors = {}

        def get_neighbor(self, other):
            return self.neighbors.get(other, None)

        def set_neighbor(self, other, weight=0):
            self.neighbors[other] = weight

        def __repr__(self):
            return f"Vertex({self.key})"

        def __str__(self):
            return (
                str(self.key)
                + " connected to: "
                + str([x.key for x in self.neighbors])
            )

        def get_neighbors(self):
            return self.neighbors.keys()

        def get_key(self):
            return self.key

The ``Graph`` class, shown in the next listing, contains a dictionary
that maps vertex names to vertex objects. In :ref:`Figure 4 <fig_adjlist>` this
dictionary object is represented by the shaded gray box. ``Graph`` also
provides methods for adding vertices to a graph and connecting one
vertex to another. The ``get_vertices`` method returns the names of all
of the vertices in the graph. In addition, we have implemented the
``__iter__`` method to make it easy to iterate over all the vertex
objects in a particular graph. Together, the two methods allow you to
iterate over the vertices in a graph by name, or by the objects
themselves.

.. _lst_graph:

**Listing 2**

::

    class Graph:
        def __init__(self):
            self.vertices = {}

        def set_vertex(self, key):
            self.vertices[key] = Vertex(key)

        def get_vertex(self, key):
            return self.vertices.get(key, None)

        def __contains__(self, key):
            return key in self.vertices

        def add_edge(self, from_vert, to_vert, weight=0):
            if from_vert not in self.vertices:
                self.set_vertex(from_vert)
            if to_vert not in self.vertices:
                self.set_vertex(to_vert)
            self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

        def get_vertices(self):
            return self.vertices.keys()

        def __iter__(self):
            return iter(self.vertices.values())

Using the ``Graph`` and ``Vertex`` classes just defined, the following
Python session creates the graph in :ref:`Figure 2 <fig_dgsimple>`. First we
create six vertices numbered 0 through 5. Then we display the vertex
dictionary. Notice that for each key 0 through 5 we have created an
instance of a ``Vertex``. Next, we add the edges that connect the
vertices together. Finally, a nested loop verifies that each edge in the
graph is properly stored. You should check the output of the edge list
at the end of this session against :ref:`Figure 2 <fig_dgsimple>`.

::

    >>> g = Graph()
    >>> for i in range(6):
    ...     g.set_vertex(i)
    >>> g.vertices
    {0: Vertex(0), 1: Vertex(1), 2: Vertex(2), 3: Vertex(3), 4: Vertex(4), 5: Vertex(5)}
    >>> g.add_edge(0, 1, 5)
    >>> g.add_edge(0, 5, 2)
    >>> g.add_edge(1, 2, 4)
    >>> g.add_edge(2, 3, 9)
    >>> g.add_edge(3, 4, 7)
    >>> g.add_edge(3, 5, 3)
    >>> g.add_edge(4, 0, 1)
    >>> g.add_edge(5, 4, 8)
    >>> g.add_edge(5, 2, 1)
    >>> for v in g:
    ...     for w in v.get_neighbors():
    ...         print("f({v.get_key()}, {w.get_key()})")
    ...
    (0, 1)
    (0, 5)
    (1, 2)
    (2, 3)
    (3, 4)
    (3, 5)
    (4, 0)
    (5, 4)
    (5, 2)
