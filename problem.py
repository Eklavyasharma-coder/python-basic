name = input("enter your name:")
print("Good Afternoon ",name)

name = input("enter your name:")
print(f"Good afternoon  , {name}" )
 
letter = ''' dear <|Name|>
 you are selected 
<|Date|>'''

print(letter.replace("<|Name|>","Eklavya").replace("<|Date|>","14 sep 2024"))


name = "eklavya shrma is good boy"
print(name.replace(" ","  "))
print(name.replace("good"," bad "))


letter = "Dear Eklavya sharma, \n \tThis python couse is good.\nThanks"
print(letter)

#tuple problem
fruit=[]
f1=input("enter the fruit name:")
fruit.append(f1)
f2=input("enter the fruit name:")
fruit.append(f2)
f3=input("enter the fruit name:")
fruit.append(f3)
f4=input("enter the fruit name:")
fruit.append(f4)
f5=input("enter the fruit name:")
fruit.append(f5)
f6=input("enter the fruit name:")
fruit.append(f6)
f7=input("enter the fruit name:")
fruit.append(f7)

print(fruit)

#tuple sum 
l=(1,34,666,875)
print(sum(l))

a=(7,0,9,0,8,0,77,0)
on=a.count(0)
print(on)

#Dict

marks= {
    "harry" : 100,
    "subham" : 50,
    "rahul" : 22,
}

print(marks,type(marks))

print(marks["harry"])

#sets

words= {
    "madad":"help",
    "kursi":"chair",
    "bol":"tell"
}

word = input("Enter the word you want to meaning of: ")

print(words[word])


s=set()
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))
n=input("Enter number :")
s.add(int(n))

print(s)


