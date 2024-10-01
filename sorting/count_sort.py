def get_max(arr):
    max = float('-inf')
    for i in arr:
        if i > max:
            max = i
    return max

def count_sort(arr):
    max = get_max(arr)
    count_arr = [0] * (max+1)
    while len(arr) > 0:
        mum = arr.pop(0)
        count_arr[mum] += 1

    
    for i in range(len(count_arr)):
        while(count_arr[i] > 0):
            arr.append(i)
            count_arr[i] -= 1
            
    return arr

if __name__ == "__main__":
    arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
    sorted = count_sort(arr)
    print(sorted)