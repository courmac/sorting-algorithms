def swapDown(myArray, last):
    insPt = 0
    done = False
    while (not done and ((2*insPt+1) <= last)):
        bigChild = 2*insPt + 1
        if ((bigChild+1) <= last and
                myArray[bigChild+1] > myArray[bigChild]):
            bigChild += 1
        if myArray[insPt] < myArray[bigChild]:
            myArray[insPt], myArray[bigChild] = \
                myArray[bigChild], myArray[insPt]
            insPt = bigChild
        else:
            done = True


def mergeHeaps(myArray, rt):
    insPt = rt
    done = False
    while (not done and ((2*insPt+1) < len(myArray))):
        bigChild = 2*insPt + 1
        if ((bigChild+1) < len(myArray) and
                myArray[bigChild+1] > myArray[bigChild]):
            bigChild += 1
        if myArray[insPt] < myArray[bigChild]:
            myArray[insPt], myArray[bigChild] = \
                myArray[bigChild], myArray[insPt]
            insPt = bigChild
        else:
            done = True


def buildHeap(myArray):
    lastChild = len(myArray) - 1
    for i in range((lastChild-1)//2, -1, -1):  # (lastChild-1)//2 parent of lastChild
        mergeHeaps(myArray, i)


def heapSort(myArray):
    buildHeap(myArray)
    for i in range(len(myArray)-1, 0, -1):
        myArray[0], myArray[i] = myArray[i], myArray[0]
        swapDown(myArray, i-1)
    return myArray


if __name__ == '__main__':
    from random import sample
    print(f"Heap Sort - Quick check")
    L = sample(range(15), 15)
    print(f"List:   {L}\nSorted: {heapSort(L.copy())}")
    # Ex.  List:   [4, 8, 12, 5, 3, 7, 0, 10, 14, 2, 6, 1, 11, 13, 9]
    #      Sorted: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
