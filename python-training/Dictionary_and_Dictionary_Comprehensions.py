# Dictionary - I is ordered collection of data item 
# It store data in key value pair
# it enclosed with {}

dic={
    234:"Adi",
    210: "Rahul",
    345: "Ashu"
}
print(dic[210]) # it print error if any value is present
print(dic.get(100)) # it print none if no key is present

print(dic .keys())


# Through iterator 
for i in dic.keys():
    print(dic[i])



print(dic.items()) ##### It return key value pair 



# Update 

ep1={1:200,2:300,3:400}
ep2={4:500,7:500}
ep1.update(ep2)
print(ep1)


ep1.pop(1)  # pop()
print(ep1)


ep1.clear() # to vacant the dictionary
print(ep1)

# popitem() it remove the lasgt key value pair from the dictionary 



####### Dictionary comprehension 

add={num:num*num for num in range(1,10)}
print(add)


string = "Adiitya"
word_count={char:string.count(char)for char in string}
print(word_count)


