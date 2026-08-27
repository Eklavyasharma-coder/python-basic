print("Hello World")

#int 
age=100
print(age , type (age))

#float 
hight=12.56 
print(hight , type (hight ))

#complex 
c=2+3j
print(c,type(c))

#string 
s1='a'
s2='rahul'
s3='my name is rahul '
print(s1,type (s1))
print(s2,type(s2))
print(s3, type(s3))

#boolean 
ismarried= False 
isGraduated= True 
print(ismarried,type(ismarried))
print(isGraduated,type(isGraduated))

#None 
name= None
print(None, type(None))

'''#input 

first_name= input()
last_name= input()
print(first_name,last_name)'''

'''# type of input 

age = int(input())
height = float(input())'''

# print funtion in python 
full_name="rahul kumar"
Age=24
address="japur "

print(full_name )
print(Age )
print(address)
print(full_name , Age , address )

# sep
name= "fukl"
age = 27
address = "fupuy"
print(full_name , Age , address, sep=",")
print(full_name , Age , address, sep="_")
print(full_name , Age , address, sep="/")
print(full_name , Age , address, sep=":")
'''2print(full_name,end="&&")'''

#type of if 
age= int(input())
if(age>=18):
    print("eligible for driving license")
else:
    print("not eligible for driving license")

age = int(input())
if(age>=18):
 test = input()
if test == "Pass":
    print("eligible for driving license")
else:
    print("not eligible for driving license")

'''# test mark 
mark = int(input())
#90 excellent 
#70-90 good 
#50-70 fair
#<30 bad '''

'''if mark>=90:
 print("excellent")
elif mark>=70:
 print("good")
elif mark>=40:
   print("fair")
else:
   print("bad")'''

'''# temp for city 
Temp= int(input())
#25-50 -> hot 
#25-1 -> cool 
#1-(-4) -> very cool

if Temp<=50 and Temp>=25 :
   print("hot")
elif Temp<=25 and Temp>=10:
 print("cool")
elif Temp<10:
   print("very cool")'''

'''# Type of ternary operatar 
age=int(input())
result = "eligible"
if age>=18:
   else
   "not eligible"
print(result)'''

'''#type of while  
i=0 
while  i < 5 : 
 print(i, end="")
i+=1'''

'''list1=[3,3,5,2,1]
for i in list1: 
   print(i,end="")
#type of range 

for i in range(1,11):
 print(i,end="")
 
for i in range(5,11):
 print(i,end="")
  
for i in range(2,11,2):
 print(i,end='')
 
 #type of range 
for i in range(20,0,-1):
   print(i,end="")

for i in range(30,4,-3):
 print(i,end="")'''

#funtion 
#def funtion name (perametrs)
def printName(name ):
  print(name)
  printName("Abhinav sharma")

#type of funtion 
def addTwoNumber(a,b):
   sum=a+b
   return sum 
ans=addTwoNumber(4,7) 
print(ans)

a = "eklavya is a good boy \n but rahul is bad boy "

print(a)

#List
friend= ["harry", "rahul", "raj" , 3 , 35.67, "ram"]
print(friend)
friend.append("kunal")
print(friend)


l1=[1,2,3,45,87657,88]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,5767)
print(l1)
l1.pop(3)
print(l1)

#tuple
a=("Rahul",'raja',"raj",4,47.766,"king")
print(a,type(a))

