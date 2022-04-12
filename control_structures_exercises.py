#This page exists as the main worktool for control structures

#we would use isdigit here to strain out an answer
#in using isdigit we can set up restting code

#we can setup a while loop

while True:
    yike = input('Input odd number from 1 - 50: ')
    if yike.isdigit(): #returns a true false check if intger
        yike=int(yike)  #data type converstion after digit confirmation
        if yike % 2 == 0:
            print('Sir this is a Wendy\'s. JK that\'s not an odd number')
        else:
            print("checks out")
            break
    else:
        print("A number, please")

print("Number to skip is: ",yike)

for i in range(50):
    if yike == i:
        print("Yikes! Skipping number:", yike)
        #the edit here was that we wanted is to order the above function first 
        #that way the leftover value will then be iteratted
        #we use elif
    elif i % 2 == 1:
        print("Here is an odd number:",i)

if yike.isdigit():
    print("Number to skip is: ",yike)

#I don't think i will really need to use is digit because i am straining my input out as a integer


#                           FIZZBUZZ
# for watev in range(101):
#     if watev % 3 == 0  and watev % 5 == 0:
#         print(watev, "fizzbuzz")
#     elif watev % 3 == 0:
#         print(watev, "fizz")
#     elif watev % 5 == 0:
#         print(watev, "buzz")
#     print(watev)

# Display a table of powers.

#     Prompt the user to enter an integer.
#     Display a table of squares and cubes from 1 to the value entered.
#     Ask if the user wants to continue.
#     Assume that the user will enter valid data.
#     Only continue if the user agrees to.

"""
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
"""

#while True:
# print('number | squared | cubed')
#     print('------ | ------- | -----')

usernum = int(input("What number would you like to go up to? "))
print("Here is your table!")
print("number | squared | cubed")
print("_________________________")
for i in range(1,usernum + 1):
    #there is more efficient  ways  to store andmanipulate  i that can be revisited
    power = i
    power2 = i * i
    power3 = i * i * i
    #f string to place in variables
    print(f" {power:<5} | {power2:^7} | {power3:5}")

"""Convert given number grades into letter grades.

    Prompt the user for a numerical grade from 0 to 100.
    Display the corresponding letter grade.
    Prompt the user to continue.
    Assume that the user will enter valid integers for the grades.
    The application should only continue if the user agrees to.

    Grade Ranges:
        A : 100 - 88
        B : 87 - 80
        C : 79 - 67
        D : 66 - 60
        F : 59 - 0
"""
grade=input("Enter a numerical grade from 0 to 100")
