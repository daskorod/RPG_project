from pygame import image
import pyganim
import re

pave1 = image.load('images/pave1.png')
pave2 = image.load('images/pave2.png')
pave3 = image.load('images/pave3.png')
pavestones = [pave1,pave2,pave3]

pave_stone1 = image.load('images/tiles/floor_stone.png')
pave_stone2 = image.load('images/tiles/floor_stone2.png')
pavestones_city = [pave_stone1, pave_stone2]
done = True
house = image.load('images/tiles/house.png')

pave_wood1 = image.load('images/tavern/base.png')
pave_wood2 = image.load('images/tavern/crack.png')
pave_tavern = [pave_wood1, pave_wood2]

bone1 = image.load('images/tiles/skull1.png')
bone2 = image.load('images/tiles/skull2.png')
bone3 = image.load('images/tiles/skull3.png')
bone4 = image.load('images/tiles/skull4.png')
bone_floor = [bone1, bone2, bone3, bone4]

bless = image.load('images/bless.png')
firer = image.load('images/fire.png')
lightr = image.load('images/light.png')
narc = image.load('images/narc.png')

arrow = image.load('images/arrow_map.png')
arrow2 = image.load('images/arrow_map2.png')
arrowl = image.load('images/arrow_map_left.png')
arrowr = image.load('images/arrow_map_right.png')
arrowd = image.load('images/arrow_map_down.png')

wall_stone1 = image.load('images/tavern/stone_wall.png')
wall_stone2 = image.load('images/tavern/stone_wall_l.png')
wall_stone3 = image.load('images/tavern/stone_wall_r.png')
wall_stone4 = image.load('images/tavern/left.png')
wall_stone5 = image.load('images/tavern/right.png')
wall_stone6 = image.load('images/tavern/down.png')
wall_stone7 = image.load('images/tavern/up.png')
wall_stone8 = image.load('images/tavern/up_right_corn.png')
wall_stone9 = image.load('images/tavern/up_left_corn.png')
wall_stone10 = image.load('images/tavern/corner_big1.png')
wall_stone11 = image.load('images/tavern/corner_big2.png')
wall_stone12 = image.load('images/tavern/down_left_corn.png')
wall_stone13 = image.load('images/tavern/down_right_corn.png')


#for i in dir ():
	#if i == match.
stone_wall_tavern = [
wall_stone1,
wall_stone2,
 wall_stone3,
  wall_stone4,
   wall_stone5,
    wall_stone6,
     wall_stone7,
    wall_stone8,
     wall_stone9,
    wall_stone10,
     wall_stone11,
    wall_stone12,
     wall_stone13

     ]
#stone_wall_tavern = [x for x in range(1,7)]

slash1 = image.load('animation/slash/Effect_Slash11.png')
slash2 = image.load('animation/slash/Effect_Slash21.png')
slash3 = image.load('animation/slash/Effect_Slash31.png')
slash4 = image.load('animation/slash/Effect_Slash41.png')

slash_list = [slash1, slash2, slash3, slash4]


boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                 ('testimages/bolt_strike_0002.png', 0.1),
                                 ('testimages/bolt_strike_0003.png', 0.1),
                                 ('testimages/bolt_strike_0004.png', 0.1),
                                 ('testimages/bolt_strike_0005.png', 0.1),
                                 ('testimages/bolt_strike_0006.png', 0.1),
                                 ('testimages/bolt_strike_0007.png', 0.1),
                                 ('testimages/bolt_strike_0008.png', 0.1),
                                 ('testimages/bolt_strike_0009.png', 0.1),
                                 ('testimages/bolt_strike_0010.png', 0.1)], loop=False)
boltAnim.rotate (270)

fireAnim = pyganim.PygAnimation([('testimages/flame_a_0001.png', 0.2),
                                 ('testimages/flame_a_0002.png', 0.2),
                                 ('testimages/flame_a_0003.png', 0.2),
                                 ('testimages/flame_a_0004.png', 0.2),
                                 ('testimages/flame_a_0005.png', 0.2),
                                 ('testimages/flame_a_0006.png', 0.2),], loop=False)


arrow_right = image.load('images/arrow_right.png')
arrow_left = image.load('images/arrow_left.png')



stone0 = image.load('images/obst/stone0.png')
stone1 = image.load('images/obst/stone1.png')
stone2 = image.load('images/obst/stone2.png')
stone3 = image.load('images/obst/stone3.png')
stone4 = image.load('images/obst/stone4.png')
stone5 = image.load('images/obst/stone5.png')
wood = image.load('images/obst/wood1.png')

obstacles_stone = [wood,stone1,stone2,stone3,stone4,stone5]
obstacles_stone_t = ['Мерзкие и противные камни, лежащие на вашей дороге', 'Здесь не пройти - камней слишком много.',"Груда камней, земли и мусора.", "Грязь, сор, обрезки ногтей и волос."]

barrel_broken = image.load('images/obst/barrel_broken.png')
box_broken = image.load('images/obst/box_broken.png')
pot_broken = image.load('images/obst/pot_broken.png')

barrel = image.load('images/obst/barrel.png')
box = image.load('images/obst/box.png')
pot = image.load('images/obst/pot.png')

barrel_t = 'Добротная бочка, может быть внутри у ней что-то есть?'
box_t = 'Ящик, сколоченный из досок.'
pot_t = 'Амфора. Или простой горшок?'

barrel_br_t = 'Старая никому ненужная бочка. Внутри вся в паутине.'
box_br_t = 'Раздолбанный ящик. Пойдёт только на дрова.'
stone_t = 'Какая-то вопиющая глыба, взгромоздившаяся у вас на пути.'
pot_br_t = 'Тресунвший кувшин. Он представляет собой жалкое зрелище.'
obstacles = [stone0,stone1,stone2,stone3,stone4,stone5]

obstacles_useful = [(barrel,barrel_t,barrel_broken, barrel_br_t), (box,box_t,box_broken,box_br_t), (pot,pot_t,pot_broken, pot_br_t)]
#obstacles = [(barrel,barrel_t), (box,box_t), (pot,pot_t), (stone,stone_t)]
obstacles_broken = [(barrel_broken,barrel_br_t), (box_broken,box_br_t), (pot_broken,pot_br_t)]

speed = 0.05
healAnim = pyganim.PygAnimation([('animation/heal/heal01.png', speed),
('animation/heal/heal02.png', speed),
('animation/heal/heal03.png', speed),
('animation/heal/heal04.png', speed),
('animation/heal/heal05.png', speed),
('animation/heal/heal06.png', speed),
('animation/heal/heal07.png', speed),
('animation/heal/heal08.png', speed),
('animation/heal/heal09.png', speed),
('animation/heal/heal10.png', speed)], loop=False)


kubert = image.load('images/tiles/kubert.png')