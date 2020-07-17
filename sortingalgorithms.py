from random import*
import datetime
from HeapSort  import *
from QuickSort import *


class Sorts:
    
    def __init__(self, size):
        self._start = 0
        self._end = 0
        self._size = size
        self._calls = 0  #number of recursive calls
        self._ops = 0  # number of array operations
        self._space = 0 #extra spaces used
        
    def __repr__(self):
        time = self._end - self._start
        time = time.total_seconds()
        time = '%.8f' % time        
        printout = ''
        printout += 'Array Operations: '+ str(self._ops) + '\nRecursive Calls: ' + str(self._calls) + '\nExtra Space: ' + str(self._space) + '\nElapsed Time: ' + time
        return printout
    
    
    def quick_sort(self, A):  return self.quickSort(A, 0, len(A)-1)   # Wrapper for quickSort()
    def heap_sort(self, A):   return self.heapSort(A)                 # Wrapper for heapSort()
    
    #===============================================================================
    
    def selection_sort(self,A): # From Cmpt101
        self._start = datetime.datetime.now() # start time
        self._space += 3
        for i in range(len(A)-1, -1, -1):
            self._ops += 1
            iMax = i
            self._ops += 1
            for j in range(i):
                self._ops += 1
                if A[j] > A[iMax]:
                    self._ops += 1
                    iMax = j
                    self._ops += 1
            A[iMax], A[i] = A[i], A[iMax]
            self._ops += 1
        self._end = datetime.datetime.now() # end time
        return A 
    
    def insertion_sort(self, X):                              # From Cmpt101
        n = len(X)
        for end in range(1, n):        # Each pass starts here
            new = X[end]               # Pull out element [end] to make room
            insPt = end                # Where we will eventually insert above value
            while (insPt > 0 and X[insPt-1] > new):     # Proceed down the list:
                X[insPt] = X[insPt-1]                   #   move data up
                insPt = insPt - 1                       #     insertion point
            X[insPt] = new                              # Put 'new' in here
        return X
    
    def bubble_sort(self,L):# From Cmpt103
        for end in range(len(L), 0, -1):
            for i in range(end-1):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
        return L 
    
    def merge_sort(self, A):  # From Cmpt103
        self._start = datetime.datetime.now() # start time
        if len(A) < 2:  return A
        self._ops += 1        
        self._calls +=1
        mid = len(A)//2
        self._ops += 1  
        L, R = self.merge_sort(A[:mid]),  self.merge_sort(A[mid:])
        self._space += 2
        self._ops += 1  
        self._calls += 1
    
        Z = []                              # Merged list to be returned
        while len(L) > 0 and len(R) > 0:
            self._ops += 1  
            self._calls += 1
            Z.append( L.pop(0) if L[0] < R[0]  else  R.pop(0) ) # pop() takes TIME !
            self._space += 1
            self._ops += 1  
        Z += L + R
        self._ops += 1  
        self._end = datetime.datetime.now() # end time
        return Z 
    #-----------------------------------------------
    #---------------- Heap Sort -------------------
    
    def swapDown(self, myArray, last) :
        insPt = 0
        done = False
        while (not done and ((2*insPt+1) <= last)):
            self._ops += 1
            bigChild = 2*insPt + 1
            if ((bigChild+1) <= last and
                myArray[bigChild+1] > myArray[bigChild]) :
                self._space += 1
                self._ops += 1
                bigChild += 1
            if myArray[insPt] < myArray[bigChild] :
                self._space += 1
                self._ops += 1
                myArray[insPt], myArray[bigChild] = \
                    myArray[bigChild], myArray[insPt]
                self._ops += 1
                insPt = bigChild
            else:
                done = True
                
    def mergeHeaps(self, myArray, rt) :
        insPt = rt
        done = False
        while (not done and ((2*insPt+1) < len(myArray))):
            self._ops += 1
            bigChild = 2*insPt + 1
            if ((bigChild+1) < len(myArray) and
                myArray[bigChild+1] > myArray[bigChild]) :
                self._space += 1
                self._ops += 1
                bigChild += 1
            if myArray[insPt] < myArray[bigChild] :
                self._space += 1
                self._ops += 1
                myArray[insPt], myArray[bigChild] = \
                    myArray[bigChild], myArray[insPt]
                insPt = bigChild
                self._ops += 1
            else:
                done = True
                
    def buildHeap(self, myArray) :
        lastChild = len(myArray) - 1
        self._ops += 1
        for i in range((lastChild-1)//2, -1, -1): #(lastChild-1)//2 parent of lastChild
            self._ops += 1
            mergeHeaps(myArray,i)
        
    def heapSort(self, myArray) :
        self._start = datetime.datetime.now() # start time
        buildHeap(myArray)
        self._space += 1
        for i in range(len(myArray)-1,0,-1) :
            self._ops += 1
            myArray[0],myArray[i] = myArray[i],myArray[0]
            self._space += 1
            self._ops += 1
            swapDown(myArray,i-1)
            
            self._end = datetime.datetime.now() # end time
        return myArray
    
    #-----------------------------------------------
    #---------------- Quick Sort -------------------
    
    def partition(self, array,first,last) :
        #print("first:", first, "last:", last)
        big = first + 1
        small = last
        pivot = array[first]
        self._space += 3
        while (big <= small) :
            self._ops += 1  
            while (big <= last and array[big] <= pivot) :
                self._ops += 1  
                big += 1
            while array[small] > pivot :
                self._ops += 1  
                small -= 1
            if big < small :
                self._ops += 1  
                array[small], array[big] = array[big], array[small]
                self._ops += 1  
        array[first], array[small] = array[small], array[first]
        self._ops += 1  
        return small
    
    def quickSort(self, array, first, last) :
        self._start = datetime.datetime.now() # start time
        self._ops += 1  
        if first >= last :
            self._ops += 1  
            self._calls += 1
            return
        pivLoc = partition(array,first,last)
        self._ops += 1  
        
        quickSort(array, first, pivLoc-1)
        self._calls += 1
        self._ops += 1  
        quickSort(array, pivLoc+1, last)
        self._ops += 1  
        self._calls += 1
        self._end = datetime.datetime.now() # end time
        return array
    
    #-----------------------------------------------
    #-----------------------------------------------   
    
    def sort(self, sort_type, data):
        # sort data
        sort_type = sort_type.lower()
        if sort_type == 'quicksort':
            quicksorted = self.quick_sort(data.copy())
            print('Quick Sorted: ')         
            return quicksorted

        elif sort_type == 'mergesort':
            mergesorted = self.merge_sort(data.copy())
            print('Merge Sorted')
            return mergesorted
        
        elif sort_type == 'insertionsort':
            insertsorted = self.insertion_sort(data.copy())
            print('Insertion Sorted: ')
            return insertsorted
        
        elif sort_type == 'selectionsort':
            selectionsorted = self.selection_sort(data.copy())
            print('Selection Sorted: ')
            return selectionsorted
        
        
        
        else:
            print('Sort type must be merge, insertion, bubble, selection, quick or heap.')
            
        return
    
    def save(self, filename):
        '''Reads what's in the repr and writes it into a file'''
        f = open('filename', 'w')
        f.write(self.__repr__) #writes what is returned from __repr__
        
        f.close()
        return f   
    
    def test_select(self):
        '''Runs selction sort on four data sizes'''
        N = [10, 100, 1000, 10000]
        for n in N:
            data = sample(range(n), n) 
            self.selection_sort(data)
            print()
            print('Selection Sort ----- Data Size : ', n)
            print(self)
            
            self._calls = 0
            self._ops = 0 
            self._space = 0
        print('--------------------------------')
        self._calls = 0
        self._ops = 0  
        self._space = 0
        return   
    
    
    def test_merge(self):
        '''Runs merge sort on four data sizes'''
        N = [10, 100, 1000, 10000]
        for n in N:
            data = sample(range(n), n)
            self.merge_sort(data)
            print()
            print('Merge Sort ----- Data Size : ', n)
            print(self)
            self._calls = 0
            self._ops = 0  
            self._space = 0
        print('--------------------------------')
        self._calls = 0
        self._ops = 0  
        self._space = 0
        return
    
    def test_quick(self):
        N = [10, 100, 1000, 10000]
        for n in N:
            data = sample(range(n), n)
            self.quick_sort(data)
            print()
            print('Quick Sort ----- Data Size : ', n)
            print(self)
            self._calls = 0
            self._ops = 0   
            self._space = 0
        print('--------------------------------')
        self._calls = 0
        self._ops = 0  
        self._space = 0
        return
    
    def test_heap(self):
        N = [10, 100, 1000, 10000]
        for n in N:
            data = sample(range(n), n)
            self.heap_sort(data)
            print()
            print('Heap Sort ----- Data Size : ', n)
            print(self)
            self._calls = 0
            self._ops = 0  
            self._space = 0
        print('--------------------------------')
        self._calls = 0
        self._ops = 0  
        self._space = 0
        return    
#===============================================================================
#===============================================================================

    
def main():
    
    t = 15
    test = sample(range(t), t)
    s = Sorts(t)
    for fn in [s.selection_sort, s.insertion_sort, s.bubble_sort, s.merge_sort, s.quick_sort, s.heap_sort]: 
             
        print(f"\n{fn.__name__.replace('_', ' ').title()}")
        print("Original: ", test)    
        print()
        print()
    
    
    
    s.test_select()       
    s.test_merge()    
    s.test_quick()
    s.test_heap()
    
        

        #print(f"\n{fn.__name__.replace('_', ' ').title()}") 
        #print()
        #N = [10, 100, 1000, 10000]
        #for n in N:
            #data = sample(range(n), n) 
            #done = fn(data.copy())
            #length = s.get_time(fn, data)
            #print('\tData Size',n)
            #print('Array Operations: ',  '\t', s._ops)
            #print('Recursive Calls: ', '\t', s._calls)
            #print('Extra Space: ', '\t\tspace')
            #print('Elapsed Time: ','\t\t', length)  
            #print('----------------------------------')
            #s._calls = 0
            #s._ops = 0 
        #s._calls = 0
        #s._ops = 0                             
    
    '''
    for fn in [ s.bubble_sort, s.selection_sort, s.insertion_sort, 
                s.merge_sort,  s.heap_sort,      s.quick_sort    ]:
        # Display the sort function name, show data before and after sorting
        print(f"\n{fn.__name__.replace('_', ' ').title()}")
        print(f"Original: {data}\nSorted:   {fn(data.copy())}")
        print('****************here*******************')    
    '''
    return 

if __name__ == '__main__':
    main()