from kandinsky import *
color1=(0,0,0)
color0=(255,255,255)
try:
  color1=get_palette()['Toolbar']
  color0=get_palette()['AccentText']
except NameError:
  pass

fill_rect(0,0,320,222,color1)
with open("qrcodedata.py", "r") as f:
  content = f.read()
  content = content.split("\n")
  sizecorrector = int(222/len(content))
  x=int(320/2/sizecorrector-(len(content)/2))
  y=int(222/2/sizecorrector-(len(content)/2))-int(18/2/sizecorrector)
  y = max(y, 0)
  for lineitem, linecontent in enumerate(content):
      lineitem+=x
      linenotvalid=0
      for item, value in enumerate(linecontent):
          item+=y
          if value == "0":
              fill_rect(lineitem*sizecorrector,(item-linenotvalid)*sizecorrector,sizecorrector,sizecorrector,color0)
          elif value == "1":
              fill_rect(lineitem*sizecorrector,(item-linenotvalid)*sizecorrector,sizecorrector,sizecorrector,color1)
          else:
              print(value, "not valid !")
              linenotvalid += 1
