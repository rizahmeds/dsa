## Heap data structure
Heap data structure is a complete binary tree, nodes at each level are fully filled except the last level, which is filled from left to right.

## Types of Heap
**<ins>Min Heap</ins>:** All the node element should be smaller than its childern elements.

**<ins>Max Heap</ins>:** All the node element should be greater than its childern elements.

## Operation
**<ins>Heapify</ins>:** Given an array, modify the array so that it will maintain the heap properties. Heapifing array depends upon type of heap. For Min heapify all the node elments should be smaller than its childern nodes. For Max heapify all the node elments should be greater than its childern nodes.

**<ins>Insertion</ins>:** Always apppend the element at the end of the array or last available leaf node from left to right. Perform the heapify operation the heap array so that it maintains the heap properties.

**<ins>Deletion</ins>:** Delete the root element of the heap by first swapping it with the last element then delete the last element. Perform the heapify operation over the heap array so that it maintains the heap properties.



