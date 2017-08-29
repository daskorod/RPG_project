from pygame import image
import re

pave1 = image.load('images/pave1.png')
pave2 = image.load('images/pave2.png')
pave3 = image.load('images/pave3.png')
pavestones = [pave1,pave2,pave3]

pave_stone1 = image.load('images/tiles/floor_stone.png')
pave_stone2 = image.load('images/tiles/floor_stone2.png')
pavestones_city = [pave_stone1, pave_stone2]
done = True


pave_wood1 = image.load('images/tavern/base.png')
pave_wood2 = image.load('images/tavern/crack.png')
pave_tavern = [pave_wood1, pave_wood2]


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