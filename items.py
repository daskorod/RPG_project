
class Item ():
	def __init__ (self, name, description):
		self.name = name
		self.description = description
		self.use_description = ''
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

class Potion (Item):
	def __init__ (self, name, description, value, species, use_description = '' ):
		Item.__init__ (self, name, description)
		self.use_description = use_description
		self.value = value
		self.species = species



short_sword = Weapon ('Короткий меч', "Довольно качественная вещь. Урон 1.", 1, '1 - экипировать/снять; 2 - выбросить.')
long_sword = Weapon ('Длинный меч', "Очень опасная вещь. Урон 2.", 2, '1 - экипировать/снять; 2 - выбросить.')
first = Weapon ('Кулак', "Ничто не заменит доброго удара кулаком", 1, at_mod = (-2))
no_item = Item ('Ничего', "Совсем ничего")
bouquet = Item ('Букет цветов', "Его можно подарить какой-нибудь даме. Нажмите (2), чтобы выбросить.")
scythe = Item ('Коса','Старая сломанная крестьянская коса для сельскохозяйственных работ. К сожалению она безвозвратно испорчена и непригодна ни к чему. Лучше её вообще выбросить, что вы и можете сделать нажав (2).')
garbage = Item ('Хлам', 'Просто старый вонючий хлам.')
hp_potion = Potion ('Лечебное зелье', 'Вы можете восстановить свои жизни, выпив это зелье.', 6, 'hp', '1 - выпить; 2 - выбросить.')
silver_key = Item ('Серебряный ключ', 'Изящный серебряный ключик.')
gold_key = Item ('Золотой ключ', 'Искусно сделанный ключ из чистого золотого высокой пробы.')
death_water = Item ('Фляжка с водой из колодца', 'Холодная прозрачная вода.')
rope = Item ('Верёвка', 'Им всегда нужна эта !@#$% верёвка.')
dogma = Item ('Пречистые догмы', 'На истлевшем пергаменте написаны суровые заповеди. Вас охватывает священный трепет при чтении их: "Да не будет у тебя других богов, кроме Меня. Не произноси имени Господа, Бога твоего напрасно. Помни день субботний, чтобы святить его. Не убивай. Не прелюбодействуй. Не кради. Не ври. Не пожелай чужого".')