#! /usr/bin/env python
import random
## test github upload

##############  Randomic number to increase a health bar  ###############
separator = ("=")
health = 50
difficult = 1
nmr_random = int(random.randint(10, 20) / difficult)

health = (health + nmr_random)
print(health)

print (separator *30)


############# String concatenation ##################

A = "My name is "
B = "Paulo Janoti "
C = 1

Text = A + B + str(C) # var C is a integer
print (Texto)
print (separator * 30)

num1 = float(input ("Write a number : "))
num2 = float(input ("Write another number: " ))

sum = (num1 + num2)
mult = (num1 * num2)

print ("The Sum is ", soma)
print ("The mult is ", mult)

#another ay to concatenate
text = (" The sum í {} and the mult is {}")
output = texto.format(soma,mult)
print (output)
print (separator * 30)


start = "I am "
age = 33
end = " years old"
output = "{} {} {}".format(start,age,end)

print (output)
print(separator * 30)


############ count the number of times a particular character appears ############# 

path = "/home/administrador/PycharmProjects/estudos/venv/bin/python /home/administrador/PycharmProjects/estudos/estudos.py"
qtd_a = path.count("a")
qtd_slash = path.count("/")
print(" Letter 'a' appers {} times and foward slash appears {} times".format(qtd_a,qtd_slash))
print (separator * 30)


