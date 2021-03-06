import pygame
import pyganim
import classes
import functions
from screens import *
from constants import *
import fonts
import text
import camera
import constructor
import img
timer = pygame.time.Clock  ()
import event
import text_data.corpse_dict

class SuperLevel ():
	def __init__ (self, lev, battle, son, control):

		#self.create = create
		self.lev = lev
		self.battle = battle
		self.description = ''
		self.son = son
		self.techname = self.__class__.__name__.strip('_')
		self.control = control	
		self.auto = True	
		
		self.block_group, self.background, self.decor = self.create ()

		self.level_width = len(lev[0])*PF_WIDTH
		self.level_height = len(lev)*PF_HEIGHT
		self.camera = camera.Camera (self.level_width, self.level_height, 840, 420)
	#	self.x_hero = (self.camera.apply(self.hero))
		self.back = True
		self.event = event.Event(text_data.corpse_dict.text)
		self.inception = True
		self.render_information = True



# The piece of code which you can see below
# is accounted for automatic selection of image for wall`s tile

	def up_check (self, checked_wall, walls_set):
		for i in walls_set:
			if i.rect.y == checked_wall.rect.y-45 and i.rect.x == checked_wall.rect.x:
				return True
		return False

	def up_check_left (self, checked_wall, walls_set, wall_left):
		for i in walls_set:
			if i.rect.y == checked_wall.rect.y-45 and i.rect.x == checked_wall.rect.x:
				if i.image == wall_left:
					return True
		return False	

	def up_check_right (self, checked_wall, walls_set, wall_right):
		for i in walls_set:
			if i.rect.y == checked_wall.rect.y-45 and i.rect.x == checked_wall.rect.x:
				if i.image == wall_right:
					return True
		return False			

	def down_check (self, checked_wall, walls_set):
		for i in walls_set:
			if i.rect.y == checked_wall.rect.y+45 and i.rect.x == checked_wall.rect.x:
				return True
		return False

	def left_check (self, checked_wall, walls_set):
		for i in walls_set:
			if i.rect.y == checked_wall.rect.y and i.rect.x == checked_wall.rect.x-45:
				return True
		return False

	def right_check (self, checked_wall, walls_set):
		for i in walls_set:
			if i.rect.y == checked_wall.rect.y and i.rect.x == checked_wall.rect.x+45:
				return True
		return False
	def is_down_flor (self, checked_wall, ground):
		for i in ground:
			if i.rect.y == checked_wall.rect.y+45 and i.rect.x == checked_wall.rect.x:
				return True
		return False

	def is_up_flor (self, checked_wall, ground):
		for i in ground:
			if i.rect.y == checked_wall.rect.y-45 and i.rect.x == checked_wall.rect.x:
				return True
		return False

	def is_right_flor (self, checked_wall, ground):
		for i in ground:
			if i.rect.y == checked_wall.rect.y and i.rect.x == checked_wall.rect.x+45:
				return True
		return False

	def is_left_flor (self, checked_wall, ground):
		for i in ground:
			if i.rect.y == checked_wall.rect.y and i.rect.x == checked_wall.rect.x-45:
				return True
		return False

	def wall_check (self, checked_wall, walls):
		a = 0
		for i in walls:
			
			if i.rect.y == checked_wall.rect.y-45 and i.rect.x == checked_wall.rect.x:
				return a
			a += 1

		return False


	def create_addition_wall (self, i, addition, image):
		wall_up = (classes.Platform(i.rect.x, i.rect.y-45))
		wall_up.image = image
		addition.append (wall_up)
		
	def wall_determination (self, walls_set, addition, ground):

		wall_base = pygame.image.load ('images/wall/wall.png')
		wall_c = pygame.image.load ('images/wall/wall_c.png')
		wall_c_up = pygame.image.load ('images/wall/wall_c_up.png')
		wall_up_img = pygame.image.load ('images/wall/wall_up.png')
		wall_right = pygame.image.load ('images/wall/right.png')
		wall_left = pygame.image.load ('images/wall/left.png')
		wall_c_1 = pygame.image.load ('images/wall/wall_c_1.png')
		wall_c_3 = pygame.image.load ('images/wall/wall_c_3.png')
		wall_down = pygame.image.load ('images/wall/wall_down.png')
		wall_c_4 = pygame.image.load ('images/wall/wall_c_4.png')

		for i in walls_set:
			if self.up_check(i, walls_set) == False and (self.left_check (i, walls_set) == True and self.right_check (i, walls_set) == True) and self.is_up_flor(i,ground) == False:
				i.image = wall_base
				self.create_addition_wall (i, addition, wall_up_img)

			elif self.up_check(i, walls_set) == True and (self.left_check (i, walls_set) == True or self.right_check (i, walls_set) == True) and self.is_down_flor(i,ground) == True:
				i.image = wall_base
				a = self.wall_check (i, walls_set)

				if a != False:
					walls_set[a].image = wall_c
				else:
					self.create_addition_wall (i, addition, wall_c)

			elif self.up_check(i, walls_set) == False and self.left_check (i, walls_set) == False and self.is_left_flor(i, ground) == False and self.is_up_flor (i, ground) == False and self.is_down_flor (i, ground) == False:
				i.image = wall_left
				self.create_addition_wall (i, addition, wall_c_1)

			elif self.up_check(i, walls_set) == False and self.left_check (i, walls_set) == False and self.is_left_flor(i, ground) == False and self.is_up_flor (i, ground) == False and self.is_down_flor (i, ground) == True:

				i.image = wall_base
				self.create_addition_wall (i, addition, wall_up_img)

			elif self.up_check(i, walls_set) == False and self.left_check (i, walls_set) == False and self.is_left_flor(i, ground) == True and self.is_right_flor (i, ground) == True:
				i.image = wall_c

			elif self.up_check(i, walls_set) == False and self.right_check (i, walls_set) == False and self.is_right_flor(i, ground) == False and self.down_check (i, walls_set) == True:
				i.image = wall_right
				if self.is_up_flor(i, ground) == False:
					self.create_addition_wall (i, addition, wall_c_up)

			elif self.up_check(i, walls_set) == False and self.right_check (i, walls_set) == False and self.is_right_flor(i, ground) == False and self.down_check (i, walls_set) == False and self.is_down_flor(i, ground) == True:
				i.image = wall_base
				self.create_addition_wall (i, addition, wall_up_img)
