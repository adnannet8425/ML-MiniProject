fp=open("File2.txt","w")
import random
import string 
a=[]
string.strs='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=int(input("Enter number of elements:"))
for j in range(n):
    #a.append(random.choice(string.strs))
    a.append(random.randint(100000,999999))

print(a)
values = '\n'.join(map(str, a))
print(values)

for i in values:
	fp.write(i)
	
fp.close()


