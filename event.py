
import ideas
import text_data.final_dict, text_data.inception_dict, text_data.old_book_dict

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