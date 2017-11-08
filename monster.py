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
import img
import items
import text_data.skelet_lord2_dict
from functions import end_dialog, war, br_change, br_auto
import ideas

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
	def __init__(self, x, y, battle, textus, control, at, ac, hp, dem, son, exp, item = items.no_item, special_opt = False):
		sprite.Sprite.__init__(self)
		#self.image = Surface ((45,45))
		#self.image.fill ((120,30,200))

		#BASE DATA
		self.image=image.load('images/zombi.png')
		#self.image.set_colorkey ((255,255,255))
		self.race = 'undead'
		self.flee = True


		self.rect = Rect (0,0, 45,45)
		self.rect.x = x*PF_WIDTH
		self.rect.y = y*PF_HEIGHT

		self.control = control
		self.son = son
		self.battle = battle

		#CHAR DATA
		self.mname = 'Зомби'
		self.at = at
		self.ac = ac
		self.hp = hp
		self.damage = dem
		self.exp = exp

		self.item = item

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
		self.order = False

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
		self.icon = pygame.image.load ('images/skull.png')
		self.hp_bar =Bar (12,15, red)
		self.at_ic = pygame.image.load ('images/at.png')
		self.ac_ic = pygame.image.load ('images/ac.png')

	def render_monster_inf (self):

		instrumental_screen.blit (monster_screen, (678,15))
		monster_screen.fill ((black))
		monster_screen.blit (self.icon, (25,45))

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
	def special_death (self,hero):
		pass
	def death_check (self, hero):

		if self.hp <= 0:
			if self.item == items.no_item:

				self.son.clear_text ()
				hero.char_value['2exp'] += self.exp
				self.son.change_text (2, "%s повержен!" % self.mname.lstrip())
				self.son.change_text (4, "Вы получаете опыт: %s " % self.exp)
				gold = random.randint(1,30)
				self.son.change_text (5, "Так же вы нашли немного золотишка: %s " % str(gold) )
				hero.gold +=gold
#				self.son.change_text (5, "С трупа вы забрали: %s " % self.item.name)	
				self.status = 'killed'
				hero.turn_main = True
				hero.move = True
				self.kill ()
				hero.collide_control = False
			elif self.item != items.no_item:
				self.get_item(hero, self.item)	

				self.son.clear_text ()
				hero.char_value['2exp'] += self.exp
				self.son.change_text (2, "%s повержен!" % self.mname.lstrip())
				self.son.change_text (4, "Вы получаете опыт: %s " % self.exp)
				self.son.change_text (5, "С трупа вы забрали: %s " % self.item.name)	
				gold = random.randint(1,30)
				self.son.change_text (6, "Так же вы нашли немного золотишка: %s " % str(gold) )
				hero.gold +=gold
				self.status = 'killed'
				hero.turn_main = True
				hero.move = True
				self.kill ()
				hero.collide_control = False
			self.special_death(hero)

	def interaction (self, hero):
		if self.order == False:
			for i in hero.journal:
				if i.name == 'Порядок магнитуд':
					self.branch = 1
					self.order = True

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
			adventure_screen.blit(fonts.font4.render (str(self.hp_mod)+ ' hp', True, (self.color)),(position.x+self.x_mod*(self.x_mod/60), position.y - 30 - self.x_mod))

			if self.x_mod > 200:
				self.start_rendering = False
				self.x_mod = 0

	# DIALOG METHODS


	def dialog_special (self, hero):

		pass


	def dialog_options (self,hero):
		self.dialog_special (hero)

		if self.add_information == 'end':

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

#			a = random.randint (1,6)
			self.branch_do = 'done'
			self.s = 1
			self.n = 0
			self.branch = self.branch_id
#			if a >3:
#				self.branch = 1
#			if a <=3:
#				self.branch = 2

		if self.add_information == 'passage' and self.control.k_e == True:


			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
				hero.view.a = 0

		if self.add_information == 'go':
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
				hero.view.a = 0

				
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

		if self.control.k_e == True and self.wait_for_next_turn == True and self.control.e_cntrl == True and hero.is_death == False:
			self.control.k_e = False
			hero.turn_main = True
			self.son.clear_text ()

	def get_item (self, hero, item):
		hero.inv.append(item)


