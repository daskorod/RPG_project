#! /usr/bin/env python3
import pygame

from constants import *
import fonts

import sys


import screens

timer = pygame.time.Clock  ()

menu_text = "  Нажмите SPACE"

start_screen = pygame.Surface((840, 630))

intro_screen = pygame.Surface((600, 370))		
		

def menu_loop ():

		done1 = True
		time = 0
		x = 225
		up = True

		main_image = pygame.image.load ('images/main_pic_de.gif')
		text_image = pygame.image.load ('images/logo_text.gif')

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
			start_screen.blit(screens.start_screen_version_surface, (700, 570))

			screens.start_screen_text_surface.fill ((black))
			screens.start_screen_text_surface.blit(fonts.font2.render (menu_text,True, (x,x,x)), (10,10))
			screens.start_screen_version_surface.fill ((black))
			screens.start_screen_version_surface.blit(fonts.font3.render (version,True, (200,200,200)), (50,10))	


			start_screen.blit (main_image, (120, 40))
			start_screen.blit (text_image, (120, 430))

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

def load ():

		done1 = True
		time = 0
		x = 225
		up = True
		while time < 10:
			time = time+1
			screens.window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit(screens.start_screen_text_surface, (320, 310))
			screens.start_screen_text_surface.fill ((black))
			screens.start_screen_text_surface.blit(fonts.font2.render ("    ЗАГРУЗКА ...",True, (x,x,x)), (10,10))
		
			pygame.display.update() 

def pause ():

		done1 = True
		time = 0
		x = 225
		up = True
		while time < 10:
			time = time+1
			screens.window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit(screens.start_screen_text_surface, (320, 310))
			screens.start_screen_text_surface.fill ((black))
			#screens.start_screen_text_surface.blit(fonts.font2.render ("        ЗАГРУЗКА ...",True, (x,x,x)), (10,10))
		
			pygame.display.update() 

text1 = 'В начале сотворил Бог небо и землю...'




#stroke_compendium = [str() for x in range(6)]

def splittext (text):
	splitted_by_space = text.split(' ')
	current_stroke = 0
	stroke_compendium = [str() for x in range(6)]

	for wort in splitted_by_space:
		if len(stroke_compendium[current_stroke]+' '+wort)<48:
			stroke_compendium[current_stroke] = stroke_compendium[current_stroke]+' '+wort
		else:
			current_stroke+=1
			stroke_compendium[current_stroke] = stroke_compendium[current_stroke]+' '+wort

	return stroke_compendium



def experiment_loop (text, pic, end_black = False, pic_x = 50, pic_y = 20, time_scroll = 10000, speed_mod = 3):

		done1 = True
		time = 0
		x = 225
		up = True
		time2 = 0
		count = 0
		sound1 = pygame.mixer.Sound('sound/7.ogg')
		sound1.set_volume(0.01)
		time3 = 0
		end = False
		intro = pygame.image.load (pic)
		text_to_print_compendium = [str() for x in range(6)]
		stroke_compendium = splittext (text)
		time4 = 0
		while done1:



			screens.window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit (intro_screen, (120,20))
			intro_screen.fill ((black))

			start_screen.blit(screens.start_screen_text_surface, (560, 570))

			screens.start_screen_text_surface.fill ((black))

			

			start_screen.blit (screens.text_intro_screen, (120, 430))
			screens.text_intro_screen.fill ((black))
			intro_screen.blit (intro, (pic_x, pic_y-time2))
			text2 = text1[:time2]
			

			if end != True:
				try:

					if stroke_compendium[count][time3-1] != ' ':

						sound1.play()
				except:
					pass

			if end == True:
				screens.start_screen_text_surface.blit(fonts.font2.render ("           SPACE ",True, (x,x,x)), (10,10))


			text_to_print_compendium[count] = stroke_compendium[count][:time3]

			if len(stroke_compendium[count])<time3:
				
				if len(stroke_compendium)>count+1:
					count +=1
					time3 = 0
					time4 = 0
				else:
					end = True
					


			for i in range(6):

				screens.text_intro_screen.blit(fonts.underdog.render (text_to_print_compendium[i], True, (white)), (10,10+i*20))


			if up == True:
				x = x - 5
			if up == False:
				x = x + 5
	
			if x > 210:
				up = True
			if x < 10:
				up = False

			timer.tick (30)
			time4 = time4 + 1
			time = time + 1
			time3 = time3 + 2

			if time2 < time_scroll:
				time2 = int(time//speed_mod)


			for e in pygame.event.get ():
					if e.type == pygame.QUIT:
							sys.exit ()

					if e.type == pygame.KEYDOWN:
						if e.key == pygame.K_SPACE:

							done1 = False
#							if end_black == True:
#								screens.window.blit(start_screen, (10, 10))
#								start_screen.fill ((black))
#								start_screen.blit(screens.start_screen_text_surface, (300, 510))
#								screens.start_screen_text_surface.fill ((black))
#	
#								screens.start_screen_text_surface.blit(fonts.font2.render ("ЗАГРУЗКА...",True, (255,255,255)), (10,10))

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
