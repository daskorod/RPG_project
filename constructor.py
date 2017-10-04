import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text
import items
import npc
import monster
import text_data.zombisad,text_data.guard_dict, text_data.zombi_lord_dict, text_data.monk, text_data.gilbert_dict,text_data.barmen_dict, text_data.skeletonw_dict, text_data.skelet_lord2_dict, text_data.corpse_dict,text_data.skeleton_king_dict, text_data.martin_dict, text_data.rouge_dict, text_data.august_dict, text_data.guard2_dict
import img
import functions

stuff = []
addition = []

def create_dungeon1 (level, battle, control, son, locationname):

       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "z":
                            z = classes.Zombi (x/45,y/45,battle, text_data.zombisad.text, control, 10,0,10,1, son,20, item = items.hp_potion)
                            sprite_group.add (z)

#                    if col == 'e':
#                           e = classes.PortalS (x,y, 'end', (15,4))
#                           sprite_group.add (e)

                     if col == 'w':

                            pr = classes.PortalLink (x,y, 'dung1fromdung2', 'dung2fromdung1', 'L', locationname )
                            sprite_group.add (pr)

                     if col == 'e':
                            pr = classes.PortalLink (x,y, 'oldhousefromdung', 'todung1', 'U', locationname )
                            sprite_group.add (pr)

                     if col == 's':
                            s = classes.MinorChest2 (x,y, 'open', items.garbage )
                            sprite_group.add (s)
                     if col == 'O':
                            well = classes.Obstacle(x,y, img.obstacles)  
                            sprite_group.add (well)

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

                            pr = classes.PortalLink (x,y, 'dung2fromdung1', 'dung1fromdung2', 'R', locationname )
                            sprite_group.add (pr)
                     if col == 'w':
                            e = classes.PortalS (x,y, 'dungeon3', (1,4))
                            sprite_group.add (e)

                     if col == 's':
                            s = classes.MinorChest (x,y, 'open', items.scythe )
                            sprite_group.add (s)
                     if col == 'a':
                            a = classes.Skelet ((x/45)+(20/45),y/45,battle, text_data.skeletonw_dict.text, control, 10,8,30,3, son, 120)
                            sprite_group.add (a)
                     if col == 'Q':
                            s = classes.MinorChest (x,y, 'open', items.hp_potion )
                            sprite_group.add (s)
                     if col == 'W':
                            s = classes.Trap (x,y)
                            sprite_group.add (s)  
                     if col == 'E':
                            cupboard = classes.Cupboard(x,y)  
                            sprite_group.add (cupboard)                 
                     if col == 'R':
                            well = classes.Well(x,y)  
                            sprite_group.add (well)
                     if col == 'T':
                            well = monster.SkeletLord(x/45,y/45,battle, text_data.skelet_lord2_dict.text, control, 6,5,6,2, son, 150)  
                            sprite_group.add (well)
                     if col == 'Y':
                            pr = classes.PortalLink (x,y, 'dung3', 'dung2', 'D', locationname )
                            sprite_group.add (pr)
                     if col == 'U':
                            pr = classes.GoldDoor (x,y)
                            sprite_group.add (pr)
                            dec = classes.Ding(x,y, 'images/tiles/door_open.png', 'Открытая дверь')
                            addition.append(dec)
                     if col == 'I':
                            well = monster.ZombiLord(x/45,y/45,battle, text_data.zombi_lord_dict.text, control, 15,5,16,4, son, 250)  
                            sprite_group.add (well)      
                     if col == 'O':
                            well = classes.Obstacle(x,y, img.obstacles)  
                            sprite_group.add (well)
                     if col == 'P':
                            cupboard = classes.Cupboard2(x,y)  
                            sprite_group.add (cupboard)
                     if col == 'A':
                            s = classes.MinorChest (x,y, 'open', items.old_axe )
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
                     if col == 'Q':
                            pr = classes.PortalLink (x,y, 'dung2', 'dung3', 'U', locationname )
                            sprite_group.add (pr)
                     if col == 'T':
                            pr = monster.SkeletKing (x/45,y/45, battle, text_data.skeleton_king_dict.text, control, 12, 8, 15, 4, son, 100)
                            sprite_group.add (pr)
                     if col == 'S':
                            pr = classes.DingSpecial (x,y, img.kubert, text_data.corpse_dict.text, functions.dialog_special, functions.interaction_special)
                            sprite_group.add (pr)
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

