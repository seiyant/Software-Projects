# student name:   Seiya Nozawa-Temchenko
# student number: 34838482

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    global testcase, sortedFirstHalf, sortedSecondHalf, SortedFullList #use main variables

    split_i = len(testcase) // 2; #index of list split

    if firstHalf:
        sortedFirstHalf = quickSort(testcase[:split_i]) #copy and sort 1st half
    else:
        sortedSecondHalf = quickSort(testcase[split_i:]) #copy and sort 2nd half

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    global testcase, sortedFirstHalf, sortedSecondHalf, SortedFullList #use main variables

    i = 0; j = 0

    while i < len(sortedFirstHalf) and j < len(sortedSecondHalf):
        if sortedFirstHalf[i] < sortedSecondHalf[j]:
            SortedFullList.append(sortedFirstHalf[i])
            i += 1
        else:
            SortedFullList.append(sortedSecondHalf[j])
            j += 1
    
    while i < len(sortedFirstHalf):
        SortedFullList.append(sortedFirstHalf[i])
        i += 1

    while j < len(sortedSecondHalf):
        SortedFullList.append(sortedSecondHalf[j])
        j += 1

def quickSort(arr: list) -> list:
    """
    Implemented from:
    https://stackoverflow.com/questions/78450781/quicksort-implementation-inclusion-vs-exclusion-a-pivot-element-during-partitio    
    """
    if len(arr) <= 1: #empty array or 1 entry
        return arr
    
    pivot = arr[len(arr) // 2] #set middle element
    #Note: middle value is more likely to minimize worst-case than first value

    left = [x for x in arr if x < pivot] #left partition
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] #right partition

    return quickSort(left) + middle + quickSort(right) #recursive sort and combination

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    sortFirstHalf = threading.Thread(target= sortingWorker, args= (True,)) #sort 1st half
    sortSecondHalf = threading.Thread(target= sortingWorker, args= (False,)) #sort 2nd half
    #Note: Thread allows to create and manage threads (setup)

    sortFirstHalf.start() #start sorts and wait sorts to finish
    sortSecondHalf.start()
    sortFirstHalf.join()
    sortSecondHalf.join()

    mergeThread = threading.Thread(target= mergingWorker) #merge threads post sort
    mergeThread.start()
    mergeThread.join()

    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)