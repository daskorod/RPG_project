# -*- coding: utf-8 -*-

class svin ():
	def __init__ (self):
	
		self.a = self.act ()
	def act(self):
		return 5
	def pr (self):
		print (self.a)

class borov (svin):
	def __init__ (self):
		svin.__init__ (self)
	def act (self):
		return 10

a = svin ()
a.pr ()

b = borov ()
b.pr ()



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
