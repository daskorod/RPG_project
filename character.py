import pygame
import pyganim
import functions
import screens
import fonts
import random
import classes
from screens import *
from constants import *
import items

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()


class Hero(pygame.sprite.Sprite):

	def __init__(self, x, y, battle, control, compose_text, at, ac, hp, dem ,son):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load('images/hero2.png')
		self.image.set_colorkey ((255,255,255))
		self.control = control
		self.battle = battle
		self.name = 'Рихтер'
		#self.image = pygame.Surface ((45,45))
		#self.image = svin_anim.getImagesFromSpriteSheet()
		#self.image.fill ((100,200,230))
		self.sp = 2
		self.rect = pygame.Rect (x,y, 45,45)
		self.rect.x = x*45
		self.rect.y = y*45
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

		self.turn_main = False
		self.attack_roll = False
		self.wait_for_next_turn = False
		self.gold = 0
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
		self.press_to_kill = False
		self.back = False
		self.branch_do = 'qwd'
		self.hp_max = 7
		self.hp_old = hp
		self.x_mod = 0
		self.start_rendering = False
		self.start_conv = True
		self.conv_stop = True
		self.door_interaction = False
		self.at_ic = pygame.image.load ('images/at.png')
		self.ac_ic = pygame.image.load ('images/ac.png')
		self.icon = image.load ('images/icon.png')
		self.inventory_flag = False
		self.exp = 0
		self.weapon = items.short_sword
		self.weapon.status = 'экипировано'
		self.no_item = items.no_item
		self.inv = [self.weapon, items.long_sword,self.no_item,items.bouquet,self.no_item,self.no_item,self.no_item,self.no_item,self.no_item]
		self.inv_index_pos = 0
		
		self.first = items.first
		#self.at += self.weapon.at_mod
		self.damage = self.weapon.dem
		self.level = 1
		self.inv_question = False
	def inventory_manage (self):

		if self.control.k_i == True and self.inventory_flag == False:
			self.move = False
			self.inventory_flag = True
			self.control.k_i = False

		if self.control.k_i == True and self.inventory_flag == True:
			self.control.k_i = False
			self.move = True
			self.inventory_flag = False
			self.son.clear_text ()

		if self.inventory_flag == True:
			adventure_screen.blit (inventory_screen, (200,10))
			inventory_screen.fill (sea_color)
			a = 0
			for i in self.inv:
				inventory_screen.blit(fonts.font2.render ('Инвентарь', True, (250,250,250)),(90,10))
				inventory_screen.blit(fonts.font2.render (str(i.name)+' ( '+ i.status + ' )', True, (250,250,250)),(40,50+(a*30)))
				a +=1

			

			if self.inv_question == False:
				self.inv_index()
				self.son.change_text_tree (self.view.render_text (self.inv[self.inv_index_pos].name+ '. ' + self.inv[self.inv_index_pos].description, self.inv[self.inv_index_pos].use_description))

			if self.inv_question == False:

				if self.control.k_1 == True:
					self.control.k_1 = False
					if self.inv[self.inv_index_pos].status == 'в рюкзаке':
						for i in self.inv:
							if i.species == 'оружие' and i.status == 'экипировано':
								i.status = "в рюкзаке"
						self.inv[self.inv_index_pos].status = 'экипировано'
						if self.inv[self.inv_index_pos].species == 'оружие':
							self.weapon = self.inv[self.inv_index_pos]
							self.at += self.weapon.at_mod
							self.damage = self.weapon.dem
					elif self.inv[self.inv_index_pos].status == 'экипировано':
						self.inv[self.inv_index_pos].status = 'в рюкзаке'
	
						if self.inv[self.inv_index_pos].species == 'оружие':
							self.weapon = self.first
							#self.at += self.weapon.at_mod
							self.damage = self.weapon.dem
	
				if self.control.k_2 == True:
					self.inv_question = True
					self.control.k_2 = False
					self.son.clear_text ()
					self.son.change_text (1, 'Вы уверены, что хотите выбросить ' +self.inv[self.inv_index_pos].name+ ' на фиг!' )
					self.son.change_text (3, '1 - Да, 2 - Нет')

			if self.inv_question == True:
				if self.control.k_1 == True:
					self.control.k_1 = False

					if self.inv[self.inv_index_pos].status == 'экипировано':
						if self.inv[self.inv_index_pos].species == 'оружие':
							self.weapon = self.first
							#self.at += self.weapon.at_mod
							self.damage = self.weapon.dem
					self.inv.pop (self.inv_index_pos)
					self.inv.insert (self.inv_index_pos, items.no_item)
					self.inv_question = False

				if self.control.k_2 == True:
					self.control.k_2 = False
					self.inv_question = False

	def inv_index (self):
		inventory_screen.blit(self.at_ic, (13,53+(self.inv_index_pos*30)))

		if self.control.down == True and self.inv_index_pos <8:
			self.control.down = False
			self.inv_index_pos += 1
		if self.control.up == True and self.inv_index_pos >0:
			self.control.up = False
			self.inv_index_pos -= 1



	def render_hp_mod(self, position):

		if self.hp_old != self.hp:
			if self.hp_old > self.hp:
				self.hp_mod = self.hp -self.hp_old

				self.color = red
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


