# -*- coding: utf-8 -*-

class a ():
	def __init__ (self, *f):
		self.b = []
		for i in f:
			self.b.append(i)

	def print (self):
		print (self.b)

d = a (1,2,3)
d.print ()

class MinorChestOld(sprite.Sprite):
	def __init__(self, x, y, status, *item):
		sprite.Sprite.__init__(self)
		self.image=image.load('images/chest2.png')
		self.image.set_colorkey ((255,255,255))
		#self.image = Surface ((45,45))
		#self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "chest"
		self.status = status
		self.items = item
		self.inside = []
		for i in self.items:
			self.inside.append (i)

		self.items_name = ''

		for i in self.items:
			self.items_name = self.items_name + i.name + ', '
		self.items_name = self.items_name[:-2] + '.'

		#conversation data
		self.tree = text.mchest
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def interaction (self, hero):

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

	def dialog_special (self, hero):
		pass

	def dialog_options (self,hero):

		self.dialog_special (hero)
		if self.add_information == 'end_chest':

			hero.son.change_text_tree (hero.view.render_text ('В сундуке находится: ' + self.items_name, 'Нажмите E, чтобы забрать вещи...'))
		if self.add_information == 'end_chest' and hero.control.k_e == True:
			hero.move = True

			hero.control.k_e = False

			hero.son.clear_text ()




			hero.collide_control = False
			hero.start_conv = True

			empty_space = 0
			for item in hero.inv:
				if item.name == 'Ничего':
					empty_space += 1

			if empty_space >= len (self.inside):
				self.kill ()
				hero.son.change_text (4, 'Вы взяли все вещи...')
				counter = 0
				for i in self.inside:
					for item in hero.inv:
						if item.name == 'Ничего':
							hero.inv.pop (counter)
							hero.inv.insert (counter, i)
							break
						counter += 1
					counter = 0

			if empty_space < len (self.inside):
				hero.son.change_text (4, 'Вы взяли не всё, слишком много добра. Не убирается...')
				counter = 0
				taken = 0
				for i in self.inside:
					if taken > empty_space:
						break
					for item in hero.inv:
						if item.name == 'Ничего':
							hero.inv.pop (counter)
							hero.inv.insert (counter, i)
							self.inside.remove(i)
							taken += 1
							break
						counter += 1
					counter = 0

				self.items_name = ''
				for i in self.inside:
					self.items_name = self.items_name + i.name + ', '
				self.items_name = self.items_name[:-2] + '.'

		if self.add_information == 'end' and hero.control.k_e == True:

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			self.s = 1
			self.n = 0
			self.branch = 0
'''a={'1lvl':1,'2exp':0,'3at':6,'4ac':6,'5hp':7,'6sp':2,'7points':1}

self.char_value ={'1lvl':1,'2exp':0,'3at':6,'4ac':6,'5hp':7,'6sp':2,'7points':1}
b = sorted(a.keys())
print (b)

def create_level (level, battle, control,son, grType):
	sprite_group = sprite.Group ()
	platforms = []
	ground = sprite.Group()
	x = 0
	y = 0
	grrr = grType
	for row in level:
		for col in row:
			
			gr = grrr (x,y)
			ground.add (gr)
			if col == "-":
				#pf = classes.Platform (x,y)
				platforms.append (classes.Platform (x,y))
				sprite_group.add (classes.Platform (x,y))
			if col == "d":
				door = classes.Door (x,y)
				#platforms.append (pf)
				sprite_group.add (door)
			if col == "c":
				ch = classes.Chest (x,y)
				#chests.append (ch)
				sprite_group.add (ch)
			if col == "m":
				mn = classes.Monster (x/45,y/45,battle, text.zombi1, control, 10,0,10,1, son)
				sprite_group.add (mn)
			if col == "t":
				tr = classes.Candel (x,y)
				#chests.append (ch)
				sprite_group.add (tr)
			if col == 'p':
				pr = classes.Portal (x,y, control)
				sprite_group.add (pr)

			if col == 'z':
				pr = classes.Portal2 (x,y, control)
				sprite_group.add (pr)

			x += 45
		x = 0
		y += 45
	x = 0
	y = 0
	return  platforms, sprite_group, ground'''


