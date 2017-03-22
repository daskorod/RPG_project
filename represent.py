class Son ():
	'''render text information'''

	def __init__ (self):
		self.b1 = self.b2 = self.b3 = self.b4 = self.b5 = self.b6 = self.b7 = ''
		self.strokelist = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7]

	def render_text (self):
		n = 0
		for i in self.strokelist:
			information_screen.blit(fonts.font2.render (str(i), True, (250,250,250)),(2,22*n))
			n += 1

	def change_text (self, n, a):
		self.strokelist[n+1] = str(a)

	def clear_text (self):
		for i in range len(self.strokelist):
			self.strokelist[i] = ''