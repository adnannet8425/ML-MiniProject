fp=open("File2.txt","w")
import random
import string 
a=[]
string.strs='COMPUTER ENGINEERING','MECHANICAL ENGINEERIN','CIVIL ENGINEERING','ELECTRICAL ENGINEERING','ENGINEERING','PHARMACY','ARCHITECTURE','DOCTOR','POLICE','COMMERCE','ARTS','SCIENCE','TEACHING','BUSSINESS MANAGEMENT','HOTEL MANAGEMENT','MILITRY','AIR FORCE','NAVY','PILOT','CA','BUSSINESSMAN','DATABASE ADMINSITRATOR','SOFTWARE DEVELOPER','SOFTWARE TESTER','WEB DEVELOPER','IS OFFICER','ACCOUNTANT','BANK MANAGER','FASHION DESIGNER','CHEMICAL ENGINEER','ENVIRONMENTAL ENGINEER','GEATECHNICAL ENGINEER','AGRTICULTURAL ENGINEER'
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.choice(string.strs))
    #a.append(random.randint(100000,999999))

print(a)
values = '\n'.join(map(str, a))
print(values)

for i in values:
	fp.write(i)
	
fp.close()


