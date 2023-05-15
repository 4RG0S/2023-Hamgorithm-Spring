x=[0]*20
for k in range(20):
    x[k]=input()
y=[[1]*4 for h in range(20)]
for q in range(20):
    y[q]=x[q].split()
o=0
for z in range(20):
    y[z][1]=float(y[z][1])
sum1=0
for g in range(20):
    if(y[g][2]=="P"):
        continue
    sum1+=y[g][1]
for t in range(20):
    if(y[t][2]=="A+"):
        y[t][2]=4.5
    elif(y[t][2]=="A0"):
        y[t][2]=4.0
    elif(y[t][2]=="B+"):
        y[t][2]=3.5
    elif(y[t][2]=="B0"):
        y[t][2]=3.0
    elif(y[t][2]=="C+"):
        y[t][2]=2.5
    elif(y[t][2]=="C0"):
        y[t][2]=2.0
    elif(y[t][2]=="D+"):
        y[t][2]=1.5
    elif(y[t][2]=="D0"):
        y[t][2]=1.0
    elif(y[t][2]=="F"):
        y[t][2]=0
    elif(y[t][2]=="P"):
        y[t][2]=0
        o+=1
for z in range(20):
    y[z][2]=float(y[z][2])


sum=0
for c in range(20):
    sum+=y[c][1]*y[c][2]
print("%.6f"%(sum/(sum1)))