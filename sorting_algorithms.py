# Insertion sort
def insertion_sort(arr):
    '''
    Sort list using insertion sort.
    Return number of comparisons made.
    '''
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            comparisons += 2
            arr[j+1] = arr[j]
            j -= 1
        else:
            comparisons += 2
        arr[j+1] = key
    
    return comparisons

# Selection sort
def selection_sort(arr):
    '''
    Sort list using selection sort.
    Return number of comparisons made.
    '''
    comparisons = 0
    for i in range(len(arr)):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            comparisons += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return comparisons

# Shell sort
def shell_sort(arr):
    '''
    Sort list using shell sort.
    Return number of comparisons made.
    '''
    comparisons = 0
    gap = len(arr)//2

    while gap > 0:
        comparisons += 1
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                comparisons += 2
                arr[j] = arr[j-gap]
                j -= gap
            else:
                comparisons += 2
            
            arr[j] = temp
        gap //= 2
    
    return comparisons


# Merge sort
def merge_sort(arr):
    '''
    Sort list using merge sort.
    Return number of comparisons made.
    '''
    comparisons = 0

    if len(arr) > 1:
        comparisons += 1
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        comparisons += merge_sort(left) + merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            comparisons += 2
            if left[i] < right[i]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            comparisons += 1
            k += 1
        else:
            comparisons += 2
        
        while i < len(left):
            comparisons += 1
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            comparisons += 1
        
        while j < len(right):
            comparisons += 1
            arr[k] = right[j]
            j += 1
            k += 1
        else:
            comparisons += 1
        
    return comparisons
