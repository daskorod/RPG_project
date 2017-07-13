﻿import pygame
import pyganim
import classes
import functions
from screens import *
from constants import *
import fonts
import text
import camera
from superlevel import SuperLevel
import constructor
#functions.create_level
timer = pygame.time.Clock  ()



# Подземелье для первого квеста
# First stage
class dungeon (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.block_group, self.background = self.create (create_level = constructor.create_dungeon1)
		self.name = '- - - Подземелье - - -'
		self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)
	def stage_content (self, hero):
		pass

# second stage
class dungeon2 (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.block_group, self.background = self.create (create_level = constructor.create_dungeon2)
		self.name = '- - - Подземелье 2 этаж - - -'
		#self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)
	def stage_content (self, hero):
		pass

class dungeon3 (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.block_group, self.background = self.create (create_level = constructor.create_dungeon3)
		self.name = '- - - Тронный зал- - -'
		#self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)
	def stage_content (self, hero):
		pass


class Level1 (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.auto = False
		self.block_group, self.background = self.create ()
		self.skeletLord = classes.SkeletLord (19,5, self.battle, text.zombitext, self.control, 3,6,8,1, son)
		self.block_group.add (self.skeletLord)
		self.back = True
		self.name = '- - - Неизвестное подземелье !- - -'

	def stage_content (self, hero):
		pass
		#classes.boltAnim.blit (adventure_screen, (self.x_hero.x - 49, self.x_hero.y - 80))

class Level2 (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.auto = False
		self.block_group, self.background = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)
		self.name = '- - - Окраины города - - -'

	def stage_content (self, hero):
		pass




class Platz (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.auto = False
		self.block_group, self.background = self.create (create_level = functions.create_level_city)
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


class Temple (SuperLevel):
	def __init__ (self, control, lev, battle, son):
		SuperLevel.__init__ (self, control, lev, battle, son)
		self.auto = False
		self.block_group, self.background = self.create (create_level = functions.create_level_city)
		
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)
		self.name = '- - - Храм Единого - - -'

	def stage_content (self, hero):

		pass
