﻿
class Item ():
	def __init__ (self, name, description, cost, use_description = ''):
		self.name = name
		self.description = description
		self.use_description = use_description
		self.species = ''
		self.status = ''
		self.cost = cost
	def use (self):
		pass

class Weapon (Item):
	def __init__ (self, name, description, cost, dem, use_description = '', at_mod = 0):
		Item.__init__ (self, name, description, cost)
		self.dem = dem
		self.use_description = use_description
		self.status = 'в рюкзаке'
		self.species = 'оружие'
		self.at_mod = at_mod

class Armor (Item):
	def __init__ (self, name, description, cost, ac, prevent, use_description = '', dex_mod = 0):
		Item.__init__ (self, name, description, cost)
		self.armor = ac
		self.prevent =  prevent
		self.use_description = use_description
		self.status = 'в рюкзаке'
		self.species = 'доспех'
		self.dex_mod = dex_mod


class Potion (Item):
	def __init__ (self, name, description, cost, value, species, use_description = '' ):
		Item.__init__ (self, name, description, cost)
		self.use_description = use_description
		self.value = value
		self.species = species

class Potion_Resist (Item):
	def __init__ (self, name, description, cost, value, species, use_description = '' ):
		Item.__init__ (self, name, description, cost)
		self.use_description = use_description
		self.value = value
		self.species = species

class Potion_Buff (Item):
	def __init__ (self, name, description, cost, value, species, use_description = '' ):
		Item.__init__ (self, name, description, cost)
		self.use_description = use_description
		self.value = value
		self.species = species

class Narco (Item):
	def __init__ (self, name, description, cost, value, species, use_description = '' ):
		Item.__init__ (self, name, description, cost)
		self.use_description = use_description
		self.value = value
		self.species = species

chain_mail = Armor ('Кольчуга', 'Искусно сделанная добротная кольчуга, которая может вас защитить от шального удара. А может и не защитить. Броня 2.', 100, 2, 0, '1 - экипировать/снять; 2 - выбросить.')
mail = Armor ('Бахтерец', 'Хорошая вещь. Броня 4.', 300, 2, 0, '1 - экипировать/снять; 2 - выбросить.')
no_armor = Armor ('Нет брони', 'Простая одежда. Броня 0.', 0, 0, 0, '1 - экипировать/снять; 2 - выбросить.')
plate_mail = Armor ('Панцырь', 'Доспех, который надежно защитить все ваши жизненно важные органы, если вы, конечно, сможете его унести на себе. Тяжелый, сволочь. Броня 5. Превент 1.', 500, 5, 1, '1 - экипировать/снять; 2 - выбросить.', dex_mod =-1)
full_plate = Armor ('Латы', 'Рыцарские латы, в них не страшен и прямой удар мечом. Вот только двигаться в них не очень удобно. Броня: 8. Превент:2.', 1000, 8, 2, '1 - экипировать/снять; 2 - выбросить.', dex_mod=-3)

short_sword = Weapon ('Короткий меч', "Довольно качественная вещь. Урон 1.", 20, 1, '1 - экипировать/снять; 2 - выбросить.')
long_sword = Weapon ('Длинный меч', "Очень опасная вещь. Урон 2.", 50, 2, '1 - экипировать/снять; 2 - выбросить.')
great_sword = Weapon ('Двуручный меч', "Вот им можно заехать так заехать. Урон 3.", 120, 3, '1 - экипировать/снять; 2 - выбросить.')

first = Weapon ('Кулак', "Ничто не заменит доброго удара кулаком", 0, 1, at_mod = (-2))
no_item = Item ('Ничего', "Совсем ничего", 0)


hp_potion = Potion ('Лечебное зелье', 'Вы можете восстановить свои жизни, выпив это зелье.', 40, 6, 'hp', '1 - выпить; 2 - выбросить.')

fire_resist = Potion_Resist ('Зелье защиты от огня', 'Выпив это зелье вы на 20-ть ходов получаете 50% сопротивление огню.', 100, 50, 'fire', '1 - выпить; 2 - выбросить.')

