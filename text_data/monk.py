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

empty = '(Конец разговора)'
text = [
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
