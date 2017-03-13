from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import Surface
import pyganim
import screens
import fonts
import functions
import text
from screens import *
from constants import *
import random
#from functions import self.battle.render_inf




class Monster(sprite.Sprite):
	def __init__(self, x, y, battle, textus, control, at, ac, hp, dem):
		sprite.Sprite.__init__(self)
		#self.image=image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((120,30,200))
		self.a = "Я злобный монстр!"
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x*PF_WIDTH
		self.rect.y = y*PF_HEIGHT
		self.name = "monster"
		self.textus = text
		self.n = 0
		self.s = 1
		self.tree = text.zombi1
		self.at = at
		self.ac = ac
		self.hp = hp
		self.damage = dem
		self.wait_for_next_turn = False
		self.control = control
		self.battle = battle

	#def conversation (self):
		#hero.conversation (text.zombi1)

	def interaction (self):
		#screens.information_screen.blit(fonts.font1.render ((self.a), True, (250,250,250)),(0,0))
		#self.conversation ()
		pass

	def battle_action (self, hero):
		if hero.monster_turn == True:
			self.battle.clear_inf ()
			a = random.randint (1,6)
			b = random.randint (1,6)
			c = self.at + a 
			d = hero.ac + b
		
			self.battle.change_inf (1, "Атака монстра: "+str(c) + "  Защита ваша: "+ str(d))
			if c >= d:
				
				if int(c/d)>1:
					hero.hp = hero.hp - self.damage*int(c/d)
					self.battle.change_inf (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
					self.battle.change_inf (5, 'Критический урон: '+str(self.damage*int(c/d)))
					
				else:
					self.battle.change_inf (4, "Монстр попал и нанес сокрушительный удар!")
					hero.hp = hero.hp - self.damage
					self.battle.change_inf (5, 'Урон: '+str(self.damage))
			elif c<d:
				self.battle.change_inf (4, 'Вы уклонились!')	
		
			self.battle.change_inf (7, 'Нажмите Е')
			hero.monster_turn = False
			self.wait_for_next_turn = True

		if self.control.k_e == True and self.wait_for_next_turn == True:
			self.control.k_e = False
			hero.turn_main = True
			self.battle.clear_inf ()


class Platform(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		#self.image=image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "block"
	def interaction (self):
		pass

class Chest(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		#self.image=image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "chest"
	def interaction (self):
		pass
