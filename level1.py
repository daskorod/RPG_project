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

class Level ():

	def __init__ (self, control, hero, lev, battle, son):

		self.platforms, self.block_group, self.background = functions.create_level (lev, battle, control,son, classes.Pavestone)
		self.control = control
		self.hero = hero
		#self.camera = camera
		self.level_width = len(lev[0])*PF_WIDTH
		self.level_height = len(lev)*PF_HEIGHT
		self.battle = battle
		self.skeletLord = classes.SkeletLord (19,5, self.battle, text.zombitext, self.control, 10,10,10,1, son)
		#self.zomb = classes.Monster (0,0, self.battle, text.zombitext, self.control, 10,0,10,1, son)
		self.description = 'Вы в мрачном подземелье'
		#self.block_group.add (self.zomb)
		self.block_group.add (self.skeletLord)
		self.n = 0
		self.son = son
		self.g = 1200
		son.change_text (1, self.description)
		self.name = '- - - Неизвестное подземелье - - -'
		self.camera = camera.Camera (self.level_width, self.level_height, 840, 420)
		
	def render_stage1 (self):
		
		main_interface (self)

		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))

		if self.hero.status != 'dead':
			adventure_screen.blit (self.hero.image, self.camera.apply(self.hero))


	def stage_loop (self):

		x_hero = (self.camera.apply(self.hero))
		classes.boltAnim.blit (adventure_screen, (x_hero.x - 49, x_hero.y - 80))
		self.hero.render_hp_mod(x_hero)
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
