import pygame
import pyganim
import classes
import functions
from screens import *
from constants import *
import fonts
import text
import camera

timer = pygame.time.Clock  ()
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                 ('testimages/bolt_strike_0002.png', 0.1),
                                 ('testimages/bolt_strike_0003.png', 0.1),
                                 ('testimages/bolt_strike_0004.png', 0.1),
                                 ('testimages/bolt_strike_0005.png', 0.1),
                                 ('testimages/bolt_strike_0006.png', 0.1),
                                 ('testimages/bolt_strike_0007.png', 0.1),
                                 ('testimages/bolt_strike_0008.png', 0.1),
                                 ('testimages/bolt_strike_0009.png', 0.1),
                                 ('testimages/bolt_strike_0010.png', 0.1)])
boltAnim.rotate (270)
boltAnim.play() # there is also a pause() and stop() method
#boltAnim.loop = False
class Level ():

	def __init__ (self, control, hero, lev, camera, battle, son):

		self.platforms, self.block_group = functions.create_level (lev, battle, control,son)
		self.control = control
		self.hero = hero
		self.camera = camera
		
		self.battle = battle
		self.skeletLord = classes.SkeletLord (10,10, self.battle, text.zombitext, self.control, 10,10,10,1, son)
		self.zomb = classes.Monster (0,0, self.battle, text.zombitext, self.control, 10,0,10,1, son)

		self.block_group.add (self.zomb)
		self.block_group.add (self.skeletLord)
		self.n = 0
		self.son = son
		self.g = 1200

	def render_stage1 (self):

		main_interface ()
		self.g += 1
		for b in self.block_group:
			adventure_screen.blit(b.image, self.camera.apply (b))

		if self.hero.status != 'dead':
			adventure_screen.blit (self.hero.image, self.camera.apply(self.hero))
		start_screen.blit(fonts.font1.render (str(self.a), True, (250,250,250)),(0,0))

	def stage_loop (self):
		if self.skeletLord.lbolt == True:
			self.g = 185
			self.skeletLord.lbolt = False

		
		x_hero = (self.camera.apply(self.hero))
		if self.g > 190 and self.g< 220:
			x_hero.x -=49
			x_hero.y -=80
			boltAnim.blit (adventure_screen, (x_hero))
		self.a = timer.get_fps()
		self.render_stage1 ()

		if self.hero.status == 'dead':
			self.hero.end_text ()

		if self.hero.status != 'dead':
			self.hero.update (self.block_group)
		self.hero.chang ()
 
		if self.hero.collide_control == True and self.hero.etwas.agression == True:
			self.battle.main_loop (self.hero, self.hero.etwas)

		self.son.render_text ()

		self.hero.render_information ()

		self.camera.update(self.hero)
		timer.tick (60)

		if self.control.k_space == True:
			self.control.stage1_flag = False
			self.control.stage2_flag = True
