import os, math,termios, tty, sys, select, json, datetime, calendar, addanevent
import todo as t
dat,disp = "",""
def ensureexists():
	open("todolist.json","a").write("")
	open("list.json","a").write("")
ensureexists()
todolist = json.loads(open("todolist.json","r").read())
def loaddata():
	f = open("list.json", "r")
	return (f.read())
	
	
def controlsmenu():
	print("╠════════════════════════════════════════════════════════════╩═══════════════════════╣")
	print("║ CONTROLS:      t - to do list                   x - exit                           ║")
	print("║                p - timer                        c - calendar                       ║")
	print("╚════════════════════════════════════════════════════════════════════════════════════╝")
	
def controlstodo():
	print("╠════════════════════════════════════════════════════════════╩═══════════════════════╣")
	print("║ CONTROLS:     w - up       s - down           x - exit         r - select          ║")
	print("║               v - see completed tasks         y - add task     u - back to menu    ║")
	print("╚════════════════════════════════════════════════════════════════════════════════════╝")
	
def controlscal():	
	print("╠════════╧═══════╧════════╧═══════╧════════╧════════╧════════╩═══════════════════════╣")
	print("║ CONTROLS:    wasd to move     e - next month        r - select    m - add event    ║")
	print("║                               q - prev month        x - exit      u - menu         ║")
	print("╚════════════════════════════════════════════════════════════════════════════════════╝")
class NonBlockingConsole(object):

	def __enter__(self):
		self.old_settings = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		return self

	def __exit__(self, type, value, traceback):
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)


	def get_data(self):
		if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
			return sys.stdin.read(1)
		return False
def draw():
	print(disp)
	if disp == "c":
		calendardisp()
	if disp == "t":
		listdisp()

def save():
	with open("list.json", "w") as file:
		json.dump(dat, file)
	(open("todolist.json","w").write(json.dumps(todolist)))
def processdata(d):
	print(dat)
