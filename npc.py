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
from monster import Monster
import classes
import ideas
from functions import end_dialog, war, br_change, br_auto
import items
import ends
import menu


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
		
			self.son.change_text (1, 'Священник шепчет слова молитвы:')
			self.son.change_text (2, '"Возврати меч твой в его место, ибо')
			self.son.change_text (3, 'все, взявшие меч, мечом погибнут." ... ')
			self.son.change_text (5, 'Нажмите Е')
			self.lbolt = True
			self.ll = True

		if hero.monster_turn == True and self.ll == True and self.control.k_e == True:
			self.ll = False
			self.lbolt = False
			self.son.clear_text ()
			self.son.change_text (1, "... вас охватывает пламя.")
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

			hero.sp = hero.char_value['6sp']
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
				hero.hp = hero.hp + 1

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
		
			self.son.change_text (1, 'Священник шепчет слова молитвы:')
			self.son.change_text (2, '"Возврати меч твой в его место, ибо')
			self.son.change_text (3, 'все, взявшие меч, мечом погибнут." ... ')
			self.son.change_text (5, 'Нажмите Е')
			self.lbolt = True
			self.ll = True

		if hero.monster_turn == True and self.ll == True and self.control.k_e == True:
			self.ll = False
			self.lbolt = False
			self.son.clear_text ()
			self.son.change_text (1, "... вас охватывает пламя.")
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

class Rouge (classes.Monk):
	def __init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp):
		Monster.__init__ (self, x, y, battle, textus, control, at, ac, hp, dem, son, exp)
		self.tree = textus
		self.lbolt = False
		self.mname = 'Вор'
		#self.image.fill ((220,130,100))
		self.ll = False
		self.image = image.load('images/tiles/rouge.png')
		self.icon = pygame.image.load ('images/priest_av.png')
		#self.image.set_colorkey ((254,254,254))

		self.order = True
		self.quest = False
		self.peid = False

	def interaction (self, hero):
		Monster.interaction (self, hero)
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

		self.order = True
		self.quest = False
		self.second = False
		self.step_away = False

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

#	def interaction (self, hero):
		#Monster.interaction (self, hero)
	def special_death (self,hero):
		hero.collide_control = True
		for i in hero.locations_dict['tower1'].block_group:
			if i.__class__.__name__ == 'Augustine':
				i.agression = True
				hero.etwas = i	

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
						
#			self.ll = False
#			img.boltAnim.play ()
#			self.son.clear_text ()
#			self.son.change_text (1, "... в вас ударяет ослепительная молния.")
#			self.son.change_text (2, "Вы получаете " + str(a) + ' урона')
#			hero.hp -= a
#			self.son.change_text (4, 'Нажмите Е')
#			self.wait_for_next_turn = True
#			hero.monster_turn = False
#			self.control.k_e = False

#		if self.control.k_e == True and self.wait_for_priest_turn == True:
#			self.priest_turn = True
#			self.control.k_e = False
#
#			self.son.clear_text ()	

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

#	def interaction (self, hero):
#		Monster.interaction (self, hero)


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