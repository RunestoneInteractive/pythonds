..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Search Tree Operations
~~~~~~~~~~~~~~~~~~~~~~

Before we look at the implementation, let’s review the interface
provided by the map ADT. You will notice that this interface is very
similar to the Python dictionary.

-  ``Map()`` creates a new empty map.

-  ``put(key, val)`` adds a new key--value pair to the map. If the key is
   already in the map, it replaces the old value with the new value.

-  ``get(key)`` takes a key and returns the matching value stored in the map or
   ``None`` otherwise.

-  ``del`` deletes the key--value pair from the map using a statement of
   the form ``del map[key]``.

-  ``size()`` returns the number of key--value pairs stored in the map.

-  ``in`` return ``True`` for a statement of the form ``key in map`` if
   the given key is in the map, ``False`` otherwise.

