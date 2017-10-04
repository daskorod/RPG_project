import camera
from superlevel import SuperLevel
import constructor
import classes
import screens
import img
#import time
#import math
#functions.create_level
#timer = pygame.time.Clock  ()



# Подземелье для первого квеста
# First stage


class _dungeon1(SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self,  lev, battle, son, control)
		self.block_group, self.background, self.decor = self.create (create_level = constructor.create_dungeon1)
		self.name = '- - - Подземелье - - -'
		self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)

	def render_location_info (self):
		

		self.son.change_text (2, 'Вы спустились в жуткое и мрачное подземелье.')
		self.son.change_text (3, 'Откуда-то из глубины коридора пахнет затхлостью и смертью')		
		self.son.change_text (4, 'Стены сложены из старых камный, влажных на ощупь,')
		self.son.change_text (5, 'кое-где поросших мхом. Пол покрыт трещинами, мусором и пылью.')

	def stage_content (self, hero):
		pass

# second stage
class _dungeon2 (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_dungeon2)
		self.name = '- - - Подземелье 2 этаж - - -'
		#self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)

	def render_location_info (self):
		
		self.son.change_text (2, 'Вы спустились ещё глубже...')
		self.son.change_text (3, 'Здесь всё гораздо суше. Однако дышать ещё менее приятно.')
		self.son.change_text (4, 'Вентиляции никакой, пыли полно. ')		


	def additional_content(self, hero):
		for i in constructor.addition:
			screens.adventure_screen.blit(i.image, self.camera.apply (i))
		
	def stage_content (self, hero):
		img.fireAnim.blit (screens.adventure_screen, (self.camera.apply(hero).x-45, self.camera.apply(hero).y-45))
		img.boltAnim.blit (screens.adventure_screen, (self.camera.apply(hero).x-45, self.camera.apply(hero).y-45))
		#classes.boltAnim.stop()

class _dungeon3 (SuperLevel):
	def __init__ (self,  lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_dungeon3)
		self.name = '- - - Тронный зал- - -'
		#self.camera = camera.Camera (self.level_width, self.level_height, 750, 400)

	def render_location_info (self):
		
		self.son.change_text (1, 'Вы вышли в непонятный зал. По периметру его оссвещают')
		self.son.change_text (2, 'факелы, которые горят вечным необжигающим пламенем.')
		self.son.change_text (3, 'В центре возвышается странного рода трон.')		
		self.son.change_text (4, 'Вы чувствуете тревогу, которая, при приближении к ')
		self.son.change_text (5, 'центру зала усиливается. Что-то нечеловеческое находистя')
		self.son.change_text (6, 'здесь, что-то, что инстинктивно заставляет вас бежать прочь,')		
		self.son.change_text (7, 'не разбирая дороги.')

	def stage_content (self, hero):
		pass

class _end (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 780, 360)
		self.name = '- - - Окраины города - - -'
		self.x = 0
		self.up = True

	def render_location_info (self):

		self.son.change_text (1, 'Вы оказались на городских окраинах.')
		self.son.change_text (2, '')
		self.son.change_text (3, 'Обстановка здесь не самая лучшая. Разруха, бандитизм.')		
		self.son.change_text (4, 'Нормальных людей здесь не встретишь - всё какие-то')
		self.son.change_text (5, 'сомнительные элементы. Бомжи, нищие, больные, психопаты -')
		self.son.change_text (6, 'все неучтённые системой элементы. Божьи люди, короче.')		
		self.son.change_text (7, 'Блаженны нищие духом, ибо их есть Царство Небесное.')


	def stage_content (self, hero):
		pass
		if self.up == True:
			self.x +=1
		else:
			self.x -=1

		if self.x > 6:
			self.up = False

		if self.x < -6:
			self.up = True

		pos = self.camera.apply(constructor.stuff[0])
		screens.adventure_screen.blit (img.arrow, (pos.x+20,pos.y+10+self.x))
		#classes.slashAnim.blit (screens.adventure_screen, (self.camera.apply(hero).x, self.camera.apply(hero).y))

class _platz (SuperLevel):
	def __init__ (self,lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Главная площадь -'		
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 825, 420)
		self.x = 0
		self.up = True	


	def render_location_info (self):
		
		self.son.change_text (1, 'Главная площадь представляет собой печальное зрелище.')
		self.son.change_text (2, 'Здесь практически никого нет.')
		self.son.change_text (3, 'Даже в праздники эта площадь не знает народа.')		
		self.son.change_text (4, 'Редкий люд, обитающий в городе, занят делом,')
		self.son.change_text (5, 'чтобы заработать себе на кусок хлеба.')
		self.son.change_text (6, 'На улицах этого проклятого города, же слишком опасно,')		
		self.son.change_text (7, 'чтобы лишний раз шляться где попало.')


	def stage_content (self, hero):
		pass
		if self.up == True:
			self.x +=1
		else:
			self.x -=1

		if self.x > 6:
			self.up = False

		if self.x < -6:
			self.up = True

		pos = self.camera.apply(constructor.stuff[1])
		screens.adventure_screen.blit (img.arrow, (pos.x+20,pos.y+10+self.x))

		pos2 = self.camera.apply(constructor.stuff[2])
		screens.adventure_screen.blit (img.arrow, (pos2.x+12,pos2.y+10+self.x))

