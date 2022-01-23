# Data: Quiz 1 Preparation

 The Quiz will be composed of 6 questions:
 1. a mix of True/False, Multiple Choice, Multi-Select, and Matching question styles
 2. Please be prepared to inspect a few code snippets and answer short questions regarding those. 
 3. Essential concepts will be asked regarding Numpy, Matplotlib, and Pandas 
 4. as well as interpretation of some simple plots (line, scatter, histograms, violin, and box plots).

# Numpy

Basic Concepts:
```
▷ Numpy Array -> ndarray
○ a grid of values
○ all of the same type
○ it is indexed by a tuple of nonnegative integers

▷ Rank
○ Number of dimensions
a.ndim

▷ Shape
○ a tuple of integers giving the size of the array along each dimension
a.shape

import numpy as np

# You can reshape your array dimensions using the reshape function
d = b.reshape(3, 2)

indexing: Positions in numpy arrays can be accessed or modified using nonnegative integers.
a[0]
a[0,0]     # 2Dimensional numpy array
```
Arange: This function creates an array within a range with regularly incrementing values.
```
a = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
np.arange(2, 10, dtype=float) # [2. 3. 4. 5. 6. 7. 8. 9.]
np.arange(2, 3, 0.1) #[2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9]
```
Linspace: This function will create arrays with a specified number of elements, and spaced equally between the specified beginning and end values.
```
np.linspace(1,4,7) #start, stop, number of list :[1.,  1.5 ,2.,  2.5, 3.,  3.5, 4. ]
```
zeros, ones: Creates an array with the desired shape with all elements equal to 0 or 1, respectively.
```
np.zeros((2, 2)) 
np.ones((5, ))   //[1., 1., 1., 1., 1.]
```
full, random: Creates an array with the desired shape with all elements equal to a specified value or randomly, respectively.
```
np.full((3, 2), 7)        //shape(3,2) full of 7                      
np.random.random((2, 3))   //shape(2,3) with random number
```
slicing: provide parameters separated by a colon : (start:stop:step) directly to the array.
```
np.arange(9)  # [0 1 2 3 4 5 6 7 8]
a[2:7:2]     # [2 4 6]
a[2:8]       # [2 3 4 5 6 7]
```

1. A mask allows you to filter your data based on more complicated criteria.
   A mask is an array with the same shape as your data, but instead of holding your values, it will hold boolean values.
   ```
   a=np.linspace(1,50,24, dtype=int).reshape(6,4)
   mask= a % 4 == 0      //array hold boolean values
   a[mask]               //list hold number in the arry matched mask
   ```
2. Transpose: every element's row and column indices are swapped
   ```
   a.T
   a.transpose()
   ```
3. Sorting: specifies the way to arrange data in a particular order
   ```
   np.sort(a)
   np.sort(a, axis=None) //flatten the array
   np.sort(a, axis=0) // ↓ 
   np.sort(a, axis=1) // →
   
   np.argsort(a) // display indexes array →
   ```
4. Concatenate: function can be used to concatenate two arrays either row-wise or column-wise
   ```
   concatenate((a,b)) //default axis=0 ↓ 
   concatenate((a,b), axis=1) //→
   concatenate((a,b), axis=None) //flatten the array and concatenate
   ```
5. Append: add values to the <span style="color:red"> **end** </span> of a numpy array
   ```
   np.append(a, [2])
   np.append(a, b)     // two lists add together
   np.append(a, b, axis=0) // two arrays add together↓
   np.append(a, b, axis=1) // two arrays add together→
   ```
6. Stacking: 
   the hstack function is used to stack the sequence of input arrays horizontally (i.e., column wise) to make a single array
   ```
   np.hstack((a,b)) // it is like horizontal concatenation
   np.concatenate((a,b), axis=1)
   ```
   the vstack function is used to stack the sequence of input arrays vertically (i.e., row wise) to make a single array.
   ```
   np.vstack((a,b)) // it is like horizontal concatenation
   np.concatenate((a,b), axis=0)
   ```
7. Union: the **union1d** function returns a unique and sorted array with values that are in the both of two input arrays
   ```
   np.union1d(a,b)  //a, b can be different shape of array, output is a list
   ```
8. Aggregation: standard deviation, variance, argmin, argmax, percentile, cumprod, cumsum, and corrcoef
   
   min returns the min of a numpy array
   
   argmin returns the min index of a numpy array
   
   mean(average) compute the arithmetic mean along the specified axis
   
   std calculates the standard deviation
   
   sum of array elements over a given axis
   ```
   a.min()              // output is one min number
   a.min(axis=0)       //↓ a is array output is mix number list
   a.argmin(axis=0).   //↓ a is array output is index list
   
   np.mean(a)
   np.mean(a, axis=0)
   np.mean(a, axis=1)
   ```


# Matplotlib

# Pandas

# Line, Scatter, Histograms

# Violin, and Box Plots
