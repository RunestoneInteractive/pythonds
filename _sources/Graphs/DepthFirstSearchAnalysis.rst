..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Depth-First Search Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~


The general running time for depth-first search is as follows. The loops
in ``dfs`` both run in :math:`O(|V|)`,
not counting what happens in ``dfs_visit``, since they are executed once
for each vertex in the graph. In ``dfs_visit`` the loop is executed once
for each edge in the adjacency list of the current vertex.
Since ``dfs_visit`` is only called
recursively if the vertex is white, the loop will execute a maximum of
once for every edge in the graph, or :math:`O(|E|)`. Therefore, the total time
for depth-first search is :math:`O(|V| + |E|)`.

