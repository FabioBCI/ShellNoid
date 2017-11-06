#Autor: FabioBCI
#Data : 05/11/2017

from threading import Thread
from random import randint
import curses
import time
import os
import board
import enemy
import blocks
import sys
import msvcrt

def clear():
	if os.name == "posix":
		os.system ("clear")
	else:
		os.system ("cls")

def message_welcome(stdscr):
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	stdscr.addstr(1, 1,"******************************************",curses.color_pair(2))
	stdscr.addstr(2, 1,"*          Welcom to ShellNoid           *",curses.color_pair(3))
	stdscr.addstr(3, 1,"*                                        *",curses.color_pair(2))
	stdscr.addstr(4, 1,"*          Author: FabioBCI              *",curses.color_pair(3))
	stdscr.addstr(5, 1,"******************************************",curses.color_pair(2))
	#print("******************************************")
	#print("*          Welcom to ShellNoid           *")
	#print("*                                        *")
	#print("*          Author: FabioBCI              *")
	#print("*                                        *")
	#print("******************************************")
	stdscr.refresh()
	
	time.sleep(2)
	clear()

def message_exit(stdscr):
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	stdscr.addstr(1, 1,"******************************************",curses.color_pair(3))
	stdscr.addstr(2, 1,"*          Use Free Software             *",curses.color_pair(3))
	stdscr.addstr(3, 1,"*         if you want be free            *",curses.color_pair(3))
	stdscr.addstr(4, 1,"*          FabioBCI 2017                 *",curses.color_pair(3))
	stdscr.addstr(5, 1,"******************************************",curses.color_pair(3))
	stdscr.refresh()

def generate_enemys():
	names_list=os.listdir('./')
	enemys=[]
	for f in names_list:
		e=enemy.enemy(f,35)
		enemys.append(e)

	return enemys

def main_loop(stdscr):
	k=0
	main_board=board.board(35,35)
	bloques=blocks.blocks(20,stdscr)
	enemigos=generate_enemys() #Se generan los enemigos que son los nombres de los ficheros
	proceso_key=Thread(target=catch_key, args=(stdscr,main_board,enemigos,bloques,))
	proceso_key.start()


def catch_key(stdscr,main_board,enemigos,bloques):
	k=0
	l=len(enemigos)
	num=randint(0,l-1)
	e=enemigos[num]
	num_ant=num

	while(k!=ord('q')):
		if(e.killed==True):
			num=randint(0,l-1)
			e=enemigos[num]
		else:
			pass
		main_board.show(stdscr)		
		stdscr.refresh()
		stdscr.clear()

		e=enemigos[num]		
		e.move()
		e.show(stdscr)		
		bloques.show(stdscr)
		if(msvcrt.kbhit()==True):
			k = stdscr.getch()
		else:
			k=0
		main_board.move(k)
		main_board.show(stdscr)
		stdscr.refresh()
		time.sleep(0.2)
		stdscr.clear()
	message_exit(stdscr)

def scan_dir(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            return path
        else:
            scan_dir(path)

def main():
	stdscr = curses.initscr()
	try:
		curses.start_color()
	except:
		pass
	message_welcome(stdscr)
	main_loop(stdscr)


if __name__ == "__main__":
    main()
