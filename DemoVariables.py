# set two string variables to the same value using single quotes
a='nyc'
b='nyc'
# set third string variable to the same value as the previous two but use double quotes
c="nyc"
# print all three variables
print(a)
print(b)
print(c)
# Confirm first two varibles are the same value
print(a==b)
# Confirm get same result using is keyword
print(a is b)
# Confirm that first and third variables are the same, if so is agnostic to type of quotes used
print(a==c)
# Confirm that first and third variables are the same, using is keyword, if so is agnostic to type of quotes used
print(a is c)

# set variable to 10
d=10
# set another variable to 11
e=11
# print values
print(d)
print(e)
# Confirm are different
print(d==e)
# Confirm again using is keyword, check it works with integers
print( d is e)
# subtract 1 from 11
e=e-1
# Confirm subtraction worked
print(e)
# Confirm if the variables now match
print(d==e)
# Confirm again using is key word
print(d is e)




