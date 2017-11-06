#Autor: FabioBCI
#Data : 25/10/2017
import curses

class block:

	def __init__(self,pos_x,pos_y,stdscr):
		self.pos_x=pos_x
		self.pos_y=pos_y
		self.visible=True
		self.value=1
		self.stdscr=stdscr
		self.text='R'

	def show(self,stdscr):
		if(self.visible==True):
			#Mostramos el bloque
			curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
			stdscr.addstr(self.pos_y, self.pos_x,self.text,curses.color_pair(3))
			stdscr.refresh()
		else:
			#No mostramos el bloque
			pass

