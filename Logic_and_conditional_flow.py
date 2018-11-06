###### Boeleans & Comparison Operators
B = True
C = False


result = 2 > 3
print(" 2 is greater than 3? - {} ".format(result))
result2 = 2 == 2
print("2 is equal 2? - {}".format(result2))
result3 = 4 >= 3
print(" 4 is greater ou equal to 3? - {}".format(result3))

###### IF Statements
num1 = input("Insert a number: ")

num2 = input("Insert another number: ")

if num1 > num2 :
    print("Num1 is greater than num 2")
elif num2 > num1:
    print("num2 is greater than num 1")
else:
    print("Both are equals")

print("\n")


### Not statement
D = 10
E = 20
if not (D > 10 and E > 10):

     print ("D is not greater than 10, is equal (FALSE)--- and --- E is greater than 10 (TRUE),so FALSE and TRUE = FALSE")

#### OR statament

F = 5
G = -1

if F > 1 or G >1:
    print("F is 5 and G is -1, if F is greater than 1 (TRUE) OR G greater than 1 (FALSE) --- TRUE OR FALSE = TRUE")

endA = False and False
endB = False and True
endC = True and False
endD = True and True

orA =  False or False
orB =  False or True
orC =  True or False
orD =  True or True

print ("    \nAND TABLE ")
print ("A       B      OUTPUT")
print ("0       0          {} ".format(endA))
print ("0       1          {} ".format(endB))
print ("1       0          {} ".format(endC))
print ("1       1          {} ".format(endD))
print ("\n")
print ("    \nOR TABLE ")
print ("A       B      OUTPUT")
print ("0       0          {}  ".format(orA))
print ("0       1          {} ".format(orB))
print ("1       0          {}  ".format(orC))
print ("1       1          {} ".format(orD))
