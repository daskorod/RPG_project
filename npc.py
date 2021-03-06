﻿from pygame import sprite
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
from monster import Monster
import classes
import ideas
from functions import end_dialog, war, br_change, br_auto
import items
import ends
import menu
import sounds
import img


class Gilbert (classes.Monk):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.race = 'human'
		self.mname = 'Отец Гильберт'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		self.image.set_colorkey ((254,254,254))
		self.g = 1000
		self.order = True
		self.quest = False
		self.hit = False

	def battle_action (self, hero):
		if self.hit == False:
			hero.quest['gilbert_hit'] = True
			self.hit = True
		classes.Monk.battle_action (self, hero)

	def dialog_special (self, hero):
		if self.add_information == 'gold' and self.control.k_e == True:
			self.control.k_e = False
			if hero.gold >= 20:
				hero.gold -= 20

				self.branch = 4
				self.s = 1
				self.n = 0

			else:
				self.branch = 6
				self.s = 1
				self.n = 0

		if self.add_information == 'gold_inf' and self.control.k_e == True:
			self.control.k_e = False
			if hero.gold >= 20:
				hero.gold -= 20

				self.branch = 5
				self.s = 1
				self.n = 0

			else:
				self.branch = 13
				self.s = 1
				self.n = 0						

		if self.add_information == 'hit' and self.control.k_e == True:
			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Потирая кулак вы отошли во свояси.')
			hero.son.change_text (3, 'Посетители таверны даже не отреагировали.')
			hero.son.change_text (4, 'Они просто пили своё пиво.')
			hero.son.change_text (5, 'А вас кольнула булавочкой совесть: правильно ли?')


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.quest['gilbert_hit'] = True
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'trinktour' and self.control.k_e == True:
			hero.move = True

			self.control.k_e = False
			hero.gold = 0
			if ideas.gelassenheit not in hero.journal:

				hero.son.clear_text ()
				hero.son.change_text (2, 'Вы долго пили. И пьянствовали. Но для чего?')
				hero.son.change_text (3, 'Вы и сами не знаете. Вы тупо просадили все деньги.')
				hero.son.change_text (4, 'Вы и сами уже не помните, что происходило и кто за что платил.')
				hero.son.change_text (5, 'Теперь у вас лишь головная боль, а впереди много дел.')

				self.branch = 7
				self.s = 1
				self.n = 0


			if ideas.gelassenheit in hero.journal:

				hero.son.clear_text ()
				hero.son.change_text (2, 'Вы долго пили. И пьянствовали. Но для чего?')
				hero.son.change_text (3, 'Вспомнив концепцию отрешённости, вы восприняли данную пьянку как нечто пустое.')
				hero.son.change_text (4, 'Отрешившись от своего тела, потребляющего алкоголь вы обратились к вечности.')
				hero.son.change_text (5, 'И преисполнились внутреннего спокойствия и силы. ')
				hero.son.change_text (6, 'На утро вы чувствовали себя отлично. Ваша вера возросла.')

				hero.char_value['6sp'] += 1
				hero.sp +=1


				self.branch = 12
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'stupid' and self.control.k_e == True:
			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы презрительно отозвались об идеях монаха, которые')
			hero.son.change_text (3, 'он вынашивал у себя под сердцем. Достойный ли это поступок?')
			hero.son.change_text (4, 'Кто знает? Может вы искренне считали его построения заблужденем?')
			hero.son.change_text (5, 'Или же проявили невнимание и нетерпение?')


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
				
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'magnus' and self.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.order_of_magnitude
					break
				x +=1


			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Порядка Магнитуд в свой журнал.')
			hero.son.change_text (3, 'Теперь вы будете по-другому смотреть на мир монстров.')
			hero.son.change_text (4, 'Кто знает, до чего вас это доведёт.')

			if ideas.individ not in hero.journal:
				self.branch = 9			
				self.s = 1
				self.n = 0

			else:
				self.branch = 7
				self.s = 1
				self.n = 0


			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'individ' and self.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.individ
					break
				x +=1


			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Индивидуации Города в свой журнал.')
			hero.son.change_text (3, 'Теперь вы будете по-другому смотреть на городские противоречия.')
			hero.son.change_text (4, 'Кто знает, до чего вас это доведёт.')


			if ideas.order_of_magnitude not in hero.journal:
				self.branch = 8			
				self.s = 1
				self.n = 0

			else:
				self.branch = 7
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True


		if self.add_information == 'gelassenheit' and self.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.gelassenheit
					break
				x +=1


			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Отрешённости в свой дневничок.')
			hero.son.change_text (3, 'Теперь вы по-другому будете относиться к внутреннему и внешнему.')
			hero.son.change_text (4, 'Кто знает, до чего вас это доведёт?')

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True


		if self.add_information == 'passage' and self.control.k_e == True:


			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0




