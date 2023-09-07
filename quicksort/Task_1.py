# быстрая сортировка

from random import randint

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # list comprehension («генератора списка»)
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

list_1 = [randint(1,20) for _ in range(50)]
print(list_1)
print(quicksort(list_1))

str