import numpy as np

def my_func(matrix_1, matrix_2):
    try:
        return matrix_1 * matrix_2
    except ValueError:
        return None

my_matrix = np.identity(4)
my_second_matrix = np.identity(4)

print(my_func(my_matrix, my_second_matrix))

#this code is practice on uploading changes to github