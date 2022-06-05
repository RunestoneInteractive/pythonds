..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


The Graph Abstract Data Type
----------------------------

The graph abstract data type is defined as a collection of vertices
and edges. Vertices may be either connected to each other or isolated. Edges join
two vertices and may be weighted.

-  ``Graph()`` creates a new empty graph.

-  ``add_vertex(vert)`` adds an instance of ``Vertex`` to the graph.

-  ``add_edge(from_vert, to_vert)`` adds a new directed edge to the graph
   that connects two vertices.

-  ``add_edge(from_vert, to_vert, weight)`` adds a new weighted directed
   edge to the graph that connects two vertices.

-  ``get_vertex(vert_key)`` finds the vertex in the graph named
   ``vert_key``.

-  ``get_vertices()`` returns the list of all vertices in the graph.

-  ``in`` returns ``True`` for a statement of the form
   ``vertex in graph`` if the given vertex is in the graph, ``False``
   otherwise.

Now that we have looked at the definition for the graph ADT,
there are several ways we can implement it in Python. We will see that there are
trade-offs in using different representations to implement the ADT
described above. There are two well-known implementations of a graph,
the **adjacency matrix** and the **adjacency list**. We will explain
both of these options, and then implement one as a Python class.

