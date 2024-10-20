#you can add and subtract integers in python
print(1+1)
print(3-2)

#exponents are indicated by two asteriks (also known as 2 mutliplication symbols)
print(3**3)

#you can do multiple different types of operations within a single line of text. python will also follow the order of operations, so you can add parenthesis to utilize this feature
#spacing does not matter in these scenarios 
print(2 + 3*4)
print((2 + 3)*4)

#floats are numbers with decimal values
print(4.1)
print(0,2)
print(4.1 + 0.2)
print(4.1 * 0.2)
print(4.1/2)

#mixing floats and integers will always produce a float value (ex. 4 + 2.0 = 6.0)
#dividing integers will also always produce a float value (ex. 4 / 2 = 2.0)
 
#numbers can be grouped with underscores. this can help when writing long numbers
long_number = 150_000_000_021_022_001
print(long_number)

#assign multiple integers to multiple variables using a single line of code
name,name_2,name_3 = 0,1,2
print(name)
print(name_2)
print(name_3)
print(name,name_2,name_3)