class Barmen (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Бармен'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/barmen.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True

	def pay (self, add_information, quantity, where_sucsess, where_not_sucsess, hero):
		if self.add_information == add_information:
			if hero.gold >= quantity:
				hero.gold -= quantity

				self.branch = where_sucsess
				self.s = 1
				self.n = 0

			else:
				self.branch = where_not_sucsess
				self.s = 1
				self.n = 0
				self.matter = where_sucsess
			

	def dialog_special (self, hero):
		self.pay ('pay_for_sleep', 100, 2, 1, hero)
		

		self.pay ('pay_for_food', 40, 3, 1, hero)
		

		self.pay ('pay_for_drink', 20, 4, 1, hero)
		

		if self.add_information == 'sleep' and self.control.k_e == True:
			self.control.k_e = False

			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы отлично отдохнули.')
			hero.son.change_text (3, 'Ваши силы восстанавливаются.')
			hero.son.change_text (4, 'Хотя, тяжесть грехов и старые раны так просто не исцелить.')
			hero.son.change_text (5, 'Но вы готовы к новому дню!')
			hero.day += 1
			#hero.sp = hero.char_value['6sp']
			hero.hp = hero.char_value['5hp']

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

			hero.collide_control = False
			hero.start_conv = True								

		if self.add_information == 'pray':
			if random.randint(1,6) <= hero.sp:
				self.branch = 6
				self.s = 1
				self.n = 0

			else:
				self.branch = 5
				self.s = 1
				self.n = 0		

		if self.add_information == 'pray_ok' and self.control.k_e == True:
			self.control.k_e = False

			self.branch = self.matter
			self.s = 1
			self.n = 0



		if self.add_information == 'food' and self.control.k_e == True:
			self.control.k_e = False

			hero.move = True

			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы неплохо поели и частично восстановили свои силы.')


			if hero.hp < hero.char_value['5hp']:
				hero.hp = hero.hp + 2

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

			hero.collide_control = False
			hero.start_conv = True			

		if self.add_information == 'passage' and self.control.k_e == True:


			self.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


class Martin (classes.Monk):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.race = 'human'
		self.mname = 'Отец Мартин'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		self.image.set_colorkey ((254,254,254))
		self.g = 1000
		self.order = True
		self.quest = False
		self.qcheck = False
		self.gold_quest = False
		self.first = True


	def interaction (self, hero):
		Monster.interaction (self, hero)
		if 'gilbert_hit' in hero.quest and self.qcheck == False and self.first == False:
			self.branch = 2
			self.qcheck = True
		elif 'gilbert_hit' in hero.quest and self.qcheck == False and self.first == True:
			self.branch = 6
			self.qcheck = True
		self.first = False
		if 'martin_gold' in hero.quest and hero.quest['gold_cup'] >= 1000 and self.gold_quest == False:
			self.branch = 9
			self.gold_quest = True

	def dialog_special (self, hero):
		if self.add_information == 'gold_quest':
			hero.quest['martin_gold'] = True

		if self.add_information == 'concept' and self.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.dark
					break
				x +=1

			self.control.k_e = False
			hero.char_value['6sp'] +=1
			hero.sp +=1
			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Божественного Мрака в свой дневничок.')
			hero.son.change_text (3, 'Теперь вы по-другому будете относиться к сущему и не-сущему.')
			hero.son.change_text (4, 'Кто знает, до чего вас это доведёт?')

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

class Peter (classes.Monk):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.race = 'human'
		self.mname = 'Отец Пётр'
		self.image = image.load('images/priest4.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.g = 1000
		self.order = True
		self.quest = False
		self.qcheck = False
		self.gold_quest = False
		self.first = True

	def dialog_special (self, hero):
		if self.add_information == 'exsor' and self.control.k_e == True:
			hero.control.k_esc = True


class Rouge (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Вор'
		self.race = 'human'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/rouge.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))

		self.order = True
		self.quest = False
		self.peid = False
		self.first_peid = True

	def interaction (self, hero):
		Monster.interaction (self, hero)

		if 'pedron_quest' in hero.quest and self.first_peid == True:
			self.first_peid = False
			br_change (self, 3)


		if self.peid == True:
			if ideas.anarcho in hero.journal and hero.gold >= 1000:
				br_change (self, 10)
			elif ideas.anarcho in hero.journal and hero.gold < 1000:
				br_change (self, 12)
			elif ideas.anarcho not in hero.journal and hero.gold >= 1000:
				br_change (self, 14)
			elif ideas.anarcho not in hero.journal and hero.gold <= 1000:
				br_change (self, 13)

	def dialog_special (self, hero):
		if self.add_information == 'anarcho':

			if 'anarcho' not in hero.quest:
				hero.quest['anarcho'] = True

		if self.add_information == 'gold' and self.control.k_e == True:

			hero.gold -= 1000
			br_auto (self)	

		if self.add_information == 'anarcho' and self.control.k_e == True:

			br_auto (self)

		if self.add_information == 'sliv' and self.control.k_e == True:
			self.peid = False
			for i in hero.locations_dict['tower2'].block_group:
				try:
					if i.mname == 'Пейдрон':
						i.kill ()
						break
				except:
					pass

			hero.char_value['2exp'] += 200
			hero.quest['peidron_in_prison'] = True

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы провернули многоходовочку.')
			hero.son.change_text (3, 'Конечно, вы вступили в сговор с ворами.')
			hero.son.change_text (4, 'Но ведь вы предотвратили кровавую гекатомбу?')
			hero.son.change_text (5, 'Вы нанесли удра в основание злой силы, клубящейся над городом... ?')			
			end_dialog (self, hero)			

		if self.add_information == 'do_it' and self.control.k_e == True:
			self.peid = True
			if ideas.anarcho in hero.journal and hero.gold >= 1000:
				br_change (self, 10)
			elif ideas.anarcho in hero.journal and hero.gold < 1000:
				br_change (self, 12)
			elif ideas.anarcho not in hero.journal and hero.gold >= 1000:
				br_change (self, 14)
			elif ideas.anarcho not in hero.journal and hero.gold <= 1000:
				br_change (self, 13)

		if self.add_information == 'narco' and self.control.k_e == True:


			if ideas.anarcho in hero.quest:
				if hero.gold > 50:
					br_change (self, 8)
				else:
					br_change (self, 9)					
			else:
				if hero.gold > 50:
					br_change (self, 6)
				else:
					br_change (self, 7)					

		if self.add_information == 'narco_buy' and self.control.k_e == True:

			hero.gold -= 50

			hero.inv.append (items.melanj)
			br_auto (self)

		if self.add_information == 'anarcho_concept' and self.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.anarcho
					break
				x +=1


			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Анархизма в свой дневничок.')

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True


		if self.add_information == 'passage' and self.control.k_e == True:


			self.control.k_e = False

			hero.view.a = 0
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

class Augustine (classes.Monk):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Августин'
		self.race = 'human'
		self.item = items.peidron_key
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))

		self.order = True
		self.quest = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
		if 'gov1' in hero.quest and 'anarcho' in hero.quest:
			self.branch = 12
			hero.quest.pop('gov1')


	def dialog_special (self, hero):
