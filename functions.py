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

	def render_text (self,text):

		self.a_max = len(text)//350
		self.n = self.a*350

		if self.control.k_n == True:
			self.control.k_n = False
			self.s1 = text[self.n+0:self.n+50]
			if self.a < self.a_max:
				self.a = self.a+1
			else:
				self.a = 0

		s1 = text[self.n+0:self.n+50]
		s2 = text[self.n+50:self.n+100]
		s3 = text[self.n+100:self.n+150]
		s4 = text[self.n+150:self.n+200]
		s5 = text[self.n+200:self.n+250]
		s6 = text[self.n+250:self.n+300]
		s7 = text[self.n+300:self.n+350]
	
		information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
		information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
		information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
		information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
		information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
		information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
		information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))	



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

		hero.battle_action_main ()
		monster.battle_action (hero)
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
				mn = classes.Monster (x/45,y/45,battle, text.zombitext, control, 10,0,10,1)
				sprite_group.add (mn)
			x += 45
		x = 0
		y += 45
	x = 0
	y = 0
	return  platforms, sprite_group

#def talks (a, n):
#	z = {1: s1, 2: s2, 3:s3, 4:s4, 5:s5, 6:s6, 7:s7}
#	z[n] = "a"
#
#	information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
#	information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
#	information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
#	information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
#	information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
#	information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
#	information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))

def talk (a, n):
	'''7 strokes'''
	information_screen.blit(fonts.font2.render (str(n), True, (250,250,250)),(2,0+(22*a)))



def render_text (text, control, a, s1):
	a_max = len(text)//350

	n = a*350

	if control.k_n == True:
		control.k_n = False
		s1 = text[n+0:n+50]
		if a < a_max+1:
			a = a+1
#		else:
#			a = 0

	#s1 = text[n+0:n+50]
	s1 = a
	s2 = a_max
	#s2 = text[n+50:n+100]
	s3 = text[n+100:n+150]
	s4 = text[n+150:n+200]
	s5 = text[n+200:n+250]
	s6 = text[n+250:n+300]
	s7 = text[n+300:n+350]
#	text = s1, s2, s3
	information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
	information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
	information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
	information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
	information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
	information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
	information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))


def text_split (text):
	s1 = text[0:50]
	s2 = text[50:100]
	s3 = text[100:150]
	return s1, s2, s3

