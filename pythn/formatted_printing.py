for x in range(4):
    print(x)  #will print number in next line after every itteration 
for x in range(4):    
    print(x,end='')  #will print in same line

d,m,y=22,8,2025
print("\ntoday's date is", d,m,y,sep="/")   #sep is a another parameter reffered a seperator it's default value is " "(1 blank space)
print("today's date is",end=' ')
print(d,m,y,sep="/")

t=int(input("enter the number for table"))
for i in range(1,11):
    # print(t,'X',i,'=',t*i)
    # print(f'{t} X {i} = {t*i}')   #formatted printing
    # print('{0} X {1} = {2}'.format(t,i,t*i)) #print using format function 
    print('%d X %d = %d'%(t,i,t*i))

pi=22/7
print(f'value of pi = {pi}')
print('value of pi = {0}'.format(pi))
print('value of pi = %f'%(pi))

#using format specifiers
print(f'value of pi = {pi:.2f}')
print('value of pi = {0:.4f}'.format(pi))
print('value of pi = %.3f'%(pi))

# printing pattern left allinged
print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))

#right alligned
print('{0:5d}'.format(1))                         #5d means it will take 5 spaces nd d specifying that it's integer value
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

