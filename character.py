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
import ideas
import img
import math
import event
import menu

time = 0.2


slashAnim = pyganim.PygAnimation([('animation/slash/Effect_Slash11.png', 0.1),
                                 ('animation/slash/Effect_Slash21.png', 0.1),
                                 ('animation/slash/Effect_Slash31.png', 0.1),
                                 ('animation/slash/Effect_Slash41.png', 0.1)], loop=False)

dustAnim = pyganim.PygAnimation([('testimages/smoke_puff_0001.png', 0.1),
                                 ('testimages/smoke_puff_0002.png', 0.1),
                                 ('testimages/smoke_puff_0003.png', 0.1),
                                 ('testimages/smoke_puff_0004.png', 0.1),
                                 ('testimages/smoke_puff_0005.png', 0.1),
                                 ('testimages/smoke_puff_0006.png', 0.1),
                                 ('testimages/smoke_puff_0007.png', 0.1),
                                 ('testimages/smoke_puff_0008.png', 0.1),
                                 ('testimages/smoke_puff_0009.png', 0.1),
                                 ('testimages/smoke_puff_0010.png', 0.1)], loop=False)


heroAnim = pyganim.PygAnimation([
								('images/anim/d1.png', time),
								('images/anim/stand.png', time),
								('images/anim/d2.png', time),
('images/anim/stand.png', time)
								])

heroAnim_l = pyganim.PygAnimation([
	#('images/anim/l1.png', time),
								('images/anim/l2.png', time),
								('images/anim/l3.png', time),
								('images/anim/l4.png', time),
('images/anim/l1.png', time)
								])

heroAnim_r = pyganim.PygAnimation([
	#('images/anim/r13.png', time),
								('images/anim/r2.png', time),
								('images/anim/r13.png', time),
								('images/anim/r4.png', time),
('images/anim/r13.png', time)
								])

heroAnim_u = pyganim.PygAnimation([
	#('images/anim/u13.png', time),
								('images/anim/u2.png', time),
								('images/anim/u13.png', time),
								('images/anim/u4.png', time),
('images/anim/u13.png', time)
								])

standd = pygame.image.load('images/anim/stand.png')
standr = pygame.image.load('images/anim/r13.png')
standl = pygame.image.load('images/anim/l1.png')
standu = pygame.image.load('images/anim/u13.png')

dirlist = [standd, standl, standr, standu]

heroAnim.play ()
heroAnim_l.play()
heroAnim_r.play()
heroAnim_u.play()

animlist = [heroAnim, heroAnim_l, heroAnim_r, heroAnim_u]

