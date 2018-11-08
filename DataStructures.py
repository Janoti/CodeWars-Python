############ LISTS

my_list = [1, 2, 3, 4, 5]
mix_list = ["A", "B", 1, 2, True, False]

a = mix_list[0:2] ## -- SLICE Print A , B
print(a)
print("\n")

nestlist = [1,2,3,[4,5,6],7,8]
# 4 , 5 and 6 is inside another list
nlist = nestlist[3]
print(nlist)
# access a index inside the another list
nlist2 = nestlist[3][0]
print (nlist2)

#### TABLE

my_table = [[1,2,3],[4,5,6],[7,8,9]]

print(my_table[0]) #Print 1º position (1,2,3)
print(my_table[1][2]) # Print number 6