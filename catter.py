def categorise(pe):
  pe=pe.lower()
  authed=['i','v','x']
  cats={
    1:['i','ii','iii','iv','v'],
    2:['vi','vii','viii'],
    3:['ix','x','xi','xii']
  }
  clen=''
  for i in pe:
    if i in authed:  
      clen=clen+i
    else:
      break
  for x in cats.keys():
    if clen in cats[x]:
      return x

def catcon(p,t):
  if p==t:
    return True
  else:
    if p==1 and t==4:
      return True
    if p==2 and t==4:
      return True
    if p==3 and t==5:
      return True
    if p==2 and t==5:
      return True
    else:
      return False