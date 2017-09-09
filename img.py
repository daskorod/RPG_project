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


barrel = image.load('images/tiles/barrel.png')
box = image.load('images/tiles/box.png')
pot = image.load('images/tiles/pot.png')
stone = image.load('images/tiles/stone.png')

barrel_t = 'Старая никому ненужная бочка. Внутри вся в паутине.'
box_t = 'Раздолбанный ящик. Пойдёт только на дрова.'
stone_t = 'Какая-то вопиющая глыба, взгромоздившаяся у вас на пути.'
pot_t = 'Тресунвший кувшин. Он представляет собой жалкое зрелище.'

obstacles = [(barrel,barrel_t), (box,box_t), (pot,pot_t), (stone,stone_t)]

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