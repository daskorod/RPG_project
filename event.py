import text_data.final_dict

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

		if self.add_information == 'war' and hero.control.k_e == True:
			self.son.clear_text ()
			hero.control.k_e = False
			self.agression = True
			hero.turn_main = True
			hero.start_conv = True
			hero.view.a = 0

#			a = random.randint (1,6)
			self.branch_do = 'done'
			self.s = 1
			self.n = 0
			self.branch = self.branch_id
#			if a >3:
#				self.branch = 1
#			if a <=3:
#				self.branch = 2

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


	def dialog_special (self, hero):
		pass


final = Event(text_data.final_dict.text)