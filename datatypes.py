#data types in python
 
i:int  # we assign integer type to variable i 
i=10 #we assign 10 value to i 
print(i)

s:str # we assign string value to variables 
s="string"
print(s)

s='single quated string'
print(s)


s='''
this is 
single tripple quated 
multi-line string
'''
print(s)
s="""
this is 
double tripple quated 
multi-line string
"""
print(s)

#float data type in python
f:float
f=10.30
print(f)


#list data type in python
l:list
l=["Banana","Apple",1,2.5]
print(l)


#tuple data type in python
t:tuple
t=("Apple","cherry","Mango",7,8,9)
print(t)



#set data type in python
s:set
s={1,2,3,1,2,3,7,4,5,6,5} #set does'nt contain duplicate values
print(s)



#dictionary data type in python
d:dict
d={"key":"value"}
#example
d={"fruits":["Apple","banana","custed-Apple","Dragon-fruit"]}
print(d)


#boolean data type in python
b:bool
b=False
print(b)
b=True
print(b)


#complex number in python
c:complex
c=1+2j
print(c)


#range in python
r:range
r=range(10)
print(r)


#loops in python
#For loop

for i in r:
    print(i)

for i in l:
    print(i)

for i in t:
    print(i)

for i in s:
    print(i)

for i in d:
    print(i,d[i])

#while loop

while b:
    br=(input(" to continue y/n:"))
    if "n" in br or "N" in br:
        break  


b=bool(int(input("Enter true or false : ")))
if b:
    print("true block")
else: 
    print("False block")

   





