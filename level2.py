import pygame
import pyganim
import classes
import functions
from functions import create_level
from screens import *
from constants import *
from fonts import *


timer = pygame.time.Clock  ()

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()


class Level ():

	def __init__ (self, control,hero, lev):
		
	    #self.platforms, self.block_group = create_level (lev, hero)
	    self.control = control
	    self.hero = hero
	    #self.hero.block_group = self.block_group
		#self.camera = camera



	def render_stage (self):

		main_interface ()
		self.block_group.draw (adventure_screen)
		start_screen.blit(font1.render (str(self.a), True, (250,250,250)),(0,0))
#		for b in self.block_group:
#			adventure_screen.blit(b.image, self.camera.apply (b))
#
#		adventure_screen.blit (self.hero.image, self.camera.apply(self.hero))

	def stage_loop (self):

		self.a = timer.get_fps()
		self.render_stage ()
		svin_anim.blit (adventure_screen, (10,10))
		#self.hero.render (adventure_screen)
		self.hero.update (self.block_group)	

		if self.control.k_space == True:
			self.control.stage2_flag = False
			self.control.stage1_flag = True

		timer.tick (30)
	