import camera
from superlevel import SuperLevel
import constructor
#functions.create_level
#timer = pygame.time.Clock  ()



# Подземелье для первого квеста
# First stage


class _dungeon1(SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self,  lev, battle, son, control)
		self.block_group, self.background = self.create (create_level = constructor.create_dungeon1)
		self.name = '- - - Подземелье - - -'
		self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)

	def stage_content (self, hero):
		pass

# second stage
class _dungeon2 (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.block_group, self.background = self.create (create_level = constructor.create_dungeon2)
		self.name = '- - - Подземелье 2 этаж - - -'
		#self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)
	def stage_content (self, hero):
		pass

class _dungeon3 (SuperLevel):
	def __init__ (self,  lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.block_group, self.background = self.create (create_level = constructor.create_dungeon3)
		self.name = '- - - Тронный зал- - -'
		#self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)

	def stage_content (self, hero):
		pass

class _end (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)
		self.name = '- - - Окраины города - - -'

	def stage_content (self, hero):
		pass

class _platz (SuperLevel):
	def __init__ (self,lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Главная площадь -'		
		self.auto = False
		self.block_group, self.background = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)

	def stage_content (self, hero):
		pass

class _tavern (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Таверна "Приют героев" -'
		self.auto = False		
		self.block_group, self.background = self.create (create_level = constructor.create_level_city)
		#self.back = False

		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)

	def stage_content (self, hero):
		pass


class _temple (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background = self.create (create_level = constructor.create_level_city)
		
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)
		self.name = '- - - Храм Единого - - -'

	def stage_content (self, hero):
		pass