#		high_screen.blit(fonts.font5.render (self.name, True, (250,250,250)),(10,0))
		high_screen.blit(fonts.font5.render ('Опыт '+str(self.exp), True, (250,250,250)),(230,0))
		high_screen.blit(fonts.font5.render ('Деньги '+str(self.gold), True, (250,250,250)),(115,0))
		high_screen.blit(fonts.font5.render ('Уровень '+str(self.level), True, (250,250,250)),(10,0))
#		high_screen.blit(fonts.font5.render ('мн '+str(self.sp), True, (250,250,250)),(230,0))
#		high_screen.blit(fonts.font5.render ('ур '+str(self.damage), True, (250,250,250)),(280,0))
		
		hero_screen.blit(fonts.font5.render (self.name, True, (250,250,250)),(70,0))
		hero_screen.blit(fonts.font5.render (str((self.at+self.weapon.at_mod)) +'/'+str(self.damage) , True, (250,250,250)),(80,155))
		hero_screen.blit(fonts.font5.render (str(self.ac), True, (250,250,250)),(130,155))
		hero_screen.blit(self.at_ic,(65,160))
		hero_screen.blit(self.ac_ic,(115,160))
		hero_screen.blit (self.icon, (50,35))

	def conversation (self, tree, interlocutor):
		'''s - порядок десяток в диалоге, он прибавляется после нажатия на клавишу, поэтому должен = 1,
		 чтобы не сводился на ноль постоянно. n - это значение которое растёт - это путсое вместилище,
		  которое передаётся дальше. Растёт оно всегда при помощи s.'''


		text_massive, self.etwas.add_information, *other = tree[interlocutor.branch][interlocutor.n]

		try:
			text_massive_answer, branch = other
			self.etwas.branch_do, self.etwas.branch_id = branch

		except:
			text_massive_answer = other[0]

		self.son.change_text_tree(self.view.render_text (text_massive, text_massive_answer))

		self.etwas.dialog_options (self)

		if self.control.k_1 == True:
			self.control.k_1 = False
			self.son.clear_text ()

			self.etwas.s = self.etwas.s*10
			self.etwas.n = (self.etwas.n+(1*self.etwas.s))
			self.view.a = 0

			if self.etwas.n not in tree[interlocutor.branch]:
				self.etwas.n = (self.etwas.n-(1*self.etwas.s))
				self.etwas.s = int(self.etwas.s/10)	

		if self.control.k_2 == True:
			self.control.k_2 = False
			self.son.clear_text ()
			self.etwas.s = self.etwas.s*10
			self.etwas.n = (self.etwas.n+(2*self.etwas.s))
			self.view.a = 0

			if self.etwas.n not in tree[interlocutor.branch]:
				self.etwas.n = (self.etwas.n-(2*self.etwas.s))
				self.etwas.s = int(self.etwas.s/10)		

		if self.control.k_3 == True:
			self.control.k_3 = False
			self.son.clear_text ()
			self.etwas.s = self.etwas.s*10
			self.etwas.n = (self.etwas.n+(3*self.etwas.s))
			self.view.a = 0

			if self.etwas.n not in tree[interlocutor.branch]:
				self.etwas.n = (self.etwas.n-(3*self.etwas.s))
				self.etwas.s = int(self.etwas.s/10)

	def collide (self, array):

		for entity in array:
			if pygame.sprite.collide_rect (self, entity):
				return entity

	def conversation_control (self):
		if self.collide_control == True and self.etwas.agression == False:

		
			if self.conv_stop == True:
				self.son.clear_text ()
				self.conv_stop = False

			self.conversation(self.etwas.tree, self.etwas)

		if self.collide_control == False or self.etwas.agression == True:
			self.conv_stop = True


	def update (self, array):
		self.conversation_control ()
		self.inventory_manage ()

		if self.move == True:

			if self.control.right == True:
				self.rect.x += 1
				self.etwas = self.collide(array)
	
				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.x += 44
	
				self.control.right = False
	
			if self.control.left == True:
				self.rect.x -= 1
				self.etwas = self.collide(array)
	
				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.x -= 44
	
				self.control.left = False
	
			if self.control.up == True:
				self.rect.y -= 1
				self.etwas = self.collide(array)

				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.y -= 44
	
				self.control.up = False
	
			if self.control.down == True:
				self.rect.y += 1
				self.etwas = self.collide(array)

				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.y += 44
	
				self.control.down = False

