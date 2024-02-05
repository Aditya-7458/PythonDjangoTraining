#List - 
'''
It is the ordered collection of data.
We use it to store multiple data in a single variable.
List items are separated by commas and enclosed within square brackets [].
List are changeble meaning we can alter them after creation
'''

list = [2,4,6]
print(list)
print(list[0])
print(list[2])


list2 = [2,4,6,"adi",True]
print(list2)

'''List start from 0th index'''

#Negative indexing 
print(list2[-3])   # converting it into positive  print(list2[len(list2)-3])
print(list2[len(list2)-3])


#Checking something present in list or not

if 7 in list2:
    print("YES")
else:
    print("NO")


if "adi" in list2:
    print("YES")
else:
    print("NO")



 #  Same concept in string 
if "Ad" in "Aditya":
    print("YES")
else:
    print("NO")



if "ya" in "Aditya":
    print("YES")
else:
    print("NO")


print(list2[:])
print(list2[2:]) # start printing from 2 till last
print(list2[1:4])

print(list2[1:4:2]) # its jump index means  it first take 1th and then 3th till 4th index




##### List Comprehensions 
'''
List Comprehensions are used for creating new lists from other iterables like lists, tuples, Dictionary , sets ,array , strings.

'''

list3 = [i for i in range(2,10)]
print(list3)

#another
list3 = [i+2 for i in range(2,10)]
print(list3)




list4 = [i*i for i in range(2,10) if i%2==0] # i want to put i*i in list4 if the condition is true, i%2==0
print(list4)

name=["Aditya","Hello","Ritu","Raj","Apurv"]
name_with_A=[i for i in name if "a" in i]  
print(name_with_A)



## Methods of list in python

l=[1,3,5,67,45,1,32]
print(l)


l.append(10)
print(l)



l.sort()
print(l)



l.sort(reverse=True)
print(l)


l.reverse()
print(l)

print(l.index(67)) # it return index at which 67 present


print(l.count(1))



m=l.copy()
m[0]= 230
print(m)


l.insert(1,80000)
print(l)

m=[100,300,600,500] # to merge two list but our "l" will change 
l.extend(m)
print(l)


k=l+m
print(k)

k.pop(1) # here we give indext from which we want to pop
print(k)

