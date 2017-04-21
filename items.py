﻿
class Item ():
	def __init__ (self, name, description):
		self.name = name
		self.description = description
		self.use_description = 'Вы ничего не можете сделать с ничем'
		self.species = ''
		self.status = ''
	def use (self):
		pass

class Weapon (Item):
	def __init__ (self, name, description, dem, use_description = '', at_mod = 0):
		Item.__init__ (self, name, description)
		self.dem = dem
		self.use_description = use_description
		self.status = 'в рюкзаке'
		self.species = 'оружие'
		self.at_mod = at_mod


short_sword = Weapon ('Короткий меч', "Довольно качественная вещь. Урон 1.", 1, '1 - экипировать/снять; 2 - выбросить.')
long_sword = Weapon ('Длинный меч', "Очень опасная вещь. Урон 2.", 2, '1 - экипировать/снять; 2 - выбросить.')
first = Weapon ('Кулак', "Ничто не заменит доброго удара кулаком", 3, at_mod = (-2))
no_item = Item ('Ничего', "Совсем ничего")
bouquet = Item ('Букет цветов', "Его можно подарить какой-нибудь даме")