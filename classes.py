from pygame import sprite
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
import items
import text_data.well_dict
import event
from functions import end_dialog

class Zombi (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son,exp, item = items.no_item):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp, item)
		self.tree = textus
		self.image=image.load('images/zombi.png')
		self.image.set_colorkey ((255,255,255))
		self.mname = '     Зомби'
		self.order = True
		self.branch = 4
		self.order_special = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
		for i in hero.inv:
			if i.name == 'Хлам':
				self.branch = 3
		if self.order_special == False:
			for i in hero.journal:
				if i.name == 'Порядок магнитуд':
					self.branch = 0
					self.order_special = True

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

		if self.add_information == 'solve':

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
				
		if self.add_information == 'quest':
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
		self.item = items.rope
		self.quest = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
		if self.order == False:
			for i in hero.journal:
				if i.name == 'Порядок магнитуд':
					self.branch = 1
					self.order = True
		for i in hero.quest:
			if i == 'axe':
				if items.old_axe in hero.inv:

					self.branch = 3
				else:
					self.branch = 2
	def dialog_special (self, hero):

		if self.add_information == 'fault' and self.control.k_e == True:
			functions.war(self,hero)

		elif self.add_information == 'turn' and self.control.k_e == True:


			if hero.sp > random.randint(1,6):
				hero.inv.append (self.item)
				hero.dustAnim.play()
				hero.son.clear_text ()
				hero.son.change_text (3, 'Скелет рассыпается в прах.')
				hero.son.change_text (4, 'В куче праха вы видите верёвку, которую забираете с собой.')
				self.kill()
				end_dialog (self,hero)
				hero.char_value['2exp'] += 60				

			elif hero.sp < random.randint(1,6):
				self.add_information = 'fault'
				hero.son.clear_text ()
				hero.son.change_text (3, 'Вы чувствуете страх и неуверенность, ваши слова звучат фальшиво.')
				hero.son.change_text (4, 'Вы видите как зловещий череп ухмыляется. Вы перестаёте понимать')
				hero.son.change_text (5, 'его речь. Теперь это для вас лишь злобное чудовище.')

				hero.son.change_text (5, 'Нажмите E')


		elif self.add_information == 'solve' and self.quest == False:
			self.quest = True
			self.hp = self.hp//3

		elif self.add_information == 'solve'  and self.control.k_e == True:

			self.son.clear_text ()
			self.son.change_text(2, 'Вы помогли скелету в его странных стремлениях')	
			self.son.change_text(3, '+ 50 опыта.')	
			self.son.change_text(5, 'Вы получаете вещь и это: %s' % self.item.name.lower())
			self.son.change_text(4, 'Вы отдали скелету нечто: %s' % items.old_axe.name.lower())	



			hero.inv.remove(items.old_axe)
			hero.inv.append(self.item)
			self.item = items.old_axe
			hero.char_value['2exp'] +=50
			self.rect.x = self.rect.x + 25
			end_dialog (self,hero)
				
		elif self.add_information == 'quest'and self.control.k_e == True:
			hero.quest['axe'] = 'is'
			self.son.clear_text ()
			self.son.change_text(3, 'Вы подписались на то, что найдёте топор, коим скелет')	
			self.son.change_text(4, 'был убит. Где ж его теперь сыскать-то?')
			end_dialog (self,hero)









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

class PlatformBlack(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)

		self.image = Surface ((45,45))
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
		hero.son.change_text (1, 'Тьма.')

class Nothing(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)

		self.image = Surface ((1,1))
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
		hero.son.change_text (1, 'Нет прохода')

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
		#self.image_set = img.stone_wall_tavern
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

class TavernWall (Platform):
	def __init__ (self, x, y, form):
		Platform.__init__ (self, x,y)
		self.form_number = form
		self.image = img.stone_wall_tavern[self.form_number]

	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (3, random.choice (['Каменная кладка, жирная от сальных рук и свечной копоти.', 'Деревянные балки заоптились от времени чадом свечей.',"Стена как стена, добротная крепкая, приятная на ощупь.", "Ничего интересного - просто стена из какого-то грубо обработанного камня."]) )