#heroAnim.blit (adventure_screen, (self.rect.x, self.rect.y))
#self.camera.apply(self.hero)
#heroAnim.blit (adventure_screen, (self.camera.apply(self.hero)))
class Hero(pygame.sprite.Sprite):

	def __init__(self, x, y, battle, control, compose_text, at, ac, hp, dem ,son, location_list, locations_dict, test_arg):
		pygame.sprite.Sprite.__init__(self)

		#BASE

		#self.image=pygame.image.load('images/hero2.png')
		#self.image = heroAnim
		#self.image.set_colorkey ((255,255,255))
		#self.image = heroAnim.getImagesFromSpriteSheet()
		self.test_arg = test_arg
		self.standlist = [standd, standl, standr, standu]
		#pygame.image.load ('images/anim/stand.png')
		self.control = control
		self.battle = battle
		self.name = 'Рихтер'
		self.dustAnim = dustAnim
		self.slashAnim = slashAnim
		self.inception = True
		
		self.image = pygame.Surface ((45,45))
		self.image.fill ((100,200,230))
		self.image.set_colorkey ((100,200,230))		
		self.rect = pygame.Rect (x,y, 45,45)
		self.rect.x = x*45
		self.rect.y = y*45	
		self.view = compose_text	
		self.son = son
		self.icon = image.load ('images/icon.png')

		#map
		self.location_list = location_list
		self.locations_dict = locations_dict
		self.location = locations_dict['platz']
		self.level_mark = 0

		#move
		self.velo = 44
		self.direction = 0
		self.back_move = 1		
		self.anima = animlist[self.direction]

		#CHARACTERSTICS
		self.exp_old = 0
		self.level = 1
		self.sp = 2
		self.sp_max = 2
		self.at = at 
		self.ac = ac
		self.hp = hp
		self.gold = 160
		self.mx = 20
		self.my = 40
		self.exp = 0
		self.hp_max = 7
		self.hp_old = hp
		self.x2_mod = 0	
		self.x1_mod = 0		
		self.next_level = 100
		self.x_mod = 0
		self.x3_mod = 0
		self.is_death = False
		self.exp_mod = 0
		self.sp_mod = 0
		self.sp_old = self.sp


		#QEST
		self.quest = {}
		#DIALOG

		self.start_conv = True
		self.conv_stop = True

		#BATTLE

		self.collision = False
		self.collide_control = False
		self.back = False # В бою обратно идти в меню
		self.assault = False
		self.flee = False
		self.special = False
		self.turn_main = False
		self.attack_roll = False
		self.wait_for_next_turn = False
		self.dice_fun = False
		self.dice_value = 0
		self.monster_turn = False
		self.press_to_kill = False
		self.go_left = False # В бою движение меча

		#TECH
		self.marker = classes.Marker (self.mx,self.my)
		self.line = image.load ('images/line.png')
		self.status = "alive"
		self.move = True
		self.start_rendering = False # переключатель для отображения изменения HP
		self.start_rendering_exp = False
		self.start_rendering_sp = False
		self.start_rendering_lev = False
		self.dict = {'trap' : False}

		#BAR LIFE MANA
		self.at_ic = pygame.image.load ('images/at.png')
		self.ac_ic = pygame.image.load ('images/ac.png')
		self.hp_bar = classes.Bar (12,15, red)
		self.sp_bar = classes.Bar (12,15, blue)

		#INVENTORY

		self.inventory_flag = False
		self.weapon = items.short_sword
		self.weapon.status = 'экипировано'
		self.no_item = items.no_item
		self.inv = [self.weapon, items.long_sword,items.bouquet,items.hp_potion]
		self.inv_index_pos = 0
		self.first = items.first
		self.damage = self.weapon.dem
		self.inv_question = False
		self.inv_quit = False
		self.hp_potions = 0
		self.inv_page = 0
		self.number_of_things_on_the_page = 9

		#JOURNAL

		self.journal_flag = False

		self.no_ideas = ideas.no_ideas
		self.journal = [ideas.revelation, self.no_ideas, self.no_ideas, self.no_ideas,self.no_ideas,self.no_ideas,self.no_ideas,self.no_ideas,self.no_ideas]
		self.journal_index_pos = 0
		self.journal_question = False
		self.journal_quit = False

		if self.test_arg == True:
			self.gold +=1000
			self.sp +=2

		#ChAr options
		self.char_flag = False
		self.char_point = 1
		self.d = 'Е - повысить параметр'
		self.char_quit = False

		self.char_value ={'1lvl':1,'2exp':0,'3at':6,'4ac':6,'5hp':7,'6sp':2,'7points':1}

		self.sorted_char_value_keys = sorted(self.char_value.keys())
		self.char = [

#0
		('Уровень', self.char_value['1lvl'], 'Каждый уровень вы получаете одно очко для распределения', '','lvl'),
#1
		 ('Опыт',self.char_value['2exp'], 'Когда его достаточно много вы повышаете уровень', '','exp'),
#2
		  ('Атака',self.char_value['3at'], 'Влияет на то, как успешно вы нападаете и вышибаете двери', self.d,'at'),
#3
		   ('Защита',self.char_value['4ac'], 'Ваши навыки обороны', self.d),
#4
		    ('Жизни',self.char_value['5hp'], 'Сколько ударов вы можете держать', self.d),
#5
		     ('Вера',self.char_value['6sp'], 'Имея веры с горчичное зерно можно заставить гору сойти с места', self.d),
#6
		      ('Очки на распределение', self.char_value['7points'], 'За одно очко можно повысить один параметр', '')

		      ]
		#self.char = {level: 1, exp: 0, at:, self.ac, self.hp_max, self.sp, self.char_point}
		#

	def drink_potion (self):
		if self.control.k_q == True:
			self.control.k_q = False
			for i in self.inv:
				if i.name == 'Лечебное зелье':
					#if self.char_value
					self.hp += random.choice(range(1,i.value))
					if self.hp > self.char_value['5hp']:
						self.hp = self.char_value['5hp']
					self.inv.remove(i)
					img.healAnim.play()
					break




	def char_options (self):

		self.char = [


		('Уровень', self.char_value['1lvl'], 'Каждый уровень вы получаете одно очко для распределения', '','lvl'),

	 ('Опыт',self.char_value['2exp'], 'Когда его достаточно много вы повышаете уровень', '','exp'),

		  ('Атака',self.char_value['3at'], 'Влияет на то, как успешно вы нападаете и вышибаете двери', self.d,'at'),

		   ('Защита',self.char_value['4ac'], 'Ваши навыки обороны', self.d),

		    ('Жизни',self.char_value['5hp'], 'Сколько ударов вы можете держать', self.d),

		     ('Вера',self.char_value['6sp'], 'Имея веры с горчичное зерно можно заставить гору сойти с места', self.d),

		      ('Очки на распределение', self.char_value['7points'], 'За одно очко можно повысить один параметр', '')

		      ]





		if self.control.k_c == True and self.char_flag ==False:
			self.move = False
			self.char_flag = True
			self.control.k_c = False

		if self.char_flag == True:

			if self.control.k_c == True:
				self.control.k_c = False
				self.char_flag = False
				self.move = True



			adventure_screen.blit (char_screen, (200,10))
			char_screen.fill (swamp)
			
			#self.char = [self.level, self.exp, self.at, self.ac, self.hp_max, self.sp]
			char_screen.blit(fonts.font2.render ('Характеристики', True, (250,250,250)),(90,10))
			char_screen.blit(fonts.font2.render ('Выйти', True, (250,250,250)),(90,350))

			a = 0
			for i in range(len(self.char)):

				
				char_screen.blit(fonts.font2.render (str(self.char[i][0])+': '+ str(self.char[i][1]), True, (250,250,250)),(40,50+(a*30)))
				a +=1

			self.char_index ()

			if self.char_quit == False:
				
				
	
				if self.char[6][1] > 0:
	
					try:
						self.son.change_text_tree (self.view.render_text (self.char[self.inv_index_pos][0]+ '. ' + self.char[self.inv_index_pos][2], self.char[self.inv_index_pos][3]))
					except:
						pass
	
					if self.inv_index_pos > 1 and self.inv_index_pos <6 and self.control.k_e == True:
						self.char_value[self.sorted_char_value_keys[self.inv_index_pos]] +=1
						self.char_value['7points'] -=1
						self.control.k_e = False
				else:
	
					try:
						self.son.change_text_tree (self.view.render_text (self.char[self.inv_index_pos][0]+ '. ' + self.char[self.inv_index_pos][2], ''))
					except:
						pass
			if self.char_quit == True:

				self.son.clear_text ()
				information_screen.blit(fonts.font2.render ('Выйти? Нажмите E', True, (250,250,250)),(10,10))

				if self.control.k_e == True:
					self.control.k_e = False
					self.move = True
					self.char_flag = False
					self.inv_index_pos = 0
					self.char_quit = False

	def update_char(self):
		self.sp_max = self.char_value['6sp']
		self.hp_max = self.char_value['5hp']
		self.at = self.char_value['3at']
		self.ac = self.char_value['4ac']
		self.level = self.char_value['1lvl']
		self.exp = self.char_value ['2exp']	
		self.level_up ()

	def level_up (self):
		if self.char_value['2exp'] != self.exp_old:
			self.start_rendering_exp = True			
			self.exp_mod = self.exp - self.exp_old 
			self.exp_old = self.exp

			if self.char_value['2exp'] >= self.next_level:
				self.char_value['1lvl'] += 1
				self.start_rendering_lev = True
				self.char_value['7points'] +=1
				self.next_level = self.to_next_level(self.char_value['1lvl'])



	def to_next_level(self, current_level):
		level_table = {1:100,2:200,3:400,4:700,5:1000,6:2000,7:50000,8:100000,9:200000,10:500000}
		return level_table[current_level]


	def char_index (self):
		if self.char_quit == False:

			char_screen.blit(self.at_ic, (13,53+(self.inv_index_pos*30)))
	
			if self.control.down == True and self.inv_index_pos <6:
				self.control.down = False
				self.inv_index_pos += 1
			if self.control.up == True and self.inv_index_pos >0:
				self.control.up = False
				self.inv_index_pos -= 1		
	
			if self.control.down == True and self.inv_index_pos == 6:
				self.control.down = False
				self.char_quit = True
	
		if self.char_quit == True:

			char_screen.blit(self.at_ic, (70, 353))
			if self.control.up == True:
				self.control.up = False
				self.char_quit = False	

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
			inventory_screen.blit(fonts.font2.render ('Инвентарь', True, (250,250,250)),(90,10))
			inventory_screen.blit(fonts.font2.render ('Выйти', True, (250,250,250)),(90,350))

			for i in range(self.inv_page*self.number_of_things_on_the_page,(self.inv_page+1)*self.number_of_things_on_the_page):
				try:				
					inventory_screen.blit(fonts.font2.render (str(self.inv[i].name)+' ( '+ self.inv[i].status + ' )', True, (	250,250,250)),(40,50+(a*30)))
					a +=1
					if a > self.number_of_things_on_the_page or a > len(self.inv)-((self.inv_page)*self.	number_of_things_on_the_page):
						break
				except:
					pass

			if self.inv_question == False:
				self.inv_index()

				if self.inv_quit == False:
					#if a < len(self.inv) or a < 8:
					try:
						self.son.change_text_tree (self.view.render_text (self.inv[self.inv_index_pos+self.inv_page*self.number_of_things_on_the_page].name+ '. ' + self.inv[self.inv_index_pos+self.inv_page*self.number_of_things_on_the_page].description, self.inv[self.inv_index_pos+self.inv_page*self.number_of_things_on_the_page].use_description))
					except:
						self.inv_quit = True

			if len(self.inv)>7:
				inventory_screen.blit(fonts.font2.render (str(len(self.inv)), True, (250,250,250)),(280,10))
				inventory_screen.blit(fonts.font2.render (str(self.inv_page+1), True, (250,250,250)),(235,10))				
				if self.inv_page<len(self.inv)//self.number_of_things_on_the_page:
					inventory_screen.blit(img.arrow_right,(250,10))

				if self.inv_page >0:
							
					inventory_screen.blit(img.arrow_left,(200,10))


			if self.inv_quit == True:
				self.son.clear_text ()
				information_screen.blit(fonts.font2.render ('Выйти? Нажмите E', True, (250,250,250)),(10,10))

				if self.control.k_e == True:
					self.control.k_e = False
					self.move = True
					self.inventory_flag = False
					self.inv_index_pos = 0
					self.inv_quit = False

			if self.inv_quit == False:

				if self.inv_question == False:

					if self.control.k_1 == True:
						self.control.k_1 = False

						if self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].status == 'в рюкзаке':

							for i in self.inv:
								if i.species == 'оружие' and i.status == 'экипировано':
									i.status = "в рюкзаке"
							self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].status = 'экипировано'
							if self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].species == 'оружие':
								self.weapon = self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)]
								self.at += self.weapon.at_mod
								self.damage = self.weapon.dem

						elif self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].status == 'экипировано':
							self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].status = 'в рюкзаке'
		
							if self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].species == 'оружие':
								self.weapon = self.first
								#self.at += self.weapon.at_mod
								self.damage = self.weapon.dem

						if self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].__class__.__name__ == 'Potion':
									self.hp += random.choice(range(1,self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].value))
									if self.hp > self.char_value['5hp']:
										self.hp = self.char_value['5hp']
									#self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)] = items.no_item
					

		
					if self.control.k_2 == True:
						self.inv_question = True
						self.control.k_2 = False
						self.son.clear_text ()
						self.son.change_text (1, 'Вы уверены, что хотите выбросить ' +self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].name+ ' на фиг!' )
						self.son.change_text (3, '1 - Да, 2 - Нет')

				if self.inv_question == True:

					if self.control.k_1 == True:
						self.control.k_1 = False

						if self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].status == 'экипировано':
							if self.inv[self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page)].species == 'оружие':
								self.weapon = self.first
								#self.at += self.weapon.at_mod
								self.damage = self.weapon.dem
						self.inv.pop (self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page))
					#	self.inv.insert (self.inv_index_pos+(self.inv_page*self.number_of_things_on_the_page), items.no_item)
						self.inv_question = False

					if self.control.k_2 == True:
						self.control.k_2 = False
						self.inv_question = False

	def inv_index (self):

		if self.control.right == True and (len(self.inv)-(self.inv_page+1)*self.number_of_things_on_the_page)>0:
			self.control.right = False
			self.inv_page+= 1

		if self.control.left == True and self.inv_page>0:
			self.control.left = False
			self.inv_page -= 1

		if self.inv_quit == False:

			inventory_screen.blit(self.at_ic, (13,53+(self.inv_index_pos*30)))

			if self.control.down == True and self.inv_index_pos <8:
				self.control.down = False
				self.inv_index_pos += 1
			if self.control.up == True and self.inv_index_pos >0:
				self.control.up = False
				self.inv_index_pos -= 1

			if self.control.down == True and self.inv_index_pos == 8:
				self.control.down = False
				self.inv_quit = True

		elif self.inv_quit == True:
			inventory_screen.blit(self.at_ic, (70, 353))

			if self.control.up == True:
				if len(self.inv)//self.number_of_things_on_the_page == self.inv_page:
					self.inv_index_pos = len(self.inv)%self.number_of_things_on_the_page-1
				else:
					self.inv_index_pos = 8
				self.control.up = False
				self.inv_quit = False

	def journal_manage (self):

		if self.control.k_j == True and self.journal_flag == False:
			self.move = False
			self.journal_flag = True
			self.control.k_j = False

		if self.control.k_j == True and self.journal_flag == True:
			self.control.k_j = False
			self.move = True
			self.journal_flag = False
			self.son.clear_text ()

		if self.journal_flag == True:
			adventure_screen.blit (journal_screen, (200,10))
			journal_screen.fill (swamp)
			a = 0
			journal_screen.blit(fonts.font2.render ('Философский Дневник', True, (250,250,250)),(70,10))
			journal_screen.blit(fonts.font2.render ('Выйти', True, (250,250,250)),(152,350))
			for i in self.journal:
				
				journal_screen.blit(fonts.font2.render (str(i.name), True, (250,250,250)),(40,50+(a*30)))
				a +=1

			

			if self.journal_question == False:
				self.journal_index()

				if self.journal_quit == False:
					self.son.change_text_tree (self.view.render_text (self.journal[self.journal_index_pos].name+ '. ' + self.journal[self.journal_index_pos].description, self.journal[self.journal_index_pos].use_description))

			if self.journal_quit == True:
				self.son.clear_text ()
				information_screen.blit(fonts.font2.render ('Выйти? Нажмите E', True, (250,250,250)),(10,10))

				if self.control.k_e == True:
					self.control.k_e = False
					self.move = True
					self.journal_flag = False
					self.journal_index_pos = 0
					self.journal_quit = False


	def journal_index (self):
		if self.journal_quit == False:

			journal_screen.blit(self.at_ic, (13,53+(self.journal_index_pos*30)))

			if self.control.down == True and self.journal_index_pos <8:
				self.control.down = False
				self.journal_index_pos += 1
			if self.control.up == True and self.journal_index_pos >0:
				self.control.up = False
				self.journal_index_pos -= 1

			if self.control.down == True and self.journal_index_pos == 8:
				self.control.down = False
				self.journal_quit = True

		if self.journal_quit == True:
			journal_screen.blit(self.at_ic, (70, 353))

			if self.control.up == True:
				self.control.up = False
				self.journal_quit = False	



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
			adventure_screen.blit(fonts.font4.render (str(self.hp_mod)+ ' HP', True, (self.color)),(position.x-self.x_mod*(self.x_mod/60), position.y - 30 - self.x_mod))

			if self.x_mod > 200:
				self.start_rendering = False
				self.x_mod = 0

	def render_sp_mod(self, position):

		if self.sp_old != self.sp:

			if self.sp_old > self.sp:
				self.sp_mod = self.sp -self.sp_old

