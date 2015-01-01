Quicksort In-place
==================
### Problem Statement
The previous version of Quicksort was easy to understand, but it was not optimal. It required copying the numbers into other arrays, which takes up space and time. To make things faster, one can create an "in-place" version of Quicksort, where the numbers are all sorted within the array itself.

### Challenge 
Create an in-place version of Quicksort. Also, always select the last element in the 'sub-array' as a pivot. Partition the left side and then the right side of the array. Print out the whole array at the end of every partitioning method.

### Input Format 
There will be two lines of input:
n - the size of the array   
ar - the n numbers of the array   

### Output Format 
Print the entire array on a new line at the end of every partitioning method.
### Constraints 
1<=n<=5000    
-10000<=x<= 10000 , x ∈ ar    
There are no duplicate numbers.

### Sample Input   
    7  
    1 3 9 8 2 7 5
### Sample Output   
    1 3 2 5 9 7 8 
    1 2 3 5 9 7 8 
    1 2 3 5 7 8 9 
### Explanation    
The 5 is initally selected as the pivot, and the array is partitioned as shown in the diagram. The left side is partitioned next, with the 2 as the pivot. Finally the right side is partitioned, with the 8 as the pivot. The entire array is now sorted.