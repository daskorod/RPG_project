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

class Bar(sprite.Sprite):
	def __init__(self, xs, ys, color):
		sprite.Sprite.__init__(self)
		self.xs = xs
		self.ys = ys
		self.image = Surface ((self.xs,self.ys))
		self.image.fill ((color))

	def interaction (self):
		pass
		
class Monster (sprite.Sprite):
	def __init__(self, x, y, battle, textus, control, at, ac, hp, dem, son, exp, special_opt = False):
		sprite.Sprite.__init__(self)
		#self.image = Surface ((45,45))
		#self.image.fill ((120,30,200))

		#BASE DATA
		self.image=image.load('images/zombi.png')
		self.image.set_colorkey ((255,255,255))


		self.rect = Rect (0,0, 45,45)
		self.rect.x = x*PF_WIDTH
		self.rect.y = y*PF_HEIGHT

		self.control = control
		self.son = son
		self.battle = battle

		#CHAR DATA
		self.mname = '     Зомби'
		self.at = at
		self.ac = ac
		self.hp = hp
		self.damage = dem
		self.exp = exp

		#conversation data
		
		
		self.tree = text.zombi1
		if special_opt == True:
			self.tree = textus
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

		#battle data

		self.wait_for_next_turn = False


		#TECH DATA
		self.hp_old = hp	
		self.start_rendering = False
		self.x_mod = 0
		self.status = 'alive'

		#RENDER BATTLE INTERFACE DATA
		self.monsterList2 = [self.at, self.ac, self.hp, self.damage]
		self.m1 = ''
		self.m2 = 'А:'
		self.m3 = 'З:'
		self.m4 = 'Ж:'
		self.m5 = 'У:'
		self.monsterList = [self.m2, self.m3, self.m4, self.m5]
		self.icon = pygame.image.load ('images/zombi_icon.png')
		self.hp_bar =Bar (12,15, red)
		self.at_ic = pygame.image.load ('images/at.png')
		self.ac_ic = pygame.image.load ('images/ac.png')

	def render_monster_inf (self):

		instrumental_screen.blit (monster_screen, (678,15))
		monster_screen.fill ((black))
		monster_screen.blit (self.icon, (15,30))

		monster_screen.blit(fonts.font3.render (str(self.mname), True, (250,250,250)),(0, 0))
		

		n = 0

		for i in range (0, self.hp):
			monster_screen.blit(self.hp_bar.image, (135, 120- n))
			n = n+15
		monster_screen.blit(fonts.font2.render (str(self.hp), True, (250,250,250)),(130,140))


		monster_screen.blit(fonts.font5.render (str(self.at) +'/'+str(self.damage) , True, (250,250,250)),(25,140))
		monster_screen.blit(fonts.font5.render (str(self.ac), True, (250,250,250)),(90,140))
		monster_screen.blit(self.at_ic,(5,145))
		monster_screen.blit(self.ac_ic,(75,145))

	def death_check (self, hero):

		if self.hp <= 0:
			
			self.status = 'killed'
			hero.turn_main = True
			self.kill ()
			hero.move = True
			hero.collide_control = False
			hero.char_value['2exp'] += self.exp
			self.son.change_text (2, "Вы убили ужасного монстра!")
			self.son.change_text (3, "Вы получаете опыт: %s " % self.exp)
			self.son.clear_text ()

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

	def render_hp_mod(self, position):

		if self.hp_old != self.hp:
			if self.hp_old > self.hp:
				self.hp_mod = self.hp -self.hp_old
				self.color = (250,250,250)
			if self.hp_old < self.hp:
				self.hp_mod =self.hp - self.hp_old 
				self.color = (17, 220, 17)
			self.hp_old = self.hp
			self.start_rendering = True
		if self.start_rendering == True:

			self.x_mod += 1
		#hero_screen.blit(fonts.font2.render (str(self.sp), True, (250,250,250)),(30,140))
#			adventure_screen.blit(fonts.font2.render (str(self.hp_mod), True, (self.color)),(self.rect.x, self.rect.y - 30 - self.x_mod))
			adventure_screen.blit(fonts.font4.render (str(self.hp_mod)+ ' hp', True, (self.color)),(position.x, position.y - 30 - self.x_mod))

			if self.x_mod > 100:
				self.start_rendering = False
				self.x_mod = 0

	# DIALOG METHODS


	def dialog_special (self, hero):

		pass


	def dialog_options (self,hero):
		self.dialog_special (hero)

		if self.add_information == 'end' and self.control.k_e == True:

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

		if self.add_information == 'war' and self.control.k_e == True:
			self.son.clear_text ()
			self.control.k_e = False
			self.agression = True
			hero.turn_main = True
			hero.start_conv = True
			hero.view.a = 0

			a = random.randint (1,6)
			self.branch_do = 'done'
			self.s = 1
			self.n = 0

			if a >3:
				self.branch = 1
			if a <=3:
				self.branch = 2


	def battle_action (self, hero):
		if hero.monster_turn == True:
			self.son.clear_text ()
			a = random.randint (1,6)
			b = random.randint (1,6)
			c = self.at + a 
			d = hero.ac + b
		
			self.son.change_text (1, "Атака монстра: "+str(c) + "  Защита ваша: "+ str(d))
			if c >= d:
				
				if int(c/d)>1:
					hero.hp = hero.hp - self.damage*int(c/d)
					self.son.change_text (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
					self.son.change_text (5, 'Критический урон: '+str(self.damage*int(c/d)))
					
				else:
					self.son.change_text (4, "Монстр попал и нанес сокрушительный удар!")
					hero.hp = hero.hp - self.damage
					self.son.change_text (5, 'Урон: '+str(self.damage))
			elif c<d:
				self.son.change_text (4, 'Вы уклонились!')	
		
			self.son.change_text (7, 'Нажмите Е')
			hero.monster_turn = False
			self.wait_for_next_turn = True

		if self.control.k_e == True and self.wait_for_next_turn == True:
			self.control.k_e = False
			hero.turn_main = True
			self.son.clear_text ()
