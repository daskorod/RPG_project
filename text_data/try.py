from extractor import compose


def exwr (filename):
	
	a = compose(str(filename))

	outfile = open (str(filename)+'_dict'+'.py', 'w')

	str_to_write = 'text=' + str(a)

	outfile.write(str_to_write)

exwr('gil.txt')

print ('text structure compile success!')