#
			elif self.up_check(i, walls_set) == False and self.right_check (i, walls_set) == False and self.is_right_flor(i, ground) == True and self.is_up_flor(i, ground) == True:
				i.image = wall_c

			elif self.up_check(i, walls_set) == False and self.right_check (i, walls_set) == False and self.is_right_flor(i, ground) == True and self.is_up_flor(i, ground) == False:
				i.image = wall_base
				self.create_addition_wall (i, addition, wall_up_img)

			elif self.up_check(i, walls_set) == False and self.left_check (i, walls_set) == False and self.is_left_flor(i, ground) == True and self.is_up_flor(i, ground) == False:
				i.image = wall_base
				self.create_addition_wall (i, addition, wall_up_img)

			elif self.up_check(i, walls_set) == True and self.right_check (i, walls_set) == False and self.is_right_flor(i, ground) == False and self.left_check(i, walls_set) == False:
				i.image = wall_right

			elif self.up_check(i, walls_set) == True and self.right_check (i, walls_set) == False and self.is_right_flor(i, ground) == False and self.left_check(i, walls_set) == True:
				i.image = wall_c_3

			elif self.up_check(i, walls_set) == True and self.right_check (i, walls_set) == False and self.left_check (i, walls_set) == True and self.is_right_flor(i, ground) == True:
				i.image = wall_c

			elif self.up_check(i, walls_set) == True and self.is_right_flor(i, ground) == True and self.is_left_flor (i, ground) == False and self.down_check(i, walls_set) == True:
				i.image = wall_left

				pass


				#self.create_addition_wall (i, addition, wall_c_up)
			elif self.is_down_flor(i, ground) == False and self.down_check (i, walls_set) == False and self.up_check (i, walls_set)== False:
				i.image = wall_down

			elif self.is_down_flor(i, ground) == False and self.down_check (i, walls_set) == False and self.up_check (i, walls_set) == True and self.is_right_flor(i, ground) == True:
			#elif self.up_check(i, walls_set) == True and self.left_check (i, walls_set) == True:
				i.image = wall_left

			elif self.up_check (i, walls_set) == True and self.right_check (i, walls_set) == True and self.is_down_flor (i, ground) == False and self.is_left_flor (i, ground) == False:
				i.image = wall_c_4


