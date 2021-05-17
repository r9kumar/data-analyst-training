import numpy as np
from numpy import random as rd

# ROUTINES for creating NumPy arrays 
# arange, linspace, logspace, geomspace, meshgrid, ogrid, mgrid

# arange
print(np.arange(start=1, stop=10, step=3))
print(np.arange(1, 10, 3))
print(np.arange(5, dtype=float))
print(np.arange(32).reshape(4, 1, 8))
print(np.arange(48).reshape(1, 6, 8))

# linspace
# create an evenly spaced sequence in a specified interval
print(np.linspace(1,50))
# Since endpoint is false, 8 will not be included in the result
print(np.linspace(start = 2, stop = 8, num = 4, endpoint = False, retstep = True, dtype = float))

print(np.linspace(5, 50, 24, dtype=int).reshape(4, -1))

# logspace
print(np.logspace(2.0, 3.0, num=4, base=2.0))

# meshgrid
nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
print(xv)
print(yv)
xv, yv = np.meshgrid(x, y, sparse=True)  # make sparse output arrays
print(xv)
print(yv)


# >>>>>> Generating Random Values

#Generate a random float from 0 to 1:
print(rd.rand())

#Generate a 1-D array containing 5 random floats from 0 to 1:
print(rd.rand(5))

#Generate a 2-D array with 3 rows, each row containing 5 random numbers from 0 to 1:
print(rd.rand(3, 5))

#Generate a random integer from 0 to 100
print(rd.randint(100))

#Generate a 1-D array containing 5 random integers from 0 to 100:
print(rd.randint(100, size=(5)))

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
print(rd.randint(100, size=(3, 5)))

#Return one of the values in an array:
print(rd.choice([3, 5, 7, 9]))

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
print(rd.choice([3, 5, 7, 9], size=(3, 5)))
print(rd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)))
print(rd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5)))

# Draw three numbers greater than or equal to 1.0 and less than 2.0
print(rd.uniform(1.0, 2.0, 3))

# Draw three numbers from a normal distribution with mean 0.0
# and standard deviation of 1.0
print(rd.normal(0.0, 1.0, 3))

# Draw three numbers from a logistic distribution with mean 0.0 and scale of 1.0
print(rd.logistic(0.0, 1.0, 3))

# Set seed
rd.seed(0)
# Generate three random floats between 0.0 and 1.0
print(rd.random(3))