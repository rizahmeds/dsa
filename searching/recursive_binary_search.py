def binary_search(arr, search, start, end):
    if start >= end:
        mid = (start+end)//2
        if arr[mid] == search:
            return mid
        elif arr[mid] < search:
            start = mid + 1
            return binary_search(arr, search, start, end)
        else: 
            end = mid - 1
            return binary_search(arr, search, start, end)
    else:
        return -1
    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    search = 13
    end = len(arr)-1
    start = 0
    index = binary_search(arr, search, start, end)
    if index >= 0:
        print(f'Value {search} found at {index} index.')
    else:
        print(f'Value {search} not found in array.')