#				self.color = blue
			if self.sp_old < self.sp:
				self.sp_mod =self.sp - self.sp_old 
#				self.color = blue

			self.sp_old = self.sp
			self.start_rendering_sp = True

		if self.start_rendering_sp == True:

			self.x3_mod += 1
		#hero_screen.blit(fonts.font2.render (str(self.sp), True, (250,250,250)),(30,140))
#			adventure_screen.blit(fonts.font2.render (str(self.hp_mod), True, (self.color)),(self.rect.x, self.rect.y - 30 - self.x_mod))
			adventure_screen.blit(fonts.font4.render (str(self.sp_mod)+ ' SP', True, (blue)),(position.x-(self.x3_mod*self.x3_mod/60)-20, position.y - 60 - self.x3_mod))

			if self.x3_mod > 200:
				self.start_rendering_sp = False
				self.x3_mod = 0	

	def render_lev_mod(self, position):

		if self.start_rendering_lev == True:
			self.x1_mod += 1

			adventure_screen.blit(fonts.fontlevel.render ('+ 1 УРОВЕНЬ!', True, (white)),(position.x-70, position.y - 30 - self.x1_mod))

			if self.x1_mod > 200:
				self.start_rendering_lev = False
				self.x1_mod = 0	


	def render_exp_mod(self, position):

		if self.start_rendering_exp == True:
			self.x2_mod += 1

			adventure_screen.blit(fonts.font4.render (str(self.exp_mod)+ ' EXP', True, (yellow)),(position.x-(self.x2_mod*(self.x2_mod/60))-10, position.y - 10 - self.x2_mod))

			if self.x2_mod > 200:
				self.start_rendering_exp = False
				self.x2_mod = 0	


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



		high_screen.blit(fonts.font5.render ('Опыт '+str(self.exp), True, (250,250,250)),(230,0))
		high_screen.blit(fonts.font5.render ('Деньги '+str(self.gold), True, (250,250,250)),(115,0))
		high_screen.blit(fonts.font5.render ('Уровень '+str(self.level), True, (250,250,250)),(10,0))
		high_screen.blit(fonts.font5.render ('Сл. ур. '+str(self.next_level), True, (250,250,250)),(340,0))

		
		hero_screen.blit(fonts.font5.render (self.name, True, (250,250,250)),(55,0))
		hero_screen.blit(fonts.font5.render (str((self.at+self.weapon.at_mod)) +'/'+str(self.damage) , True, (250,250,250)),(60,155))
		hero_screen.blit(fonts.font5.render (str(self.ac), True, (250,250,250)),(120,155))
		hero_screen.blit(self.at_ic,(45,160))
		hero_screen.blit(self.ac_ic,(100,160))
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

		if self.control.button_up == True:

			if self.control.k_1 == True:
				self.control.k_1 = False
				self.control.button_up = False
				self.son.clear_text ()

				self.etwas.s = self.etwas.s*10
				self.etwas.n = (self.etwas.n+(1*self.etwas.s))
				self.view.a = 0

				if self.etwas.n not in tree[interlocutor.branch]:
					self.etwas.n = (self.etwas.n-(1*self.etwas.s))
					self.etwas.s = int(self.etwas.s/10)	

			if self.control.k_2 == True:
				self.control.k_2 = False
				self.control.button_up = False
				self.son.clear_text ()
				self.etwas.s = self.etwas.s*10
				self.etwas.n = (self.etwas.n+(2*self.etwas.s))
				self.view.a = 0

				if self.etwas.n not in tree[interlocutor.branch]:
					self.etwas.n = (self.etwas.n-(2*self.etwas.s))
					self.etwas.s = int(self.etwas.s/10)		

			if self.control.k_3 == True:
				self.control.k_3 = False
				self.control.button_up = False
				self.son.clear_text ()
				self.etwas.s = self.etwas.s*10
				self.etwas.n = (self.etwas.n+(3*self.etwas.s))
				self.view.a = 0

				if self.etwas.n not in tree[interlocutor.branch]:
					self.etwas.n = (self.etwas.n-(3*self.etwas.s))
					self.etwas.s = int(self.etwas.s/10)

			if self.control.k_4 == True:
				self.control.k_4 = False
				self.control.button_up = False
				self.son.clear_text ()
				self.etwas.s = self.etwas.s*10
				self.etwas.n = (self.etwas.n+(4*self.etwas.s))
				self.view.a = 0

				if self.etwas.n not in tree[interlocutor.branch]:
					self.etwas.n = (self.etwas.n-(4*self.etwas.s))
					self.etwas.s = int(self.etwas.s/10)

	def collide (self, array):

		for entity in array:
			if pygame.sprite.collide_rect (self, entity):
				return entity

	def conversation_control (self):
		if self.collide_control == True and self.etwas.agression == False:

		
			if self.conv_stop == True:
				self.son.clear_text ()
				self.view.a = 0
				self.conv_stop = False

			self.conversation(self.etwas.tree, self.etwas)

		if self.collide_control == False or self.etwas.agression == True:
			self.conv_stop = True



	def update (self, array):
		self.drink_potion()
		self.update_char()
		#self.location.stage_loop ()
		
		if self.move == False:
			self.anima.stop ()


		self.conversation_control ()
		if self.collide_control == False:
			if self.char_flag == False and self.journal_flag == False:
				self.inventory_manage ()
			if self.inventory_flag == False and self.journal_flag == False:
				self.char_options ()
			if self.char_flag == False and self.inventory_flag == False:
				self.journal_manage ()

		#if self.control.move_cntrl == True and self.move == True:
			#self.anima.play ()


		if self.move == True:
			self.anima.play ()




		if self.move == True:
		
			if self.control.right == True:

				self.direction = 2
				self.rect.x += self.back_move
				self.etwas = self.collide(array)
	
				if self.etwas != None:
					self.etwas.interaction(self)


	
				else:
					self.rect.x += self.velo
	
				self.control.right = False

	
			if self.control.left == True:
				self.direction = 1
				self.rect.x -= self.back_move
				self.etwas = self.collide(array)
	
				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.x -= self.velo
	
				self.control.left = False
	
			if self.control.up == True:
				self.direction = 3
				self.rect.y -= self.back_move
				self.etwas = self.collide(array)

				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.y -= self.velo
	
				self.control.up = False
	
			if self.control.down == True:
				self.direction = 0
				self.rect.y += self.back_move
				self.etwas = self.collide(array)

				if self.etwas != None:
					self.etwas.interaction(self)
	
				else:
					self.rect.y += self.velo
	
				self.control.down = False
			self.anima = animlist[self.direction]


	def transcendental_apperception (self):
		if self.test_arg == True:

			if self.control.k_space == True:
				self.control.k_space = False
				self.level_mark +=1
				try:
					self.location = self.location_list[self.level_mark]
				except:
					self.location = self.location_list[0]
					self.level_mark = 0
		else:
			if self.control.k_space == True:
				self.control.k_space = False
				
				menu.help_loop()

		self.update (self.location.block_group)
		self.location.stage_loop (self)
		if self.inception == True:
			self.inception = False
			self.collide_control = True
			self.move = False
			self.etwas = event.inception

		if self.collide_control == True and self.etwas.agression == True:
			functions.combat (self, self.etwas)			


	# BATTLE OPTIONS

	def check_for_death (self):
		if self.hp <= 0 and self.is_death != True:
			self.death ()

	def death (self):
		self.is_death = True
		self.son.clear_text ()
		#self.son.change_text (1, 'Вы умерли.')
		#self.son.change_text (2, 'На ваших костях упыри будут танцевать джигу.')
		self.auto_text (random.choice([('Теперь вы мертвы.', "Ваши кости нынче объедают шакалы и никто не вспомнит вашего имени.", "Вы канули в пучину бесконечности."),("Вы почили в бозе.", "Но мир этого даже не заметил", "Ведь вы из себя практически ничего не пресдтавляли.", "Ведь вы - песчинка на берегу неизбежности."),("Вы сгинули в пучине бесконечности.", "А мир всё также продолжал существовать.", "Что есть вы, что неn - ему без разницы.")]))
		self.son.change_text (6, 'Нажмите ESC, чтобы выйти.')
		self.status = 'dead'
		self.kill ()
		self.move = False

	def end_text (self):
		pass

	def auto_text (self, args):
		x = 1
		for i in args:
			self.son.change_text (x, i)
			x += 1

	def dice_rolling (self):

		information_screen.blit (roll_screen, (0,0))
		roll_screen.fill ((black))

		roll_screen.blit (self.line, (40, 20))
		roll_screen.blit (self.marker.image, (self.mx, self.my+10))

		if self.go_left == False:
			self.mx = self.mx + dice_speed

		if self.go_left == True:
			self.mx = self.mx - dice_speed

		if self.mx > 410:
			self.go_left = True

		if self.mx < 20:
			self.go_left = False

		try:
			color = self.line.get_at((self.mx-20, 10))
		except:
			color = 'NONE'
		finally:
			print (self.mx)
			print (str(color))

		value = self.color_defenition (color)

		roll_screen.blit(fonts.font3.render ('Нажмите E, когда меч ближе к центру.', True, (250,250,250)),(60,150))
		roll_screen.blit(fonts.font3.render ('Ваша атака!', True, (250,250,250)),(60,60))

		if value != 7:
			self.dice_value = value
			roll_screen.blit(fonts.font12.render (str(value), True, (250,250,250)),(240,60))

		if self.control.k_e == True:
			self.control.k_e = False
			self.dice_fun = False
			#self.dice_value = int((self.mx - 80) / 20)
			self.attack_roll = True
			self.control.e_cntrl = False
			#self.mx = 20

	def color_defenition (self, color):
		if color[0:3] == C1:
			return 1

		elif color[0:3] == C2:
			return 2

		elif color[0:3] == C3:
			return 3

		elif color[0:3] == C4:
			return 4

		elif color[0:3] == C5:
			return 5

		elif color[0:3] == C6:
			return 6

		else:
			return 7

												
	def battle_action_main (self):
		if self.is_death == False and self.etwas.status != 'killed':
			#self.son.change_text (7, 'Вы получили 20 монет')
			self.press_to_kill_fun ()
	
			if self.turn_main == True :
				self.son.clear_text()
				self.son.change_text (1, "Вам угрожает %s . Что будете делать?" % self.etwas.mname.strip())
				self.son.change_text (3, "1 - атаковать; 2 - спец.способность; 3 - убегать")
		
				if self.control.k_1 == True:
					self.mx = random.choice ((20, 40, 80,120,140,160,180))
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


		

	def press_to_kill_fun (self):
		if self.press_to_kill == True and self.control.k_e == True:
			self.press_to_kill = False
			self.control.k_e = False
			self.etwas.hp = 0
			self.dustAnim.play()
	#def pos_definition(self):



	def special_fun (self):


			if self.control.k_1 == True:
				self.control.k_1 = False
				self.son.clear_text ()

				if self.etwas.hp <= 100 and self.sp >0:
					self.sp -= 1
					self.press_to_kill = True
					self.son.change_text (1, "Вы шепчете слова молитвы:")
					self.son.change_text (2, "'Да воскреснет Бог, и расточатся врази Его,")
					self.son.change_text (3, "и да бежат от лица Его ненавидящии Его. Яко исчезает дым, да исчезнут;")
					self.son.change_text (4, "яко тает воск от лица огня, тако да погибнут беси от лица любящих Бога")
					self.son.change_text (5, "и знаменующихся крестным знамением...'")

					
					self.son.change_text (7, "Нажмите Е")
					
					#self.etwas.hp = 0
					#self.etwas.kill()

				elif self.etwas.hp > 100 or self.sp<=0:
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
					img.healAnim.play()


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
			self.slashAnim.play()
			self.son.clear_text ()

			a = self.dice_value
			b = random.randint (1,6)
			c = self.at + a + self.weapon.at_mod
			d = monster.ac + b
		
			self.son.change_text (2, "Ваша атака: "+str(c) + "  Защита монстра: "+ str(d))
			self.son.change_text (1, 'БРОСОК КУБИКА: '+str(self.dice_value))
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


		if self.control.k_e == True and self.control.e_cntrl == True and self.wait_for_next_turn == True and monster.hp >0:
			self.wait_for_next_turn = False
			self.control.k_e = False
			self.monster_turn = True
			self.assault = False
			self.control.e_cntrl = False
		
		elif self.control.k_e == True and self.control.e_cntrl == True and self.wait_for_next_turn == True and monster.hp <= 0:
			#monster.death_check (self)
			self.wait_for_next_turn = False
			self.control.k_e = False
			self.monster_turn = False
			self.assault = False
			self.control.e_cntrl = False


