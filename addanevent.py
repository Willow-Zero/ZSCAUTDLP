import os, math,termios, tty, sys, select, json, datetime, calendar
def entry():
	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:__________________                                   ║  Please enter the     ║")
	print("║                                                            ║  name of this event   ║")
	print("║  Urgency:___                                               ║  or list entry.       ║")
	print("║                                                            ║                       ║")    
	print("║  Start Time and Date:_________________                     ║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:__________                     ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	name = input(">")
	urgency = ""
	i=0
	while (urgency != "H" and urgency != "L" and urgency != "M" and urgency != "h" and urgency != "l" and urgency !="m"):
		print("\033c", end="")
		print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
		print("║                                                            ║                       ║")
		print("║  Name:" + name + " "*(53-len(name)) + "║  Please enter the     ║")
		print("║                                                            ║  urgency of this      ║")
		print("║  Urgency:___                                               ║  event or list entry. ║")
		print("║                                                            ║  H=high               ║")    
		print("║  Start Time and Date:_________________                     ║  L=low                ║")
		print("║                                                            ║  M=medium             ║")
		print("║  End Time and Date/Deadline:__________                     ║                       ║")
		print("║                                                            ║                       ║")
		print("║  Category:______________                                   ║                       ║")    
		print("║                                                            ║                       ║")
		print("║  Repeat Pattern:______                                     ║                       ║")
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
		controls()
		if (i == 1):
			print("Error. Please try again.")
		urgency = input(">")
		i=1
	
	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ start  date of this   ║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║ Use DD-MM-YYYY format ║")    
	print("║  Start Time and Date:_________________                     ║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:__________                     ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	stdate = input(">")

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ end  date of this     ║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║ Use DD-MM-YYYY format ║")    
	print("║  Start Time and Date:" + stdate + " "*(38-len(stdate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:__________                     ║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	endate = input(">")

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ start time of this    ║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║ Use 24 hr format      ║")    
	print("║  Start Time and Date:" + stdate + " "*(38-len(stdate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:" + endate + " "*(31-len(endate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	stime = input(">")    

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ end time of this      ║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║ Use 24 hr format      ║")    
	print("║  Start Time and Date:" + stdate + "|" + stime + " "*(37-len(stdate)-len(stime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:" + endate + " "*(31-len(endate)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	etime = input(">")    

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ category of this      ║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║                       ║")    
	print("║  Start Time and Date:" + stdate + "|" + stime + " "*(37-len(stdate)-len(stime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:" + endate + "|" + etime + "" " "*(30-len(endate)-len(etime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category:______________                                   ║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	cat = input(">")    

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ repeat pattern of this║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║                       ║")    
	print("║  Start Time and Date:" + stdate + "|" + stime + " "*(37-len(stdate)-len(stime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:" + endate + "|" + etime + "" " "*(30-len(endate)-len(etime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category: " + cat + " "*(48-len(cat)) + "║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:______                                     ║                       ║")
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
	controls()
	repattern = input(">")  

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Please enter the      ║")
	print("║                                                            ║ description of this   ║")
	print("║  Urgency:" + urgency + " "*(49) +"║ event or list entry.  ║")
	print("║                                                            ║                       ║")    
	print("║  Start Time and Date:" + stdate + "|" + stime + " "*(37-len(stdate)-len(stime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:" + endate + "|" + etime + "" " "*(30-len(endate)-len(etime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category: " + cat + " "*(48-len(cat)) + "║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:" + repattern + " "*(43-len(repattern)) + "║                       ║")
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
	controls()
	desc = input(">") 

	print("\033c", end="")
	print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║  Name:" + name + " "*(53-len(name)) + "║ Done! Switch to your  ║")
	print("║                                                            ║ preferred view!       ║")
	print("║  Urgency:" + urgency + " "*(49) +"║                       ║")
	print("║                                                            ║                       ║")    
	print("║  Start Time and Date:" + stdate + "|" + stime + " "*(37-len(stdate)-len(stime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  End Time and Date/Deadline:" + endate + "|" + etime + "" " "*(30-len(endate)-len(etime)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Category: " + cat + " "*(48-len(cat)) + "║                       ║")    
	print("║                                                            ║                       ║")
	print("║  Repeat Pattern:" + repattern + " "*(43-len(repattern)) + "║                       ║")
	print("║                                                            ║                       ║")
	print("║  Desc:" + desc + " "*(53-len(desc)) + "║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║  ________________________________________________________  ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controls()
	try:
		manip = dat[stdate]
		manip.update({name:{"starttime": stime,"enddate": endate,"endtime": etime,"priority": urgency,"desc": desc,"completion": False,"repattern": repattern}})
		print (manip)
		dat[stdate].update(manip)
		print (dat)
	except:
		dat.update({stdate:{name:{"starttime": stime,"enddate": endate,"endtime": etime,"priority": urgency,"desc": desc,"completion": False,"repattern": repattern}}}),
	

	
def controls():
	print("╠════════════════════════════════════════════════════════════╩═══════════════════════╣")
	print("║ CONTROLS:                                                                          ║")
	print("║  follow the instructions on the side panel, including instructions on formatting.  ║")
	print("║                                                                                    ║")
	print("╚════════════════════════════════════════════════════════════════════════════════════╝")
	




def save():
	f = open("list.json", "w")
	f.write(json.dumps(dat))




