from random import *


def partition(array, first, last):
    #print("first:", first, "last:", last)
    big = first + 1
    small = last
    pivot = array[first]
    while (big <= small):
        while (big <= last and array[big] <= pivot):
            big += 1
        while array[small] > pivot:
            small -= 1
        if big < small:
            array[small], array[big] = array[big], array[small]
    array[first], array[small] = array[small], array[first]
    return small


def quickSort(array, first, last):
    if first >= last:
        return
    pivLoc = partition(array, first, last)

    quickSort(array, first, pivLoc-1)
    quickSort(array, pivLoc+1, last)
    return array


if __name__ == '__main__':
    print(f"Quick Sort - Quick check")
    L = sample(range(15), 15)
    print(f"List:   {L}\nSorted: {quickSort(L.copy(), 0, len(L)-1)}")
    # Ex.  List:   [4, 8, 12, 5, 3, 7, 0, 10, 14, 2, 6, 1, 11, 13, 9]
    #      Sorted: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
