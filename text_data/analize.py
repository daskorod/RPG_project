from extractor import compose
import sys
''' Текстовый файл для анализа должен быть в кодировке ANSI почему-то я не знаю почему. Если он в utf-8, то в сохранённом словер появляются кракозябры'''

filename = str(sys.argv[1])

def exwr (filename):
  
  a = compose(str(filename)+'.txt')

  outfile = open (str(filename)+'_dict'+'.py', 'w',encoding="utf-8")

  str_to_write = 'text=' + str(a)

  outfile.write(str_to_write)

exwr(filename)

print ('text structure compile success!')