#enter into temple

                     if col == 'p':
                            pr = classes.PortalLink (x,y, 'platzfromtemle', 'intemplefromlpatz', 'U', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'e':
                            pr = classes.PortalLink (x,y, 'intemplefromlpatz', 'platzfromtemle', 'D', locationname )
                            sprite_group.add (pr)
                            stuff.append (pr)
#path to end of the city
                     if col == 'o':
                            pr = classes.PortalS (x,y,'end', (1,4))
                            sprite_group.add (pr)
#from end to platz
                     if col == 'q':
                            pr = classes.PortalS (x,y,'platz', (21,4))
                            sprite_group.add (pr)
#from end to dung
#                    if col == 'w':
#                           pr = classes.PortalS (x,y, 'dungeon1', (1,4))
#                           sprite_group.add (pr)

                     if col == 'w':
                            pr = classes.PortalLink (x,y, 'HoldHouseToEnd', 'OldHouseFromEnd', 'D', locationname )
                            sprite_group.add (pr)
                            stuff.append (pr)
                            


                     if col == 'g':
                            mn = npc.Gilbert (x/45,y/45,battle, text_data.gilbert_dict.text, control, 4,5,7,1, son, 100)
                            sprite_group.add (mn)

                     if col == 'r':
                            pr = classes.PortalLink (x,y, 'TavernOutdoor', 'TavernInside', 'D', locationname )
                            sprite_group.add (pr)
                            stuff.append (pr)
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
                     if col == 'E':
                            ding = classes.Ding (x,y, 'images/tiles/cross.png', 'Молчаливый каменный крест. Внушает страх Божий.')
                            sprite_group.add (ding)
                     if col == 'R':
                            ding = classes.Ding (x,y, 'images/tiles/pilar.png', 'Монументальная колонна, поддерживающая потолок.')
                            sprite_group.add (ding)
                            
                     if col == 'T':
                            pr = classes.PortalLink (x,y, 'End', 'Platz', 'L', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'Y':
                            pr = classes.PortalLink (x,y, 'Platz', 'End', 'R', locationname )
                            sprite_group.add (pr)
                     if col == 'O':
                            well = classes.Obstacle(x,y, img.obstacles)  
                            sprite_group.add (well)

                     if col == 'P':
                            pr = classes.PortalLink (x,y, 'TempleFromCell', 'TempleInCell', 'D', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'A':
                            pr = classes.PortalLink (x,y, 'TempleInCell', 'TempleFromCell', 'U', locationname )
                            sprite_group.add (pr)                           

                     if col == 'S':
                            mn = npc.Martin (x/45,y/45,battle, text_data.martin_dict.text, control, 4,5,7,1, son, 100)
                            sprite_group.add (mn)
                     if col == 'D':
                            pr = classes.PortalLink (x,y, 'PlatzFromStill', 'PlatzToStill', 'U', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'F':
                            pr = classes.PortalLink (x,y, 'PlatzToStill', 'PlatzFromStill', 'D', locationname )
                            sprite_group.add (pr)                           

                     if col == 'G':
                            mn = npc.Rouge (x/45,y/45,battle, text_data.rouge_dict.text, control, 6,9,4,1, son, 30)
                            sprite_group.add (mn)

                     if col == 'H':
                            pr = classes.PortalLink (x,y, 'PlatzFromTower', 'PlatzToTower', 'R', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'J':
                            pr = classes.PortalLink (x,y, 'PlatzToTower', 'PlatzFromTower', 'L', locationname )
                            sprite_group.add (pr)  

                     if col == 'K':
                            pr = classes.PortalLink (x,y, 'Tower1', 'TowerOut', 'U', locationname )
                            sprite_group.add (pr)
                            
                     if col == 'L':
                            pr = classes.PortalLink (x,y, 'TowerOut', 'Tower1', 'D', locationname )
                            sprite_group.add (pr)  
                            stuff.append(pr)   
                     if col == 'Z':
                            pr = npc.Augustine (x/45,y/45,battle, text_data.august_dict.text, control, 6,5,8,2, son, 130)
                            sprite_group.add (pr)  
                     if col == 'X':
                            pr = classes.PortalLink (x,y, 'OldHouseFromEnd', 'HoldHouseToEnd', 'U', locationname )
                            sprite_group.add (pr)

                     if col == 'C':
                            pr = classes.PortalLink (x,y, 'todung1', 'oldhousefromdung', 'D', locationname )
                            sprite_group.add (pr)
                     if col == 'V':
                            mn = npc.Guard (x/45,y/45,battle, text_data.guard_dict.text, control, 7,6,6,2, son, 50)
                            sprite_group.add (mn)
                     if col == 'B':
                            mn = npc.Guard2 (x/45,y/45,battle, text_data.guard2_dict.text, control, 7,6,6,2, son, 50)
                            sprite_group.add (mn)   
                     if col == 'N':
                            pr = classes.PortalLink (x,y, 'towerplatz', 'still2', 'U', locationname )
                            sprite_group.add (pr) 
                     if col == 'M':
                            pr = classes.PortalLink (x,y, 'park1', 'still1', 'R', locationname )
                            sprite_group.add (pr)                           
                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group

def create_level_city2 (level, battle, control, son, locationname):
       sprite_group = sprite.Group ()

       x = 0
       y = 0

       for row in level:

              for col in row:
                           
                     if col == "m":
                            mn = classes.Monk (x/45,y/45,battle, text_data.monk.text, control, 4,5,7,1, son, 100)
                            sprite_group.add (mn)
                     if col == 'Q':
                            ding = classes.Ding2 (x,y, 'images/tiles/wood2.png', 'Красивое и мощное дерево.')
                            sprite_group.add (ding)
                     if col == 'W':
                            pr = classes.PortalLink (x,y, 'still2', 'towerplatz', 'D', locationname )
                            sprite_group.add (pr)  
                     if col == 'O':
                            well = classes.Obstacle(x,y, img.obstacles)  
                            sprite_group.add (well)
                     if col == 'E':
                            pr = classes.PortalLink (x,y, 'park', 'strange', 'U', locationname )
                            sprite_group.add (pr)  
                     if col == 'R':
                            pr = classes.PortalLink (x,y, 'strange', 'park', 'D', locationname )
                            sprite_group.add (pr)
                     if col == 'T':
                            pr = classes.PortalLink (x,y, 'still1', 'park1', 'L', locationname )
                            sprite_group.add (pr)                                
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
       decor = []

       x = 0
       y = 0

       for row in level:
              for col in row:
                    if col != '0' and col != '-' and col != '!' and col != '@' and col != '#'  and col != '$' and col != '%':
                            ground.append(grType(x,y))
                    if col == '!':
                            decor.append(classes.Ding(x,y, 'images/tiles/house.png', 'таверна'))
                    if col == '@':
                            decor.append(classes.Ding(x,y, 'images/tiles/temple3.png', 'храм'))
                    if col == '#':
                            decor.append(classes.Ding(x,y, 'images/tiles/old_house.png', 'старый дом'))
                    if col == '$':
                            decor.append(classes.Ding(x,y, 'images/tiles/t_house2.png', 'дом воров'))
                    if col == '%':
                            decor.append(classes.Ding(x,y, 'images/tiles/tower7.png', 'башня'))
                    if col == 'C':
                            ding = classes.Ding2 (x,y, 'images/tiles/pit.png', 'Яма')
                    if col == '^':
                            decor.append(classes.Ding2(x,y, 'images/tiles/str_house.png', 'Странный дом'))                          
                            #ground.append(ding)
                    x +=45
              x = 0
              for col in row:
                    if col == "+":
                            pf = classes.PlatformBlack (x,y)
                            interior.append (pf)
                    
                    
                    if col == "-":
                            pf = classes.Platform (x,y)
                            walls.append (pf)
                    if col == "=":
                            pf = classes.Nothing (x,y)
                            interior.append (pf)
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

       return  interior, ground, walls, decor



def create_level_tavern (level, battle, control, son, locationname):
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
                            mn = npc.Gilbert (x/45,y/45,battle, text_data.gilbert_dict.text, control, 4,5,7,1, son, 100)
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
                     if col == 'E':
                            ding = classes.Ding (x,y, 'images/tiles/cross.png', 'Молчаливый каменный крест. Внушает страх Божий.')
                            sprite_group.add (ding)

                     if col == 'R':
                            ding = classes.Ding (x,y, 'images/tiles/pilar.png', 'Монументальная колонна, поддерживающая потолок.')
                            sprite_group.add (ding)

                     x += 45
              x = 0
              y += 45
       x = 0
       y = 0
       return sprite_group



def create_interior_tavern (level, grType):

       interior =[]
       walls = []
       ground = []
       decor = []

       x = 0
       y = 0

       for row in level:
              for col in row:
                    if col != '0' and col != '-' and col != '1' and col != '2' and col != '3' and col != '4' and col != '5' and col != '6' and col != '7' and col != '8' and col != '9'  and col != '!' and col != '@' and col != '#' and col != '$'  :
                            ground.append(classes.WoodFloor(x,y))
                    x +=45
              x = 0
              for col in row:

                    
                    
                    if col == "1":
                            pf = classes.TavernWall (x,y, 0)
                            walls.append (pf)
                    if col == "0":
                            pf = classes.PlatformBlack (x,y)
                            walls.append (pf)
                    if col == "2":
                            pf = classes.TavernWall (x,y, 1)
                            walls.append (pf)

                    if col == "3":
                            pf = classes.TavernWall (x,y,2)

                            walls.append (pf)

                    if col == "4":
                            pf = classes.TavernWall (x,y, 3)
                            walls.append (pf)

                    if col == "5":
                            pf = classes.TavernWall (x,y, 4)
                            walls.append (pf)

                    if col == "6":
                            pf = classes.TavernWall (x,y,5)
                            walls.append (pf)
                    if col == "7":
                            pf = classes.TavernWall (x,y,6)
                            walls.append (pf)

                    if col == "8":
                            pf = classes.TavernWall (x,y,7)
                            walls.append (pf)
                    if col == "9":
                            pf = classes.TavernWall (x,y,8)
                            walls.append (pf)

                    if col == "!":
                            pf = classes.TavernWall (x,y,9)
                            walls.append (pf)
                    if col == "@":
                            pf = classes.TavernWall (x,y,10)
                            walls.append (pf)
                    if col == "#":
                            pf = classes.TavernWall (x,y,11)
                            walls.append (pf)
                    if col == "$":
                            pf = classes.TavernWall (x,y,12)
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

       return  interior, ground, walls, decor
