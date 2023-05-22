def quarter_of(month):
  if month < 4: return "первого квартала"
  if 3 < month < 7 : return "второго квартала"
  if 6 < month < 10 : return "третьего квартала"
  else :
    return "четвертого квартала"
for i in range(1, 13): print(f'Месяц {i} является частью {quarter_of(i)}')
