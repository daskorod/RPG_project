# -*- coding: utf-8 -*-
z1 = "Вы видите весёлого зомби, который приплясывыет. Что вы сделеете? 1 - поговорите с ним; 2 - будете атаковать. О, милостливый государь, вы, наверное слышали о таком явлении как 'пляска смерти'? Так вот, последнее время сии мероприятия начинают упрекать в том, что они бесвкусны и уже не ввергают зрителей в тот священный трепет, что было раньше. Поэтому я и тренируюсь, чтобы выглядеть достойно, буде мне посчастливиться в ней поучаствовать."

z2 = "Вы заводите с зомби пространную беседу о сущности инобытия..."

z3 = "[11] Sed extende paululum manum tuam et tange cuncta quae possidet, nisi in faciem benedixerit tibi. [12] Dixit ergo Dominus ad Satan: Ecce universa quae habet in manu tua sunt; tantum in eum ne extendas manum tuam. Egressusque est Satan a facie Domini. [13] Cum autem quadam die filii et filiae ejus comederent et biberent vinum in domo fratris sui primogeniti, [14] nuntius venit ad Job, qui diceret: Boves arabant, et asinae pascebantur juxta eos; [15] et irruerunt Sabaei, tuleruntque omnia, et pueros percusserunt gladio; et evasi ego solus, ut nuntiarem tibi."



def textor (text):
	text_splitted = text.split (" ")
	rec = []
	s = " "
	for i in text_splitted:
		if len(s + i) < 50:
			s = s + " " +  i
			continue
		rec.append (s)
		s = " " + i
	rec.append (s)

	return rec






for i in textor (z1):
	print (i)


print (len(textor(z1)))





def textus (text, page):

	text_splitted = text.split (" ")
	s1 = ''
	s2 = ''
	s3 = ''
	s4 = ''
	s5 = ''
	s6 = ''
	s7 = ""
	s1_fil = True
	s2_fil = False
	s3_fil = False
	s4_fil = False
	s5_fil = False
	s6_fil = False
	s7_fil = False



	for i in text_splitted:


		if len(s7 +i) <=50 and s7_fil == True:
			s7 = s7 + " " + i
		if len(s7 +i) >50 and s7_fil == True:
			s7_fil = False

		if len(s6 +i) <=50 and s6_fil == True:
			s6 = s6 + " " + i
		if len(s6 +i) >50 and s6_fil == True:
			s6_fil = False
			s7_fil = True	

		if len(s5 +i) <=50 and s5_fil == True:
			s5 = s5 + " " + i
		if len(s5 +i) >50 and s5_fil == True:
			s5_fil = False
			s6_fil = True

		if len(s4 +i) <=50 and s4_fil == True:
			s4 = s4 + " " + i
		if len(s4 +i) >50 and s4_fil == True:
			s4_fil = False
			s5_fil = True	

		if len(s3 +i) <=50 and s3_fil == True:
			s3 = s3 + " " + i
		if len(s3 +i) >50 and s3_fil == True:
			s3_fil = False
			s4_fil = True	

		if len(s2 +i) <=50 and s2_fil == True:
			s2 = s2 + " " + i
		if len(s2 +i) >50 and s2_fil == True:
			s2_fil = False
			s3_fil = True	

		if len(s1 +i) <=50 and s1_fil == True:
			s1 = s1 + " " + i
		if len(s1 +i) >50 and s1_fil == True:
			s1_fil = False
			s2_fil = True

	return s1, s2, s3, s4,s5,s6,s7


b = textus (z1)

for i in b:
	print (i)#