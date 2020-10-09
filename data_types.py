import numpy as np  #I wanted to give credit to Professor Grant Robertson 

i = 10
print("The data type of i is ", type(i))

a_i = np.zeros(i,dtype=int)
print("The data type of a_i is ", type(a_i))
print("The data type of a_i[0] is ", type(a_i[0]))

x = 119.0
print("The data type of x is ", type(x))

y = 1.19e2
print("The data type of y is ", type(y))

z = np.zeros(i, dtype=float)
print("The type of z is: ", type(z))
print("The type of z[0] is: ", type(z[0]))

d = np.zeros((2,2), dtype=(float))
d[0,0] = 1.0
d[1,1] = 0.1
print(d) 
