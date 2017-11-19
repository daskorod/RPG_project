
import ideas
import img
import text_data.final_dict, text_data.inception_dict, text_data.old_book_dict
import menu

class Event ():
	def __init__ (self, text):

		self.tree = text
		self.n = 0
		self.s = 1
		self.add_information = "none"
		self.agression = False
		self.branch = 0
		self.branch_do = ''
		self.branch_id = ''

	def dialog_options (self,hero):
		self.dialog_special (hero)

		if self.add_information == 'end':

			hero.move = True
			hero.control.k_e = False
			hero.collide_control = False
			hero.start_conv = True
			hero.view.a = 0

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0


		if self.add_information == 'passage' and hero.control.k_e == True:


			hero.control.k_e = False


			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

		if self.add_information == 'go':
			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0

		if self.add_information == 'dogma':
			menu.ending ('Вы выполнили священный квест. Вы разыскали Пречистые Догмы, чтобы раз и навссегда сокрушить еретиков. Церковь восторжествует. Вот только вас будет продолжать грызть червь сомнения, до тех пор пока вы не умрёте в очередной войне.', img.dogma_end, 5, pic_x = 100, time_scroll = 250, speed_mod = 3)

		if self.add_information == 'gnosis':
			menu.ending ('Вы со всеми потрохами вступили в гностическую общину. Вы так никогда и не достигли в ней каких-то значимых высот. В то время как иерархи общины предавались наслаждениям, вам было предписано соблюдать жесткую аскезу. В итоге вас нашла инквизиция с сожгла на костре.', img.gnosis_end, 6, pic_x = 60, time_scroll = 250, speed_mod = 6)

		if self.add_information == 'true':
			menu.ending ('Вы вернули людям настоящие Пречистые Догмы. Это вызвало огромный скандал внутри Империи. Вы попытались уйти в тень, что вам удалось. До конца своих дней вы продолжали карьеру странствующего рыцаря, пока смерть не настигла вас.', img.true_end, 7, pic_x = 60, time_scroll = 50, speed_mod = 6)

		if self.add_information == 'concept' and hero.control.k_e == True:
			hero.move = True
			x = 0
			for i in hero.journal:
				if i.name == 'Символ Веры':
					hero.journal[x] = ideas.gnosis
					break
				x +=1


			hero.control.k_e = False

			hero.son.clear_text ()
			hero.son.change_text (2, 'Вы приобрели знание.')
			hero.son.change_text (3, 'Теперь вы по-другому будете относиться миру.')
			hero.son.change_text (4, 'Теперь вы чувствуете себя особенным.')
			hero.son.change_text (5, 'Вместе с этим вы ощущаете, что Святой Дух вас оставил.')
			hero.son.change_text (6, 'Вы вычёркиваете Символ Веры из своего дневника.')

			if self.branch_do == 'go':
				self.branch_do = 'done'
				self.branch = self.branch_id
				self.s = 1
				self.n = 0
			hero.collide_control = False
			hero.start_conv = True

	def dialog_special (self, hero):
		pass


final = Event(text_data.final_dict.text)
inception = Event(text_data.inception_dict.text)
old_book = Event(text_data.old_book_dict.text)