#by adding brackets to a list of strings, you now have the ability to seperately utilize each string for further operations 
bicycles = ["cannondale", "trek", "specialized"]
print(bicycles[0].title())

#you can also simply print the list of values using the assigned variable
print(bicycles)

#python also allows for a reverse method of syntax for pulling certain values from a list. You can use negative integers to reference counting back from the end of the list rather than the beginning.
print(bicycles[-1].title())

# the -1 signifies the final value in a list, allowing for easier reference. This can also be applied to the rest of the components of the list as well.
print (bicycles[-3].title())

#application of a list just as any other variable
message = f"My first and favorite bike is a {bicycles[2].title()}. By far I love that kind over a {bicycles[-1].title()}."
print(message)