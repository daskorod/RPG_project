import level_data
import constants
import pygame


#state - 'экран'

#def camera_config (camera, target_rect):
#		l = -target_rect.rect.x + 810/2
#		t = -target_rect.rect.y + 420/2
#		w,h = camera.width, camera.height
#
#		l = min(0, l)                           # Не движемся дальше левой границы
#		l = max(-(camera.width-810), l)   # Не движемся дальше правой границы
#		t = max(-(camera.height-420), t) # Не движемся дальше нижней границы
#		t = min(0, t)                           # Не движемся дальше верхней границы
#
#
#		return pygame.Rect (l,t,w,h)

#def camera_config (camera, target_rect, screen_width, screen_height):
#		l = -target_rect.x + screen_width/2
#		t = -target_rect.y + screen_height/2
#		w,h = camera.width, camera.height
#
#		l = min(0, l)                           # Не движемся дальше левой границы
#		l = max(-(camera.width - screen_width), l)   		# Не движемся дальше правой границы
#		t = max(-(camera.height- screen_height), t) 		# Не движемся дальше нижней границы
#		t = min(0, t)                           # Не движемся дальше верхней границы
#
#
#		return pygame.Rect (l,t,w,h)

class Camera ():
	def __init__ (self, width, height, screen_width, screen_height):
		#self.camera_config = camera_config
		self.state = pygame.Rect (0, 0, width, height)
		self.screen_width = screen_width
		self.screen_height = screen_height
		

	def camera_config (self,camera, target_rect):
		l = -target_rect.x + self.screen_width/2
		t = -target_rect.y + self.screen_height/2
		w,h = camera.width, camera.height

		l = min(0, l)                           # Не движемся дальше левой границы
		l = max(-(camera.width - self.screen_width), l)   		# Не движемся дальше правой границы
		t = max(-(camera.height- self.screen_height), t) 		# Не движемся дальше нижней границы
		t = min(0, t)                           # Не движемся дальше верхней границы


		return pygame.Rect (l,t,w,h)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_config(self.state, target.rect)





















