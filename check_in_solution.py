def main():     #O am going to give credit to Brant Robertson for providing 
				#this code to have his students learn about iteration. 
	i = 0		#integer i = 0
	x = 119.0	# x = 119.0
	for i in range(120):
		if i % 2 == 0:
			x = x + 3.0
		else:
			x = x - 5.0
	s = "The value of x is x = %3.2e" % x
	print(s)

if __name__ == "__main__":
	main()
