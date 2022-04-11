#This page exists as the main worktool for control structures

#we would use isdigit here to strain out an answer
#in using isdigit we can set up restting code

#we can setup a while loop

# while True:
#     yike = input('Input odd number from 1 - 50: ')
#     if yike.isdigit(): #returns a true false check if intger
#         yike=int(yike)  #data type converstion after digit confirmation
#         if yike % 2 == 0:
#             print('Sir this is a Wendy\'s. JK that\'s not an odd number')
#         else:
#             print("checks out")
#             break
#     else:
#         print("A number, please")

# print("Number to skip is: ",yike)

# for i in range(50):
#     if yike == i:
#         print("Yikes! Skipping number:", yike)
#         #the edit here was that we wanted is to order the above function first 
#         #that way the leftover value will then be iteratted
#         #we use elif
#     elif i % 2 == 1:
#         print("Here is an odd number:",i)

# if yike.isdigit():
#     print("Number to skip is: ",yike)

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

power = input("What number would you like to go up to? ")

print("Here is your table!")