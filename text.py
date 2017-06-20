z0 = "Вы видите весёлого зомби, который приплясывыет. Его куски гниющей плоти отваливаются, когда он прыгает с ноги на ногу, полувывалившийся глаз пружинит на глазном нерве, но на лице у зомби остаётся нечеловеческая улыбка, в которой мерцает бездна бесконечности. Что вы сделаете?"

a0 = "1.Поговорить. 2. В бой! 3. Уйти восвояси."

z10 = "Зомби останавливает свой пляс и вопросительно смотрит на вас. 'Да-да, чем я могу вам помочь?'"

z20 = 'Вы достаёте мечь и стремглав бросаетесь на ходячий труп, дабы освободить его от мучений не-жизни.'

z30 = 'Вы разворачиваетесь и уходите. Зомби продолжает плясать.'

a10 = "1. А почему вы пляшете? 2. Как вам живётся?"

z110 = "О, милостливый государь, вы, наверное слышали о таком явлении как 'пляска смерти'? Так вот, последнее время сии мероприятия начинают упрекать в том, что они безвкусны и уже не ввергают зрителей в тот священный трепет, что было раньше. Поэтому я и тренируюсь, чтобы выглядеть достойно, буде мне посчастливиться в ней поучаствовать. "

z210 = "Да как сказать... Я жизнь после смерти на которую я обречён так же неопределённа и бессмысленна, как и жизнь до смерти, которая, я иногда не уверен, что у меня и была. Но ты мне можешь помочь облегчить мою участь! Принеси мне зомби-водки - я напьюсь, немного помечтаю. Мы, зомби, очень сентиментальный народ."

a110 = '(Конец разговора) Нажмите E.'

а210 = '(Конец разговора) Нажмите E.'

zq0 = 'Ты принёс мне то, что я хочу?'

zi0 = 'Зомби пляшет тектоник.'

zi1 = 'Зомби отбивает чечётку'

empty = '(Конец разговора) Нажмите E.'

zia0 = "1. В бой! 2.Уйти."
z1 = 'sdefwe'
z2 = 'ded'
z3 = '21'
z4 = 'dew'

zombitext = {0: (z1, "peace"), 10: (z2, "peace"), 20: (z4, "war"), 110: (z3, "peace")}

zombi1 = [
#0
	{

	0: (z0, "next", a0),
	 10: (z10, "next", a10),
	  20: (z20, "war", empty),
	   30: (z30, "end", empty, ('go', 1)),
	    110 : (z110, 'end', a110,('go', 1)),
	      210: (z210, 'end', а210, ('go', 2))

	      },
#1
    {
    0: (zi0, "end", zia0),
     10: (z20, 'war', empty),
      20: (z30, 'end', empty, ('go', 2))
    },

#2
    {
    0: (zi1, "end", zia0),
     10: (z20, 'war', empty),
      20: (z30, 'end', empty, ('go', 1))
    }
    ]

#SKELET LORD

l0 = 'Большой мосёл, ты ли принёс мне свежей человеченки?'

al0 = '1. Да, это я. 2. Нет.'

l10 = 'Отлично! На 20 золотых монет, которые я тебе должен.'

l20 = 'Тогда я тебя сотру в порошок!'


lord = [{0: (l0, 'next', al0), 10: (l10, 'gold', empty, ('go', 0)), 20:(l20, 'war', empty)}]

#DOOR

d0 = 'Вы стоите перед старой, обветшалой дверью.'
da0 = 'Что вы будете делать? 1 - открыть; 2- уйти прочь.'
d20 = 'Вы ушли.'
d10 = 'Вы открыли дверь'
door = [{0: (d0, 'wait', da0), 10: (d10, 'open', empty), 20: (d20, 'end', empty)}]

#CHEST

c0 = 'Вы видите пыльный сундук.'

aс0 = '1. Открыть. 2. Уйти прочь.'

с10 = 'Отлично! Вы открыли сундук и нашли 10 золотых'

с20 = 'Вы грустно ушли'