light_resist = Potion_Resist ('Зелье защиты от молний', 'Выпив это зелье вы на 20-ть ходов получаете 50% сопротивление электричеству.', 100, 50, 'light', '1 - выпить; 2 - выбросить.')

str_potion = Potion_Buff ('Зелье силы', 'Выпив это зелье вы на 20-ть ходов получаете + 2 к атаке.', 100, 1, 'b3at', '1 - выпить; 2 - выбросить.')

dex_potion = Potion_Buff ('Зелье ловкости', 'Выпив это зелье вы на 20-ть ходов получаете + 2 к защите.', 100, 1, 'b4ac', '1 - выпить; 2 - выбросить.')

faith_potion = Potion ('Зелье веры.', 'Вы можете восстановить свою веру, выпив это зелье.',120, 6, 'sp', '1 - выпить; 2 - выбросить.')

melanj = Narco ('Меланж', 'Белый порошок. Наркотик, увеличивающий вашу подвижность и реакцию, приводящий вас в возмуждённое состояние.', 20, 6, 'narc', '1 - нюхнуть; 2 - выбросить.')

potion_list = [hp_potion, fire_resist, light_resist, str_potion, dex_potion, melanj]

#QUEST ITEMS

silver_key = Item ('Серебряный ключ', 'Изящный серебряный ключик.', 20)
gold_key = Item ('Золотой ключ', 'Искусно сделанный ключ из чистого золотого высокой пробы.', 30)
death_water = Item ('Фляжка с водой из колодца', 'Холодная прозрачная вода.', 2)
rope = Item ('Верёвка', 'Им всегда нужна эта !@#$% верёвка.', 5)
dogma = Item ('Пречистые догмы', 'На истлевшем пергаменте написаны суровые заповеди. Вас охватывает священный трепет при чтении их: "Да не будет у тебя других богов, кроме Меня. Не произноси имени Господа, Бога твоего напрасно. Помни день субботний, чтобы святить его. Не убивай. Не прелюбодействуй. Не кради. Не ври. Не пожелай чужого".', 100)
old_axe = Item ('Старый лабрис', "Большой двухлезвенный топор покрытый ржавчиной. Лезвие нечищено, покрыто сколами. Сражаться им неудобно и неэффективно. Не лучше ли его переплавить?", 10)
doc = Item ('Подорожная грамота', 'Грамота, санкционирующая ваше пребывание в городе Тархан в течение трёх дней.', 1)
permit = Item ('Пропуск в подземелье', "По этому пропуску вы можете пройти мимо охраны, стоящей у входа в подземелье.", 10)
bottle = Item ('Странная бутылка', "Бутылка из тёмного стелка, заткнутая пробкой. Внутри какая-то бурда, пахнет гнилью. Я б такое пить не стал. ", 1, 'Если же всё же хотите рискнуть - нажмите (1)')
old_book = Item ('Старая книга', "Обшарпанная книга на духовные темы.От этой книги явно веет ересью. Ничего хорошего в ней содержаться не может. Чтение таких книг - опасное дело. ", 20, 'Если же всё же хотите прочитать - нажмите (1).')
doc_elite = Item ('Красная грамота', 'Грамота, санкционирующая ваше пребывание в городе Тархан в течение месяца.', 1)
peidron_key = Item ('Ключ от комнаты пейдрона', 'Изящный ключик. Им вы можете открыть дверь на втором этаже баншни', 10)
bouquet = Item ('Букет цветов', "Его можно подарить какой-нибудь даме.", 5, "Нажмите (2), чтобы выбросить.")
scythe = Item ('Коса','Старая сломанная крестьянская коса для сельскохозяйственных работ. К сожалению она безвозвратно испорчена и непригодна ни к чему. ', 3, 'Лучше её вообще выбросить, что вы и можете сделать нажав (2).')
garbage = Item ('Хлам', 'Просто старый вонючий хлам.', 2)
