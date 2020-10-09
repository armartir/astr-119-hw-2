import numpy as np #I wanted to give credit to Grant Robertson
import sys

def expo(x):
	return np.exp(x)

def show_expo(n):
	for i in range(n):
		print(expo(float(i)))

def main():
	n = 10
	if(len(sys.argv) > 1):
		n = int(sys.argv[1])
	print("The value of n is", n)
	show_expo(n)

if __name__ == "__main__":
	main()