#	global  # 
#	return(dat)
#	try:
#		dat.update({d[2]:dat[d[2]], d[0]: {d[1], d[3], d[4], d[5], d[6], d[7], d[8]}})
#	except:
#		dat.update({d[2]: {d[0]: {d[1], d[3], d[4], d[5], d[6], d[7], d[8]}}})
def menuprint():
	print("\033c╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
	print("║                                                            ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠐⢷⣦⠀⠙⢿⣿⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠙⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣿⡄⠀⢸⡿⠋⠉⢻⣷⣤⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⠇⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣷⡀⠸⣷⡀⠀⠀⠀⠙⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⡏⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⣿⡄⠀⠀⠀⠹⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⠁⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢸⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣇⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⣾⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⡄⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⢰⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║              \033[92m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\033[0m               ║                       ║")
	print("║                                                            ║                       ║")
	print("║            Zero's Super Cool And Useful To Do              ║                       ║")
	print("║                 List Program (ZSCAUTDLP)                   ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	print("║                                                            ║                       ║")
	controlsmenu()
menuprint()
def listdisp():
	lines = t.todoout(todolist,listitem)
	try:
		print("\033c", end="")
		print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
		print("║                                                            ║                       ║")
		print("║ " + lines[0] + " ║ "+ todolist[listitem-1][0] + " "*(21-len(todolist[listitem-1][0])) +" ║")
		print("║ " + lines[1] + " ║ Priority "+ str(todolist[listitem-1][2]) + " "*(21-9-len(str(todolist[listitem-1][2]))) +" ║")
		print("║ " + lines[2] + " ║ "+ todolist[listitem-1][4] + " "*(21-len(todolist[listitem-1][4])) +" ║")
		print("║ " + lines[3] + " ║ "+ todolist[listitem-1][5][:21] + " "*(21-len(todolist[listitem-1][5])) +" ║")
		print("║ " + lines[4] + " ║ "+ todolist[listitem-1][5][21:42] + " "*(min(21,(42-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[5] + " ║ "+ todolist[listitem-1][5][42:63] + " "*(min(21,(63-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[6] + " ║ "+ todolist[listitem-1][5][63:84] + " "*(min(21,(84-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[7] + " ║ "+ todolist[listitem-1][5][84:105] + " "*(min(21,(105-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[8] + " ║ "+ todolist[listitem-1][5][105:126] + " "*(min(21,(126-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[9] + " ║ "+ todolist[listitem-1][5][126:147] + " "*(min(21,(147-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[10] + " ║ "+ todolist[listitem-1][5][147:168] + " "*(min(21,(168-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[11] + " ║ "+ todolist[listitem-1][5][168:189] + " "*(min(21,(189-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[12] + " ║ "+ todolist[listitem-1][5][189:210] + " "*(min(21,(210-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[13] + " ║ "+ todolist[listitem-1][5][210:231] + " "*(min(21,(231-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[14] + " ║ "+ todolist[listitem-1][5][231:252] + " "*(min(21,(252-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[15] + " ║ "+ todolist[listitem-1][5][252:273] + " "*(min(21,(273-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[16] + " ║ "+ todolist[listitem-1][5][273:294] + " "*(min(21,(294-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[17] + " ║ "+ todolist[listitem-1][5][294:315] + " "*(min(21,(315-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[18] + " ║ "+ todolist[listitem-1][5][315:336] + " "*(min(21,(336-(len(todolist[listitem-1][5]))))) +" ║")
		print("║ " + lines[19] + " ║ "+ todolist[listitem-1][5][336:357] + " "*(min(21,(357-(len(todolist[listitem-1][5]))))) +" ║")
		print("║                                                            ║                       ║")
		controlstodo()
	except:
		print("\033c", end="")
		print("╔════════════════════════════════════════════════════════════╦═══════════════════════╗")
		print("║                                                            ║                       ║")
		print("║ " + lines[0] + " ║                       ║")
		print("║ " + lines[1] + " ║                       ║")
		print("║ " + lines[2] + " ║                       ║")
		print("║ " + lines[3] + " ║                       ║")
		print("║ " + lines[4] + " ║                       ║")
		print("║ " + lines[5] + " ║                       ║")
		print("║ " + lines[6] + " ║                       ║")
		print("║ " + lines[7] + " ║                       ║")
		print("║ " + lines[8] + " ║                       ║")
		print("║ " + lines[9] + " ║                       ║")
		print("║ " + lines[10] + " ║                       ║")
		print("║ " + lines[11] + " ║                       ║")
		print("║ " + lines[12] + " ║                       ║")
		print("║ " + lines[13] + " ║                       ║")
		print("║ " + lines[14] + " ║                       ║")
		print("║ " + lines[15] + " ║                       ║")
		print("║ " + lines[16] + " ║                       ║")
		print("║ " + lines[17] + " ║                       ║")
		print("║ " + lines[18] + " ║                       ║")
		print("║ " + lines[19] + " ║                       ║")
		print("║                                                            ║                       ║")
		controlstodo()
	


def calendardisp():
	marker="\033[37m🮰\033[0m"
	print("\033c", end="") 
	thisdict =	{"11":{"mark":" ", "num":"  "},"12":{"mark":" ", "num":"  "},"13":{"mark":" ", "num":"  "},"14":{"mark":" ", "num":"  "},"15":{"mark":" ", "num":"  "},"16":{"mark":" ", "num":"  "},"17":{"mark":" ", "num":"  "},"21":{"mark":" ", "num":"  "},"22":{"mark":" ", "num":"  "},"23":{"mark":" ", "num":"  "},"24":{"mark":" ", "num":"  "},"25":{"mark":" ", "num":"  "},"26":{"mark":" ", "num":"  "},"27":{"mark":" ", "num":"  "},"31":{"mark":" ", "num":"  "},"32":{"mark":" ", "num":"  "},"33":{"mark":" ", "num":"  "},"34":{"mark":" ", "num":"  "},"35":{"mark":" ", "num":"  "},"36":{"mark":" ", "num":"  "},"37":{"mark":" ", "num":"  "},"41":{"mark":" ", "num":"  "},"42":{"mark":" ", "num":"  "},"43":{"mark":" ", "num":"  "},"44":{"mark":" ", "num":"  "},"45":{"mark":" ", "num":"  "},"46":{"mark":" ", "num":"  "},"47":{"mark":" ", "num":"  "},"51":{"mark":" ", "num":"  "},"52":{"mark":" ", "num":"  "},"53":{"mark":" ", "num":"  "},"54":{"mark":" ", "num":"  "},"55":{"mark":" ", "num":"  "},"56":{"mark":" ", "num":"  "},"57":{"mark":" ", "num":"  "}}
	thisdict[str(coords[0])+str(coords[1])]["mark"] = "\033[37m🮰\033[0m"
	stday = calendar.monthrange(int(yr), mn+1)[0] #MONDAY IS 0
	i = 0
	first = -1
	if stday == 0:
		first = 12
		ray = ["12", "13", "14", "15", "16", "17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57", "11"]
	if stday == 1:
		first = 13
		ray = ["13", "14", "15", "16", "17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57", "11", "12"]
	if stday == 2:
		first = 14
		ray = ["14", "15", "16", "17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57", "11", "12", "13"]
	if stday == 3:
		first = 15
		ray = ["15", "16", "17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57", "11", "12", "13", "14"]
	if stday == 4:
		first = 16
		ray = ["16", "17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57", "11", "12", "13", "14", "15"]
	if stday == 5:
		first = 17
		ray = ["17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57", "11", "12", "13", "14", "15", "16"]
	if stday == 6:
		first = 11
		ray = ["11", "12", "13", "14", "15", "16", "17", "21", "22","23", "24", "25", "26", "27", "31", "32", "33", "34","35", "36", "37", "41", "42", "43", "44", "45", "46", "47", "51", "52", "53", "54", "55", "56", "57"]
	i = 1
	for n in ray:
		if i <=  calendar.monthrange(int(yr), mn+1)[1]:
			#print(n)
			thisdict[str(n)]["num"] = str('%02d' % i)
			i += 1
			#print(i)
	selected = ""
	for n in ray:
		if (thisdict[n]["mark"] != " "):
			selected = thisdict[n]["num"]
	21 == 21
	seldate = selected + "-" + str(mn+1) + "-" + str(yr)
	list=["                     ","                     ","                     ","                     ","                     ","                     ","                     ","                     ","                     ","                     "]
	i = 0
	for n in dat:
		if (n == seldate):
			for f in  dat[n]:
				if (i < 10 and len(f)<=20):
					list[i] = "-" + f + " "*(20-len(f))
				elif (i < 10 and len(f)>20):
					list[i] = "-" + b[:20]
				i += 1
#					
#	
#	
	month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	m = int(len(month[mn])/2)
	print("╔════════╤═══════╤════════╤═══════╤════════╤════════╤════════╦═══════════════════════╗")
	if (len(month[mn])%2) == 0:
		print("║  \033[91mSUN \033[0m  │\033[91m  MON\033[0m  │  \033[91mTUE\033[0m   │ \033[91m WED\033[0m  │  \033[91mTHU \033[0m  │  \033[91mFRI\033[0m   │  \033[91mSAT \033[0m  ║ \033[92m" + " "*(8-m) + month[mn] + " " + str(yr) + " "*(8-m) + "\033[0m ║")
	else:
		print("║  \033[91mSUN  \033[0m │\033[91m  MON\033[0m  │ \033[91m TUE\033[0m   │\033[91m  WED\033[0m  │ \033[91m THU  \033[0m │  \033[91mFRI  \033[0m │  \033[91mSAT\033[0m   ║ \033[92m" + " "*(8-m) + month[mn] + " " + str(yr) + " "*(8-m) + "\033[0m║")
	print("║  " + thisdict['11']["num"] + "    │   " + thisdict['12']["num"] + "  │    " + thisdict['13']["num"] + "  │   " + thisdict['14']["num"] + "  │    " + thisdict['15']["num"] + "  │    " + thisdict['16']["num"] + "  │   " + thisdict['17']["num"] + "   ║ "+ list[0] +" ║")
	print("║        │       │        │       │        │        │        ║                       ║")
	print("║        │       │        │       │        │        │        ║ "+ list[1] +" ║")
	print("║   " + thisdict['11']["mark"] + "    │    " + thisdict['12']["mark"] + "  │     " + thisdict['13']["mark"] + "  │    " + thisdict['14']["mark"] + "  │     " + thisdict['15']["mark"] + "  │     " + thisdict['16']["mark"] + "  │    " + thisdict['17']["mark"] + "   ║                       ║")
	print("║────────┼───────┼────────┼───────┼────────┼────────┼────────╢ "+ list[2] +" ║")
	print("║   " + thisdict['21']["num"] + "   │   " + thisdict['22']["num"] + "  │    " + thisdict['23']["num"] + "  │   " + thisdict['24']["num"] + "  │    " + thisdict['25']["num"] + "  │    " + thisdict['26']["num"] + "  │   " + thisdict['27']["num"] + "   ║                       ║")
	print("║        │       │        │       │        │        │        ║ "+ list[3] +" ║")
	print("║   " + thisdict['21']["mark"] + "    │    " + thisdict['22']["mark"] + "  │     " + thisdict['23']["mark"] + "  │    " + thisdict['24']["mark"] + "  │     " + thisdict['25']["mark"] + "  │     " + thisdict['26']["mark"] + "  │    " + thisdict['27']["mark"] + "   ║                       ║")
	print("║────────┼───────┼────────┼───────┼────────┼────────┼────────╢ "+ list[4] +" ║")
	print("║  " + thisdict['31']["num"] + "    │  " + thisdict['32']["num"] + "   │   " + thisdict['33']["num"] + "   │  " + thisdict['34']["num"] + "   │   " + thisdict['35']["num"] + "   │   " + thisdict['36']["num"] + "   │   " + thisdict['37']["num"] + "   ║                       ║")
	print("║        │       │        │       │        │        │        ║ "+ list[5] +" ║")
	print("║        │       │        │       │        │        │        ║                       ║")
	print("║   " + thisdict['31']["mark"] + "    │    " + thisdict['32']["mark"] + "  │     " + thisdict['33']["mark"] + "  │    " + thisdict['34']["mark"] + "  │     " + thisdict['35']["mark"] + "  │     " + thisdict['36']["mark"] + "  │    " + thisdict['37']["mark"] + "   ║ "+ list[6] +" ║")
	print("║────────┼───────┼────────┼───────┼────────┼────────┼────────╢                       ║")
	print("║  " + thisdict['41']["num"] + "    │  " + thisdict['42']["num"] + "   │   " + thisdict['43']["num"] + "   │  " + thisdict['44']["num"] + "   │   " + thisdict['45']["num"] + "   │   " + thisdict['46']["num"] + "   │   " + thisdict['47']["num"] + "   ║ "+ list[7] +" ║")
	print("║        │       │        │       │        │        │        ║                       ║")
	print("║   " + thisdict['41']["mark"] + "    │    " + thisdict['42']["mark"] + "  │     " + thisdict['43']["mark"] + "  │    " + thisdict['44']["mark"] + "  │     " + thisdict['45']["mark"] + "  │     " + thisdict['46']["mark"] + "  │    " + thisdict['47']["mark"] + "   ║ "+ list[8] +" ║")
	print("║────────┼───────┼────────┼───────┼────────┼────────┼────────╢                       ║")
	print("║  " + thisdict['51']["num"] + "    │  " + thisdict['52']["num"] + "   │   " + thisdict['53']["num"] + "   │  " + thisdict['54']["num"] + "   │   " + thisdict['55']["num"] + "   │   " + thisdict['56']["num"] + "   │   " + thisdict['57']["num"] + "   ║ "+ list[9] +" ║")
	print("║        │       │        │       │        │        │        ║                       ║") 
	print("║   " + thisdict['51']["mark"] + "    │    " + thisdict['52']["mark"] + "  │     " + thisdict['53']["mark"] + "  │    " + thisdict['54']["mark"] + "  │     " + thisdict['55']["mark"] + "  │     " + thisdict['56']["mark"] + "  │    " + thisdict['57']["mark"] + "   ║                       ║")
	controlscal()
	



def goup():
	global listitem
	if disp == "c" and coords[0] > 1:
		coords[0] = coords[0] - 1
		print(coords)
	if disp == "t" and listitem > 1:
		listitem = listitem - 1
def godown():
	global listitem
	if disp == "c" and coords[0] < 5:
		coords[0] = coords[0] + 1
		print(coords)
	if disp == "t" and listitem < 20:
		listitem = listitem + 1
def goleft():
	if disp == "c" and coords[1] > 1:
		coords[1] = coords[1] - 1
		print(coords)
	
def goright():
	if disp == "c" and coords[1] < 7:
		coords[1] = coords[1] + 1
		print(coords)
def nextmonth():
	global mn
	global yr
	if disp == "c" and mn < 11:
		mn += 1
	elif disp == "c":
		yr += 1
		mn = 0
	draw()

def prevmonth():
	global mn
	global yr
	if disp == "c" and mn > 0:
		mn += -1
	elif disp == "c":
		yr += -1
		mn = 11
	draw()

def sel():
	if disp =="t":
		todolist.remove(todolist[listitem-1])
		draw()

def getinput():
	global disp
	nowvar = datetime.datetime.now()
	with NonBlockingConsole() as nbc:
		
		d = nbc.get_data() 
		if d == "x" or d == "w" or d == "u" or d == "y" or d == "v" or d == '' or d == 'q' or d == 'e' or d == "d" or d == "s" or d == "a" or d == "r" or d == "c" or d == "t" or d == "m":
			if d == "x":
				save()
				return("end")
			elif d == "w":
				goup()
				draw()
			elif d == "s":
				godown()
				draw()
			elif d == "r": 
				sel()
			elif d == "d":
				goright()
				draw()
			elif d == "p":
				pomodoro()
			elif d == "q":
				prevmonth()
			elif d == "e":
				nextmonth()
			elif d == "a":
				goleft()
				draw()
			elif d == "c":
				disp = "c"
				calendardisp()
			elif d == "t":
				disp = "t"
				listdisp()
			elif d == "m":
				return("add")
			elif d == "u":
				menuprint()
			elif d == "y":
				global todolist
				todolist = (t.addevent(todolist))
				save()
				draw()
			elif d == "v":
				t.viewcomplete()
nowvar = datetime.datetime.now()
wk = nowvar.strftime("%w")
yr = int(nowvar.strftime("%Y"))
mn = int((nowvar.strftime("%m")))-1
dat = json.loads(loaddata())
dates = []
for x in dat:
	dates.append(x)
global listitem
listitem=1
coords=[1,1]
selecteditem=0
while True:
	f = getinput()
	if f == "add":
		addanevent.entry()
	if f == "end":
		break