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
import classes


class Monk (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son):
		classes.Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son)
		self.tree = text.monk
		#self.lbolt = False
		self.mname = 'Отец Изольд'
		#self.image.fill ((220,130,100))
		#self.ll = False
		self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		self.image.set_colorkey ((254,254,254))
		#self.g = 1000

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