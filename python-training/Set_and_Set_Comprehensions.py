# Set- set is unordered collection of data item . It is enclosed by curly brackets
# sets are unchangable means once we create set we can not modify it .
# It not contain duplicate items.

s={2,4,5,4,2}
print(s) # it print only unique value

seet={}
print(type(seet)) # it not an empty set 

# for making empty set we write like this
sett = set()
print(type(sett))


# Accesing set using for loop 
for i in s:
    print(i)


a={1,3,5}
b={3,6,3,1,6,8}
print(a.union(b)) # our a and b will be unhanged 
print(a)
print(b)

# for changing any one we  do like this 
a.update(b)
print(a)


# a.issubset(b)
# a.issuperset(b)
# a.isdisjoint(b)

# add()
place={"bth","delhi","noida","bihar"}
place.add("kabul")
print(place)


# discard and remove are same but remove through an error if their is no matching item present 

place.remove("bth")
place.discard("noida")
print(place)

# del is a keyword through which we delete entire set

#del place
print(place)

place.clear() # to only delete the elements of set
print(place)


b.pop()  # it remove the last item of set.
print(b)



#Set Comprehensions
'''Set Comprehensions are used for creating new set from other iterables like lists, tuples, Dictionary , sets ,array , strings.'''

sss= {i*i for i in range(10) if i%2==0}
print(sss)

name=["Aditya","Hello","Ritu","Raj","Apurv"]
name_startwith_A={i[0] for i in name }  # It print the all name starting charecter (unique)
print(name_startwith_A)