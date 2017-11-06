#Autor: FabioBCI
#Data : 05/11/2017
from ctypes import *
import curses
import sys,os
 
STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]

class board:

	def __init__(self,x,y):
		self.pos_x=x
		self.pos_y=y
		self.text='---'

	def show(self,stdscr):
		curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
		stdscr.addstr(self.pos_y, self.pos_x,self.text,curses.color_pair(2))
		stdscr.refresh()

	def move(self,key):
		if(key==97):
			self.pos_x=self.pos_x-5
		else:
			if(key==100):
				self.pos_x=self.pos_x+5
			else:
				pass
