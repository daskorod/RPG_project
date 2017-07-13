import pygame
import sys

class Holy_Spirit ():
	def __init__ (self):

		self.k_space = False
		self.stage1_flag = False
		self.stage2_flag = True
		self.flag = 0
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		self.k_1 = False
		self.k_2 = False
		self.k_3 = False
		self.k_4 = False
		self.k_n = False
		self.k_e = False
		self.k_i = False
		self.k_c = False
		self.button_up = True
#		R = False
#		L = False
#		U = False
#		D = False
#		self.direction = [R,L,U,D]
		self.current_location = ''
		self.move_cntrl = False
		
	def control (self):
			for e in pygame.event.get ():

				if e.type == pygame.QUIT:
					sys.exit ()

				if e.type == pygame.KEYDOWN:

					if e.key == pygame.K_SPACE:
						self.k_space = True

				if e.type == pygame.KEYUP:

					if e.key == pygame.K_SPACE:
						self.k_space = False

				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_LEFT:
						self.left = True
						self.move_cntrl = True

					if e.key == pygame.K_RIGHT:
						self.right = True
						self.move_cntrl = True

				if e.type == pygame.KEYDOWN:
					self.move_cntrl = True
					if e.key == pygame.K_UP:
						self.up = True
						

					if e.key == pygame.K_DOWN:
						self.down = True

				if e.type == pygame.KEYUP:
					if e.key == pygame.K_LEFT:
						self.left = False
						self.move_cntrl = False

					if e.key == pygame.K_RIGHT:
						self.right = False
						self.move_cntrl = False

				if e.type == pygame.KEYUP:
					self.move_cntrl = False
					if e.key == pygame.K_UP:
						self.up = False

					if e.key == pygame.K_DOWN:
						self.down = False

				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_1:
						self.k_1 = True

					if e.key == pygame.K_2:
						self.k_2 = True

					if e.key == pygame.K_3:
						self.k_3 = True

					if e.key == pygame.K_4:
						self.k_4 = True

					if e.key == pygame.K_n:
						self.k_n = True
					if e.key == pygame.K_e:
						self.k_e = True

					if e.key == pygame.K_i:
						self.k_i = True
					if e.key == pygame.K_c:
						self.k_c = True
				if e.type == pygame.KEYUP:
					if e.key == pygame.K_1:
						self.k_1 = False
						self.button_up = True

					if e.key == pygame.K_2:
						self.k_2 = False
						self.button_up = True
					if e.key == pygame.K_3:
						self.k_3 = False
						self.button_up = True

					if e.key == pygame.K_4:
						self.k_4 = False
						self.button_up = True

					if e.key == pygame.K_n:
						self.k_n = False
					if e.key == pygame.K_e:
						self.k_e = False
					if e.key == pygame.K_i:
						self.k_i = False
					if e.key == pygame.K_c:
						self.k_c = False
