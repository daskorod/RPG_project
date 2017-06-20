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