class WoodFloor(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = self.random(img.pave_tavern)
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

class DingSpecial(sprite.Sprite):
	def __init__(self, x, y, imagee, text, dialog, interaction_add):
		sprite.Sprite.__init__(self)
		self.image = imagee
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'

		self.dialog = dialog
		self.interaction_add = interaction_add

		#conversation data
		self.tree = text
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
		self.interaction_add(self,hero)

	def dialog_special (self, hero):
		pass

	def dialog_options (self,hero):
		self.dialog_special (hero)
		self.dialog(self, hero)


class Throne(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/tiles/throne.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'

		#conversation data
		self.tree = text.door_gold
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

		if self.add_information == 'key':
			for i in hero.inv:
				if i.name == 'Серебряный ключ':
					for i in hero.inv:
						if i.name ==  'Золотой ключ':
							hero.move = True
							hero.control.k_e = False
							hero.son.clear_text ()
							hero.son.change_text (1, 'Вы вставили серебряный и золотой ключи в замочные скважины и провернули их.')
							hero.son.change_text (2, 'Раздался лёгкий щелчок и дверь отворилась.')

							hero.son.change_text (4, 'Вы открыли эту жалкую дверь!')
							self.kill ()
							hero.collide_control = False
							hero.start_conv = True
							hero.char_value['2exp']+=50
							break
					else:
						hero.move = True
						hero.control.k_e = False
						hero.son.clear_text ()
						hero.son.change_text (1, 'Один из ключей, который вы вставили подошёл.')
						hero.son.change_text (2, 'К сожалению, там две замочных скважины, а значит и два замка.')
						hero.son.change_text (3, 'Не переживайте, поищите ещё. Может что и найдёте.')
						hero.collide_control = False
						hero.start_conv = True

				elif i.name == 'Золотой ключ':
					for i in hero.inv:
						if i.name ==  'Серебряный ключ':
							hero.move = True
							hero.control.k_e = False
							hero.son.clear_text ()
							hero.son.change_text (1, 'Вы вставили серебряный и золотой ключи в замочные скважины и провернули их.')
							hero.son.change_text (2, 'Раздался лёгкий щелчок и дверь отворилась.')

							hero.son.change_text (4, 'Вы открыли эту жалкую дверь!')
							self.kill ()
							hero.collide_control = False
							hero.start_conv = True
							hero.char_value['2exp']+=50
							break
					else:
						hero.move = True
						hero.control.k_e = False
						hero.son.clear_text ()
						hero.son.change_text (1, 'Один из ключей, который вы вставили подошёл.')
						hero.son.change_text (2, 'К сожалению, там две замочных скважины, а значит и два замка.')
						hero.son.change_text (3, 'Не переживайте, поищите ещё. Может что и найдёте.')
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


class GoldDoor(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/door_gold.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'

		#conversation data
		self.tree = text.door_gold
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def interaction (self, hero):
		for i in hero.inv:
			if i.name == 'Серебряный ключ' or i.name == 'Золотой ключ':
				self.branch = 1
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

		if self.add_information == 'key':
			for i in hero.inv:
				if i.name == 'Серебряный ключ':
					for i in hero.inv:
						if i.name ==  'Золотой ключ':
							hero.move = True
							hero.control.k_e = False
							hero.son.clear_text ()
							hero.son.change_text (1, 'Вы вставили серебряный и золотой ключи в замочные скважины и провернули их.')
							hero.son.change_text (2, 'Раздался лёгкий щелчок и дверь отворилась.')

							hero.son.change_text (4, 'Вы открыли эту жалкую дверь!')
							self.kill ()
							hero.collide_control = False
							hero.start_conv = True
							hero.char_value['2exp']+=50
							break
					else:
						hero.move = True
						hero.control.k_e = False
						hero.son.clear_text ()
						hero.son.change_text (1, 'Один из ключей, который вы вставили подошёл.')
						hero.son.change_text (2, 'К сожалению, там две замочных скважины, а значит и два замка.')
						hero.son.change_text (3, 'Не переживайте, поищите ещё. Может что и найдёте.')
						hero.collide_control = False
						hero.start_conv = True

				elif i.name == 'Золотой ключ':
					for i in hero.inv:
						if i.name ==  'Серебряный ключ':
							hero.move = True
							hero.control.k_e = False
							hero.son.clear_text ()
							hero.son.change_text (1, 'Вы вставили серебряный и золотой ключи в замочные скважины и провернули их.')
							hero.son.change_text (2, 'Раздался лёгкий щелчок и дверь отворилась.')

							hero.son.change_text (4, 'Вы открыли эту жалкую дверь!')
							self.kill ()
							hero.collide_control = False
							hero.start_conv = True
							hero.char_value['2exp']+=50
							break
					else:
						hero.move = True
						hero.control.k_e = False
						hero.son.clear_text ()
						hero.son.change_text (1, 'Один из ключей, который вы вставили подошёл.')
						hero.son.change_text (2, 'К сожалению, там две замочных скважины, а значит и два замка.')
						hero.son.change_text (3, 'Не переживайте, поищите ещё. Может что и найдёте.')
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
	#	hero.char_value['2exp'] += 50


class Cupboard (Platform):
	def __init__(self, x, y):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load('images/tiles/books.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'
	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, 'Книжный шкаф. Очень старый.')
		hero.son.change_text (2, 'На полках пусто, нет ничего интересного.')
		#hero.char_value['2exp'] += 50


class Cupboard2 (Platform):
	def __init__(self, x, y):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load('images/tiles/books.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect = self.image.get_rect()

		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'
	def interaction (self,hero):
		Platform.interaction (self, hero)
		hero.son.change_text (1, 'Книжный шкаф. Очень старый.')
		#hero.char_value['2exp'] += 50



class Well(Platform):
	def __init__(self, x, y):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.image = image.load('images/tiles/well.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'

		#conversation data
		self.tree = text_data.well_dict.text
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def dialog_options (self,hero):	
		#self.dialog_special (hero)
		if self.add_information == 'drink' and hero.control.k_e == True:
			if random.randint(1,6)>hero.sp:

				hero.move = True
				hero.control.k_e = False
	
				hero.son.clear_text ()
				hero.son.change_text (4, 'Вы чувствуете упадок сил, словно из вас отжали все соки.')
				hero.hp = 1
				self.s = 1
				self.n = 0

	
				hero.collide_control = False
				hero.start_conv = True
			else:
				self.s = 1
				self.n = 0
				hero.move = True
				hero.control.k_e = False
	
				hero.son.clear_text ()
				hero.son.change_text (4, 'Вы чувствуете себя нехорошо, но ваша вера придаёт вам надежду.')
	
				hero.collide_control = False
				hero.start_conv = True				

		elif self.add_information == 'take' and hero.control.k_e == True:

				if items.death_water in hero.inv:

					hero.son.clear_text ()
					hero.son.change_text (4, 'Вы обновили воду в своей фляжке.')
					
					hero.move = True
					hero.control.k_e = False
					hero.collide_control = False
					hero.start_conv = True
					hero.view.a = 0
					self.s = 1
					self.n = 0

					
				else:

					hero.inv.append(items.death_water)
					hero.move = True
					hero.control.k_e = False
					hero.son.clear_text ()					
					hero.son.change_text (4, 'Вы налили воду из колодца в свою фляжку.')
					hero.son.change_text (5, 'Получен новый предмет!')
					hero.collide_control = False
					hero.start_conv = True
					hero.view.a = 0
					self.s = 1
					self.n = 0

		elif self.add_information == 'infinity' and hero.control.k_e == True:
			hero.hp = 0
			hero.check_for_death()
			hero.move = False
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0

		 		
		elif self.add_information == 'end':

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			#self.branch = 0
		 		

	def interaction (self,hero):
		for i in hero.inv:
			if i.name == 'Верёвка':
				self.branch = 1
		Platform.interaction (self, hero)
		hero.move = False
		hero.collide_control = True

		#hero.son.change_text (1, 'Вот вода, а вот и колодец! Напейся.')




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
		self.image.set_colorkey ((0,127,14))
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

class Obstacle(Platform):
	def __init__(self, x, y, random_set):
		#sprite.Sprite.__init__(self)
		Platform.__init__(self, x, y)
		self.choice = random.choice(random_set)		
		self.image = self.choice[0]
		self.image.set_colorkey ((255,255,255))

		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.text = self.choice[1]
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
			img.fireAnim.play ()

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

#test treasure chest
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

#BASIC CHEST

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
		self.gold = random.randint(1,50)
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

			hero.son.change_text_tree (hero.view.render_text ('В сундуке находится: ' + self.items_name, 'Нажмите E, чтобы всё забрать...'))

		if self.add_information == 'end_chest' and hero.control.k_e == True:
			end_dialog (self,hero)
			hero.son.clear_text ()


			self.kill ()
			hero.son.change_text (3, 'Вы взяли все вещи...')
			hero.son.change_text (4, 'Вы нашли немного денег: %s ' % str(self.gold))	
			hero.gold += self.gold		
			for i in self.inside:
				hero.inv.append(i)



		if self.add_information == 'end' and hero.control.k_e == True:

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0

#quest chest for the sad zombie
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

			hero.son.change_text_tree (hero.view.render_text ('В сундуке находится: ' + self.items_name, 'Нажмите E, чтобы всё забрать...'))

		if self.add_information == 'end_chest':
			hero.move = True
			hero.control.k_e = False
			hero.son.clear_text ()
			hero.collide_control = False
			hero.start_conv = True

			self.kill ()
			hero.son.change_text (4, 'Вы взяли все вещи...')
			for i in self.inside:
				hero.inv.append(i)

		if self.add_information == 'end':

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0

#class Portal2(sprite.Sprite):
#	def __init__(self, x, y,control):
#		sprite.Sprite.__init__(self)
#		self.image=image.load('images/portal.png')
#		#self.image.set_colorkey ((255,255,255))
#		#self.image = Surface ((45,45))
#		#self.image.fill ((200,30,70))
#		self.rect = Rect (0,0, 45,45)
#		self.rect.x = x
#		self.rect.y = y
#		self.name = "portal"
#		self.control = control
#	def interaction (self, hero):
#		#self.control.stage1_flag = False
#		#self.control.stage2_flag = True
#		hero.location = hero.locations_dict['end']
#		hero.rect.x = 675
#		hero.rect.y = 180
#		#hero.son.change_text (1, self.description)
#
#class Portal (sprite.Sprite):
#	def __init__(self, x, y,control):
#		sprite.Sprite.__init__(self)
#		self.image=image.load('images/portal.png')
#		#self.image.set_colorkey ((255,255,255))
#		#self.image = Surface ((45,45))
#		#self.image.fill ((200,30,70))
#		self.rect = Rect (0,0, 45,45)
#		self.rect.x = x
#		self.rect.y = y
#		self.name = "portal"
#		self.control = control
#	def interaction (self, hero):
#		#self.control.stage2_flag = False
#		#self.control.stage1_flag = True
#		hero.location = hero.locations_dict['1']
#		hero.rect.x = 45
#		hero.rect.y = 45
#
#class PortalS (sprite.Sprite):
#	def __init__(self, x, y, loc, coordinates):
#		sprite.Sprite.__init__(self)
#		self.image=image.load('images/portal.png')
#		self.rect = Rect (0,0, 45,45)
#		self.rect.x = x
#		self.rect.y = y
#		self.name = "portal"
#		self.loc_num = loc
#		self.px, self.py = coordinates
#
#	def interaction (self, hero):
#		hero.location = hero.locations_dict[self.loc_num]
#		hero.rect.x, hero.rect.y = self.px*45, self.py*45

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
		self.x = 0
		self.up = True
		self.y = 0
	def animation(self, camera):
		#self.y = random.randint(1,3)
		
		if self.up == True:
			self.x +=1
		else:
			self.x -=1

		if self.x > 6:
			self.up = False
			#self.y = random.randint(1,6)
		if self.x < -6:
			self.up = True		
			#self.y = random.randint(1,6)
		pos = camera.apply(self)

		if self.exitside == 'L':

			screens.adventure_screen.blit (img.arrowr, (pos.x+10+self.x,pos.y+10+self.y))

		elif self.exitside == 'R':

			screens.adventure_screen.blit (img.arrowl, (pos.x+10+self.x,pos.y+10+self.y))

		elif self.exitside == 'D':

			screens.adventure_screen.blit (img.arrow2, (pos.x+10+self.y,pos.y+5+self.x))

		elif self.exitside == 'U':

			screens.adventure_screen.blit (img.arrowd, (pos.x+10+self.y,pos.y+5+self.x))				

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
		self.image = image.load('images/priest2.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.g = 1000
		self.order = True
		self.quest = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
		if self.quest == True:
			for i in hero.quest.keys():
				if i == 'main':
					for a in hero.inv:
						if a == items.dogma:
							self.branch = 2
							#self.quest = False
							self.s = 1
							self.n = 0
							break

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

		if self.add_information == 'dogma' and self.control.k_e == True:
			hero.char_value['2exp'] +=500
			hero.etwas = event.final
			hero.inv.remove(items.dogma)
			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


		if self.add_information == 'quest':
			self.quest = True
			hero.quest['main'] = 'take'
			#hero.etwas = event.final

			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.move = True
			hero.collide_control = False
			hero.start_conv = True


	def battle_action (self, hero):

		if self.lbolt == True:

			self.lbolt = False



			
#			x_hero.x -=49
#			x_hero.y -=80
#			classes.boltAnim.blit (adventure_screen, (x_hero.x - 49, x_hero.y - 80))
			img.fireAnim.play ()


		if hero.monster_turn == True:
			self.son.clear_text ()
			a = random.randint (1,3)
			#boltAnim.blit (adventure_screen, (100, 100))
		
			self.son.change_text (1, 'Священник шепчет слова молитвы:')
			self.son.change_text (2, '"Возврати меч твой в его место, ибо')
			self.son.change_text (3, 'все, взявшие меч, мечом погибнут." ... ')
			self.son.change_text (5, 'Нажмите Е')
			#self.lbolt = True
			self.ll = True

		if hero.monster_turn == True and self.ll == True and self.control.k_e == True:
			self.ll = False
			self.lbolt = True
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
