import pygame
import pyganim
import classes
import functions
from screens import *
from constants import *
import fonts
import text
import camera

#functions.create_level
timer = pygame.time.Clock  ()

class SuperLevel ():
	def __init__ (self, control, lev, battle, son):

		#self.create = create
		self.lev = lev
		self.battle = battle
		self.description = ''
		self.son = son
		self.name = 'location`s name'
		self.control = control		
		self.platforms, self.block_group, self.background = self.create ()

		self.level_width = len(lev[0])*PF_WIDTH
		self.level_height = len(lev)*PF_HEIGHT
		self.camera = camera.Camera (self.level_width, self.level_height, 840, 420)
	#	self.x_hero = (self.camera.apply(self.hero))
		self.back = False

	def create (self):
		a, b, c = functions.create_level (self.lev, self.battle, self.control,self.son, classes.Pavestone)
		return a,b,c

	def render_stage (self, hero):
		
		main_interface (self)
		if self.back == True:

			for b in self.background:
				adventure_screen.blit(b.image, self.camera.apply (b))

		#rendering map`s objects
		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))

		#rendering hero
		if hero.status != 'dead':
			adventure_screen.blit (hero.image, self.camera.apply(hero))
			hero.anima.blit (adventure_screen, (self.camera.apply(hero)))
			if hero.move == False:
				adventure_screen.blit (hero.stand, self.camera.apply(hero))

		#render text_information
		self.son.render_text ()
		hero.render_information ()

	def general_stuff (self, hero):

		#hero dead or alive
		if hero.status == 'dead':
			hero.end_text ()

		#if self.hero.status != 'dead':
			#MAIN HERO RENDER FUNCTION!!!
		#	self.hero.update (self.block_group)

		#render hp mod of monsters in a battle
		try:	
			x_monster = (self.camera.apply(hero.etwas))
			hero.etwas.render_hp_mod(x_monster)
		except:
			pass

		#Rendering hero hp modification
		self.x_hero = (self.camera.apply(hero))
		hero.render_hp_mod(self.x_hero)

		#activation of a battle loop
		if hero.collide_control == True and hero.etwas.agression == True:	
			self.battle.main_loop (hero, hero.etwas)

		#camera
		self.camera.update(hero)

		#timer
		self.a = timer.get_fps()		
		timer.tick (60)

	def stage_content (self, hero):
		pass

	def stage_loop (self, hero):
		self.general_stuff (hero)
		self.stage_content (hero)
		self.render_stage (hero)




class Level1 (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.skeletLord = classes.SkeletLord (19,5, self.battle, text.zombitext, self.control, 10,10,10,1, son)
		self.block_group.add (self.skeletLord)
		self.name = '- - - Неизвестное подземелье - - -'

	def stage_content (self, hero):

		#classes.boltAnim.blit (adventure_screen, (self.x_hero.x - 49, self.x_hero.y - 80))

		if self.control.k_space == True:
			self.control.stage1_flag = False
			self.control.stage2_flag = True




class Level2 (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)
		self.name = '- - - Окраины города - - -'

	def stage_content (self, hero):

		if self.control.k_space == True:
			self.control.stage2_flag = False
			self.control.stage1_flag = True

class Platz (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)
		self.name = '- - - Главная площадь - - -'

	def stage_content (self, hero):

		pass

class Tavern (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.back = False
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)
		self.name = '- - - Таверна - - -'

	def stage_content (self, hero):

		pass


