#Exercise 1
# Creates list
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

# Defines empty list
list3 =[]

#Loops to remove uneven numbers
for i in range(len(list1)): 
    for j in range(len(list2)):
        if i%2 and j%2 ==1:
            list3.append(list1[i])
            list3.append(list2[j])
            print(list3)

########################################################################################################################################################################

# Exercise 2
#List creates
List_ex2 = [54, 44, 27, 79, 91, 41]
print("list before change:", List_ex2)

#removing index
index_to_rmv = List_ex2.pop(4)

#printing removed index
print("list after removal:",List_ex2)

#printing inserted index in different position
List_ex2.insert(2,index_to_rmv)
print("list after adding it back in:",List_ex2)

#print final
List_ex2.append(index_to_rmv)
print("list after appending:", List_ex2,"\n")

########################################################################################################################################################################

#Exercise 3
#Creates list
List_ex3 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

#prints list
print("original list:", List_ex3)

#first slice and reverse
list_chunk1 = List_ex3[0:3] 
print("first chunk:", list_chunk1)
print("reversed chunk 1:",list_chunk1[::-1],"\n")

#second slice and reverse
list_chunk2 = List_ex3[3:6]
print("second chunk:", list_chunk2)
print("reversed chunk 2", list_chunk2[::-1],"\n")

#third slice and reverse
list_chunk3 = List_ex3[6:9]
print("second chunk:", list_chunk3)
print("reversed chunk 3", list_chunk3[::-1],"\n")

#######################################################################################################################################################################

#Exercise 4
#Did not know how to do exercise 4

########################################################################################################################################################################

#Exercise 5
#Created list and print
list_5_1 = [20,55,66,52,81,612,578]
print("List one:\n", list_5_1)
list_5_2 = [4, 9, 16, 25, 36, 49, 64]
print("List two:\n", list_5_2)

#combines list
comb_list = zip(list_5_1, list_5_2)

#prints combination
print(tuple(comb_list))

########################################################################################################################################################################

#Exercise 6
#sets
set_6_1 = {65, 42, 78, 83, 23, 57, 29}
set_6_2 = {67, 73, 43, 48, 83, 57, 29}

#checks set intersection
com_set = set_6_1.intersection(set_6_2)

#prints intersection
print(set(com_set))
print(set_6_1-com_set)

#######################################################################################################################################################################

#Exercise 7
#Meant create set not "list"
list_ex_7_1 = {57, 83, 29}
list_ex_7_2 = {57, 83, 29, 67, 73, 43, 48}

#Prints sets
print("set one: ", list_ex_7_1)
print("set two ", list_ex_7_2)

#Checks if subset
check_sub_1 = list_ex_7_1.issubset(list_ex_7_2)
check_sub_2 =  list_ex_7_2.issubset(list_ex_7_1)

#Prints result
print("Check first set for sub:",check_sub_1)
print("check second set for sub:",check_sub_2)

#Checks if superset
check_sup_1 = list_ex_7_1.issuperset(list_ex_7_2)
check_sup_2 =  list_ex_7_2.issuperset(list_ex_7_1)

#Prints result
print("Check set 1 for super:", check_sup_1)
print("Check set 2 for super:",check_sup_2)

#Desicion tree
if(list_ex_7_1.issubset(list_ex_7_2)):
  list_ex_7_1.clear()
  if(list_ex_7_2.issubset(list_ex_7_1)):
      list_ex_7_2.clear()

#Final result
print("set one:", list_ex_7_1)
print("set two:",list_ex_7_2)
########################################################################################################################################################################