#	def update (self, array):
#
#
#
#		if self.collide_control == True and self.etwas.agression == False:
#
#		
#			if self.conv_stop == True:
#				self.son.clear_text ()
#				self.conv_stop = False
#
#			self.conversation(self.etwas.tree, self.etwas)
#
#	#	if self.door_interaction == True:
#	#		self.etwas.door_event (self)
#
#
#		if self.collide_control == False or self.etwas.agression == True:
#			self.conv_stop = True
#
#		if self.move == True:
#			#		high_screen.blit(fonts.font5.render (self.name, True, (250,250,250)),(10,0))
#		#RIGHT
#			if self.control.right == True:
#				self.collide_control = False
#
#	
#				self.rect.x += 1
#	
#				self.etwas = self.collide(array)
#	
#				if self.etwas != None:
#	
#					if self.etwas.name == "block":
#						self.rect.x -= 1
#						self.etwas.interaction (self)
#	
#					elif self.etwas.name == "chest":
#						self.rect.x -= 1
#						self.rect.x += 45
#						array.remove (self.etwas)
#
#					elif self.etwas.name == "monster":
#						self.rect.x -= 1
#						self.collide_control = True
#						self.etwas.interaction (self)
#
#					else:
#						self.rect.x -= 1
#						self.etwas.interaction (self)
#
#				self.control.right = False
#				if self.etwas == None: 
#					self.rect.x += 45
#					self.rect.x -= 1
#				
#			#LEFT
#			if self.control.left == True:
#				self.collide_control = False
#				self.rect.x -= 1
#	
#				self.etwas = self.collide(array)
#				if self.etwas != None:
#	
#					if self.etwas.name == "block":
#						self.rect.x += 1
#	
#					elif self.etwas.name == "chest":
#						self.rect.x += 1
#						self.rect.x -= 45
#						array.remove (self.etwas)
#	
#					elif self.etwas.name == "monster":
#	
#						self.rect.x += 1
#						self.collide_control = True
#						self.etwas.interaction (self)
#
#					else:
#						self.rect.x += 1
#						self.etwas.interaction (self)	
#	
#				if self.etwas == None: 
#					self.rect.x -= 45
#					self.rect.x += 1
#				self.control.left = False
#	
#			#UP
#			if self.control.up == True:
#				self.collide_control = False
#				self.rect.y -= 1
#	
#				self.etwas = self.collide(array)
#	
#				if self.etwas != None:
#	
#					if self.etwas.name == "block":
#						self.rect.y += 1
#						
#						self.etwas.interaction (self)
#					elif self.etwas.name == "chest":
#						self.rect.y += 1
#						self.rect.y -= 45
#						array.remove (self.etwas)
#	
#					elif self.etwas.name == "monster":
#						self.collide_control = True
#						self.etwas.interaction (self)
#						self.rect.y += 1
#					else:
#						self.rect.y += 1
#						self.etwas.interaction (self)		
#				if self.etwas == None: 
#					self.rect.y +=1
#					self.rect.y -=45
#	
#				self.control.up = False
#			#DOWN
#			if self.control.down == True:
#				self.collide_control = False
#				self.rect.y += 1
#	
#				self.etwas = self.collide(array)
#				if self.etwas != None:
#					if self.etwas.name == "block":
#						self.rect.y -= 1
#	
#						self.etwas.interaction (self)
#					elif self.etwas.name == "chest":
#						self.rect.y -= 1
#						self.rect.y += 45
#						array.remove (self.etwas)
#					elif self.etwas.name == "monster":
#						self.rect.y -=1
#						self.collide_control = True
#						self.etwas.interaction (self)
#					else:
#						self.rect.y -= 1
#						self.etwas.interaction (self)		
#				if self.etwas == None: 
#					self.rect.y += 45
#					self.rect.y -= 1
#				self.control.down = False
