a="FCU"
txt=list(("NTU","NCHU","FCU","NCKU","FCU","FCU"))
t=0 ;b=0
while a in txt[b:]:
    t+=1
    if txt[b:].index(a)==len(txt)-1:
        break
    b=txt[b:].index(a)+1
print(t)