#		if self.add_information == 'passage' and self.control.k_e == True:
#			self.control.k_e = False
#
#			if self.branch_do == 'go':
#				self.branch_do = 'done'
#				self.branch = self.branch_id
#				self.s = 1
#				self.n = 0
		if self.add_information == 'gain' and  self.control.k_e == True:
			
			hero.inv.append (items.doc_elite)
			br_auto (self)
			hero.gold += 20
			hero.char_value['2exp'] += 50
			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы получаете Красную грамоту и немного золотишка.')
			hero.son.change_text (3, 'Как приятно работать на родное правительство!')
			hero.son.change_text (4, 'Оно о тебе всегда позабится.')
			end_dialog (self, hero)

		if self.add_information == 'info' and  self.control.k_e == True:
			
			if ideas.anarcho in hero.journal:
				br_change (self, 14)
			else:
				br_change (self, 15)
			
		if self.add_information == 'quest1':
			
			hero.quest['gov1'] = True
			hero.inv.append (items.doc)
			end_dialog (self, hero)


		if self.add_information == 'arrest' and self.control.k_e == True:
			self.control.k_e = False
			if hero.gold <30:
				br_change(self, 4)
			else:

				br_change(self, 3)

			#переход на локацию башня, или тюрьма.

		if self.add_information == 'yel':
			
			if hero.gold <30:
				br_change(self, 6)
			else:
				hero.gold -= 30
				br_change(self, 7)
				hero.inv.append (items.doc)

		if self.add_information == 'permit':
			
			if hero.gold <100:
				br_change(self, 10)
				hero.son.clear_text ()
				hero.son.change_text (2, 'К сожалению у вас не хватает денег,')
				hero.son.change_text (3, 'чтобы получить пропуск в подземелье.')
				hero.son.change_text (4, 'Приходите, когда у вас будет больше денег.')
				hero.son.change_text (4, 'Или не приходите вообще!')
				end_dialog (self, hero)
			else:
				hero.gold >= 100
				hero.gold -= 100
				br_change(self, 10)
				hero.inv.append (items.permit)
				hero.son.clear_text ()
				hero.son.change_text (2, 'Вы получаете Пропуск в подземелье.')
				hero.son.change_text (3, 'За него вам пришлось отвалить 100 золотых.')
				hero.son.change_text (4, 'Действительно, что такое ограбление по сравнению с')
				hero.son.change_text (4, 'основанием государства!')
				end_dialog (self, hero)


		if self.add_information == 'red':
			
			if hero.gold <200:
				br_change(self, 6)
			else:
				hero.gold -= 200
				br_change(self, 7)
				hero.inv.append (items.doc)

		if self.add_information == 'prison' and self.control.k_e == True:
			self.control.k_e = False
			
			end_dialog (self, hero)
			#hero.death()
			menu.ending ('Вы закончили свою жизнь в тюрьме. Вас посадили за решётку и забыли за ненадобностью. Кормили вас скудно. От холода и голода вы заболели и вскоре умерли. Лёжа на гнилой соломе вы прошептали ваши последние слова "еды..." и испустили дух.', 'images/end/prison.png', 2, pic_x = 50, time_scroll = 40, pic_y = 60, speed_mod = 5)

		if self.add_information == 'war' and self.control.k_e == True:
			self.control.k_e = False
			self.agression = True
			#self.agression = True
			hero.turn_main = True
			hero.start_conv = True
			hero.view.a = 0
			hero.direction = 2

			for i in hero.locations_dict['tower1'].block_group:
				if i.__class__.__name__ == 'Guard2':
					i.agression = True
					hero.etwas = i			

