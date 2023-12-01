from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer,Static
from textual.widget import Widget
import os, math,termios, tty, sys, select, json, datetime, calendar, addanevent
import todo as t

dat,disp = "",""
todolist = json.loads(open("todolist.json","r").read())

def ensureexists():
	open("todolist.json","a").write("")
	open("list.json","a").write("")

ensureexists()


def loaddata():
	f = open("list.json", "r")
	return (f.read())



logo = "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠐⢷⣦⠀⠙⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠙⣿⣿⣿\n⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣿⡄⠀⢸⡿⠋⠉⢻⣷⣤⣿⣿⣿⣿\n⣿⣿⣿⠇⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣷⡀⠸⣷⡀⠀⠀⠀⠙⣿⣿⣿⣿\n⣿⣿⡏⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⣿⡄⠀⠀⠀⠹⣿⣿⣿\n⣿⣿⠁⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢿⣿⣿\n⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿\n⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢸⣿⣿\n⣿⣿⣇⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⣾⣿⣿\n⣿⣿⣿⡄⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⢰⣿⣿⣿\n⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n Zero's Super Cool And Useful To Do List Program\n(ZSCAUTDLP)"
class maindisp(Static):
	def on_mount(self) -> None:
		self.update(logo)
class sidedisp(Static):
	def on_mount(self) -> None:
		self.update("")
class ToDoApp(App):
	CSS_PATH = "todo.tcss"
	"""textual interface to migrate my to do app to"""
	BINDINGS = [("t","displayToDo","to do list"),
				("p","displayTimer","timer"),
				("c","displayCalendar","calendar"),
			    ("y","addTask","add task"),
				("m","addEvent","add event")
			   ]
	def compose(self) -> ComposeResult:
		"""Create child widgets for the app."""
		yield Header()
		yield Container(
			Horizontal(
				maindisp(
					logo, classes = "test"),
				sidedisp()))
		yield Footer()
	def action_toggle_dark(self) -> None:
		"""An action to toggle dark mode."""
		self.dark = not self.dark


if __name__ == "__main__":
	app = ToDoApp()
	app.run()

