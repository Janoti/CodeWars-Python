########## Locate for the start position of a string ############
x = "uahsiahsoahsohappybirthdayakjpaásajsajs"
position = x.find("birthday")
print('birthday start in {} position this string, starts with 0'.format(position))

########## Strip #################################################

y = "000000000text000000000"
normalStrip = y.strip("0")
leftStrip = y.lstrip("0")
rigtStrip = y.rstrip("0")

print("Normal Strip, excluding all zeros: {} - Left Strip, excluding all zeros at left: {} - Rigth Strip, excluding all zeros at rigth: {}".format(normalStrip,leftStrip,rigtStrip))

z = "text with spaces at the end                  "
yz = z.strip()
print("Empty strip function, strip spaces --- {} ".format(yz))
print("Length of string before - {}".format(len(z)))
print("Lenght of String after  - {}".format(len(yz)))

################## COUNT ###############
letters = "hello".count("l")
print("Letter 'l' count in hello: {}".format(letters))

