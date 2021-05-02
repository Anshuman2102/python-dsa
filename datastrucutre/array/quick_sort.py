"""
Quicksort Running Time:
Quick sort average case is O(n log n
Worse case is O(log n2)
    O(n) * O(n) = O(n2)
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

array = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]
print(quicksort(array)) 

