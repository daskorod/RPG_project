import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text
#import npc

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
			information_screen.blit(fonts.font5.render (str(i), True, (250,250,250)),(2,22*n))
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
		self.stroke_size = 60
		self.son = son
		self.arrowUp = image.load('images/arrow2.png')
		self.arrowDw = image.load('images/arrow.png')


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

		if self.control.down == True and self.a < int((len(all_strokes)) // 7):
			self.control.down = False
			self.a = self.a+1

		if self.control.up == True and self.a > 0:
			self.control.up = False
			self.a = self.a-1

#			else:
#				self.a = 0
#
		if self.a < int((len(all_strokes)) // 7):
			information_screen.blit (self.arrowDw, (600, 70))
		if self.a !=0:
			information_screen.blit (self.arrowUp, (600, 0))

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
	def main_loop (self, hero, monster):
		if hero.status != 'dead' and monster.status != 'killed':
			hero.battle_action_main ()
			monster.death_check (hero)	
			monster.battle_action (hero)
			hero.check_for_death ()
			monster.render_monster_inf ()

def combat (hero, monster):
	if hero.status != 'dead' and monster.status != 'killed':
		hero.battle_action_main ()
		monster.death_check (hero)	
		monster.battle_action (hero)
		hero.check_for_death ()
		monster.render_monster_inf ()

		
def create_level_dungeon (level, battle, control, son):

       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "m":
                            mn = classes.Monster (x/45,y/45,battle, text.zombi1, control, 10,0,10,1, son)
                            sprite_group.add (mn)

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
       return sprite_group

def create_dungeon1 (level, battle, control, son):

       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "z":
                            z = classes.Monster (x/45,y/45,battle, text.zombipeasant, control, 10,0,10,1, son, special_opt = True)
                            sprite_group.add (z)

                     if col == 'e':
                            e = classes.PortalS (x,y, 'end', (1,4))
                            sprite_group.add (e)

                     if col == 's':
                            s = classes.Chest (x,y)
                            sprite_group.add (s)

                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group

def create_interior_standart (level, grType):

       interior =[]
       ground = []

       x = 0
       y = 0

       for row in level:
              for col in row:

                    ground.append (grType (x,y))
                    
                    if col == "-":
                            pf = classes.Platform (x,y)
                            interior.append (pf)

                    if col == "d":
                            door = classes.Door (x,y)
                            interior.append (door)

                    if col == "c":
                            ch = classes.Chest (x,y)
                            interior.append (ch)

                    if col == "t":
                            tr = classes.Candel (x,y)
                            interior.append (tr)

                    x += 45
              x = 0
              y += 45
       x = 0
       y = 0

       return  interior, ground


def create_level_city (level, battle, control, son):
       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "m":
                            mn = classes.Monk (x/45,y/45,battle, text.monk, control, 4,5,7,1, son)
                            sprite_group.add (mn)
# exit from temple
                     if col == 'p':
                            pr = classes.PortalS (x,y,'platz', (11,1))
                            sprite_group.add (pr)
#enter into temple
                     if col == 'e':
                            pr = classes.PortalS (x,y,'temple', (10,4))
                            sprite_group.add (pr)

#path to end of the city
                     if col == 'o':
                            pr = classes.PortalS (x,y,'end', (1,4))
                            sprite_group.add (pr)
#from end to platz
                     if col == 'q':
                            pr = classes.PortalS (x,y,'platz', (21,4))
                            sprite_group.add (pr)
#from end to dung
                     if col == 'w':
                            pr = classes.Portal (x,y, control)
                            sprite_group.add (pr)

                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group

def create_background (grType, level):

	ground = sprite.Group()
	x = 0
	y = 0
	for row in level:
		for col in row:

			gr = grType (x,y)
			ground.add (gr)

			x += 45
		x = 0
		y += 45
	x = 0
	y = 0

	return  ground
