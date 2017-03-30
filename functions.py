import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text

class Son ():
	'''render text information'''

	def __init__ (self):
		self.b1 = self.b2 = self.b3 = self.b4 = self.b5 = self.b6 = self.b7 = ''
		self.strokelist = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7]
		self.all_strokes = []
		self.n = 0
	def render_text (self):
		n = 0

		for i in self.strokelist:
			information_screen.blit(fonts.font2.render (str(i), True, (250,250,250)),(2,22*n))
			n += 1
	def change_text (self, n, a):
		self.strokelist[n-1] = str(a)

	def clear_text (self):
		for i in range (len(self.strokelist)):
			self.strokelist[i] = ''

	def change_text_tree (self, x):
		self.clear_text ()
		text_tree, n = x
		self.n = n
		self.all_strokes = text_tree

		counter = 0
		for i in self.strokelist:
			try:
				self.strokelist[counter] = self.all_strokes [self.n+counter]
#			information_screen.blit(fonts.font2.render (str(self.strokelist[counter]), True, (250,250,250)),(2,counter*22))
				counter = counter + 1
			except IndexError:
				pass

class Compose_dialog_tree ():
	'''split text for dialog and render it at dialog screen'''
	
	def __init__ (self, control,son):
		#Son.__init__ (self)
		self.n = 0
		self.a = 0
		self.control = control
		self.empty = ''
		self.stroke_size = 47
		self.son = son

	def text_splitter (self, text):

		text_splitted = text.split (" ")

		rec = []
		s = ""

		for i in text_splitted:
			if len(s + i) < self.stroke_size:
				s = s + " " +  i
				continue
			rec.append (s)
			s = " " + i
		rec.append (s)

		return rec

	def render_text (self, text, answer):

		s1 = s2 = s3 = s4 = s5 = s6 = s7 = ''
		ss = [s1,s2,s3,s4,s5,s6,s7]

		all_strokes = self.text_splitter (text)	
		all_strokes_ans = self.text_splitter (answer)
		all_strokes.append (self.empty)
		all_strokes.extend(all_strokes_ans)

		self.n = (self.a * 7)

		if self.control.k_n == True:
			self.control.k_n = False

			if self.a < int((len(all_strokes)) // 7):
				self.a = self.a+1
			else:
				self.a = 0


		return all_strokes, self.n
#		counter = 0
#
#		for i in ss:
#			try:
#				ss[counter] = all_strokes [self.n+counter]
#				information_screen.blit(fonts.font2.render (str(ss[counter]), True, (250,250,250)),(2,counter*22))
#				counter = counter + 1
#			except IndexError:
#				pass
#

#		for i in self.strokelist:
#			try:
#				self.strokelist[counter] = all_strokes [self.n+counter]
#				counter = counter + 1
#			except IndexError:
#				pass

class Battle ():
	def __init__ (self, control):

		self.conntrol = control
		self.m1 = ''
		self.m2 = 'Атака: '
		self.m3 = 'Защита: '
		self.m4 = 'Жизни: '
		self.m5 = 'Урон: '
		self.monsterList = [self.m1, self.m2, self.m3, self.m4, self.m5]

	def main_loop (self, hero, monster):



		if hero.status != 'dead' and monster.status != 'killed':

			hero.battle_action_main ()
			monster.death_check (hero)	
			monster.battle_action (hero)
			hero.check_for_death ()
			self.render_monster_inf (monster)

	
	def render_monster_inf (self, monster):

		instrumental_screen.blit (monster_screen, (678,8))
		monster_screen.fill ((sea_color))
		monsterList2 = [monster.name, monster.at, monster.ac, monster.hp, monster.damage]
	
		for i in range (5):
			monster_screen.blit(fonts.font3.render (str(self.monsterList[i] + str(monsterList2[i])), True, (250,250,250)),(2,15*i))

def create_level (level, battle, control,son):
	sprite_group = sprite.Group ()
	platforms = []

	x = 0
	y = 0
	for row in level:
		for col in row:
			if col == "-":
				pf = classes.Platform (x,y)
				platforms.append (pf)
				sprite_group.add (pf)
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
			x += 45
		x = 0
		y += 45
	x = 0
	y = 0
	return  platforms, sprite_group



