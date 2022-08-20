import numpy as np
import pandas as pd
geo =  []
li =[]
for i in open('data.txt', errors="ignore"):
    if (i.split(":"))[0]=="Geo-coordinates":
        geo.append(i.split(":")[1].strip('\n'))

# we are taking geo coordinates as the base for the no. of the values
parti=[None]*len(geo)
prog = [None]*len(geo)
coll=[None]*len(geo)
#Now dividing the data according to the geo coordinates
l=[]
b=[]
f = open('data.txt',"r", errors="ignore")
d= f.readlines()
for i in d:
    if "Geo-coordinates" in i:
        b.append(l)
        l=[]
        continue
    else:
        l.append(i) 
#b contains divided data wrt the geo coordinates
lis=[]
j=[]
for line in b:
     for i in line:
       lis.append((i.split(":")))
     j.append(lis)
     lis=[] 
for ik in range(len(j)):
    for i in j[ik]:
        if i[0]=="Total Participants":
             parti[ik]=(int(i[1].strip('\n')))
        if i[0]=="Type of programme":
              prog[ik]=(i[1].strip('\n'))
        if i[0]=="College/University":
            coll[ik]=(i[1].strip('\n'))
        
data = {"Geo-coordinates":geo, "Total Participants":parti,"Type of programme":prog,"College/University":coll}
df = pd.DataFrame(data = data)
print(df)