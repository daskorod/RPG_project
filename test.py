z1 = "Вы видите весёлого зомби, который приплясывыет. Что вы сделеете? 1 - поговорите с ним; 2 - будете атаковать."

z2 = "Вы заводите с зомби пространную беседу о сущности инобытия..."

z3 = "[11] Sed extende paululum manum tuam et tange cuncta quae possidet, nisi in faciem benedixerit tibi. [12] Dixit ergo Dominus ad Satan: Ecce universa quae habet in manu tua sunt; tantum in eum ne extendas manum tuam. Egressusque est Satan a facie Domini. [13] Cum autem quadam die filii et filiae ejus comederent et biberent vinum in domo fratris sui primogeniti, [14] nuntius venit ad Job, qui diceret: Boves arabant, et asinae pascebantur juxta eos; [15] et irruerunt Sabaei, tuleruntque omnia, et pueros percusserunt gladio; et evasi ego solus, ut nuntiarem tibi."

z4 = "бой!"

z5 = ' '
zombitext = {0: (z1, "peace"), 10: (z2, "peace"), 20: (z4, "war"), 110: (z3, "peace")}

zombi1 = {0: (z1, "peace"), 10: (z2, "peace"), 20: (z4, "war"), 110: (z3, "peace")}


if 0 in zombi1:
	print (zombi1[0])


z4 = "123"*10 + z4 + '1'*10 + z1

print (z4) 

a = 130
b = 50

c = 130 % 50

print ('/n/n/n' + str (c) +' /n')