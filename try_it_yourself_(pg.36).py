#3-1 Names
names = ["tom", "dick", "harry"]
print(names[0].title())
print(names[1].title())
print(names[2].title())

#3-2 Greetings
message_1 = f"Hey {names[0].title()}, I like your shoes!"
message_2 = f"Hey {names[1].title()}, I like your shoes!"
message_3 = f"Hey {names[2].title()}, I like your shoes!"
print(message_1)
print(message_2)
print(message_3)

#3-3 Your Own List
motorcycles = ["indian", "harley davidson", "triumph"]
message = f"I would love to own a {motorcycles[-3].title()} someday. If not, then definitely a {motorcycles[2].title()} or a {motorcycles[-2].title()}."
print(message)