#! /usr/bin/env python3
import pygame
import levels
import classes
import controller
import character
from level_data import *
from constants import *
import camera
import functions

#global settings
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

#main function

def main_loop():
	while True:
		control.control () #control loop, control of events, key press
		hero.transcendental_apperception () #construct and render all the world from the character itself
		pygame.display.update() #update the screen
		
#create objects (cosmic forces)

son = functions.Son ()
control = controller.Holy_Spirit () 
battle = functions.Battle () #delet
compose_text = functions.Compose_dialog_tree (control,son)

#create locations
#stage1 = levels.Level1(control, lev1, battle, son)
stage2 = levels.Level2(control, lev2, battle, son)
mainplatz = levels.Platz (control, platz, battle, son)
tavern_loc = levels.Tavern (control, tavern, battle, son)
temple_loc = levels.Temple (control, temple, battle, son)
dungeon1_loc = levels.dungeon (control, dungeon1, battle, son)
dungeon2_loc = levels.dungeon2 (control, dungeon2, battle, son)
dungeon3_loc = levels.dungeon3 (control, dungeon3, battle, son)

#list of locations
levels_list = [dungeon1_loc, dungeon2_loc, dungeon3_loc, temple_loc, stage2, mainplatz]
levels_dict = {'dung1' : dungeon1_loc, 'end':stage2, 'temple':temple_loc, "tavern":tavern_loc, "platz":mainplatz, 'dung2' : dungeon2_loc, 'dung3' : dungeon3_loc }


#create hero
hero = character.Hero (7,6, battle, control, compose_text, 6,6,6,1, son, levels_list, levels_dict)

print ('Привет доброму человеку Кириллу Герою!')

#start game
main_loop ()


