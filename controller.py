import pygame
import sys
import sounds

class Holy_Spirit ():
	def __init__ (self):
		self.auto = True
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
		self.k_q = False
		self.button_up = True
		self.clic = False
		self.k_j = False
		self.k_esc = False
		self.e_cntrl = False
		self.up_is = False
		self.down_is = False
		self.k_1_control = False
		self.k_2_control = False
		self.k_3_control = False	
		self.k_a = False	
		self.move_cntrl_a = False
#		R = False
#		L = False
#		U = False
#		D = False
#		self.direction = [R,L,U,D]
		self.current_location = ''
		self.move_cntrl = False
		self.e_lock = False
		
	def control (self):
			if self.k_esc == True:
				sys.exit ()				
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
						if self.move_cntrl_a == False:
							self.move_cntrl = True
							self.move_cntrl_a = True

					if e.key == pygame.K_RIGHT:
						self.right = True
						if self.move_cntrl_a == False:
							self.move_cntrl = True
							self.move_cntrl_a = True

				if e.type == pygame.KEYDOWN:
					
					if e.key == pygame.K_UP:
						self.up = True
						self.up_is = True
						if self.move_cntrl_a == False:
							self.move_cntrl = True
							self.move_cntrl_a = True

					if e.key == pygame.K_DOWN:
						self.down = True
						self.down_is = True
						if self.move_cntrl_a == False:
							self.move_cntrl = True
							self.move_cntrl_a = True

				if e.type == pygame.KEYUP:
					if e.key == pygame.K_LEFT:
						self.left = False
						self.move_cntrl_a = False

					if e.key == pygame.K_RIGHT:
						self.right = False
						self.move_cntrl_a = False

				if e.type == pygame.KEYUP:
					
					if e.key == pygame.K_UP:
						self.up = False
						self.up_is = False
						self.move_cntrl_a = False

					if e.key == pygame.K_DOWN:
						self.down = False
						self.down_is = False
						self.move_cntrl_a = False

				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_1 and self.k_1_control == False:
						self.k_1 = True
						self.k_1_control = True
						self.clic = True

					if e.key == pygame.K_2 and self.k_2_control == False:
						self.k_2 = True
						self.k_2_control = True
						self.clic = True

					if e.key == pygame.K_3 and self.k_3_control == False:
						self.k_3 = True
						self.k_3_control = True
						self.clic = True

					if e.key == pygame.K_4:
						self.k_4 = True

					if e.key == pygame.K_n:
						self.k_n = True
					if e.key == pygame.K_e and self.e_lock == False:
						#self.e_cntrl = False
						self.k_e = True
						sounds.clic2.play()
						self.e_lock = True

					if e.key == pygame.K_i:
						self.k_i = True

					if e.key == pygame.K_a:
						self.k_a = True

					if e.key == pygame.K_c:
						self.k_c = True
					if e.key == pygame.K_j:
						self.k_j = True
					if e.key == pygame.K_q:
						self.k_q = True
					if e.key == pygame.K_ESCAPE:
						self.k_esc = True

				if e.type == pygame.KEYUP:
					if e.key == pygame.K_1:
						self.k_1 = False
						self.button_up = True
						self.k_1_control = False

					if e.key == pygame.K_2:
						self.k_2 = False
						self.button_up = True
						self.k_2_control = False

					if e.key == pygame.K_3:
						self.k_3 = False
						self.button_up = True
						self.k_3_control = False

					if e.key == pygame.K_4:
						self.k_4 = False
						self.button_up = True

					if e.key == pygame.K_n:
						self.k_n = False
					if e.key == pygame.K_e:
						self.e_cntrl = True
						self.k_e = False
						self.e_lock = False
						

					if e.key == pygame.K_i:
						self.k_i = False

					if e.key == pygame.K_a:
						self.k_a = False


					if e.key == pygame.K_c:
						self.k_c = False
					if e.key == pygame.K_j:
						self.k_j = False
					if e.key == pygame.K_q:
						self.k_q = False

					if e.key == pygame.K_ESCAPE:
						self.k_esc = False