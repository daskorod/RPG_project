a = open ('zlk.txt')

dict1 = {}
dict2 = {}

empty = 'NO'

for i in a:
  if i == '\n':
    continue
  print(i)
  ls = i.split('=')
  print(ls)
  string = ls[0].strip()
  value = ls[1].strip()
  dict1[string] = value

#print (dict1)
for key in sorted(dict1.keys()):
  if key.startswith('a') == True:
    continue
  digit_key = int(key)
  value = dict1[key]
  try:
    answer_key = 'a'+key
    answer = dict1[answer_key]
  except:
    answer = empty
  dict2[digit_key] = (value, 'next', answer)

outfile = open ('qwert.txt', 'w')
outfile.write('text='+str(dict2))
