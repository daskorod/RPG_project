''' Текстовый файл для анализа должен быть в кодировке ANSI почему-то я не знаю почему. Если он в utf-8, то в сохранённом словаре появляются кракозябры'''


def compose (filename):
  a = open (filename)
  
  generalls = []
  textbar = []
  
  empty = 'Нажмите E'
  end = 'Взаимодействие завершено (можете идти)'
  branch = 0
  
  for i in a:
    if i == '\n':
      continue
  
    if i.strip().isdigit() == True:
      generalls.append ({})
      number = int(i.strip())
      continue
  
  
    ls = i.split('=')
  
    tech_str = ls[0].strip()
    value = ls[1].strip()
  
    if ',' in tech_str:
      tech_ls = tech_str.split(',')
      if len(tech_ls) > 1:
        key_str = tech_ls[0].strip()
        add_information_str = tech_ls[1].strip()
        value = value, add_information_str
        if len(tech_ls) == 3:
          branch_change_inf = tech_ls[2].strip()
          value = value, ('go', int(branch_change_inf))
  
  
    else:
      if tech_str.startswith('a') == False :
        add_information_str = 'next'
        key_str = tech_str
        value = value, add_information_str
      else:
        key_str = tech_str
  
    generalls[number][key_str] = value
  
  
  for branch_number in range(len(generalls))  :
    textbar.append({})
  
    for key in sorted(generalls[branch_number].keys()):
      if key.startswith('a') == True:
        continue
      digit_key = int(key)
  
      value, add_information = generalls[branch_number][key]

      try:
        answer_key = 'a'+key
        answer = generalls[branch_number][answer_key]
      except:
        answer = empty
      if len(generalls[branch_number][key][1]) == 2:
        value1, value2 = value
        if value2 == 'end':
          answer = end
        textbar[branch_number][digit_key] = (value1, value2, answer, add_information)
      else:
        if add_information == 'end':
          answer = end
        textbar[branch_number][digit_key] = (value, add_information, answer)
        
  
      value, add_information = generalls[branch_number][key]

  return textbar

