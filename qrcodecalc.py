from kandinsky import *
sizecorrector = 3
with open("qrcodedata.py", "r") as f:
    content = f.read()
    content = content.split("\n")
    sizecorrector = int(222/len(content))
    for lineitem, linecontent in enumerate(content):
        linenotvalid=0
        for item, value in enumerate(linecontent):
            if value == "0":
                fill_rect(lineitem*sizecorrector,(item-linenotvalid)*sizecorrector,sizecorrector,sizecorrector,(0,0,0))
            elif value == "1":
                fill_rect(lineitem*sizecorrector,(item-linenotvalid)*sizecorrector,sizecorrector,sizecorrector,(255,255,255))
            else:
                print(value, "not valid !")
                linenotvalid += 1
