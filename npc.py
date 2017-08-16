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
import classes

class Monk2 (classes.Monk):
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
			self.control.k_e = False
			if hero.gold >= 20:
				hero.gold -= 20

				self.branch = 4
				self.s = 1
				self.n = 0

			else:
				self.branch = 6
				self.s = 1
				self.n = 0
						

		if self.add_information == 'hit' and self.control.k_e == True:
			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Потирая кулак вы отошли во свояси.')
			hero.son.change_text (3, 'Посетители таверны даже не отреагировали.')
			hero.son.change_text (4, 'Они просто пили своё пиво.')
			hero.son.change_text (5, 'А вас кольнула булавочкой совесть: правильно ли?')


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'passage' and self.control.k_e == True:


			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


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

class Barmen (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Бармен'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		#self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0

	def pay (self, add_information, quantity, where_sucsess, where_not_sucsess, hero):
		if self.add_information == add_information:
			if hero.gold >= quantity:
				hero.gold -= quantity

				self.branch = where_sucsess
				self.s = 1
				self.n = 0

			else:
				self.branch = where_not_sucsess
				self.s = 1
				self.n = 0
				self.matter = where_sucsess
			

	def dialog_special (self, hero):
		self.pay ('pay_for_sleep', 100, 2, 1, hero)
		

		self.pay ('pay_for_food', 40, 3, 1, hero)
		

		self.pay ('pay_for_drink', 20, 4, 1, hero)
		

		if self.add_information == 'sleep' and self.control.k_e == True:
			self.control.k_e = False

			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы отлично отдохнули.')
			hero.son.change_text (3, 'Ваши силы восстанавливаются.')
			hero.son.change_text (4, 'Хотя, тяжесть грехов и старые раны так просто не исцелить.')
			hero.son.change_text (5, 'Но вы готовы к новому дню!')

			hero.sp = hero.char_value['6sp']
			hero.hp = hero.char_value['5hp']

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

			hero.collide_control = False
			hero.start_conv = True								

		if self.add_information == 'pray':
			if random.randint(1,6) < hero.sp+6:
				self.branch = 6
				self.s = 1
				self.n = 0

			else:
				self.branch = 5
				self.s = 1
				self.n = 0		

		if self.add_information == 'pray_ok' and self.control.k_e == True:
			self.control.k_e = False

			self.branch = self.matter
			self.s = 1
			self.n = 0



		if self.add_information == 'food' and self.control.k_e == True:
			self.control.k_e = False

			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы неплохо поели и частично восстановили свои силы.')


			if hero.hp < hero.char_value['5hp']:
				hero.hp = hero.hp + 1

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

			hero.collide_control = False
			hero.start_conv = True			

		if self.add_information == 'passage' and self.control.k_e == True:


			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


