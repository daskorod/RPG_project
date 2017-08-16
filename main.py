#! /usr/bin/env python3
import pygame
import superlevel
import levels
import classes
import controller
import character
import level_data
from constants import *
import camera
import functions

import sys




#global settings
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

#main function



def main_loop():
	while True:
		control.control () #control loop, control of events, keys press
		hero.transcendental_apperception () #construct and render all the world from the character itself
		pygame.display.update() #update the screen

def levels_constructor (classlevellist):
	levels_list = []
	levels_dict= {}
	for clss in classlevellist:
		#a = levels_factory (i, getattr(level_data, str(i.__name__)), battle, son, control)
		exemp = clss(getattr(level_data, str(clss.__name__)), battle, son, control)
		print (exemp)
		levels_list.append(exemp)
		levels_dict[clss.__name__.strip('_')] = exemp
	return levels_list, levels_dict

def create_class_levels_list(levelsmodule):
	class_levels_list = []
	for levelname in levelsmodule:
		if levelname.startswith ('_') == True and levelname.endswith ('__') == False:
			class_levels_list.append(getattr (levels, levelname))
	return class_levels_list

#create objects (cosmic forces)

son = functions.Son ()
control = controller.Holy_Spirit () 

if len(sys.argv)>1:
	if sys.argv[1] == 'test':
		print ('Test mode')
		control.auto = False

battle = functions.Battle () #to delete

compose_text = functions.Compose_dialog_tree (control,son)

levels_list, levels_dict = levels_constructor (create_class_levels_list (dir(levels)))

print ('\n',levels_list, '\n\n', levels_dict,'\n')


#create hero
hero = character.Hero (7,6, battle, control, compose_text, 6,6,6,1, son, levels_list, levels_dict)


#start game
main_loop ()