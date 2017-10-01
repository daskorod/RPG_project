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
import menu
import sys

test_arg = False

if len(sys.argv)>1:
	if sys.argv[1] == 'test':
		print ('Test mode')

		test_arg = True


#global settings
#pygame.mixer.pre_init (44100, -16, 1, 2512)
#pygame.mixer.init()
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

menu.pause()

#main function
if test_arg == False:
	menu.menu_loop()
	#menu.intro_loop()
	menu.experiment_loop ('В начале сотворил Бог небо и землю... Земля же была безвидна и пуста, и тьма над бездною, и Дух Божий носился над водою. И сказал Бог: да будет свет. И стал свет. И увидел Бог свет, что он хорош, и отделил Бог свет от тьмы.', 'images/intro/3.png', pic_x = 0, pic_y = 40, time_scroll = 200)

	menu.experiment_loop('И упал с неба денница, сын зари! разбился о землю, попиравший народы. Низвержен он ныне в ад, в глубины преисподней. Тот, который говорил: "взойду на небо, выше звезд Божиих вознесу престол мой... взойду на высоты облачные, буду подобен Всевышнему".', 'images/intro/DL2.png', time_scroll = 400, speed_mod = 1)
	
	menu.experiment_loop('Много времени прошло с тех времён. Память о первой Войне Сил, проходившей в небесах, сохранилась 	только в легендах и священных текстах. Но зло в сердцах людей дало свои всходы. Сыны тьмы начали войну на Земле против людей света.', 'images/intro/cl.png', pic_x = 10, time_scroll = 100) 
	
	menu.experiment_loop('Это была вторая Война Сил, которая оказалась столь разрушительна, что большая часть мира превратилась в безлюдную пустошь, наполненную тварями, порождёнными Войной...', 'images/intro/2.gif',time_scroll = 50) 
	
menu.load()

#menu.help_loop()

def main_loop():
	while True:
		control.control () #control loop, control of events, keys press
		hero.transcendental_apperception () #construct and render all the world from the character itself
		pygame.display.update() #update the screen

#def menu_loop():




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

		control.auto = False



battle = functions.Battle () #to delete

compose_text = functions.Compose_dialog_tree (control,son)

levels_list, levels_dict = levels_constructor (create_class_levels_list (dir(levels)))

print ('\n',levels_list, '\n\n', levels_dict,'\n')


#create hero
hero = character.Hero (10,10, battle, control, compose_text, 6,6,6,1, son, levels_list, levels_dict, test_arg)


#start game
main_loop ()