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

class SuperLevel ():
	def __init__ (self, control, hero, lev, battle, son):

		self.platforms, self.block_group, self.background = functions.create_level (lev, battle, control,son, classes.Pavestone)
		self.control = control
		self.hero = hero
		self.level_width = len(lev[0])*PF_WIDTH
		self.level_height = len(lev)*PF_HEIGHT
		self.battle = battle
		self.description = ''
		self.son = son
		self.name = 'location`s name'
		self.camera = camera.Camera (self.level_width, self.level_height, 840, 420)
		self.x_hero = (self.camera.apply(self.hero))
		self.back = False

	def render_stage (self):
		
		main_interface (self)
		if self.back == True:

			for b in self.background:
				adventure_screen.blit(b.image, self.camera.apply (b))

		#rendering map`s objects
		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))

		#rendering hero
		if self.hero.status != 'dead':
			adventure_screen.blit (self.hero.image, self.camera.apply(self.hero))
			self.hero.anima.blit (adventure_screen, (self.camera.apply(self.hero)))
			if self.hero.move == False:
				adventure_screen.blit (self.hero.stand, self.camera.apply(self.hero))

		#render text_information
		self.son.render_text ()
		self.hero.render_information ()

	def general_stuff (self):

		#hero dead or alive
		if self.hero.status == 'dead':
			self.hero.end_text ()

		if self.hero.status != 'dead':
			self.hero.update (self.block_group)

		#render hp mod of monsters in a battle
		try:	
			x_monster = (self.camera.apply(self.hero.etwas))
			self.hero.etwas.render_hp_mod(x_monster)
		except:
			pass

		#Rendering hero hp modification
		self.x_hero = (self.camera.apply(self.hero))
		self.hero.render_hp_mod(self.x_hero)

		#activation of a battle loop
		if self.hero.collide_control == True and self.hero.etwas.agression == True:	
			self.battle.main_loop (self.hero, self.hero.etwas)

		#camera
		self.camera.update(self.hero)

		#timer
		self.a = timer.get_fps()		
		timer.tick (60)

	def stage_content (self):
		pass

	def stage_loop (self):

		self.stage_content ()
		self.render_stage ()
		self.general_stuff ()



class Level1 (SuperLevel):
	def __init__ (self, control, hero, lev, battle, son):
		SuperLevel.__init__ (self, control, hero, lev, battle, son)
		self.skeletLord = classes.SkeletLord (19,5, self.battle, text.zombitext, self.control, 10,10,10,1, son)
		self.block_group.add (self.skeletLord)
		self.name = '- - - Неизвестное подземелье - - -'

	def stage_content (self):

		classes.boltAnim.blit (adventure_screen, (self.x_hero.x - 49, self.x_hero.y - 80))

		if self.control.k_space == True:
			self.control.stage1_flag = False
			self.control.stage2_flag = True




class Level2 (SuperLevel):
	def __init__ (self, control, hero, lev, battle, son):
		SuperLevel.__init__ (self, control, hero, lev, battle, son)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)
		self.name = '- - - Окраины города - - -'

	def stage_content (self):

		if self.control.k_space == True:
			self.control.stage2_flag = False
			self.control.stage1_flag = True