#			a = random.randint (1,6)


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

class Guard (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Стражник'
		self.race = 'human'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/guard.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.sound = sounds.hit
		self.order = True
		self.quest = False
		self.second = False
		self.step_away = False
		self.armor = 2
	def interaction (self, hero):
		Monster.interaction (self, hero)
		if self.step_away == False:
			if items.permit in hero.inv and self.second == False:
				br_change(self, 11)
			elif items.permit in hero.inv and self.second == True:
				br_change(self, 10)
			elif hero.gold>200 in hero.inv and self.second == True:
				br_change(self, 8)
			elif self.second == True:
				br_change(self, 9)

	def dialog_special (self, hero):
		if self.add_information == 'what':
			
			if hero.gold <20:
				br_change(self, 2)
			else:
				br_change(self, 1)
		if self.add_information == 'doc' and self.control.k_e == True:
			self.control.k_e = False
			if items.doc in hero.inv:
				br_change(self, 7)
			else:
				br_change(self, 4)

		if self.add_information == 'arrest' and self.control.k_e == True:
			end_dialog (self, hero)
			menu.ending ('Вы закончили свою жизнь в тюрьме. Вас посадили за решётку и забыли за ненадобностью. Кормили вас скудно. От холода и голода вы заболели и вскоре умерли. Лёжа на гнилой соломе вы прошептали ваши последние слова "еды..." и испустили дух.', 'images/end/prison.png', 2, pic_x = 50, time_scroll = 40, pic_y = 60, speed_mod = 5)
			
			#переход на локацию башня, или тюрьма.

		if self.add_information == 'briber':
			
			if hero.gold <100:
				br_change(self, 6)
			else:
				br_change(self, 5)

		if self.add_information == 'open':
			self.rect.x += 45
			self.step_away = True
			hero.char_value['2exp'] += 60			
			br_auto (self)
			end_dialog (self, hero)

		if self.add_information == 'second':

			self.second = True			
			br_auto (self)
			end_dialog (self, hero)

		if self.add_information == 'briebery_gold':
			hero.gold -= 100

			self.second = True			

			end_dialog (self, hero)

		if self.add_information == 'briebery_200' and self.control.k_e == True:
			self.control.k_e = False
			hero.gold -= 200
			self.rect.x += 45
			self.step_away = True	
			self.second = True			
			br_auto (self)


class Guard2 (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Стражник'
		self.race = 'human'
		self.flee = False
		self.sound = sounds.hit
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/guard.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))

		self.order = True
		self.quest = False
		self.second = False
		self.step_away = False
		self.priest_action = False
		self.wait_for_priest_turn = False
		self.priest_turn = False
		self.heal = False
		self.armor = 2

