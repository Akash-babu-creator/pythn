alpha = "abcdefghijklmnopqrstuvwxyz"
# i=28
# print(alpha[i%26])
# a="akash"
a=input("enter the string you want to be shifted:-\t")
# i expect the output blbti
t=''
k=int(input("enter how many letter you want it to be shifted:-\t"))
for i in range(len(a)):
    t=t+(alpha[(((alpha.index(a[i]))+k)%26)])
print(t)