#	def render (self, surface):
#		surface.blit(self.image, (self.rect.x, self.rect.y))


	# BATTLE OPTIONS

	def check_for_death (self):
		if self.hp <= 0:
			self.death ()

	def death (self):
		self.son.clear_text ()
		self.son.change_text (1, 'Вы умерли.')
		self.son.change_text (2, 'На ваших костях упыри будут танцевать джигу.')
		self.status = 'dead'
		self.kill ()


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

		if self.mx > 550:
			self.go_left = True

		if self.mx < 40:
			self.go_left = False

		if self.control.k_e == True:
			self.control.k_e = False
			self.dice_fun = False
			self.dice_value = int((self.mx - 80) / 20)
			self.attack_roll = True
		
	def battle_action_main (self):
		#self.son.change_text (7, 'Вы получили 20 монет')
		self.press_to_kill_fun ()

		if self.turn_main == True:


			
			self.son.change_text (1, "Что будете делать?")
			self.son.change_text (3, "1 - атаковать; 2 - спец.способность; 3 - убегать")
	
			if self.control.k_1 == True:
				self.turn_main = False
				self.control.k_1 = False
				self.assault = True
				self.dice_fun = True
				self.son.clear_text ()
	
			if self.control.k_2 == True:
				self.turn_main = False
				self.control.k_2 = False
				self.special = True
				self.son.clear_text ()
				self.son.change_text (1, "Что будете делать?")
				self.son.change_text (3, "1 - изгонение нежити; 2 - лечение; 3 - назад")

			if self.control.k_3 == True:
				self.turn_main = False
				self.control.k_3 = False
				self.flee = True
				self.son.clear_text ()

		if self.assault == True:
			self.assault_fun (self.etwas)

		if self.flee == True:
			self.flee_fun ()

		if self.special == True:
			self.special_fun ()

#	def chang (self):
#		pass
#		
	def press_to_kill_fun (self):
		if self.press_to_kill == True and self.control.k_e == True:
			self.press_to_kill = False
			self.control.k_e = False
			self.etwas.hp = 0

	def special_fun (self):


			if self.control.k_1 == True:
				self.control.k_1 = False
				self.son.clear_text ()

				if self.etwas.hp <= 10 and self.sp >0:
					self.sp -= 1
					self.press_to_kill = True
					self.son.change_text (1, "Монстры рассылпался в прах!")
					self.son.change_text (3, "Нажмите Е")

				if self.etwas.hp > 10 or self.sp<=0:
					self.back = True
					self.son.change_text (1, "Ничего не произошло.")
					self.son.change_text (3, "Нажмите Е")

			if self.control.k_e == True and self.back == True:
				self.turn_main = True
				self.control.k_e = False
				self.special = False
				self.back = False

			if self.control.k_2 == True:
				self.turn_main = False
				self.control.k_2 = False
				self.special = True
				self.son.clear_text ()
				if self.sp > 0:
					self.sp -= 1
					self.hp += 4
					if self.hp > self.hp_max:
						self.hp = self.hp_max
					self.son.change_text (1, "Ваши раны восстановились чудесным образом. +4 ЖС")
					self.son.change_text (3, "Нажмите Е")
					self.back = True

				if self.sp <=0:
					self.back = True
					self.son.change_text (1, "Ничего не произошло.")
					self.son.change_text (3, "Нажмите Е")

			if self.control.k_3 == True:
				self.turn_main = True
				self.control.k_3 = False
				self.special = False

	def flee_fun (self):
				self.son.change_text (1, "Вы позорно бежали.")
				#self.son.change_text (3, "Нажмите Е")		
				self.collide_control = False
				self.move = True
				self.flee = False
				self.turn_main = True

	def assault_fun (self, monster):
		if self.dice_fun == True:
			self.dice_rolling ()

		if self.attack_roll == True:
			self.son.clear_text ()

			a = self.dice_value
			b = random.randint (1,6)
			c = self.at + a + self.weapon.at_mod
			d = monster.ac + b
		
			self.son.change_text (1, "Ваша атака: "+str(c) + "  Защита монстра: "+ str(d))
			if c >= d:
				
				if int(c/d)>1:
					monster.hp = monster.hp - self.damage*int(c/d)
					self.son.change_text (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
					self.son.change_text (5, 'Критический урон: '+str(self.damage*int(c/d)))
					
				else:
					self.son.change_text (4, "Вы попали и нанесли сокрушительный удар!")
					monster.hp = monster.hp - self.damage
					self.son.change_text (5, 'Урон: '+str(self.damage))
			elif c<d:
				self.son.change_text (4, 'Вы промазали!')	
			self.attack_roll = False
			self.wait_for_next_turn = True
			self.son.change_text (7, 'Нажмите Е')

		if self.control.k_e == True and self.wait_for_next_turn == True:
			self.wait_for_next_turn = False
			self.control.k_e = False
			self.monster_turn = True
			self.assault = False