#	def interaction (self, hero):
		#Monster.interaction (self, hero)
	def special_death (self,hero):
		hero.collide_control = True
		hero.move = False
		hero.direction = 1
		for i in hero.locations_dict['tower1'].block_group:
			if i.__class__.__name__ == 'Augustine':
				i.agression = True
				hero.etwas = i	

	def dialog_special (self, hero):
		pass

	def battle_action (self, hero):
		if hero.monster_turn == True:
			self.son.clear_text ()
			a = random.randint (1,6)
			b = random.randint (1,6)

			c = self.at + a

			if self.master_of_sword != 0:
				if a > 6-self.master_of_sword:
					d = hero.ac + b

			else:
				d = hero.ac + b + hero.armor

			self.son.change_text (1, "Атака монстра: "+str(c) + "  Защита ваша: "+ str(d))
			if c >= d:
				
				if int(c/d)>1:
					damg = self.damage*int(c/d)
					self.son.change_text (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
					self.son.change_text (5, 'Критический урон: '+str(self.damage*int(c/d)))
					
				else:
					self.son.change_text (4, "Монстр попал и нанес сокрушительный удар!")
					damg = self.damage
					self.son.change_text (5, 'Урон: '+str(self.damage))

				if hero.prevent == 0: hero.hp = hero.hp - damg

				else:
					if hero.prevent >= damg: 
						pass
					else:
						hero.hp = hero.hp - (damg-hero.prevent)

			elif c<d:
				self.son.change_text (4, 'Вы уклонились!')	
		
		
			self.son.change_text (7, 'Нажмите Е')
			hero.monster_turn = False
			self.priest_turn = True

		if self.priest_turn == True and self.control.k_e == True:
			self.control.k_e = False
#			self.wait_for_priest_turn = False
			self.son.clear_text ()
			a = random.randint (1,3)
			#boltAnim.blit (adventure_screen, (100, 100))
		
			self.son.change_text (1, "Священник тем временем бормотал слова молитв...")
			#self.son.change_text (2, "")
			self.son.change_text (3, 'Нажмите Е')
		
			self.lbolt = True
			self.priest_turn = False
			self.heal = True

		if self.heal == True and self.control.k_e == True:
			self.control.k_e = False
			self.son.clear_text ()
			a = random.randint (1,3)
			#boltAnim.blit (adventure_screen, (100, 100))
		
			self.son.change_text (1, "Раны на стражнике начали затягиваться!")
			#self.son.change_text (2, "")
			self.son.change_text (3, 'Нажмите Е')
			self.hp += a
			if self.hp > 7:
				self.hp = 7
		
			self.heal = False
			self.wait_for_next_turn = True
						
		if self.control.k_e == True and self.wait_for_next_turn == True and self.control.e_cntrl == True and hero.is_death == False:
			self.wait_for_next_turn = False
			self.control.k_e = False
			hero.turn_main = True
			self.son.clear_text ()


class Hermit (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Отшельник'
		self.race = 'human'
		self.flee = True
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/hermit.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))

		self.order = True
		self.quest = False
		self.second = False
		self.step_away = False
		self.priest_action = False
		self.wait_for_priest_turn = False
		self.priest_turn = False
		self.heal = False