chest = [{0: (c0, 'next', aс0), 10: (с10, 'end_chest', empty), 20:(с20, 'end', empty, ('go', 0))}]


# minor chest

c0 = 'Вы видите пыльный сундук.'

aс0 = '1. Открыть. 2. Уйти прочь.'

с10 = 'Отлично! Вы открыли сундук и нашли...'

с20 = 'Вы грустно ушли'


mchest = [
{0: (c0, 'next', aс0), 10: (с10, 'end_chest', empty), 20:(с20, 'end', empty, ('go', 0))}, 

]

#PRIEST

i0 = 'Вы видите сухопарого мужчину в годах, гладко выбритого, с аккуратной тонзурой на макушке. Он облачён в простую черную рясу, подпоясонную вервием, на шее висит, на какой-то бечевке, небольшое распятие. Он внимательно смотрит на вас." Что вы сделаете?'

ai0 = '1. Поговорить. 2. Уйти. 3. Напасть.'

i10 = 'Pax vobiscum, путник! Меня зовут отец Изольд. Я священник церкви Единого. Чем я могу помочь тебе?'
i20 = 'Вы, не выдержав взгляда священника, обуреваемые стыдом, разворачиваетесь и уходите.'
ai10 = '1. Я желаю послужить святой церкви, есть ли у вас какое-то богоугодное дело для человека с мечом и горячим сердцем? 2. Я хотел бы поупражняться в теологических диспутациях. 3. Ничего, святой отец. (Уйти). 4. Я тебя ненавижу, тебя и всю твою церковь. Я хочу пролить твою кровь. (Напасть).'

i110 = '"Вы хотите послужить церкви и Богу?" Отец Изольд окивдывает вас взглядом больших пронзительных глаз. "Если ты действительно хочешь послужить церкви, то есть одно дело. Брат Франциск в библиотеке Араксана нашёл свидетельства, что где-то под руинами этого города сокрыт апокриф, представляющий ценность для истории нашей церкви. Если бы спустился в подземелья под городом, отыскал его и вернул, то сослужил бы хорошую службу. Мать церковь щедра, и она бы тебя щедро возблагодарила.'

i210 = 'Да, конечно, брат Тубус с радостью подиспутирует с тобой. Он как раз занимается вопросом того, возможно ли интуитивное познание несуществующего объекта.'

i310 = 'Что ж, заходи, в любой момент, чадо моё. Мать церковь милостлива и принимает всех, кто приходит к ней с покаянием.'

i410 = 'Вы бросаетесь на бедного священника с мечом.'

ai110 = '1. С радостью помогу вам, отец. Эта миссия будет для священным квестом моей жизни. Никакой награды не надо, кроме краюхи хлеба, чтобы не умереть с голоду и вашего благословления. 2. Ну, возможно. По обстоятельствам, кароче. 3. Нет, спасибо, отче. В подобном не участвую. Всё это очень сомнительно выглядит.'

i1110 = 'Что ж, да благословит тебя Господь в этом нелёгком деле, храбрый паладин!'

i2110 = 'Что ж, если вдруг тебе посчастливиться найти то, о чём я говорил - приходи, и мать-церковь возблагодарит тебя.'

i3110 = 'Отец Изольд грустно качает головой: "Но, как ты тепл, а не горяч и не холоден, то извергну тебя из уст Моих".'


monk = [
#0
  {

  0: (i0, "next", ai0),
  10: (i10, "next", ai10),
    110 : (i110, 'next', ai110),
     1110 : (i1110, 'end', empty),
     2110 : (i2110, 'end', empty),
     3110 : (i3110, 'end', empty),
    210: (i210, 'end', empty),
    310: (i310, 'end', empty),
    410: (i410, 'war', empty),    
  20: (i20, "end", empty),
  30: (i410, 'war', empty) 

    }

    ]

#Zomb_peasant

zp0 = 'Вы видите грустного одинокого зомби, который жалобно смотрит на вас. Или не на вас - это сложно понять, так как оба его глаза отсутствуют: там где должны быть глазные яблоки у него две ужасных ямы. Однако, кажется, он прекрасно вас чувствует и знает о том, что вы рядом. '

