#I wanted to give credit to Professor Grant Robertson
example_dict = {"class" : "Astr 119", "prof" : "Brant", "awesomeness" : 10}
print(type(example_dict))

course = example_dict["class"]
print(course)

example_dict["awesomeness"] *= 10

print(example_dict)

for x in example_dict.keys():
	print(x,example_dict[x])