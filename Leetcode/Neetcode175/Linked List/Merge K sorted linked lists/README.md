  ![image](https://user-images.githubusercontent.com/53051383/195201818-bc6cf580-a2f7-4a2a-81e6-8b4730d4a1f9.png)
# Solution
### Use heap to store the values of the whole linked lists in the list. Create new node for each value while popping the heap.
### It can be done without creating new nodes if instead of creating a node just modify the pointer of each node, but python's heapq won't allow node comparison when storing (value,node).
## Time Complexity O(n log n)  n-total amount of nodes
## Memory Complexity O(n)
