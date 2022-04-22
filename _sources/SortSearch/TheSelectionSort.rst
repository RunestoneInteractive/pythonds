..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


The Selection Sort
~~~~~~~~~~~~~~~~~~

The **selection sort** improves on the bubble sort by making only one
exchange for every pass through the list. In order to do this, a
selection sort looks for the largest value as it makes a pass and, after
completing the pass, places it in the proper location. As with a bubble
sort, after the first pass, the largest item is in the correct place.
After the second pass, the next largest is in place. This process
continues and requires :math:`n - 1` passes to sort :math:`n` items, since the
final item must be in place after the :math:`(n - 1)`-th pass.

:ref:`Figure 3 <fig_selectionsort>` shows the entire sorting process for the selection sort. On each pass,
the largest remaining item is selected and then placed in its proper
location. The first pass places 93, the second pass places 77, the third
places 55, and so on. The function is shown in
:ref:`ActiveCode 1 <lst_selectionsortcode>`.

.. _fig_selectionsort:

.. figure:: Figures/selectionsortnew.png
   :align: center

   
   Figure 3: Selection Sort: Complete



.. activecode:: lst_selectionsortcode
    :caption: Selection Sort

    def selection_sort(a_list):
        for i, item in enumerate(a_list):
            min_idx = len(a_list) - 1
            for j in range(i, len(a_list)):
                if a_list[j] < a_list[min_idx]:
                    min_idx = j
            if min_idx != i:
                a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]


    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(a_list)
    print(a_list)

.. animation:: selection_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: SelectionSortModel
   :viewer: BarViewer
   

.. For more detail, CodeLens 3 allows you to step through the algorithm.
..
..
.. .. codelens:: selectionsortcodetrace
..     :caption: Tracing the Selection Sort
..
..     def selection_sort(a_list):
..         for i, item in enumerate(a_list):
..             min_idx = len(a_list) - 1
..             for j in range(i, len(a_list)):
..                 if a_list[j] < a_list[min_idx]:
..                     min_idx = j
..             if min_idx != i:
..                 a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]
..
..     a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
..     selection_sort(a_list)
..     print(a_list)

You may see that the selection sort makes the same number of comparisons
as the bubble sort and is therefore also :math:`O(n^{2})`. However,
due to the reduction in the number of exchanges, the selection sort
typically executes faster in benchmark studies. In fact, for our list,
the bubble sort makes 20 exchanges, while the selection sort makes only
8.


.. admonition:: Self Check

   .. mchoice:: question_sort_2
      :correct: d
      :answer_a: [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
      :answer_b: [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
      :answer_c: [11, 7, 12, 14, 1, 6, 8, 18, 19, 20]
      :answer_d: [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
      :feedback_a: Selection sort is similar to bubble sort (which you appear to have done) but uses fewer swaps
      :feedback_b: This looks like an insertion sort.
      :feedback_c: This one looks similar to the correct answer but instead of swapping the numbers have been shifted to the left to make room for the correct numbers.
      :feedback_d: Selection sort improves upon bubble sort by making fewer swaps.

      Suppose you have the following list of numbers to sort:
      [11, 7, 12, 14, 19, 1, 6, 18, 8, 20] which list represents the partially sorted list after three complete passes of selection sort?


