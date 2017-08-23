﻿from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import Surface
import pygame
import pyganim
import screens
import fonts
import functions
import text
from screens import *
from constants import *
import random
import controller
from monster import Monster
import img

boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                 ('testimages/bolt_strike_0002.png', 0.1),
                                 ('testimages/bolt_strike_0003.png', 0.1),
                                 ('testimages/bolt_strike_0004.png', 0.1),
                                 ('testimages/bolt_strike_0005.png', 0.1),
                                 ('testimages/bolt_strike_0006.png', 0.1),
                                 ('testimages/bolt_strike_0007.png', 0.1),
                                 ('testimages/bolt_strike_0008.png', 0.1),
                                 ('testimages/bolt_strike_0009.png', 0.1),
                                 ('testimages/bolt_strike_0010.png', 0.1)], loop=False)
boltAnim.rotate (270)
#boltAnim.play() # there is also a pause() and stop() method

fireAnim = pyganim.PygAnimation([('testimages/flame_a_0001.png', 0.2),
                                 ('testimages/flame_a_0002.png', 0.2),
                                 ('testimages/flame_a_0003.png', 0.2),
                                 ('testimages/flame_a_0004.png', 0.2),
                                 ('testimages/flame_a_0005.png', 0.2),
                                 ('testimages/flame_a_0006.png', 0.2),], loop=False)


