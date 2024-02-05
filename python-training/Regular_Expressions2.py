# Matching any single letter or number

# \w is same as [a-zA-Z0-9_]
# \W is same as [^a-zA-Z0-9_]
import re
phNum="412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}",phNum):
    print("Valid Phone Number")


if re.search("\w{9,20}", "JohnDoe123"):
    print("Valid Name")



# \s same as[\f\n\r\t\v]
    #\s same as[^\f\n\r\t\v]



if re.search("\w{2,20}\s\w{2,20}","Aditya"):
    print("Valid Full name")




# + matches 1 or more charecters
    
print(re.findall("a+","Adityakumar add ape"))



#Q. Create a regex that matches email addresses from a List
email="db@aol.com m@.com @apple.com db@.com"
print(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-z]{2,3}",email))





import re

text = "Contact us at john.doe@example.com or support@company.org for assistance"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(email_pattern, text)
print(matches)

