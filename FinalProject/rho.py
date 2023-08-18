import numpy as np
import array as arr

def numpy_resize(col, row, rank, array):
    return np.resize(array, (rank, row, col))
    
def resize(col, row, rank, array):
    new_array = []
    # iterate through each rank, representing an index in the array of matrices
    for r in range(rank):
        # each rank is an array of arrays  
        inner_array = []
        # iterate through each row in the matrix in the current rank
        for i in range(row):
            row_array = []
            # iterate through each column in the matrix in the current rank
            for j in range(col):
                # calculate the index of the element in the original array
                index = r * row * col + i * col + j
                # append the element to the row array; use modulo to wrap around 
                row_array.append(array[index % len(array)])
            # append the row array to the inner array at current rank
            inner_array.append(row_array)
        # append the inner array to the new array
        new_array.append(inner_array)

    return new_array

# print resized array to look similar to NumPy.resize()
def print_Array(array):
    print("[", end="")
    rank = 1
    for matrix in array:
        print("[", end="")
        for row in matrix:
            # do not print space if it sthe first row
            if row != matrix[0]:
                print(" ", end="")
            print(row)
        print("]")
        print("end of rank", rank)
        if (rank != len(array)):
            print()
        rank += 1
    print("]")
    print()

list = [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1]
list2 = [5, 4, 3, 2, 1]

# creates a contiguous array of 9 integers
# create an array of both char and int
a = arr.array('i', list2)
# prompt user for the dimensions of the array and rank
col = input("Enter the number of cols: ")
# if enter is pushed without entering a value, default to 1
if col.strip(): 
    col = int(col)
else:
    col = 1
row = input("Enter the number of rows: ")
#if enter is pushed without entering a value, default to 1
if row.strip():
    row = int(row)
else:
    row = 1
rank = input("Enter the rank: ")
#if enter is pushed without entering a value, default to 1
if rank.strip():
    rank = int(rank)
else:
    rank = 1

# prints the array before resizing
print("Before resizing: \n", a)

# create a copy of the array for numpy_resize()
numpy_a = a
# resize the array using numpy_resize()
numpy_a = numpy_resize(col, row, rank, numpy_a)
# prints the array after resizing
print("After resizing with NumPy: \n", numpy_a)
print()

# create a copy of the array for resize()
fakenewsarray = a
# resize the array using resize()
fakenewsarray = resize(col, row, rank, a)
# prints the array after resizing
print("After resizing with resize(): \n")
#print(fakenewsarray)
print_Array(fakenewsarray)
