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

	def __init__ (self, control, hero, lev, camera, battle, son):

		self.platforms, self.block_group = functions.create_level (lev, battle, control,son)
		self.control = control
		self.hero = hero
		self.camera = camera
		
		self.battle = battle
		self.skeletLord = classes.SkeletLord (19,5, self.battle, text.zombitext, self.control, 10,10,10,1, son)
		#self.zomb = classes.Monster (0,0, self.battle, text.zombitext, self.control, 10,0,10,1, son)

		#self.block_group.add (self.zomb)
		self.block_group.add (self.skeletLord)
		self.n = 0
		self.son = son
		self.g = 1200
		son.change_text (1, 'Вы в мрачном подземелье.')
		
	def render_stage1 (self):

		main_interface ()
		#self.g += 1
		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))

		if self.hero.status != 'dead':

			adventure_screen.blit (self.hero.image, self.camera.apply(self.hero))
		#start_screen.blit(fonts.font1.render (str(self.a), True, (250,250,250)),(0,0))

	def stage_loop (self):

		
		
		x_hero = (self.camera.apply(self.hero))
		classes.boltAnim.blit (adventure_screen, (x_hero.x - 49, x_hero.y - 80))
		self.hero.render_hp_mod(x_hero)

#		if self.skeletLord.lbolt == True:
#			self.g = 185
#
#			self.skeletLord.lbolt = False
#
#
#		if self.g > 190 and self.g< 240:
#			
##			x_hero.x -=49
##			x_hero.y -=80
##			classes.boltAnim.blit (adventure_screen, (x_hero.x - 49, x_hero.y - 80))
#			classes.boltAnim.play ()
#			if self.g==239:
#				classes.boltAnim.stop()

		self.a = timer.get_fps()
		self.render_stage1 ()

		if self.hero.status == 'dead':
			self.hero.end_text ()

		if self.hero.status != 'dead':
			self.hero.update (self.block_group)
		try:	
			x_monster = (self.camera.apply(self.hero.etwas))
			self.hero.etwas.render_hp_mod(x_monster)
		except:
			pass

		if self.hero.collide_control == True and self.hero.etwas.agression == True:
			
			self.battle.main_loop (self.hero, self.hero.etwas)

		self.son.render_text ()

		self.hero.render_information ()

		self.camera.update(self.hero)
		timer.tick (60)

		if self.control.k_space == True:
			self.control.stage1_flag = False
			self.control.stage2_flag = True
