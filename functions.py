import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text

def event_go ():
	c = 0


class Compose_dialog_tree ():
	def __init__ (self, control):
		self.a_max = 0
		self.n = 0
		self.a = 0
		self.control = control
		self.strokes_number = 0
		self.super_a_max = 0
		self.an = 0
		self.start = True

	def text_splitter (self, text):
		text_splitted = text.split (" ")
		rec = []
		s = ""
		for i in text_splitted:
			if len(s + i) < 50:
				s = s + " " +  i
				continue
			rec.append (s)
			s = " " + i
		rec.append (s)
		return rec


	def render_text (self, text, answer):

		s1 = ''
		s2 = ''
		s3 = ''
		s4 = ''
		s5 = ''
		s6 = ''
		s7 = ''

		all_strokes = self.text_splitter (text)	

		self.n = (self.a * 6)+1

		if self.control.k_n == True:
			self.control.k_n = False
			if self.a < int(((len(all_strokes)) // 6)+1):
				self.a = self.a+1
			else:
				self.a = 0
		
		 
		try:

			s1 = all_strokes[self.n+0]
		except IndexError: 
   			#all_strokes[self.n+1] = None
   			pass
		try:
			s2 = all_strokes[self.n+1]
		except IndexError: 
   			#all_strokes[self.n+2] = None
   			pass
		try:
			s3 = all_strokes[self.n+2]
		except IndexError: 
   			#all_strokes[self.n+3] = None
   			pass
		try:
			s4 = all_strokes[self.n+3]
		except IndexError: 
   			#all_strokes[self.n+4] = None
   			pass
		try:
			s5 = all_strokes[self.n+4]
		except IndexError: 
   			#all_strokes[self.n+5] = None
   			pass
		try:
			s6 = all_strokes[self.n+5]
		except IndexError: 
   			#all_strokes[self.n+6] = None
   			pass
		try:
			s7 = all_strokes[self.n+6]
		except IndexError: 
   			#all_strokes[self.n+7] = None
   			pass

		information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
		information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
		information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
		information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
		information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
		information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
		information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))	

#	def render_text (self,text,answer):
#
#
#
#
#		self.a_max = (len(text)//350)
#		num_end_symb = len(text)%50
#		answer = " "*len(text)+(" "*(100-num_end_symb))+answer 
#		self.super_a_max = len (answer)// 350
#		self.n = self.a*350
#
#		if self.control.k_n == True:
#			self.control.k_n = False
#			if self.a < self.super_a_max:
#				self.a = self.a+1
#			else:
#				self.a = 0
#		
#		all_strokes = text_splitter (text)	 
#
#		an1 = answer[self.n+0:self.n+50]
#		an2 = answer[self.n+50:self.n+100]
#		an3 = answer[self.n+100:self.n+150]
#		an4 = answer[self.n+150:self.n+200]
#		an5 = answer[self.n+200:self.n+250]
#		an6 = answer[self.n+250:self.n+300]
#		an7 = answer[self.n+300:self.n+350]	
#
#		information_screen.blit(fonts.font2.render (str(an1), True, (250,250,250)),(2,0))
#		information_screen.blit(fonts.font2.render (str(an2), True, (250,250,250)),(2,22))
#		information_screen.blit(fonts.font2.render (str(an3), True, (250,250,250)),(2,44))
#		information_screen.blit(fonts.font2.render (str(an4), True, (250,250,250)),(2,66))
#		information_screen.blit(fonts.font2.render (str(an5), True, (250,250,250)),(2,88))
#		information_screen.blit(fonts.font2.render (str(an6), True, (250,250,250)),(2,110))
#		information_screen.blit(fonts.font2.render (str(an7), True, (250,250,250)),(2,132))
#	
#		s1 = text[self.n+0:self.n+50]
#		s2 = text[self.n+50:self.n+100]
#		s3 = text[self.n+100:self.n+150]
#		s4 = text[self.n+150:self.n+200]
#		s5 = text[self.n+200:self.n+250]
#		s6 = text[self.n+250:self.n+300]
#		s7 = text[self.n+300:self.n+350]
#
#		information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
#		information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
#		information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
#		information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
#		information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
#		information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
#		information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))	


		#adventure_screen.blit(fonts.font2.render ((str(self.a) + ' self.a'), True, (250,250,250)),(0,35))
		#adventure_screen.blit(fonts.font2.render ((str(self.an) + " self.an"), True, (250,250,250)),(0,55))
		#adventure_screen.blit(fonts.font2.render ((str(self.super_a_max) + " super a"), True, (250,250,250)),(0,75))
		#adventure_screen.blit(fonts.font2.render ((str(self.a_max) + " self.a_max"), True, (250,250,250)),(0,95))





