import pygame
import pyganim
import functions
import screens
import fonts
#from functions import self.battle.render_inf
import random

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()

class Hero(pygame.sprite.Sprite):

	def __init__(self, x, y, battle, control, compose_text, at, ac, hp, dem):
		pygame.sprite.Sprite.__init__(self)

		#self.image=pygame.image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.control = control
		self.battle = battle
		self.image = pygame.Surface ((45,45))
		#self.image = svin_anim.getImagesFromSpriteSheet()
		self.image.fill ((100,200,230))
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
		

	def conversation (self, tree):

		text_massive, self.add_information = tree[self.n]

		self.view.render_text (text_massive)
		#except:
		#	self.n = 0
		#	self.s = 1

		if self.control.k_1 == True:
			self.control.k_1 = False
			self.s = self.s*10
			self.n = (self.n+(1*self.s))
			self.view.a = 0
		if self.control.k_2 == True:
			self.control.k_2 = False
			self.s = self.s*10
			self.n = (self.n+(2*self.s))
			self.view.a = 0
		if self.control.k_3 == True:
			self.control.k_3 = False
			self.s = self.s*10
			self.n = (self.n+(3*self.s))
			self.view.a = 0

	def collide (self, array):

		for entity in array:
			if pygame.sprite.collide_rect (self, entity):
				return entity


	def update (self, array):
		if self.collide_control == True and self.add_information != "war":
			self.conversation(self.etwas.tree)


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
					self.etwas.interaction ()

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
					self.etwas.interaction ()

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
					self.etwas.interaction ()
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
					self.etwas.interaction ()

			if self.etwas == None: 
				self.rect.y += 45
				self.rect.y -= 1

	def render (self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))
		#self.image.fill ((0,0,0))
		#svin_anim.blit (surface, (self.rect.x,self.rect.y))

	# BATTLE OPTIONS


		
	def battle_action_main (self):
		if self.turn_main == True:
			self.battle.change_inf (1, "Что будете делать? 1 - атаковать; 2 - спец.способность; 3 - убегать.")
	
			if self.control.k_1 == True:
				self.turn_main = False
				self.control.k_1 = False
				self.assault = True
				self.attack_roll = True
	
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
		if self.attack_roll == True:
			self.battle.clear_inf ()

			a = random.randint (1,6)
			b = random.randint (1,6)
			c = self.at + a 
			d = monster.ac + b
		
			self.battle.change_inf (1, "Ваша атака: "+str(c) + "  Защита монстра: "+ str(d))
			if c >= d:
				
				if int(c/d)>1:
					monster.hp = monster.hp - self.damage*int(c/d)
					self.battle.change_inf (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
					self.battle.change_inf (5, 'Критический урон: '+str(self.damage*int(c/d)))
					
				else:
					self.battle.change_inf (4, "Вы попали и нанесли сокрушительный удар!")
					monster.hp = monster.hp - self.damage
					self.battle.change_inf (5, 'Урон: '+str(self.damage))
			elif c<d:
				self.battle.change_inf (4, 'Вы промазали!')	
			self.attack_roll = False
			self.wait_for_next_turn = True
			self.battle.change_inf (7, 'Нажмите Е')

		if self.control.k_e == True and self.wait_for_next_turn == True:
			self.wait_for_next_turn = False
			self.control.k_e = False
			self.monster_turn = True
			self.assault = False


