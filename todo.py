import os, math,termios, tty, sys, select, json, datetime, calendar
def todoout(todo,selected):
	todoarray = []
	i = 1
	for item in todo:
		6 == 6 
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





def addevent(listin):
	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:__________________                                   ║  Please enter the     ║")
	print("║                                                            ║  name of this list    ║")
	print("║  Urgency:___                                               ║  entry.               ║")
	print("║                                                            ║                       ║")    
	print("║  Due Date:_________________                                ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Blurb:________________                                    ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:___________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	name = input(">")
	urgency = -1
	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║  Please enter the     ║")
	print("║                                                            ║  urgency of this      ║")
	print("║  Urgency:___                                               ║  list entry.          ║")
	print("║                                                            ║  The lower the number ║")    
	print("║  Due Date:_________________                                ║  the higher the       ║")
	print("║                                                            ║  priority.            ║")
	print("║  Category:______________                                   ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Blurb:________________                                    ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:___________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")    
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	urgency = int(input(">"))
	i=1
	
	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ due date of this      ║")
	print("║  Urgency:" + str(urgency) + " "*(49) +"║ list entry.           ║")
	print("║                                                            ║ Use DD-MM-YYYY format ║")    
	print("║  Due Date:_________________                                ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Blurb:________________                                    ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:___________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	duedate = input(">")


	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ category of this      ║")
	print("║  Urgency:" + str(urgency) + " "*(49) +"║ list entry.           ║")
	print("║                                                            ║                       ║")    
	print("║  Due Date:" + duedate + " "*(49-len(duedate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Blurb:________________                                    ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:___________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	cat = input(">")    

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter a short  ║")
	print("║                                                            ║ description of this   ║")
	print("║  Urgency:" + str(urgency) + " "*(49) +"║ list entry.           ║")
	print("║                                                            ║                       ║")    
	print("║  Due Date:" + duedate + " "*(49-len(duedate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category: " + cat + " "*(48-len(cat)) + "║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Blurb:________________                                    ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:___________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	blurb = input(">")  

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter a long   ║")
	print("║                                                            ║ description of this   ║")
	print("║  Urgency:" + str(urgency) + " "*(49) +"║ list entry.           ║")
	print("║                                                            ║                       ║")    
	print("║  Due Date:" + duedate + " "*(49-len(duedate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category: " + cat + " "*(48-len(cat)) + "║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Blurb: " + blurb + " "*(51-len(blurb)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:___________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	desc = input(">") 

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Urgency:" + str(urgency) + " "*(49) +"║                       ║")
	print("║                                                            ║                       ║")    
	print("║  Due Date:" + duedate + " "*(49-len(duedate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category: " + cat + " "*(48-len(cat)) + "║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Blurb: " + blurb + " "*(51-len(blurb)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:" + desc[:53] + " "*(53-len(desc)) + "║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlstodo()
	listin.append([name,blurb,urgency,duedate,cat,desc,False])
	return listin

	
def controlstodo():
	print("╠════════════════════════════════════════════════════════════╩═══════════════════════╣")
	print("║ CONTROLS:                                                                          ║")
	print("║  follow the instructions on the side panel, including instructions on formatting.  ║")
	print("║                                                                                    ║")
	print("╚════════════════════════════════════════════════════════════════════════════════════╝")