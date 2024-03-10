#For loop
names = ["Manasseh", "Joseph", "James", "Gideon"]

for name in names:
    print(name)
    
my_details = "I live in Thika"
for i in range(5):
    print(my_details)
    
#While loop
count = 0
while(count <= 2):
    print(count)
    count+=1
    
#Challene 1
colours = ["Green", "Red", "Blue", "White", "Orange"]
colour_i_want = "Blue"

for color in colours:
    if color == colour_i_want:
        print("They have the color i want")
        break
    print(color)
    
#Using while loop
length = len(colours)
             
count2 = 0

while count <= length:
    print(colours[count2])
    
    if colours[count2] == colour_i_want:
        print("They have the color I want")
        break
    count2+=1
    
#Continue
ages = [19, 23, 34, 43, 54]
for age in ages:
    if age<21:
        continue
    print(age)

#Nested loops
groups =[["Josiah", "Beth"],["Glory", "James"]]
for group in groups:
    for name in group:
        print(name)


#Lists comprehension
#Without list comprehension
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_list = []

for num in list:
    doubled_list.append(num * 2)
print(doubled_list)

#With list Comprehension
doubled_list2 = [num * 2 for num in list]
print(doubled_list2)


        