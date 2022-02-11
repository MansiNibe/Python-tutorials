#tuples in python
t1=("Apple","Banana","cherry","Mango")
print(type(t1))
print(len(t1)) 

#we can also define a mix tuple 
mix_tup=("heyy",12,True,"banana")
print(mix_tup)

print(len(mix_tup))
print(type(mix_tup))

print(mix_tup[0]) #tuple strts the indexing from 0

print(mix_tup[-1])  # here -1 indicates the index of the last item of the tuple

#providing range to the tuple by using slicing operator
print(mix_tup[0:3])

#tuples are immutable ...to add elements in tuple conver it into a list
#for example
t1=("apple",1,2,3,4,5)  #create a tuple
l1=list(t1)  #convert tuple into list
l1[1]="Watermellon"  #add value in to list
t1=tuple(l1)  #convert list into tuple
print(t1)


#list in python
l2=["mansi","Amrapali","Shiva",1,2,2,2,2,2,3,7,8,9,'c',23]
print(l2)
l2.append(23)   #adds the element at the end of the list  
print(l2)
print(l2.count(2)) #count unction counts the given value how many time presents in the list
print(l2.copy())  #copy function returns the copy of the list
l3=[1,2,3]
print(l2.extend(l3))  #extend method add the list items to the end o the list
print(l2)
print(l2.index(2)) #returns the index of the specified element
print(l2.pop(2))  #by using index of the element it removes the element
print(l2)

print(l2.remove("mansi"))
print(l2)



#dictionary in python
colours={ 
    "Name":"Mansi",
    "Roll_no":10,
    "Class":"TEIT"
    }

print(colours)


table={
       "name":["mansi","ram","sham","riya"],
       "roll_no":[32,31,12,13],
       "college":["prec","coep","sanjivani","amrutvahini"]
}
print(table)



