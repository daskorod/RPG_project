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

boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                 ('testimages/bolt_strike_0002.png', 0.1),
                                 ('testimages/bolt_strike_0003.png', 0.1),
                                 ('testimages/bolt_strike_0004.png', 0.1),
                                 ('testimages/bolt_strike_0005.png', 0.1),
                                 ('testimages/bolt_strike_0006.png', 0.1),
                                 ('testimages/bolt_strike_0007.png', 0.1),
                                 ('testimages/bolt_strike_0008.png', 0.1),
                                 ('testimages/bolt_strike_0009.png', 0.1),
                                 ('testimages/bolt_strike_0010.png', 0.1)])
boltAnim.rotate (270)
#boltAnim.play() # there is also a pause() and stop() method




class Monster(sprite.Sprite):
	def __init__(self, x, y, battle, textus, control, at, ac, hp, dem, son):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/zombi.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((120,30,200))
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
		self.agression = False
		self.add_information = "none"
		self.status = 'alive'
		self.son = son
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''
		self.hp_old = hp
		self.start_rendering = False
		self.x_mod = 0

	def death_check (self, hero):

		if self.hp <= 0:
			
			self.status = 'killed'
			hero.turn_main = True
			self.kill ()
			hero.move = True
			hero.collide_control = False
			self.son.change_text (2, "Вы убили ужасного монстра!")
			self.son.clear_text ()

	def interaction (self, hero):
		hero.move = False

	def render_hp_mod(self, position):

		if self.hp_old != self.hp:
			if self.hp_old > self.hp:
				self.hp_mod = self.hp -self.hp_old
#				self.color = (208,17,17)
				self.color = (250,250,250)
			if self.hp_old < self.hp:
				self.hp_mod =self.hp - self.hp_old 
				self.color = (17, 220, 17)
			self.hp_old = self.hp
			self.start_rendering = True
#			except:
#				pass
		if self.start_rendering == True:

			self.x_mod += 1
		#hero_screen.blit(fonts.font2.render (str(self.sp), True, (250,250,250)),(30,140))
#			adventure_screen.blit(fonts.font2.render (str(self.hp_mod), True, (self.color)),(self.rect.x, self.rect.y - 30 - self.x_mod))
			adventure_screen.blit(fonts.font4.render (str(self.hp_mod)+ ' hp', True, (self.color)),(position.x, position.y - 30 - self.x_mod))

			if self.x_mod > 100:
				self.start_rendering = False
				self.x_mod = 0

	def dialog_options (self,hero):

		if self.add_information == 'end' and self.control.k_e == True:
			hero.move = True
			self.control.k_e = False
			hero.collide_control = False

#			if self.branch_do == 'random1,2':
#				a = random.randint (1,6)
#				self.branch_do = 'done'
#				self.s = 1
#				self.n = 0
#
#				if a >3:
#					self.branch = 1
#				if a <=3:
#					self.branch = 2

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

		if self.add_information == 'war' and self.control.k_e == True:
			self.control.k_e = False
			self.agression = True
			hero.turn_main = True

#		if self.branch_do == 'random1,2' and self.control.k_e == True and self.add_information != 'end':
#			self.control.k_e = False

			a = random.randint (1,6)
			self.branch_do = 'done'
			self.s = 1
			self.n = 0

			if a >3:
				self.branch = 1
			if a <=3:
				self.branch = 2


		if self.branch_do == 'go' and self.control.k_e == True and self.add_information != 'end':
			self.control.k_e = False
			self.branch_do = 'done'
			self.branch = self.branch_id
			self.s = 1
			self.n = 0




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


class Zombi (Monster):
	pass

class Skelet (Monster):
	pass




class SkeletLord (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son)
		self.tree = text.lord
		self.lbolt = False
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/skeleton3.png')
		self.image.set_colorkey ((254,254,254))
		self.g = 1000

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
		self.image = image.load('images/wall.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "block"
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
		self.status = 'open'
	def interaction (self, hero):
		if self.status == 'open':

			if hero.control.right == True:
				hero.rect.x +=45 
			elif hero.control.left == True:
				hero.rect.x -=45 

			elif hero.control.up == True:
				hero.rect.y -=45 
			elif hero.control.down == True:
				hero.rect.y +=45 

		else:
			pass

class Candel(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = image.load('images/candel41.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = ""
		self.status = 'closed'
	def interaction (self, hero):
		if self.status == 'open':

			if hero.control.right == True:
				hero.rect.x +=45 
			elif hero.control.left == True:
				hero.rect.x -=45 

			elif hero.control.up == True:
				hero.rect.y -=45 
			elif hero.control.down == True:
				hero.rect.y +=45 

		else:
			pass


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
	def interaction (self, hero):
		hero.move = False

class Portal(sprite.Sprite):
	def __init__(self, x, y,control):
		sprite.Sprite.__init__(self)
		#self.image=image.load('images/chest2.png')
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "portal"
		self.control = control
	def interaction (self, hero):
		self.control.stage1_flag = False
		self.control.stage2_flag = True
		hero.rect.x = 0
		hero.rect.y = 0

class Bar(sprite.Sprite):
	def __init__(self, xs, ys, color):
		sprite.Sprite.__init__(self)
		self.xs = xs
		self.ys = ys
		self.image = Surface ((self.xs,self.ys))
		self.image.fill ((color))

	def interaction (self):
		pass

		