k=0
try:
	user_array = str(input("Please enter the items, separated by commas and gaps: "))
	inputted_list_as_array = user_array.split(", ")
	delta = int(input("DELTA: "))
	min_item = int(min(inputted_list_as_array, default=0))
	a = min_item + delta

	for x in inputted_list_as_array:
		if x == str(a) :
			k+=1
	print (k)
except ValueError:
	print ("Incorrect input!")