#	def interaction (self, hero):
		#Monster.interaction (self, hero)
#	def special_death (self,hero):
#		hero.collide_control = True
#		for i in hero.locations_dict['tower1'].block_group:
#			if i.__class__.__name__ == 'Augustine':
#				i.agression = True
#				hero.etwas = i	

	def dialog_special (self, hero):
		if self.add_information == 'reductio':
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.reductio
					break
				x +=1


			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Редукции в свой дневничок.')
			hero.son.change_text (3, 'Может быть теперь при встрече с чем-то неразрешимым и тёмным')
			hero.son.change_text (4, 'вам удастся свести его к чему-то более простому и ясному?')

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'thing' and self.control.k_e == True:
			self.control.k_e = False
			hero.inv.append(items.bottle)

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы взяли странную бутылку у старика.')
			hero.son.change_text (3, 'Кто знает, может вам её лучше выбросить?')
			end_dialog (self, hero)
		if self.add_information == 'learn':
			if ideas.reductio in hero.journal:
				br_change(self, 4)
			else:
				br_change(self, 3)
			
class Peidron (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Пейдрон'
		self.race = 'human'
		self.flee = False
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/peid.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.sound = sounds.pain
		self.order = True
		self.quest = False
		self.second = False
		self.step_away = False
		self.priest_action = False
		self.wait_for_priest_turn = False
		self.priest_turn = False
		self.heal = False
		self.armor = 5
		self.prevent = 1

#	def interaction (self, hero):
		#Monster.interaction (self, hero)
#	def special_death (self,hero):
#		hero.collide_control = True
#		for i in hero.locations_dict['tower1'].block_group:
#			if i.__class__.__name__ == 'Augustine':
#				i.agression = True
#				hero.etwas = i	
	def special_death (self,hero):
		hero.quest['peidron_is_dead'] = True


	def dialog_special (self, hero):
		if self.add_information == 'wars' and self.control.k_e == True:
			hero.hp -= 3
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

class Merch (Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Купец'
		self.race = 'human'
		self.flee = True
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/merch.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))

		self.order = True
		self.quest = False
		self.second = False
		self.step_away = False
		self.priest_action = False
		self.wait_for_priest_turn = False
		self.priest_turn = False
		self.heal = False

#	def interaction (self, hero):
		#Monster.interaction (self, hero)
