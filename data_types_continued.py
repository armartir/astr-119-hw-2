#I wanted to give credit to Professor Grant Robertson
s = "I am a String"
print("The type of s is ", type(s))

yes = True
print("The type of yes is ",type(yes))

no = False
print("The type of no is ",type(no))

alpha_list = ["a", "b", "c"]
print("The type of alpha_list is ",type(alpha_list))
print("The type of alpha_list[0] is ",type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

alpha_tuple = ("a", "d", "c")
print("The type of alpha_tuple is ",type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't add elements to tuples!")
print(alpha_tuple)
