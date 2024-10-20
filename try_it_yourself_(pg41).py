#3-4 Guide List
list = ["harry", "ron", "hermione"]
print(f"{list[0].title()}! I am having a party and you are invited.")
print(f"{list[1].title()}! I am having a party and you are invited.")
print(f"{list[2].title()}! I am having a party and you are invited.")

#3-5 Changing Guest List
list = ["harry", "ron", "hermione"]
print (f"\nUnfortunately, {list[0].title()} can not make it to the party tonight.")
list.pop(0)
list.insert(0, "dumbledore")
print(list)
print(f"However, there is some great news! {list[0].title()} can make it to the party so we invited him as well!")
print(f"{list[0].title()}! I am having a party tonight and you are invited!")
print(f"{list[1].title()}! I am having a party tonight and you are invited!")
print(f"{list[2].title()}! I am having a party tonight and you are invited!")

#3-6 More Guests
print(f"\nActually {list[0].title()}, {list[1].title()}, and {list[2].title()}, I have some more great news! I just realized that I have a bigger table that needs more people around it for the party tonight.")
print(list)
list.insert(0, "dobby")
list.insert(1, "hagrid")
list.append("jinny")
print(list)
print(f"{list[0].title()}! You are invited to my party tonight!")
print(f"{list[1].title()}! You are invited to my party tonight!")
print(f"{list[2].title()}! You are invited to my party tonight!")
print(f"{list[3].title()}! You are invited to my party tonight!")
print(f"{list[4].title()}! You are invited to my party tonight!")
print(f"{list[5].title()}! You are invited to my party tonight!")

#3-7 Shrinking Guest List
print("\nOh no! My new large table was just burnt up by a dragon. Now I can only have two guests for dinner tonight!")
print(f"Apologies {list[5].title()}! Unfortunately, I can't have you for dinner tonight!")
list.pop()
print(f"Apologies {list[4].title()}! Unfortunately, I can't have you for dinner tonight!")
list.pop()
print(f"Apologies {list[3].title()}! Unfortunately, I can't have you for dinner tonight!")
list.pop()
print(f"Apologies {list[2].title()}! Unfortunately, I can't have you for dinner tonight!")
list.pop()
print(list)
print(f"No need to worry {list[0].title()}! You are more than welcome to come for dinner tonight. See you soon!")
print(f"No need to worry {list[1].title()}! You are more than welcome to come for dinner tonight. See you soon!")
del list[1]
del list[0]
print(list)
