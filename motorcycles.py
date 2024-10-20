#the syntax for modifying a list is essentially the same as accessing a value within it. 
motorcycles = ["honda", "harley davidson", "yamaha"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

#there's different methods of adding to a list, but one of the easiest ways is to use the append() method. This simply adds to the end of your list.
motorcycles.append("honda")
print(motorcycles)

#The append() method also can come in handy for building a dynamic list that can be built up or torn down. You can create a list by just doing multiple appends to a variable.
#this is a common method for building lists because the data that will need to go in lists will not even be able to have been added until users already have access to the running program
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("harley davidson")
print(motorcycles)

#Elements of a list can also be added by using the insert() method. By doing this, you are able to pick exactly where you would like your variable to be and push the rest of the following info to the right
motorcycles.insert(0, "ducati")
print(motorcycles)

#one way to delete items from a list is by using the del statement. This specifically allows you to delete any component within a list as long as you know the position of that variable
motorcycles = ["honda", "harley davidson", "yamaha"]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#In comparrison to the del statement (which deletes values permanently), the pop() method can be used to remove an element from a list and assign it to a new variable which can be utilized for further application
favorite_motorcycles = ["honda", "harley davidson", "yamaha"]
least_favorite_motorcycles = []
least_favorite_motorcycles = motorcycles.pop()
print(favorite_motorcycles)
print(least_favorite_motorcycles)

#this method can be used to help keep track of things such as the last motorcycle you owned 
motorcycles = ["honda", "harley davidson", "yamaha"]
last_owned_moto = motorcycles.pop()
print(f"The last owned motorcycle you've owned is the {last_owned_moto.title()}.")

#You can also use the pop() method to remove and reassign any value within a list, as long as you know the position of the value
motorcycles = ["honda", "harley davidson", "yamaha"]
first_owned_motorcycle = motorcycles.pop(0)
print(f"The first motorcycle you have ever owned was a {first_owned_motorcycle.title()}.")

#using the remove() method allows you to name the variable you would like to remove. This can be helpful if you simply do not remember the position of the value that you want to remove
motorcycles = ["honda", "harley davidson", "yamaha"]
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)

#even after removing from the list, as long as you assign an individual variable first, the removed value is still assigned to its variable
motorcycles = ["honda", "harley davidson", "yamaha"]
print(motorcycles)
too_expensive = "honda"
motorcycles.remove("honda")
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me to afford right now.")


