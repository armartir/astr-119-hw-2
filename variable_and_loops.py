import numpy as np #Crediting Professor Brant Robertson

def main():
	i = 0
	n = 10
	x = 119.0


	y = np.zeros(n,dtype=float) #made a quick array

	for i in range(n):
		y[i] = 2.0 * float(i) + 1.0 

	for y_element in y:
		print(y_element)

if __name__ == "__main__":
	main()
