#Autor: FabioBCI
#Data : 05/11/2017

import block
import curses

class blocks:

	def __init__(self,num_blocks,stdscr):
		self.num_blocks=num_blocks
		self.blocks_array=[]
		pos_x=35
		pos_y=5
		for i in range(0,self.num_blocks):
			if(i==10):
				pos_y=pos_y+1
				pos_x=35
			else:
				pass
			b=block.block(pos_x,pos_y,stdscr)
			self.blocks_array.append(b)
			pos_x=pos_x+1

	def show(self,stdscr):
		for e in self.blocks_array:
			e.show(stdscr)
