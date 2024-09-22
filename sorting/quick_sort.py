def partition(arr, low, high):
    pivot = arr[high]
    ptr = low-1
    for i in range(low, high):
        if arr[i] < pivot:
            ptr += 1
            arr[i], arr[ptr] = arr[ptr], arr[i]
    arr[ptr+1], arr[high] = arr[high], arr[ptr+1]
    return ptr+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

if __name__ == "__main__":
    arr1 = [3,2,5,0,1,8,7,6,9,4]
    print(arr1)
    # result = partition(arr1)
    quicksort(arr1)

    print(arr1)