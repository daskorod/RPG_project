#! /usr/bin/env python3
import pygame

from constants import *
import fonts

import sys


import screens

timer = pygame.time.Clock  ()

menu_text = "  Нажмите SPACE"

start_screen = pygame.Surface((840, 630))

		
		

def menu_loop ():

		done1 = True
		time = 0
		x = 225
		up = True

		main_image = pygame.image.load ('images/main_pic2.gif')

		while done1:

			for e in pygame.event.get ():
					if e.type == pygame.QUIT:
							sys.exit ()

					if e.type == pygame.KEYDOWN:
						if e.key == pygame.K_SPACE:

							done1 = False

			screens.window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit(screens.start_screen_text_surface, (300, 510))
			screens.start_screen_text_surface.fill ((black))
			screens.start_screen_text_surface.blit(fonts.font2.render (menu_text,True, (x,x,x)), (10,10))
			
			start_screen.blit (main_image, (120, 100))
			if up == True:
				x = x - 5
			if up == False:
				x = x + 5
	
			if x > 210:
				up = True
			if x < 10:
				up = False

			timer.tick (30)
			time = time + 1

			pygame.display.update() 

def help_loop ():

		done1 = True
		time = 0
		x = 225
		up = True

		main_image = pygame.image.load ('images/control.png')

		while done1:

			for e in pygame.event.get ():
					if e.type == pygame.QUIT:
							sys.exit ()

					if e.type == pygame.KEYDOWN:
						if e.key == pygame.K_SPACE:

							done1 = False

			screens.window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit(screens.start_screen_text_surface, (300, 500))
			start_screen.blit (main_image, (170, 100))
			screens.start_screen_text_surface.fill ((black))
			screens.start_screen_text_surface.blit(fonts.font2.render (menu_text,True, (x,x,x)), (10,10))

			

			if up == True:
				x = x - 5
			if up == False:
				x = x + 5
	
			if x > 210:
				up = True
			if x < 10:
				up = False

			timer.tick (30)
			time = time + 1

			pygame.display.update() 