class Zombi (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son,exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.image=image.load('images/zombi.png')
		self.image.set_colorkey ((255,255,255))
		self.mname = '     Зомби'
		self.order = False
		self.branch = 4

	def interaction (self, hero):
		Monster.interaction (self, hero)
		for i in hero.inv:
			if i.name == 'Хлам':
				self.branch = 3
		if self.order == False:
			for i in hero.journal:
				if i.name == 'Порядок магнитуд':
					self.branch = 0
					self.order = True

	def dialog_special (self, hero):
		
		if self.add_information == 'zombidead' and self.control.k_e == True:
			self.kill()
			hero.move = True
			self.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0	
			self.son.clear_text ()
			hero.char_value['2exp'] += 60
			self.son.change_text(2, 'Поздравляю, вы сделали с зомби что-то ингуманистическое!')	
			self.son.change_text(4, 'Вы получаете 60 опыта!')	
			
		if self.add_information == 'garbage':
				for i in hero.inv:
					if i.name == 'Хлам':
						hero.inv.remove(i)

		if self.add_information == 'solve' and self.control.k_e == True:

			hero.move = True
			self.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.rect.y = self.rect.y + 45
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
				
		if self.add_information == 'quest' and self.control.k_e == True:
			hero.quest['zombisad'] = 'is'
			hero.move = True
			self.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


class Skelet (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son,exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.image=image.load('images/skeleton2.png')
		self.image.set_colorkey ((255,255,255))
		self.mname = '   Скелет'
		self.order = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
		if self.order == False:
			for i in hero.journal:
				if i.name == 'Порядок магнитуд':
					self.branch = 1
					self.order = True
class SkeletLord (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = text.lord
		self.lbolt = False
		self.mname = 'Скелет Лорд'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/skeleton3.png')
		self.image.set_colorkey ((254,254,254))
		self.g = 1000

	def dialog_special (self, hero):
		if self.add_information == 'gold' and self.control.k_e == True:
			hero.move = True
			hero.gold += 20
			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (4, 'Вы получили 20 монет')
			hero.son.change_text (5, 'Ваши деньги: '+str(hero.gold))

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

	def battle_action (self, hero):
		self.g += 1
		if self.lbolt == True:
			self.g = 185

			self.lbolt = False


		if self.g > 190 and self.g< 240:
			
#			x_hero.x -=49
#			x_hero.y -=80
#			classes.boltAnim.blit (adventure_screen, (x_hero.x - 49, x_hero.y - 80))
			boltAnim.play ()
			if self.g==239:
				boltAnim.stop()

		if hero.monster_turn == True:
			self.son.clear_text ()
			a = random.randint (1,3)
			#boltAnim.blit (adventure_screen, (100, 100))
		
			self.son.change_text (1, "В руках скелета заплясали электрические разряды...")
			self.son.change_text (3, 'Нажмите Е')
		
			self.lbolt = True
			self.ll = True

		if hero.monster_turn == True and self.ll == True and self.control.k_e == True:
			self.ll = False
			self.lbolt = False
			self.son.clear_text ()
			self.son.change_text (1, "... в вас ударяет ослепительная молния.")
			self.son.change_text (2, "Вы получаете " + str(a) + ' урона')
			hero.hp -= a
			self.son.change_text (4, 'Нажмите Е')
			self.wait_for_next_turn = True
			hero.monster_turn = False
			self.control.k_e = False

		if self.control.k_e == True and self.wait_for_next_turn == True:
			
			self.wait_for_next_turn = False
			self.control.k_e = False
			hero.turn_main = True
			self.son.clear_text ()

class Platform(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/ground2.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "block"

	def interaction (self,hero):
		if hero.control.right == True:
			hero.rect.x -= hero.back_move
		elif hero.control.left == True:
			hero.rect.x += hero.back_move
		elif hero.control.up == True:
			hero.rect.y += hero.back_move
		elif hero.control.down == True:
			hero.rect.y -= hero.back_move
		hero.son.clear_text ()
		hero.son.change_text (1, 'Холодная мрачная стена, напоминает о смерти.')


class Pavestone(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/wall.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect(0,0,45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "no"



	def interaction (self,hero):
		pass


class Floor(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = self.random(img.pavestones)
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((95,95,95))
		self.rect = Rect(0,0,45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "no"

	def random(self, florlist):
		return random.choice(florlist)

	def interaction (self,hero):
		pass

class WoodFloor(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/tiles/floor.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((95,95,95))
		self.rect = Rect(0,0,45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "no"

	def random(self, florlist):
		return random.choice(florlist)

	def interaction (self,hero):
		pass

class CityFloor(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = self.random(img.pavestones_city)
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((95,95,95))
		self.rect = Rect(0,0,45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "no"

	def random(self, florlist):
		return random.choice(florlist)

	def interaction (self,hero):
		pass

class Door(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/door4.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'

		#conversation data
		self.tree = text.door
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def interaction (self, hero):

		if hero.control.right == True:
			hero.rect.x -= hero.back_move
		elif hero.control.left == True:
			hero.rect.x += hero.back_move
		elif hero.control.up == True:
			hero.rect.y += hero.back_move
		elif hero.control.down == True:
			hero.rect.y -= hero.back_move

		hero.move = False
		hero.collide_control = True


	def dialog_special (self, hero):
		pass

	def dialog_options (self,hero):
		self.dialog_special (hero)
		if self.add_information == 'open':
			hero.move = True
			hero.control.k_e = False
			hero.son.clear_text ()
			hero.son.change_text (1, 'Вы открыли эту никчёмную дверь!')
			self.kill ()
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'end':

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0


class Candel(Platform):
	def __init__(self, x, y):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load('images/candel3.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'
	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, 'Крутой подсвечник. Да и свечи ничего')
		hero.char_value['2exp'] += 50

class Table(Platform):
	def __init__(self, x, y):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load('images/tiles/table3.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, 'Добротный стол. Хоть и обшарпанный.')

class Ding(Platform):
	def __init__(self, x, y, img, text):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load(img)
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.text = text
	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, self.text)

class Chair(Platform):
	def __init__(self, x, y):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load('images/tiles/chair.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, 'Грубо сколоченный стул. Но при этом весьма прочный.')

class Marker(sprite.Sprite):
	def __init__(self,x,y):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/sword2.png')
		self.image.set_colorkey ((238,234,250))
		#self.image = Surface ((25,45))
		#self.image.fill ((150, 150, 150))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "marker"
	def interaction (self,hero):
		pass

class Trap(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = Surface ((0,0))
		#self.image=image.load('images/chest2.png')
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = str(Trap.__name__)
		self.charge = True


	def interaction (self, hero):
		if self.charge == True:
			self.charge = False
			hero.son.clear_text ()
			hero.son.change_text (4, 'Вы наступили на плиту и по вам шибанули снопы огня.')
			hero.son.change_text (5, "Больно!")
			hero.hp -=4
			fireAnim.play ()

		if hero.control.right == True:
			hero.rect.x += hero.velo
		elif hero.control.left == True:
			hero.rect.x -= hero.velo
		elif hero.control.up == True:
			hero.rect.y -= hero.velo
		elif hero.control.down == True:
			hero.rect.y += hero.velo

		hero.check_for_death()
		self.kill()

class Chest(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/chest2.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "chest"

		#conversation data
		self.tree = text.chest
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def interaction (self, hero):

		if hero.control.right == True:
			hero.rect.x -= 1
		elif hero.control.left == True:
			hero.rect.x += 1
		elif hero.control.up == True:
			hero.rect.y += 1
		elif hero.control.down == True:
			hero.rect.y -= 1
		hero.move = False
		hero.collide_control = True

	def dialog_special (self, hero):
		pass

	def dialog_options (self,hero):
		self.dialog_special (hero)
		if self.add_information == 'end_chest' and hero.control.k_e == True:
			hero.move = True
			hero.gold += 20
			hero.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (4, 'Вы получили 10 монет')
			hero.son.change_text (5, 'Ваши деньги: '+str(hero.gold))
			self.kill ()

			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'end' and hero.control.k_e == True:

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0

class MinorChest(sprite.Sprite):
	def __init__(self, x, y, status, *item):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/chest2.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "chest"
		self.status = status
		self.items = item
		self.inside = []
		for i in self.items:
			self.inside.append (i)

		self.items_name = ''

		for i in self.items:
			self.items_name = self.items_name + i.name + ', '
		self.items_name = self.items_name[:-2] + '.'

		#conversation data
		self.tree = text.mchest
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def interaction (self, hero):

		if hero.control.right == True:
			hero.rect.x -= 1
		elif hero.control.left == True:
			hero.rect.x += 1
		elif hero.control.up == True:
			hero.rect.y += 1
		elif hero.control.down == True:
			hero.rect.y -= 1
		hero.move = False
		hero.collide_control = True

	def dialog_special (self, hero):
		pass

	def dialog_options (self,hero):

		self.dialog_special (hero)
		if self.add_information == 'end_chest':

			hero.son.change_text_tree (hero.view.render_text ('В сундуке находится: ' + self.items_name, 'Нажмите E, чтобы забрать вещи...'))
		if self.add_information == 'end_chest' and hero.control.k_e == True:
			hero.move = True

			hero.control.k_e = False

			hero.son.clear_text ()




			hero.collide_control = False
			hero.start_conv = True

			empty_space = 0
			for item in hero.inv:
				if item.name == 'Ничего':
					empty_space += 1

			if empty_space >= len (self.inside):
				self.kill ()
				hero.son.change_text (4, 'Вы взяли все вещи...')
				counter = 0
				for i in self.inside:
					for item in hero.inv:
						if item.name == 'Ничего':
							hero.inv.pop (counter)
							hero.inv.insert (counter, i)
							break
						counter += 1
					counter = 0

			if empty_space < len (self.inside):
				hero.son.change_text (4, 'Вы взяли не всё, слишком много добра. Не убирается...')
				counter = 0
				taken = 0
				for i in self.inside:
					if taken > empty_space:
						break
					for item in hero.inv:
						if item.name == 'Ничего':
							hero.inv.pop (counter)
							hero.inv.insert (counter, i)
							self.inside.remove(i)
							taken += 1
							break
						counter += 1
					counter = 0

				self.items_name = ''
				for i in self.inside:
					self.items_name = self.items_name + i.name + ', '
				self.items_name = self.items_name[:-2] + '.'

		if self.add_information == 'end' and hero.control.k_e == True:

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0

class MinorChest2(sprite.Sprite):
	def __init__(self, x, y, status, *item):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/chest2.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "chest"
		self.status = status
		self.items = item
		self.inside = []
		for i in self.items:
			self.inside.append (i)

		self.items_name = ''

		for i in self.items:
			self.items_name = self.items_name + i.name + ', '
		self.items_name = self.items_name[:-2] + '.'

		#conversation data
		self.tree = text.mchest2
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def interaction (self, hero):

		if hero.control.right == True:
			hero.rect.x -= 1
		elif hero.control.left == True:
			hero.rect.x += 1
		elif hero.control.up == True:
			hero.rect.y += 1
		elif hero.control.down == True:
			hero.rect.y -= 1
		hero.move = False
		hero.collide_control = True

		if 'zombisad' in hero.quest:
			self.branch = 1
	def dialog_special (self, hero):
		pass

	def dialog_options (self,hero):
		MinorChest.dialog_options(self, hero)


		self.dialog_special (hero)
		if self.add_information == 'end_chest':

			hero.son.change_text_tree (hero.view.render_text ('В сундуке находится: ' + self.items_name, 'Нажмите E, чтобы забрать вещи...'))
		if self.add_information == 'end_chest' and hero.control.k_e == True:
			hero.move = True

			hero.control.k_e = False

			hero.son.clear_text ()




			hero.collide_control = False
			hero.start_conv = True

			empty_space = 0
			for item in hero.inv:
				if item.name == 'Ничего':
					empty_space += 1

			if empty_space >= len (self.inside):
				self.kill ()
				hero.son.change_text (4, 'Вы взяли все вещи...')
				counter = 0
				for i in self.inside:
					for item in hero.inv:
						if item.name == 'Ничего':
							hero.inv.pop (counter)
							hero.inv.insert (counter, i)
							break
						counter += 1
					counter = 0

			if empty_space < len (self.inside):
				hero.son.change_text (4, 'Вы взяли не всё, слишком много добра. Не убирается...')
				counter = 0
				taken = 0
				for i in self.inside:
					if taken > empty_space:
						break
					for item in hero.inv:
						if item.name == 'Ничего':
							hero.inv.pop (counter)
							hero.inv.insert (counter, i)
							self.inside.remove(i)
							taken += 1
							break
						counter += 1
					counter = 0

				self.items_name = ''
				for i in self.inside:
					self.items_name = self.items_name + i.name + ', '
				self.items_name = self.items_name[:-2] + '.'

		if self.add_information == 'end' and hero.control.k_e == True:

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0


class Portal2(sprite.Sprite):
	def __init__(self, x, y,control):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/portal.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "portal"
		self.control = control
	def interaction (self, hero):
		#self.control.stage1_flag = False
		#self.control.stage2_flag = True
		hero.location = hero.locations_dict['end']
		hero.rect.x = 675
		hero.rect.y = 180
		#hero.son.change_text (1, self.description)

class Portal (sprite.Sprite):
	def __init__(self, x, y,control):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/portal.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "portal"
		self.control = control
	def interaction (self, hero):
		#self.control.stage2_flag = False
		#self.control.stage1_flag = True
		hero.location = hero.locations_dict['1']
		hero.rect.x = 45
		hero.rect.y = 45

class PortalS (sprite.Sprite):
	def __init__(self, x, y, loc, coordinates):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/portal.png')
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "portal"
		self.loc_num = loc
		self.px, self.py = coordinates

	def interaction (self, hero):
		hero.location = hero.locations_dict[self.loc_num]
		hero.rect.x, hero.rect.y = self.px*45, self.py*45

class PortalLink (sprite.Sprite):
	def __init__(self, x, y, name, link, exitside, locationname):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/portal.png')
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = name
		self.link = link
		self.exitside = exitside
		self.locationname = locationname

	def interaction (self, hero):
		portal = self.find_object_of_bounded_portal(hero)
		hero.location = hero.locations_dict[portal.locationname]
		hero.rect.x, hero.rect.y = portal.entrance()

	def find_object_of_bounded_portal(self, hero):
		for i in hero.locations_dict.keys():
			for x in hero.locations_dict[i].block_group:
				try:
					if x.name == self.link:
						return x
				except:
					pass

	def entrance(self):

		if self.exitside == 'L':
			xs = self.rect.x - 45
			ys = self.rect.y
		elif self.exitside == 'R':
			xs = 45+self.rect.x
			ys = self.rect.y
			
		elif self.exitside == 'U':
			xs = self.rect.x
			ys = self.rect.y -45

		elif self.exitside == 'D':
			xs = self.rect.x
			ys = self.rect.y +45

		return xs,ys 

class IndexS (Platform):
	def __init__(self, x, y, text):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		#self.image = image.load('images/candel3.png')
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.text = text

	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, self.text)

class Bar(sprite.Sprite):
	def __init__(self, xs, ys, color):
		sprite.Sprite.__init__(self)
		self.xs = xs
		self.ys = ys
		self.image = Surface ((self.xs,self.ys))
		self.image.fill ((color))

	def interaction (self):
		pass

class Monk (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Отец Изольд'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		self.image.set_colorkey ((254,254,254))
		self.g = 1000

	def dialog_special (self, hero):
		if self.add_information == 'gold' and self.control.k_e == True:
			hero.move = True
			hero.gold += 20
			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (4, 'Вы получили 20 монет')
			hero.son.change_text (5, 'Ваши деньги: '+str(hero.gold))

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

	def battle_action (self, hero):
		self.g += 1
		if self.lbolt == True:
			self.g = 185

			self.lbolt = False


		if self.g > 190 and self.g< 240:
			
#			x_hero.x -=49
#			x_hero.y -=80
#			classes.boltAnim.blit (adventure_screen, (x_hero.x - 49, x_hero.y - 80))
			boltAnim.play ()
			if self.g==239:
				boltAnim.stop()

		if hero.monster_turn == True:
			self.son.clear_text ()
			a = random.randint (1,3)
			#boltAnim.blit (adventure_screen, (100, 100))
		
			self.son.change_text (1, 'Священник шепчет слова молитвы:')
			self.son.change_text (2, '"Возврати меч твой в его место, ибо')
			self.son.change_text (3, 'все, взявшие меч, мечом погибнут." ... ')
			self.son.change_text (5, 'Нажмите Е')
			self.lbolt = True
			self.ll = True

		if hero.monster_turn == True and self.ll == True and self.control.k_e == True:
			self.ll = False
			self.lbolt = False
			self.son.clear_text ()
			self.son.change_text (1, "... вас охватывает пламя.")
			self.son.change_text (2, "Вы получаете " + str(a) + ' урона')
			hero.hp -= a
			self.son.change_text (4, 'Нажмите Е')
			self.wait_for_next_turn = True
			hero.monster_turn = False
			self.control.k_e = False

		if self.control.k_e == True and self.wait_for_next_turn == True:
			
			self.wait_for_next_turn = False
			self.control.k_e = False
			hero.turn_main = True
			self.son.clear_text ()