#	def special_death (self,hero):
#		hero.collide_control = True
#		for i in hero.locations_dict['tower1'].block_group:
#			if i.__class__.__name__ == 'Augustine':
#				i.agression = True
#				hero.etwas = i	

	def dialog_special (self, hero):
		if self.add_information == 'reductio':
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.journal[x] = ideas.reductio
					break
				x +=1


			self.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы записали концепцию Редукции в свой дневничок.')
			hero.son.change_text (3, 'Может быть теперь при встрече с чем-то неразрешимым и тёмным')
			hero.son.change_text (4, 'вам удастся свести его к чему-то более простому и ясному?')

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

		if self.add_information == 'thing' and self.control.k_e == True:
			self.control.k_e = False
			hero.inv.append(items.bottle)

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы взяли странную бутылку у старика.')
			hero.son.change_text (3, 'Кто знает, может вам её лучше выбросить?')

		if self.add_information == 'learn':
			if ideas.reductio in hero.journal:
				br_change(self, 4)
			else:
				br_change(self, 3)

class Tubus (classes.Monk):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.race = 'human'
		self.mname = 'Брат Тубус'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/priest.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		self.image.set_colorkey ((254,254,254))
		self.g = 1000
		self.order = True
		self.quest = False
		self.item = items.gold_ring


	def interaction (self, hero):
		Monster.interaction (self, hero)
		if items.old_book in hero.inv:
			br_change(self, 3)

	def dialog_special (self, hero):
		if self.add_information == 'quest':
			hero.quest['gnostic_book'] = True

		if self.add_information == 'book_gave':
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			self.control.k_e = False
			hero.inv.remove(items.old_book)
			self.item = items.old_book
			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы отдали богопротивную книгу в жирные руки Тубуса.')
			hero.son.change_text (3, 'Теперь она в надежном месте.')
			hero.son.change_text (4, 'Брат Тубус вас горячо поблагодарил и накормил печеньем.')

			hero.char_value['2exp'] += 100
			end_dialog (self, hero)

		if self.add_information == 'book_not':
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			self.control.k_e = False
			end_dialog (self, hero)			

