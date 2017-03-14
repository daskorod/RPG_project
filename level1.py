import pygame
import pyganim
import classes
import functions
from screens import *
from constants import *
import fonts
import text
import camera

timer = pygame.time.Clock  ()
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

class Level ():

	def __init__ (self, control, hero, lev, camera, battle):

		self.platforms, self.block_group = functions.create_level (lev, battle, control)
		self.control = control
		self.hero = hero
		self.camera = camera
		
		self.battle = battle
		self.zomb = classes.Monster (0,0, self.battle, text.zombitext, self.control, 10,0,10,1)
		self.block_group.add (self.zomb)


	def render_stage1 (self):

		main_interface ()
		
		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))

		adventure_screen.blit (self.hero.image, self.camera.apply(self.hero))
		start_screen.blit(fonts.font1.render (str(self.a), True, (250,250,250)),(0,0))

	def stage_loop (self):

		self.a = timer.get_fps()
		self.render_stage1 ()

		
		self.hero.update (self.block_group)
		self.hero.chang ()

		if self.hero.add_information == 'war' and self.hero.collide_control == True:
			self.battle.main_loop (self.hero, self.hero.etwas)
			#self.battle.render_battle_info (self.hero, self.hero.etwas)
		if self.hero.add_information == 'peace':
			adventure_screen.blit(fonts.font2.render (str(self.hero.add_information), True, (250,250,250)),(0,15))

		#functions.render_text (text.text1)
		self.camera.update(self.hero)
		timer.tick (60)

		if self.control.k_space == True:
			self.control.stage1_flag = False
			self.control.stage2_flag = True
