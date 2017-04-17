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



class Bar(sprite.Sprite):
	def __init__(self, xs, ys, color):
		sprite.Sprite.__init__(self)
		self.xs = xs
		self.ys = ys
		self.image = Surface ((self.xs,self.ys))
		self.image.fill ((color))

	def interaction (self):
		pass

		

class Monster(sprite.Sprite):
	def __init__(self, x, y, battle, textus, control, at, ac, hp, dem, son):
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

		#CHAR DATA
		self.mname = '     Зомби'
		self.at = at
		self.ac = ac
		self.hp = hp
		self.damage = dem

		#conversation data
		self.tree = text.zombi1
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

		#battle data

		self.wait_for_next_turn = False
		self.battle = battle

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
			self.son.change_text (2, "Вы убили ужасного монстра!")
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
			self.son.clear_text ()
			self.control.k_e = False
			self.agression = True
			hero.turn_main = True
			hero.start_conv = True
			hero.view.a = 0

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


#		if self.branch_do == 'go' and self.control.k_e == True and self.add_information != 'end':
#			self.control.k_e = False
#			self.branch_do = 'done'
#			self.branch = self.branch_id
#			self.s = 1
#			self.n = 0




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
		self.image = image.load('images/ground.png')
		#self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "block"

	def interaction (self,hero):
		if hero.control.right == True:
			hero.rect.x -= 1
		elif hero.control.left == True:
			hero.rect.x += 1
		elif hero.control.up == True:
			hero.rect.y += 1
		elif hero.control.down == True:
			hero.rect.y -= 1

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
		if self.add_information == 'open' and hero.control.k_e == True:
			hero.move = True
			hero.control.k_e = False
			hero.son.clear_text ()
			hero.son.change_text (4, 'Дверь скрипит!')
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
		self.control.stage1_flag = False
		self.control.stage2_flag = True
		hero.rect.x = 630
		hero.rect.y = 180

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
		self.control.stage2_flag = False
		self.control.stage1_flag = True
		hero.rect.x = 45
		hero.rect.y = 45

class Bar(sprite.Sprite):
	def __init__(self, xs, ys, color):
		sprite.Sprite.__init__(self)
		self.xs = xs
		self.ys = ys
		self.image = Surface ((self.xs,self.ys))
		self.image.fill ((color))

	def interaction (self):
		pass

		