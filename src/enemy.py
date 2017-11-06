
#Autor: FabioBCI
#Data : 05/11/2017

from random import randint
from colorama import Fore, Back, Style
import colorama
from ctypes import *
import curses
import sys,os

class enemy:

	def __init__(self,text,pos_y_board):
		x=randint(10,45)
		y=randint(0,2)
		self.pos_x=x
		self.pos_y=y
		self.text=text
		self.killed=False
		self.pos_y_board=pos_y_board

	def show(self,stdscr):
		if(self.killed==False):
			curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
			stdscr.addstr(self.pos_y, self.pos_x,self.text,curses.color_pair(1))
			stdscr.refresh()
		else:
			pass

	def move(self):
		if(self.killed==False):
			x=randint(1,2)
			y=randint(1,2)
			b=randint(1,10)
			if(b>5):
				self.pos_x=self.pos_x+x
			else:
				self.pos_x=self.pos_x-x

			if(self.pos_y==self.pos_y_board):
				self.kill()
			else:
				self.pos_y=self.pos_y+1
		else:
			pass

	def kill(self):
		self.killed=True


