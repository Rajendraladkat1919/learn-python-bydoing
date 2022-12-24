
Based on some condition we are taking action. Controlling real life problem.



Indentation is important in python.


if <>:

    else:



if: 

    elif:

        else:





# Loops 


1. while

```
while condition:
   <body>
```
condition is testes until condition is invalid.

1. intital value
2. loop condition
3. Updating value.
```
i=1

#loop condition
while i<= 6:
  print("coding is awesome.")
  i+=1
```


2. Range function:

# start=0 , step=1
it include number from zero and end with 1 number of given value.

start included and end is excluded. same as slice.

for i in range(5)=> 0,1,2,3,4

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |
 |  Methods defined here:
 |
 |  __bool__(self, /)
 |      self != 0
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)