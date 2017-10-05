import pygame


pygame.mixer.pre_init (44100, -16, 1, 2512)
pygame.mixer.init()

footstep = pygame.mixer.Sound ('sound/foot3.ogg')
footstep.set_volume(0.02)

prints = pygame.mixer.Sound('sound/7.ogg')
prints.set_volume(0.01)