class Battle ():
	def __init__ (self, control):
		self.conntrol = control
		self.b1 = ''
		self.b2 = ''
		self.b3 = ''
		self.b4 = ''
		self.b5 = ''
		self.b6 = ''
		self.b7 = ''
		self.m1 = ''
		self.m2 = 'Атака: '
		self.m3 = 'Защита: '
		self.m4 = 'Жизни: '
		self.m5 = 'Урон: '


	def main_loop (self, hero, monster):

		if hero.status != 'dead':
			hero.battle_action_main ()
			monster.battle_action (hero)
			hero.check_for_death ()
			self.render_battle_info ()
			instrumental_screen.blit (monster_screen, (678,8))
			monster_screen.fill ((sea_color))
			self.render_monster_inf (monster)

	def render_monster_inf (self, monster):
		monster_screen.blit(fonts.font3.render (str(self.m1 + str(monster.name)), True, (250,250,250)),(2,0))
		monster_screen.blit(fonts.font3.render (str(self.m2 + str(monster.at)), True, (250,250,250)),(2,15))
		monster_screen.blit(fonts.font3.render (str(self.m3+ str(monster.ac)), True, (250,250,250)),(2,30))
		monster_screen.blit(fonts.font3.render (str(self.m4+ str(monster.hp)), True, (250,250,250)),(2,45))
		monster_screen.blit(fonts.font3.render (str(self.m5+ str(monster.damage)), True, (250,250,250)),(2,60))

	def render_battle_info (self):
		information_screen.blit(fonts.font2.render (str(self.b1), True, (250,250,250)),(2,0))
		information_screen.blit(fonts.font2.render (str(self.b2), True, (250,250,250)),(2,22))
		information_screen.blit(fonts.font2.render (str(self.b3), True, (250,250,250)),(2,44))
		information_screen.blit(fonts.font2.render (str(self.b4), True, (250,250,250)),(2,66))
		information_screen.blit(fonts.font2.render (str(self.b5), True, (250,250,250)),(2,88))
		information_screen.blit(fonts.font2.render (str(self.b6), True, (250,250,250)),(2,110))
		information_screen.blit(fonts.font2.render (str(self.b7), True, (250,250,250)),(2,132))	

	def change_inf (self, n, a):
		if n == 1:
			self.b1 = a
		if n == 2:
			self.b2 = a
		if n == 3:
			self.b3 = a
		if n == 4:
			self.b4 = a
		if n == 5:
			self.b5 = a
		if n == 6:
			self.b6 = a
		if n == 7:
			self.b7 = a

	def clear_inf (self):
		self.b1 = ''
		self.b2 = ''
		self.b3 = ''
		self.b4 = ''
		self.b5 = ''
		self.b6 = ''
		self.b7 = ''


def create_level (level, battle, control):
	sprite_group = sprite.Group ()
	platforms = []
	#chests = []
	x = 0
	y = 0
	for row in level:
		for col in row:
			if col == "-":
				pf = classes.Platform (x,y)
				platforms.append (pf)
				sprite_group.add (pf)
			if col == "c":
				ch = classes.Chest (x,y)
				#chests.append (ch)
				sprite_group.add (ch)
			if col == "m":
				mn = classes.Monster (x/45,y/45,battle, text.zombi1, control, 10,0,10,1)
				sprite_group.add (mn)
			x += 45
		x = 0
		y += 45
	x = 0
	y = 0
	return  platforms, sprite_group



