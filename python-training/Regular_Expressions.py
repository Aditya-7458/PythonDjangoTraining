
# to use regex we need to import it 
import re

# search() for a 'adi' in string 
a="he is the good adi for the game"
if re.search("adi",a):
    print ("Yes found")


# findall() return a list of matches, . is used to match any 1 character or space 
    
f="Adi is a very good adi Aditya"
x =re.findall("Adi.",f)
#print(x)
for i in x:
    print(i)


# finditer() it return an iterator of matching objects. You can use span to get the location.
    
theStr="Good will willaster always happen to me "
w=re.finditer("will.",theStr)
for i in w:
    aaa=i.span() # span return a tuple
    print(aaa)

    # slice the match out using the tuple values

    print(theStr[aaa[0]:aaa[1]])


allAnimal="Cat rat Mat Aat"
Ad=re.findall("[crmpA]at|[CM]at",allAnimal) # it will print all
# Ad=re.findall("[crmpA]at",allAnimal)
for i in Ad:
    print(i)




names="Cat rat Mat Aatttt"
someNames=re.findall("[a-zA-Z]at.",names)
for i in someNames:
    print(i)



names2="Cat rat Mat Aatttt"
someNames=re.findall("[^a-z]at.",names2)
for i in someNames:
    print(i)


owlFood="Rat cat mat Aat"
converted=re.compile("[crm]at")   # we can compile a regex into pattern objects which provide additional methods
owlFood=converted.sub("owl",owlFood)
print(owlFood)



# Backslash and row String
randStr="Here is \\stuff"
print(re.search("\\stuff",randStr)) # not able to find 
print(re.search(r"\\stuff",randStr)) # able to find using r
print(re.search("\\\\stuff",randStr)) # able to find uding \\


str2="F.B.I I.R.S CIA"
print(re.findall(".\..\..",str2))

print(len(re.findall(".\..\..",str2)))



str3=""" He use to
love cricket """
print(str3)
# remove new lines
sss=re.compile("\n")
str3=sss.sub(" ",str3)
print(str3)

# we can alse use many operaton like \t for tab \b for backspace.

str4="12345"
print(re.findall("\d+",str4))
print(re.findall("[0-9]+",str4))


str4="12345"
print(re.findall("\d",str4)) # 
print(re.findall("[0-9]",str4))


str5="346djudsuh264376d"
print(re.findall("^[0-9]+",str5)) # search for digits in starting

print(re.findall("[^0-9]+",str5)) # search for non digit in string 
print(re.findall("\D+",str5)) # search for non digit in string 


## Matching Multiple Numbers

if re.findall("\d{5}","21278645"): # if it is 5 digit or more than 5 digit  , go inside the condition
    print("It is a Zip Code")



str6="123 456 75443 88753 54334 652 3666664543"
r=len(re.findall("\d{5,6}",str6)) 
print(r)









