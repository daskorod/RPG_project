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

class Camera ():
	def __init__ (self,camera_config, width, height):
		self.camera_config = camera_config
		self.state = pygame.Rect (0, 0, width, height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_config(self.state, target.rect)





















