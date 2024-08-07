import numpy as np 

myarr = np.array([3,6,32,7],np.int64)

print(myarr[1])

listarray = np.array(([1,2,3],[2,3,1],[3,1,2]))
print(listarray)

print(listarray.shape)

zeros = np.zeros((2,2))
print(zeros)

rng = np.arange(15)
print(rng)

lspace = np.linspace(1,5,4)
print(lspace)

x = [1,2,3,4,5,6,7,8,9]
arr = np.array(x)
print(x)