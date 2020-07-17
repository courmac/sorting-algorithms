'''
NOTE: functions heapSort and quickSort, imported have NOT been re-named in
      their original respective modules from which they are imported.
      Thus, for the sake of necessary consistency in the test code at the end,
      which iterates through a list of function names (Python references,
      actually), and because quickSort requires three parameters, additional
      "wrapper" functions are provided, make all sort function interfaces
      consistent.


EX. SESSION

Bubble Sort
Original: [9, 13, 12, 0, 8, 6, 5, 7, 2, 3, 14, 10, 1, 11, 4]
Sorted:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Selection Sort
Original: [9, 13, 12, 0, 8, 6, 5, 7, 2, 3, 14, 10, 1, 11, 4]
Sorted:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Insertion Sort
Original: [9, 13, 12, 0, 8, 6, 5, 7, 2, 3, 14, 10, 1, 11, 4]
Sorted:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Merge Sort
Original: [9, 13, 12, 0, 8, 6, 5, 7, 2, 3, 14, 10, 1, 11, 4]
Sorted:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Heap Sort
Original: [9, 13, 12, 0, 8, 6, 5, 7, 2, 3, 14, 10, 1, 11, 4]
Sorted:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Quick Sort
Original: [9, 13, 12, 0, 8, 6, 5, 7, 2, 3, 14, 10, 1, 11, 4]
Sorted:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
*****************************************************************************'''

from HeapSort import *
from QuickSort import *


def quick_sort(A): return quickSort(A, 0, len(A)-1)   # Wrapper for quickSort()
def heap_sort(A): return heapSort(A)                 # Wrapper for heapSort()

# ===============================================================================


def selection_sort(A):
    for i in range(len(A)-1, -1, -1):
        iMax = i
        for j in range(i):
            if A[j] > A[iMax]:
                iMax = j
        A[iMax], A[i] = A[i], A[iMax]
    return A


def insertion_sort(X):
    n = len(X)
    for end in range(1, n):        # Each pass starts here
        new = X[end]               # Pull out element [end] to make room
        insPt = end                # Where we will eventually insert above value
        while (insPt > 0 and X[insPt-1] > new):     # Proceed down the list:
            X[insPt] = X[insPt-1]  # move data up
            insPt = insPt - 1  # insertion point
        X[insPt] = new                              # Put 'new' in here
    return X


def bubble_sort(L):
    for end in range(len(L), 0, -1):
        for i in range(end-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
    return L


def merge_sort(A):
    if len(A) < 2:
        return A
    mid = len(A)//2
    L, R = merge_sort(A[:mid]),  merge_sort(A[mid:])

    Z = []                              # Merged list to be returned
    while len(L) > 0 and len(R) > 0:
        Z.append(L.pop(0) if L[0] < R[0] else R.pop(0))  # pop() takes TIME !
    Z += L + R
    return Z


# ===============================================================================
if __name__ == '__main__':
    from random import sample
    N = 15
    data = sample(range(N), N)

    # Verify each sort function with a copy of the same original random data:
    for fn in [bubble_sort, selection_sort, insertion_sort,
               merge_sort,  heap_sort,      quick_sort]:
        # Display the sort function name, show data before and after sorting
        print(f"\n{fn.__name__.replace('_', ' ').title()}")
        print(f"Original: {data}\nSorted:   {fn(data.copy())}")
