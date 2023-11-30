def todoout(todo,selected):
	todoarray = []
	i = 1
	for item in todo:
		todostring = ""
		todostring += "- " + item[0] + ": " + item[1]
		if len(todostring) > 58:
			todoarray.append(todostring[:58])
		else:
			todoarray.append(todostring)
		if i == selected:
			todoarray[i-1] = "\033[92m" + todoarray[i-1]
			todoarray[i-1] += "\033[0m"
		i += 1
	while len(todoarray) < 20:
		addstring = ""
		if len(todoarray) == selected-1:
			addstring += "\033[92m"
		addstring += "----------------------------------------------------------"
		if len(todoarray) == selected-1:
			addstring += "\033[0m"
		todoarray.append(addstring)
	for item in range(len(todoarray)):
		while len(todoarray[item])<58:
			todoarray[item] = todoarray[item] + " "
		if item == (selected-1):
			while len(todoarray[item])<67:
				todoarray[item] = todoarray[item] + " "
	return(todoarray)
#print(todoout(todo,1))