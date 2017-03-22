import pygame
import pyganim
import functions
import screens
import fonts
import random
import classes
from screens import *
from constants import *

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()


class Hero(pygame.sprite.Sprite):

	def __init__(self, x, y, battle, control, compose_text, at, ac, hp, dem ,son):
		pygame.sprite.Sprite.__init__(self)

		#self.image=pygame.image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.control = control
		self.battle = battle
		self.name = 'Рихтер'
		self.image = pygame.Surface ((45,45))
		#self.image = svin_anim.getImagesFromSpriteSheet()
		self.image.fill ((100,200,230))
		self.sp = 2
		self.rect = pygame.Rect (x,y, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.collision = False
		self.collide_control = False
		self.n = 0
		self.s = 1
		self.view = compose_text
		self.add_information = 'nothing'
		self.assault = False
		self.flee = False
		self.special = False
		self.at = at
		self.ac = ac
		self.hp = hp
		self.damage = dem
		self.turn_main = True
		self.attack_roll = False
		self.wait_for_next_turn = False
		self.monster_turn = False
		self.mx = 50
		self.my = 50		
		self.marker = classes.Marker (self.mx,self.my)
		self.go_left = False
		self.dice_fun = False
		self.dice_value = 0
		self.status = "alive"
		self.move = True
		self.hp_bar = classes.Bar (12,15, red)
		self.sp_bar = classes.Bar (12,15, blue)
		self.son = son

	def conversation (self, tree, interlocutor):

		text_massive, self.etwas.add_information, text_massive_answer = tree[interlocutor.n]
		
		self.view.render_text (text_massive, text_massive_answer)

		if self.etwas.add_information == 'war' and self.control.k_e == True:
			self.control.k_e = False
			self.etwas.agression = True

		if self.control.k_1 == True:
			self.control.k_1 = False
			self.etwas.s = self.etwas.s*10
			self.etwas.n = (self.etwas.n+(1*self.etwas.s))
			self.view.a = 0
			self.view.an = 0
			if self.etwas.n not in tree:
				self.etwas.n = (self.etwas.n-(1*self.etwas.s))
				self.etwas.s = int(self.etwas.s/10)	

		if self.control.k_2 == True:
			self.control.k_2 = False
			self.etwas.s = self.etwas.s*10
			self.etwas.n = (self.etwas.n+(2*self.etwas.s))
			self.view.a = 0
			self.view.an = 0
			if self.etwas.n not in tree:
				self.etwas.n = (self.etwas.n-(2*self.etwas.s))
				self.etwas.s = int(self.etwas.s/10)		

		if self.control.k_3 == True:
			self.control.k_3 = False
			self.etwas.s = self.etwas.s*10
			self.etwas.n = (self.etwas.n+(3*self.etwas.s))
			self.view.a = 0
			self.view.an = 0
			if self.etwas.n not in tree:
				self.etwas.n = (self.etwas.n-(3*self.etwas.s))
				self.etwas.s = int(self.etwas.s/10)

		if self.etwas.add_information == 'end':
			self.move = True


	def render_information (self):

		n = 0

		for i in range (0, self.hp):
			hero_screen.blit(self.hp_bar.image, (10, 120- n))
			n = n+15
		hero_screen.blit(fonts.font2.render (str(self.hp), True, (250,250,250)),(10,140))

		n = 0
		for i in range (0, self.sp):
			hero_screen.blit(self.sp_bar.image, (30, 120-n))
			n = n+15

		hero_screen.blit(fonts.font2.render (str(self.sp), True, (250,250,250)),(30,140))



	def collide (self, array):

		for entity in array:
			if pygame.sprite.collide_rect (self, entity):
				return entity

	def update (self, array):

		if self.collide_control == True and self.etwas.agression == False:
			self.son.clear_text ()
			self.conversation(self.etwas.tree, self.etwas)

			self.battle.clear_text ()
	
			hero_screen.blit(fonts.font3.render (str(self.etwas.s), True, (250,250,250)),(2,0))
			hero_screen.blit(fonts.font3.render (str(self.etwas.n), True, (250,250,250)),(2,15))

		if self.move == True:

		#RIGHT
			if self.control.right == True:
				self.collide_control = False
				self.control.right = False
	
				self.rect.x += 1
	
				self.etwas = self.collide(array)
	
				if self.etwas != None:
	
					if self.etwas.name == "block":
						self.rect.x -= 1
						self.etwas.interaction ()
	
					if self.etwas.name == "chest":
						self.rect.x -= 1
						self.rect.x += 45
						array.remove (self.etwas)
					if self.etwas.name == "monster":
						self.rect.x -= 1
						self.collide_control = True
						self.etwas.interaction (self)
	
				if self.etwas == None: 
					self.rect.x += 45
					self.rect.x -= 1
				
			#LEFT
			if self.control.left == True:
				self.control.left = False
				self.collide_control = False
				self.rect.x -= 1
	
				self.etwas = self.collide(array)
				if self.etwas != None:
	
					if self.etwas.name == "block":
						self.rect.x += 1
	
					if self.etwas.name == "chest":
						self.rect.x += 1
						self.rect.x -= 45
						array.remove (self.etwas)
	
					if self.etwas.name == "monster":
	
						self.rect.x += 1
						self.collide_control = True
						self.etwas.interaction (self)
	
				if self.etwas == None: 
					self.rect.x -= 45
					self.rect.x += 1
	
	
			#UP
			if self.control.up == True:
				self.control.up = False
				self.collide_control = False
				self.rect.y -= 1
	
				self.etwas = self.collide(array)
	
				if self.etwas != None:
	
					if self.etwas.name == "block":
						self.rect.y += 1
						
						self.etwas.interaction ()
					if self.etwas.name == "chest":
						self.rect.y += 1
						self.rect.y -= 45
						array.remove (self.etwas)
	
					if self.etwas.name == "monster":
						self.collide_control = True
						self.etwas.interaction (self)
						self.rect.y += 1
	
				if self.etwas == None: 
					self.rect.y +=1
					self.rect.y -=45
	
	
			#DOWN
			if self.control.down == True:
				self.control.down = False
				self.collide_control = False
				self.rect.y += 1
	
				self.etwas = self.collide(array)
				if self.etwas != None:
					if self.etwas.name == "block":
						self.rect.y -= 1
	
						self.etwas.interaction ()
					if self.etwas.name == "chest":
						self.rect.y -= 1
						self.rect.y += 45
						array.remove (self.etwas)
					if self.etwas.name == "monster":
						self.rect.y -=1
						self.collide_control = True
						self.etwas.interaction (self)
	
				if self.etwas == None: 
					self.rect.y += 45
					self.rect.y -= 1

	def render (self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))





	# BATTLE OPTIONS

	def check_for_death (self):
		if self.hp <= 0:
			self.death ()

	def death (self):
		self.status = 'dead'

	def end_text (self):
		pass

	def dice_rolling (self):

		information_screen.blit (roll_screen, (0,0))
		roll_screen.fill ((black))
		roll_screen.blit (self.marker.image, (self.mx, self.my))

		if self.go_left == False:
			self.mx = self.mx +10

		if self.go_left == True:
			self.mx = self.mx -10

		if self.mx > 430:
			self.go_left = True

		if self.mx < 80:
			self.go_left = False

		if self.control.k_e == True:
			self.control.k_e = False
			self.dice_fun = False
			self.dice_value = int((self.mx - 80) / 20)
			self.attack_roll = True
		
	def battle_action_main (self):

		if self.turn_main == True:
			
			self.battle.change_text (1, "Что будете делать?")
			self.battle.change_text (3, "1 - атаковать; 2 - спец.способность; 3 - убегать")
	
			if self.control.k_1 == True:
				self.turn_main = False
				self.control.k_1 = False
				self.assault = True
				self.dice_fun = True
				self.battle.clear_text ()
	
			if self.control.k_2 == True:
				self.turn_main = False
				self.control.k_2 = False
				self.special = True

			if self.control.k_2 == True:
				self.turn_main = False
				self.control.k_2 = False
				self.flee = True

		if self.assault == True:
			self.assault_fun (self.etwas)

		if self.flee == True:
			self.flee_fun ()

		if self.special == True:
			self.special_fun ()

	def chang (self):
		pass
	def special_fun (self):
		pass
	def flee_fun (self):
		pass

	def assault_fun (self, monster):
		if self.dice_fun == True:
			self.dice_rolling ()

		if self.attack_roll == True:
			self.battle.clear_text ()

			a = self.dice_value
			b = random.randint (1,6)
			c = self.at + a 
			d = monster.ac + b
		
			self.battle.change_text (1, "Ваша атака: "+str(c) + "  Защита монстра: "+ str(d))
			if c >= d:
				
				if int(c/d)>1:
					monster.hp = monster.hp - self.damage*int(c/d)
					self.battle.change_text (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
					self.battle.change_text (5, 'Критический урон: '+str(self.damage*int(c/d)))
					
				else:
					self.battle.change_text (4, "Вы попали и нанесли сокрушительный удар!")
					monster.hp = monster.hp - self.damage
					self.battle.change_text (5, 'Урон: '+str(self.damage))
			elif c<d:
				self.battle.change_text (4, 'Вы промазали!')	
			self.attack_roll = False
			self.wait_for_next_turn = True
			self.battle.change_text (7, 'Нажмите Е')

		if self.control.k_e == True and self.wait_for_next_turn == True:
			self.wait_for_next_turn = False
			self.control.k_e = False
			self.monster_turn = True
			self.assault = False


