#! /usr/bin/env python3
import pygame
import level1
import level2
import classes
import controller
import character
from level_data import *
from constants import *
import camera
import functions

pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()


class main ():
	def __init__ (self, stage1, stage2, control):
		self.stage1 = stage1
		self.stage2 = stage2
		self.control = control
		
	def main_loop (self):
		while True:

			self.control.control ()

			if self.control.stage1_flag == True:
				if self.control.flag == 1:
					self.control.k_space = False
					self.control.flag = 0
				self.stage1.stage_loop ()

			if self.control.stage2_flag == True:
				if self.control.flag == 0:
					self.control.k_space = False
					self.control.flag = 1
				self.stage2.stage_loop ()
	
			pygame.display.update()


son = functions.Son ()
control = controller.Holy_Spirit () 
battle = functions.Battle (control)
compose_text = functions.Compose_dialog_tree (control,son)
hero = character.Hero (2,2, battle, control, compose_text, 6,6,6,1, son)
stage1 = level1.Level(control, hero, lev1, battle, son)
stage2 = level2.Level(control, hero, lev2, battle, son)
game = main (stage1, stage2, control)
game.main_loop ()