azp0 = 'Что вы сделаете? 1 - поговорить; 2 - напасть; 3 - уйти'

zp10 = '"Приветствую тебя, путник...", зомби жалостливо хрипит выплёвывая свои слова полусгнившими лёгкими'

azp10 = '1 - привет и тебе, зомбяра, как жизнь? 2 - почему ты такой грустный? 3 - не мог бы ты отойти в сторону и дать мне пройти?'

zp110 = '"Очень смешно...", зомби выглядит немного уязвлённо. "Сложно назвать моё тепершнее состояние жизнь. Я, скорее существую. Как камень, или гнилое бревно. Всё, что мне осталось - это постоянное разложение. Гниение - моя судьба, то, на что я обречён. А ведь когда-то я был человеком, радовался жизни, солнцу и свету, чистой воде и вкусному хлебу".'

zp210 = 'Вообще, точно не знаю. Сейчас, когда я мёртв у меня вроде бы и нет поводов грустить - всё уже прошло, а что-то меня словно бы терзает.'

zp310 = 'Я бы с радостью, если бы она у меня была. Но, к сожалению, у меня её нет. Я не могу, у меня нет интереса это делать. Мне совершенно всё безразлично.'

azp110 = '1 - был человеком да сплыл. Сплыл по Стиксу. Так что не парься. Все умирают. 2 - догнивай свой век, желательно побыстрей в каком-нибудь углу. А ну прочь с дороги.'

azp210 = '1 - как тебя зовут? 2 - не мог бы ты отойти с дороги, а то ты мешаешь мне пройти.'

azp310 = '1 - может быть я как-то могу помочь вернуть тебе чувства, чтобы ты нашел в себе силы сдвинуться с места? 2 - тогда мне придётся тебя убить.'

zp1110 = 'О, я не парюсь, мне глубоко всё равно. У меня нет чувств - я всего лишь бесчувственное гнилое бревно лежащее на дороге. Меня даже немного расстраивает то, что ты мог подумать, что я могу быть чем-то обеспокоен.'

zp2110 = 'Нет, с дороги я не уйду. Не хочу. Как впрочем и с тобой разговаривать у меня нет ныне тоже никакого желания.'

zp1210 = 'Зомби задумался: "Да... я, кажется, помню. Меня зовут... Г... Г... Гггг..."'

zp2210 = 'Да, я думаю, что ты мог бы мне помочь, если бы нашёл бы какую-то вещь, которая имела для меня значение. Тогда, возможно, я бы что-то и вспомнил.'

zp1310 = zp2210

zp2310 = 'Что ж, попробуй. Думаю, если ты "убьёшь" меня, хоть это уже само по себе и звучит как нонсенс, то я буду тебе "благодарен", если бы чувство благодарности я мог бы испытывать'

azp1110 = '1 - ясно'

azp2110 = '1 - уйти; 2 - тогда ты труп! (напасть)'

azp1210 = '1 - Ганс? 2 - Герхардс? 3 - Гоблинсон?'

azp2210 = '1 - что ж, я думаю это возможно; 2 - лучше я расправлюсь с тобой, чем буду вступать сделку с нечтой силой.'

zp20 = 'Вы ушли'
zp30 = 'Вы атакуете'

zombipeasant = [

{

 0: (zp0, 'next', azp0),
  10: (zp10, "next", azp10),
    110 : (zp110, 'next', azp110),
     1110 : (zp1110, 'end', azp1110),
     2110 : (zp2110, 'end', azp2110),
 #    3110 : (zp3110, 'end', empty),
    210: (zp210, 'next', azp210),
     1210 : (zp1210, 'end', azp1210),
     2210 : (zp2210, 'end', azp2210),
    310: (zp310, 'next', azp310),
     1310 : (zp1310, 'end', empty),
     2310 : (zp2310, 'end', empty),    
  20: (zp20, "end", empty),
  30: (zp30, 'war', empty) 
}
]
