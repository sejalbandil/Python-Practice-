#This program prints out all the elements of the list that are less than 5.
new_list=[]
list = [1,3,2,6,5,4,9,8]
for number in list:
    if number<5:
        new_list.append(number)

print(new_list)