#
			else: i.image = wall_c

#End of automatic wall`s taile selection

	def create (self, create_level = constructor.create_dungeon1, create_interior = constructor.create_interior_standart, floor = classes.Floor):

# create_level - create monsters, treasures and unique objects of location
# create interior - create WALLS, GROUND and other landscapes object.

		sprites = create_level (self.lev, self.battle, self.control, self.son, self.techname)
		interior, ground, walls, decor = create_interior (self.lev, floor)
		addition = []

		if self.auto == True and self.control.auto == True:
			self.wall_determination(walls,addition, ground)

		for i in interior:
			sprites.add (i)

		for i in walls:
			sprites.add (i)

		for i in addition:
			sprites.add (i)

		#for i in decor:


		return sprites, ground, decor

	def additional_content(self,hero):
		pass
	def render_location_info (self):
		self.son.change_text (1, '')
		self.son.change_text (2, '')
		self.son.change_text (3, '')		
		self.son.change_text (4, '')
		self.son.change_text (5, '')
		self.son.change_text (6, '')		
		self.son.change_text (7, '')

	def render_stage (self, hero):

		main_interface (self)

		#render background
		if self.back == True:

			for b in self.background:
				adventure_screen.blit(b.image, self.camera.apply (b))

		self.additional_content(hero)
		#rendering map`s objects
		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))
			if b.__class__.__name__ == 'PortalLink':
				b.animation(self.camera)

		for i in self.decor:
			adventure_screen.blit(i.image, self.camera.apply (i))

		try:
			pos = self.camera.apply(hero.etwas)
		except:
			pos = self.camera.apply(hero)

		hero_pos = self.camera.apply(hero)
		adventure_screen.blit (hero.image, self.camera.apply(hero))
		#rendering hero
		if hero.status != 'dead':
			
			hero.dustAnim.blit (adventure_screen, (pos.x-45, pos.y-45))
			hero.slashAnim.blit (adventure_screen, (pos.x, pos.y))
			hero.bloodAnim.blit (adventure_screen, (pos.x+20, pos.y))
			hero.slashAnim_self.blit (adventure_screen, (hero_pos.x, pos.y))
			hero.bloodAnim_self.blit (adventure_screen, (hero_pos.x+20, pos.y))

			hero.anima.blit (adventure_screen, (self.camera.apply(hero)))
			if hero.move == False:
			# or self.control.move_cntrl == False:
				adventure_screen.blit (hero.standlist[hero.direction], self.camera.apply(hero))

		#render text_information
		self.son.render_text ()

		if self.render_information == True:
			self.son.clear_text()
			self.render_location_info ()
			self.render_information = False
			for i in hero.location_list:
				if i.__class__.__name__ != self.__class__.__name__:

					i.render_information = True



		hero.render_information ()

	#def get_coordinates(self,hero):
		#return self.camera.apply(hero)

	def general_stuff (self, hero):

		#hero dead or alive
		if hero.status == 'dead':
			hero.end_text ()

		#if self.hero.status != 'dead':
			#MAIN HERO RENDER FUNCTION!!!
		#	self.hero.update (self.block_group)

		#render hp mod of monsters in a battle
		try:	
			x_monster = (self.camera.apply(hero.etwas))
			hero.etwas.render_hp_mod(x_monster)
		except:
			pass

		#Rendering hero hp modification
		self.x_hero = (self.camera.apply(hero))
		hero.render_hp_mod(self.x_hero)
		hero.render_sp_mod(self.x_hero)
		hero.render_exp_mod(self.x_hero)
		hero.render_lev_mod(self.x_hero)
		#camera
		self.camera.update(hero)

		#if self.inception == True:
		#	hero.etwas = self.event
		#	hero.collide_control = True
		#	hero.move = False
		#	self.inception = False
		pos = self.camera.apply(hero)
		#timer
		self.a = timer.get_fps()		
		timer.tick (60)
		img.healAnim.blit (adventure_screen, (pos.x-70, pos.y-70))

	def stage_content (self, hero):
		pass

	def stage_loop (self, hero):

		self.general_stuff (hero)

		self.render_stage (hero)
		self.stage_content (hero)
