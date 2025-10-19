import random as R
l=[]
for i in range(50):
    l.append(R.randint(1,365))
l.sort()
print(l)
i=0
flag=0
while(i<len(l)-1):
    if(l[i]==l[i+1]):
        print("There is repeatition of",l[i],l[i+1])
        flag=1
        # break
        
    i=i+1
if(flag==0):
    print("no repeatition")