class _tavern (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Таверна "Приют героев" -'
		self.auto = False		
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city, create_interior = constructor.create_interior_tavern, floor = classes.WoodFloor)
		#self.back = False

		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)


	def render_location_info (self):
		
		self.son.change_text (2, 'Таверна - отдушина для путника.')
		self.son.change_text (3, 'Вам в лицо пахнуло жаром, жиром и потом.')
		self.son.change_text (4, 'В таверне есть народ - в основном это заезжие люди.')		
		self.son.change_text (5, 'Здесь можно хорошенько покушать и отдохнуть.')
		self.son.change_text (6, 'Если, конечно, у вас есть деньажат...')



	def stage_content (self, hero):
		pass


class _temple (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)
		self.name = '- - - Храм Единого - - -'

	def render_location_info (self):
		
		self.son.change_text (2, 'Огромное и величественное здание храма наполняет покоем')
		self.son.change_text (3, 'вашу душу. Все плохие мысли уходят. Вся жизнь начинает')
		self.son.change_text (4, 'казаться мелкой и незначительной, по сравнению с вечностью,')		
		self.son.change_text (5, 'которая ждёт каждого, родившегося в этом бренном мире.')

	def stage_content (self, hero):
		img.fireAnim.blit (screens.adventure_screen, (self.camera.apply(hero).x-45, self.camera.apply(hero).y-45))
		pass

class _cell (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)
		self.name = '- - - Кельи - - -'

	def render_location_info (self):
		
		self.son.change_text (2, 'Вы вошли в храмовый коридор, который вёл в житейские')
		self.son.change_text (3, 'помещения монахов.')

	def stage_content (self, hero):
		pass

class _still (SuperLevel):
	def __init__ (self,lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Тихий квартал -'		
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 735, 420)
		self.x = 0
		self.up = True	


	def render_location_info (self):
		
		self.son.change_text (2, 'Вы вошли в очень мирный и тихий квартал.')
		self.son.change_text (3, 'Здесь как-то спокойно и чисто. Опрятные дома,')
		self.son.change_text (4, 'опрятные улочки - ничто не вызывает подозрений.')		
	


	def stage_content (self, hero):
		pass
#		if self.up == True:
#			self.x +=1
#		else:
#			self.x -=1
#
#		if self.x > 6:
#			self.up = False
#
#		if self.x < -6:
#			self.up = True
#
#		pos = self.camera.apply(constructor.stuff[1])
#		screens.adventure_screen.blit (img.arrow, (pos.x+20,pos.y+10+self.x))
#
#		pos2 = self.camera.apply(constructor.stuff[2])
#		screens.adventure_screen.blit (img.arrow, (pos2.x+12,pos2.y+10+self.x))

class _toweroutside (SuperLevel):
	def __init__ (self,lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Главная площадь -'		
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 735, 420)
		self.x = 0
		self.up = True	


	def render_location_info (self):
		
		self.son.change_text (2, 'Вы подошли к большой башне и серого камня.')
		self.son.change_text (3, 'На её вершине виден флаг с изображением волчьего оскала.')
		self.son.change_text (3, 'Здесь находится имперская администрация города.')
	
	


	def stage_content (self, hero):
		pass
		if self.up == True:
			self.x +=1
		else:
			self.x -=1

		if self.x > 6:
			self.up = False

		if self.x < -6:
			self.up = True

		pos = self.camera.apply(constructor.stuff[3])
		screens.adventure_screen.blit (img.arrow, (pos.x+20,pos.y+10+self.x))

class _tower1 (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 420)
		self.name = '- - - Башня - - -'

	def render_location_info (self):
		
		self.son.change_text (2, 'Большое холодное пространство первого этажа башни')
		self.son.change_text (3, 'сковало вашу душу страхом. Закон, власть и бюрократическая')
		self.son.change_text (4, 'сила словно растворены в самом воздухе этого помещения.')		

	def stage_content (self, hero):
		pass


class _oldhouse (SuperLevel):
	def __init__ (self, lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 680, 460)
		self.name = '- - - Старый дом  - - -'
		self.x = 0
		self.up = True

	def render_location_info (self):

		self.son.change_text (2, 'Старый удушливый и разваливающийся дом.')
		self.son.change_text (3, 'Внутри очень подозрительно. Кругом какие-то отбросы и испражнения;')
		self.son.change_text (4, 'пахнет затхлостью, смертью и разложением.')


	def stage_content (self, hero):
		pass


class _park2 (SuperLevel):
	def __init__ (self,lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Парк -'		
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city2)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 735, 420)
		self.x = 0
		self.up = True	


	def render_location_info (self):
		
		self.son.change_text (2, 'Мирный и тихий парк.')
		self.son.change_text (3, 'Здесь можно упокоиться навечно.')
		self.son.change_text (4, '')		
	


	def stage_content (self, hero):
		pass

class _strange (SuperLevel):
	def __init__ (self,lev, battle, son, control):
		SuperLevel.__init__ (self, lev, battle, son, control)
		self.name = '- Тупиковая улица -'		
		self.auto = False
		self.block_group, self.background,self.decor = self.create (create_level = constructor.create_level_city2)
		self.back = True
		self.camera = camera.Camera (self.level_width, self.level_height, 735, 420)
		self.x = 0
		self.up = True	


	def render_location_info (self):
		
		self.son.change_text (2, 'Интересное местечко.')
		self.son.change_text (3, 'Только тут никого нет. Полная тишина.')
	
	


	def stage_content (self, hero):
		pass