class SkeletLord (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = text_data.skelet_lord2_dict.text
		self.lbolt = False
		self.mname = 'Скелет Лорд'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/skeleton3.png')
		self.image.set_colorkey ((254,254,254))
		self.item = items.gold_key
		self.hit = False

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

		if self.add_information == 'dance':

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = 5
				self.s = 1
				self.n = 0

		if self.add_information == 'key' and self.control.k_e == True:
			

			hero.collide_control = False
			hero.start_conv = True
			hero.move = True
			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (4, 'Вы получили %s' % self.item.name)
			hero.son.change_text (3, 'Скелет-лорд протягивает вам ключик.')
			hero.char_value['2exp'] += 50
			hero.inv.append (self.item)
			
			self.item = items.no_item
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = 6
				self.s = 1
				self.n = 0


		if self.add_information == 'faith' and self.control.k_e == True:
			

			#hero.collide_control = False
			hero.start_conv = True
			#hero.move = True
			self.control.k_e = False
			
			hero.son.clear_text ()

			if hero.sp > random.randint(1,6):
				hero.inv.append (self.item)
				self.item = items.no_item
				hero.son.clear_text ()
				hero.son.change_text (5, 'Скелет рассыпается в прах.')
				hero.son.change_text (4, 'Вы подбираете из кучки праха золотой ключик.')

			elif hero.sp < random.randint(1,6):

				self.control.k_e = False
				self.agression = True
				hero.turn_main = True
				hero.start_conv = True
				hero.view.a = 0

		if self.add_information == 'pain':
			if self.hit == False:
				self.hit = True
				hero.hp -= 1
				if hero.hp <= 0:
					hero.son.clear_text ()
					hero.son.change_text (3, 'Вас съел скелет.')
					hero.son.change_text (2, 'Вы умерли и столкнулись с чем-то принципиально инаковым.')
					hero.son.change_text (4, 'О вас больше никто не вспомнит.')
					self.son.change_text (6, 'Нажмите ESC, чтобы выйти.')
					hero.status = 'dead'
					hero.kill ()
					hero.move = False

					hero.collide_control = False

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


		if self.add_information == 'go':
			self.hit = False
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


	def battle_action (self, hero):

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
			img.boltAnim.play ()
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



class ZombiLord (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Зомби Лорд'
		#self.image.fill ((220,130,100))
		self.ll = False

		self.image = image.load('images/zombi.png')
		self.image.set_colorkey ((254,254,254))
		self.item = items.silver_key
		self.quest = False
	def interaction (self, hero):
		Monster.interaction (self, hero)
		if self.quest == True:
			for i in hero.quest.keys():
				if i == 'мёртвая вода':
					for a in hero.inv:
						if a == items.death_water:
							self.branch = 5
							self.quest = False
							self.s = 1
							self.n = 0
							break

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

		if self.add_information == 'quest' and self.control.k_e == True:
			hero.move = True
			hero.quest['мёртвая вода']= True
			self.control.k_e = False
			self.quest = True

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы получили квест: найти мёртвой воды!')


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True


		if self.add_information == 'water' and self.control.k_e == True:
			hero.move = True
			hero.quest['мёртвая вода']= 'Done'
			self.control.k_e = False

			hero.inv.append (self.item)
			hero.inv.remove(items.death_water)
			
			hero.son.clear_text ()
			hero.son.change_text (3, 'Вы отдали предмет: %s ' % items.death_water.name)			
			hero.son.change_text (2, 'Вы получили предмет: %s ' % self.item.name)
			self.quest = False
			hero.son.change_text (5, 'Вы проявили доброту и человеченость + 50 опыта!')
			hero.char_value['2exp'] += 50
			self.item = items.no_item
			self.hp +=5

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True


class SkeletKing (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Скелет Король'
		#self.image.fill ((100,100,100))
		self.ll = False
		self.image = image.load('images/tiles/throne.png')
		self.image.set_colorkey ((254,254,254))
		#self.item = items.silver_key		
		self.rect = self.image.get_rect()
		self.rect.x = x*PF_WIDTH
		self.rect.y = y*PF_HEIGHT
		self.reducted = False


		#self.image.fill ((220,130,100))

		self.quest = False
		self.order = True
		self.check_for_courage = False
		self.one_death = False
		self.light1 = True
		self.light2 = True
		self.all = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
		if 'peidron_in_prison' in hero.quest and self.all == False:
			self.all = True
			self.branch = 8


		self.light1 = True
		self.light2 = True
		if hero.sp > 2 and self.check_for_courage == False:
			self.branch = 1
			self.check_for_courage = True
		if self.one_death == True and ideas.reductio in hero.journal and self.reducted == False:
			self.branch = 3



	def death_check (self, hero):

		if self.hp <= 0:


				self.son.clear_text ()
				hero.char_value['2exp'] += self.exp
				self.son.change_text (2, "%s повержен!" % self.mname.lstrip())
				self.son.change_text (4, "Вы получаете опыт: %s " % self.exp)
				gold = random.randint(1,30)
				#self.son.change_text (5, "Так же вы нашли немного золотишка: %s " % str(gold) )
				#hero.gold +=gold
#				self.son.change_text (5, "С трупа вы забрали: %s " % self.item.name)	
				#self.status = 'killed'
				hero.turn_main = True
				hero.move = True
				self.agression = False
				self.hp = 15
				#self.kill ()
				hero.collide_control = False
				self.one_death = True

	def dialog_special (self, hero):
		
		if self.add_information == 'light':
			if self.light1 == True:
				img.boltAnim.play ()
				hero.hp -= random.randint(1,6)
				self.light1 = False

		if self.add_information == 'push' and self.control.k_e == True:
			if hero.char_value['3at'] + hero.char_value['6sp']//3 >= 8:
				self.rect.y -= 45
				hero.char_value['2exp'] += 100
				br_change (self, 10)

			else:
				br_change (self, 9)


		if self.add_information == 'light2':
			if self.light2 == True:
				img.boltAnim.play ()
				hero.hp -= random.randint(1,6)
				self.light2 = False

		if self.add_information == 'idea_of_evil' and self.control.k_e == True:
			self.control.k_e = False
			hero.quest['idea_of_evil'] = True
			hero.char_value['2exp'] += 200
			self.reducted = True

			hero.son.clear_text ()
			hero.son.change_text (2, 'Потрясённые открывшимся знанием вы отходите назад.')
			hero.son.change_text (3, 'Нечеловеческий ужас отпускает вас. Вам даже не верится, что')
			hero.son.change_text (4, 'это порождение мира-без-нас связано с обычным человеческим злом.')
			hero.son.change_text (5, 'Но что делать теперь?')

			end_dialog (self, hero)


class Goblin (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = text_data.skelet_lord2_dict.text
		self.lbolt = False
		self.mname = 'Гоблин'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/skeleton3.png')
		self.image.set_colorkey ((254,254,254))
		self.item = items.faith_potion
		self.hit = False

	def dialog_special (self, hero):
		pass

