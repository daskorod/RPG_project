import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text
import items
import text_data.zombisad, text_data.monk
#import npc





def end_dialog(self, hero):
	hero.move = True
	hero.control.k_e = False
	hero.collide_control = False
	hero.start_conv = True
	hero.view.a = 0
	if self.branch_do == 'go':
		self.branch_do = 'done'
		self.branch = self.branch_id
		self.s = 1
		self.n = 0

def br_change(self, branch):
	self.branch = branch
	self.s = 1
	self.n = 0

def br_auto(self):
	if self.branch_do == 'go':
		self.branch_do = 'done'
		self.branch = self.branch_id
		self.s = 1
		self.n = 0


def war(self, hero):
			hero.son.clear_text ()
			hero.control.k_e = False
			self.agression = True
			hero.turn_main = True
			hero.start_conv = True
			hero.view.a = 0

#			a = random.randint (1,6)
			self.branch_do = 'done'
			self.s = 1
			self.n = 0
			self.branch = self.branch_id
#			if a >3:

def interaction_special(self, hero):
	pass

def dialog_special(self, hero):
		if self.add_information == 'take' and hero.control.k_e == True:
			hero.move = True
			hero.control.k_e = False
			hero.son.clear_text ()
			hero.son.change_text (1, 'Вы получили предмет: %s' % items.dogma.name)
			hero.inv.append(items.dogma)
			hero.collide_control = False
			hero.start_conv = True
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

		if self.add_information == 'end':

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0



def journal_update (self, hero, add_information, concept):
		if self.add_information == add_information and self.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Пусто':
					hero.jornal.insert (x, concept)
					break
				x +=1

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
		self.stroke_size = 70
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

		if self.control.down == True and self.a < int((len(all_strokes)+1) // 8):
			self.control.down = False
			self.a = self.a+1

		if self.control.up == True and self.a > 0:
			self.control.up = False
			self.a = self.a-1

		if self.a < int((len(all_strokes)+1) // 8):
			information_screen.blit (self.arrowDw, (600, 70))
		if self.a !=0:
			information_screen.blit (self.arrowUp, (600, 0))

		return all_strokes, self.n

class Battle ():
	def main_loop (self, hero, monster):
		if hero.status != 'dead' and monster.status != 'killed':
			hero.battle_action_main ()
			monster.death_check (hero)	
			monster.battle_action (hero)
			hero.check_for_death ()
			monster.render_monster_inf ()

def combat (hero, monster):
#	if hero.status != 'dead' and monster.status != 'killed':
		hero.battle_action_main ()
		monster.death_check (hero)	
		monster.battle_action (hero)
		hero.check_for_death ()
		monster.render_monster_inf ()