class Gnostic (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Гностик'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/barmen.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True
		self.light = False
		self.word = False
		self.armor = 2

	def interaction (self, hero):
		Monster.interaction (self, hero)
		if 'gnostic_kill' in hero.quest and 'Отец Изольд' in hero.frag_journal and ideas.gnosis in hero.journal:
			br_change (self, 5)


	def dialog_special (self, hero):

		if self.add_information == 'quest' and self.control.k_e == True:
			self.control.k_e = False
			hero.append (items.gold_ring)
			br_auto (self)


		if self.add_information == 'quest':

			end_dialog (self, hero)
			hero.quest['gnostic_kill'] = True

		if self.add_information == 'word':

			if self.word == False:
				hero.take_damage(1, 'phis')
				self.word = True


		if self.add_information == 'light':
			self.control.k_e = False
			if self.light == False:
				hero.take_damage(random.randint(1,6), 'light')
				img.boltAnim.play ()
				sounds.light.play()
				self.light = True


		if self.add_information == 'gn_end' and self.control.k_e == True:
			menu.ending ('Вы со всеми потрохами вступили в гностическую общину. Вы так никогда и не достигли в ней каких-то значимых высот. В то время как иерархи общины предавались наслаждениям, вам было предписано соблюдать жесткую аскезу. В итоге вас нашла инквизиция и сожгла на костре.', img.gnosis_end, 6, pic_x = 60, time_scroll = 250, speed_mod = 6)


class Trader (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Старьёвщик'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/trader.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True

#	def interaction (self, hero):
#		Monster.interaction (self, hero)


	def dialog_special (self, hero):


		if self.add_information == 'trade'  and self.control.k_e == True:
			hero.sell_flag = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

class Smith (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Оружейник'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/smith.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True

		self.inv = [items.mail, items.long_sword, items.plate_mail,items.full_plate,items.great_sword]


#	def interaction (self, hero):
#		Monster.interaction (self, hero)


	def dialog_special (self, hero):


		if self.add_information == 'trade'  and self.control.k_e == True:
			hero.buy_flag = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


class Master (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Мастер меча'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/master.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True
		self.master_of_sword = 1
		self.sound = sounds.pain
		self.item = items.great_sword
		self.armor = 4




#	def interaction (self, hero):
#		Monster.interaction (self, hero)


	def dialog_special (self, hero):


		if self.add_information == 'teach'  and self.control.k_e == True:
			hero.son.clear_text ()
			hero.son.change_text (2, 'С вами поделился своим боевым опытом мастер меча.')
			hero.son.change_text (3, 'Он показал ряд приёмов и хитростей.')
			hero.son.change_text (4, 'Теперь при броске 6 на кубике вы будете пробивать броню врага.')
			hero.son.change_text (5, 'Но только броню, его уклонение будет продолжать считаться!')

			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			hero.master_of_sword +=1

			end_dialog (self, hero)

		if self.add_information == 'check'  and self.control.k_e == True:
			hero.control.k_e = False
			if hero.char_value['1lvl'] >2:
				br_change (self, 3)
			else:
				br_change (self, 2)

class Bogost (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Боргост'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/bar.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True
		self.master_of_sword = 4
		self.sound = sounds.pain
		self.item = items.short_sword
		#self.armor = 4



class Bomz (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Святой бомж'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/bomz.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True
		self.master_of_sword = 1
		self.sound = sounds.pain
		self.gold1 = False
		self.gold2 = False

	def dialog_special (self, hero):


		if self.add_information == 'sword'  and self.control.k_e == True:
			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы стоите с чувством выполненного долга.')
			hero.son.change_text (4, 'Взамен своего оружия вы получили ржавый меч.')
			hero.char_value['2exp'] += 50

			for i in hero.inv:
				print(i)
				if i.__class__.__name__ == 'Weapon':
					hero.inv.remove(i)
					print(str(i)+'REMOVED')

#			print(len(hero.inv))
#			for i in range(0,len(hero.inv)-1):
#				print(i)
#
#				if hero.inv[i].__class__.__name__ == 'Weapon':
#					hero.inv.pop(i)
#					print(str(hero.inv[i])+'REMOVED')

			hero.weapon = items.first
			hero.at += hero.weapon.at_mod
			hero.damage = hero.weapon.dem
			hero.char_value['6sp']  +=1
			hero.sp +=1
			self.control.k_e = False

			hero.inv.append(items.old_sword)
			self.kill ()

			end_dialog (self, hero)

		if self.add_information == 'gold':

			
			if self.gold1 == False and hero.gold >0:
				hero.gold -= 1
				self.gold1 = True

		if self.add_information == 'allgold':

			
			if self.gold2 == False:
				hero.gold = 0
				self.gold2 = True


		if self.add_information == 'kill'  and self.control.k_e == True:
			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы убили бедного бомжа!')
			hero.char_value['2exp'] += 1
			self.kill ()
			

			hero.frag_journal.append((self.mname))
			hero.evil +=2

			end_dialog (self, hero)






class Kubert (classes.Monster):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.sound = sounds.hit
		self.mname = 'Брат Куберт'
		self.race = 'human'
		self.image = Surface ((45,45))
		self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/master.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))
		self.matter = 0
		self.order = True
		self.master_of_sword = 3
		self.item = items.true_dogma

#	def interaction (self, hero):
#		Monster.interaction (self, hero)


	def dialog_special (self, hero):

		if self.add_information == 'dogma'  and self.control.k_e == True:
			br_change (self, 5)
			self.control.k_e = False

		if self.add_information == 'give'  and self.control.k_e == True:
			hero.son.clear_text ()
			hero.son.change_text (2, 'Призрачный рыцарь истаивает во тьме.')
			hero.son.change_text (3, 'В руках у вас остаётся странный тубус.')
			hero.char_value['2exp'] += 1000
			hero.inv.append (self.item)
			self.item = items.no_item
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0


			end_dialog (self, hero)
			self.kill()