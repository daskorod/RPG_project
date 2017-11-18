import pygame


pygame.mixer.pre_init (44100, -16, 1, 2512)
pygame.mixer.init()

footstep = pygame.mixer.Sound ('sound/foot3.ogg')
#footstep.set_volume(0.2)

arr = pygame.mixer.Sound ('sound/clic.ogg')
arr.set_volume(0.5)

prints = pygame.mixer.Sound('sound/7.ogg')
#prints.set_volume(0.1)

hit = pygame.mixer.Sound('sound/hit.ogg')
flee = pygame.mixer.Sound('sound/flee.ogg')
fire = pygame.mixer.Sound('sound/fire.ogg')
light = pygame.mixer.Sound('sound/light.ogg')
pain = pygame.mixer.Sound('sound/pain.ogg')
trink = pygame.mixer.Sound('sound/trink.ogg')
barrel = pygame.mixer.Sound('sound/barrel.ogg')
alell = pygame.mixer.Sound('sound/allel.ogg')
bells = pygame.mixer.Sound('sound/bells.ogg')
bells.set_volume(3)

requiem = pygame.mixer.Sound('sound/requiem.ogg')
requiem.set_volume(50)

credo = pygame.mixer.Sound('sound/credo.ogg')