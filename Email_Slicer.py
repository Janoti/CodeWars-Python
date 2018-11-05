########################### SLICER #############################

word = "supercalifragilesticabacononfosdnfosdofndonf"
print(word)
a = word[0]
print("First caracter - {}".format(a))

print("Extract word bacon:")
bacon =  word[21:26]
print(bacon)

#automatic
total = len(word)
baconis = word.index("bacon")
print(total) # Length of string
print(baconis)
print(word[baconis:baconis+5])

print("Print reverse 1 line of code")
print(word[::-1])

o = word[word.index("bacon"):word.index("onf")]
print(o)

#Get user email
email = input("EMail: ").strip()

#Slice user name
userName = email[:email.index("@")]

#Slice Domain
domain = email[email.index("@")+1:]

#Output
output = "Your username is {} and you domain is {}".format(userName,domain)
print(output)