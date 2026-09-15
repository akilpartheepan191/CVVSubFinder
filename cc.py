def chart(absentees):
  from mainsub import substitutioner as subber
  import openpyxl as xl
  from pdffer import convert_excel_to_pdf as etp
  from date import get_current_indian_date as dater
  day='mon'
  the_guys=subber(absentees,day)
  peds = {
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
  }
  file=xl.load_workbook('sampl1.xlsx')
  sheet = file['Sheet1']
  cnt=2
  for x in the_guys.keys():
    sheet[f'A{cnt}'].value = x
    for y in the_guys[x]:
      if type(the_guys[x][y])==list:
        sheet[f'{peds[y]}{cnt}'].value = f'{the_guys[x][y][0]} - {the_guys[x][y][1]}'
      else:
        sheet[f'{peds[y]}{cnt}'].value = 'No teacher is available!'
    cnt+=1
  file.save('sampl2.xlsx')
  
  etp('sampl2.xlsx','out.pdf',f'Substitution chart for {str(dater())}',5)