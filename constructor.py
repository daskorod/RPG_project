import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text
import items
import npc
import text_data.zombisad, text_data.monk, text_data.gilbert_dict,text_data.barmen_dict
#import npc

def create_dungeon1 (level, battle, control, son, locationname):

       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "z":
                            z = classes.Zombi (x/45,y/45,battle, text_data.zombisad.text, control, 10,0,10,1, son,20)
                            sprite_group.add (z)

                     if col == 'e':
                            e = classes.PortalS (x,y, 'end', (15,4))
                            sprite_group.add (e)

                     if col == 'w':
                            e = classes.PortalS (x,y, 'dungeon2', (2,15))
                            sprite_group.add (e)

                     if col == 's':
                            s = classes.MinorChest2 (x,y, 'open', items.garbage )
                            sprite_group.add (s)


                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group

def create_dungeon2 (level, battle, control, son, locationname):

       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "z":
                            z = classes.Zombi (x/45,y/45,battle, text_data.zombisad.text, control, 10,0,10,1, son, 20)
                            sprite_group.add (z)

                     if col == 'e':
                            e = classes.PortalS (x,y, 'dungeon1', (11,4))
                            sprite_group.add (e)

                     if col == 'w':
                            e = classes.PortalS (x,y, 'dungeon3', (1,4))
                            sprite_group.add (e)

                     if col == 's':
                            s = classes.MinorChest (x,y, 'open', items.scythe )
                            sprite_group.add (s)

                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group

def create_dungeon3 (level, battle, control, son, locationname):

       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "z":
                            z = classes.Zombi (x/45,y/45,battle, text_data.zombisad.text, control, 10,0,10,1, son, 30)
                            sprite_group.add (z)

                     if col == 'e':
                            e = classes.PortalS (x,y, 'dungeon1', (15,4))
                            sprite_group.add (e)

                     if col == 'w':
                            e = classes.PortalS (x,y, 'dungeon3', (1,4))
                            sprite_group.add (e)

                     if col == 's':
                            s = classes.MinorChest (x,y, 'open', items.scythe )
                            sprite_group.add (s)

                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group

# Fuction for the city creation

def create_level_city (level, battle, control, son, locationname):
       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "m":
                            mn = classes.Monk (x/45,y/45,battle, text_data.monk.text, control, 4,5,7,1, son, 100)
                            sprite_group.add (mn)
# exit from temple
                     if col == 'p':
                            pr = classes.PortalS (x,y,'platz', (11,1))
                            sprite_group.add (pr)
#enter into temple
                     if col == 'e':
                            pr = classes.PortalS (x,y,'temple', (10,4))
                            sprite_group.add (pr)

#path to end of the city
                     if col == 'o':
                            pr = classes.PortalS (x,y,'end', (1,4))
                            sprite_group.add (pr)
#from end to platz
                     if col == 'q':
                            pr = classes.PortalS (x,y,'platz', (21,4))
                            sprite_group.add (pr)
#from end to dung
                     if col == 'w':
                            pr = classes.PortalS (x,y, 'dungeon1', (1,4))
                            sprite_group.add (pr)


                     if col == 'g':
                            mn = npc.Monk2 (x/45,y/45,battle, text_data.gilbert_dict.text, control, 4,5,7,1, son, 100)
                            sprite_group.add (mn)

                     if col == 'r':
                            pr = classes.PortalLink (x,y, 'TavernOutdoor', 'TavernInside', 'D', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'y':
                            pr = classes.PortalLink (x,y, 'TavernInside', 'TavernOutdoor', 'U', locationname )
                            sprite_group.add (pr)
                     if col == 'b':
                            b = npc.Barmen (x/45,y/45,battle, text_data.barmen_dict.text, control, 8,5,7,4, son, 80)
                            sprite_group.add (b)
                     if col == '[':
                            ding = classes.Ding (x,y, 'images/tiles/bar.png', 'Барная стойка. На ней стоят разные пойла.')
                            sprite_group.add (ding)
                     if col == 'W':
                            ding = classes.Ding (x,y, 'images/tiles/ind.png', 'На указателе написано: "Таверна"')
                            sprite_group.add (ding)
                     if col == 'Q':
                            ding = classes.Ding (x,y, 'images/tiles/ind.png', 'На указателе написано: "Храм"')
                            sprite_group.add (ding)
                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group



#Функция для создание дверей, стен, стандартных сундуков и свечей - стандартных объектов, не предполагающих настройки
def create_interior_standart (level, grType):

       interior =[]
       walls = []
       ground = []

       x = 0
       y = 0

       for row in level:
              for col in row:
                    if col != '0' and col != '-':
                            ground.append(grType(x,y))
                    x +=45
              x = 0
              for col in row:

                    
                    
                    if col == "-":
                            pf = classes.Platform (x,y)
                            walls.append (pf)

                    if col == "d":
                            door = classes.Door (x,y)
                            interior.append (door)

                    if col == "c":
                            ch = classes.Chest (x,y)
                            interior.append (ch)

                    if col == "t":
                            tr = classes.Candel (x,y)
                            interior.append (tr)
                    if col == "u":
                            t = classes.Table(x,y)
                            interior.append(t)
                    if col == "i":
                            t = classes.Chair(x,y)
                            interior.append(t)


                    x += 45
              x = 0
              y += 45
       x = 0
       y = 0

       return  interior, ground, walls






