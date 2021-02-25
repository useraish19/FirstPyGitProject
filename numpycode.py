import numpy as np

n1 = np.array([1, 2, 3, 4, 5])
print("n1:\n", n1)


n2 = np.array([[1, 2], [2, 3], [3, 4]])
print("n2:\n", n2)

n3 = np.zeros((2, 2))
print("n3:\n", n3)

n4 = np.full((3, 3), 10)
print("n4:\n", n4)

n5 = np.arange(10, 20)
print("n5:\n", n5)

n6 = np.arange(10, 50, 5)
print("n6:\n", n6)

n7 = np.random.randint(1, 100, 10)
print("n7:\n", n7)

print("n4 Shape:\n", n4.shape)

n8 = np.array([6, 7, 8, 9, 10])
print("n1n8 vertical stack:\n", np.vstack((n1, n8)))
print("n1n8 Horizontal stack:\n", np.hstack((n1, n8)))
print("n1n8 column stack:\n", np.column_stack((n1, n8)))

n9 = np.array([2, 4, 6, 8, 10])

print("Intersect array:", np.intersect1d(n1, n9))
print("Difference array:", np.setdiff1d(n1, n9))
print("Difference array:", np.setdiff1d(n9, n1))

print("Sum array(axis 0):", np.sum([n1, n8], axis=0))
print("Sum array(axis 1):", np.sum([n1, n8], axis=1))

print("n1:", n1)
n1 = n1 + 1
print("addition +1:", n1)
n1 = n1 - 1
print("Subtraction -1:", n1)
n1 = n1 * 2
print("Multiplication *2:", n1)
n1 = n1 / 2
print("Divide /2:", n1)

print("Mean:\n", np.mean(n1))
print("Median:\n", np.median(n1))
print("Std dev:\n", np.std(n1))

print("n1 + n8:\n", n1 + n8)

a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a2 = np.array([2, 5, 8])
a3 = np.array([3, 6, 9])
print("a1 + a2:\n", a1 + a2)
print("a1 shape, a2 shape:\n", a1.shape, a2.shape)
a1.shape = (3, 3)
print("a1", a1)
a2.shape = (3, 1)
print("a2", a2)
a3.shape = (1, 3)
print("a1 + a3:", a1 + a3)
print("a1:", a1)
print("a1[0]:", a1[0])
print("a1[:,2]:", a1[:, 2])
print("a1[-1:]:", a1[-1:])
print("a1 Transpose:", a1.transpose())

a4 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("a1.dot(a4):", a1.dot(a4))
print("a4.dot(a1):", a4.dot(a1))