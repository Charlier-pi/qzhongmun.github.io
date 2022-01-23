# Data: Quiz 1 Preparation

 The Quiz will be composed of 6 questions:
 1. a mix of True/False, Multiple Choice, Multi-Select, and Matching question styles
 2. Please be prepared to inspect a few code snippets and answer short questions regarding those. 
 3. Essential concepts will be asked regarding Numpy, Matplotlib, and Pandas 
 4. as well as interpretation of some simple plots (line, scatter, histograms, violin, and box plots).

# Numpy

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
