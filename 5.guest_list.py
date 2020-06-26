guests = ['bruno','mario','fred']

print(f"Please come to dinner {guests[0].title()}")
print(f"Please come to dinner {guests[1].title()}")
print(f"Please come to dinner {guests[2].title()}")

guests[0]= 'bruna'

print(f"Please come to dinner {guests[0].title()}")
print("Bigger table was found 2 more spots available")

guests.append("fab")
guests.insert(0, "mario1")

guests.sort()

print(guests)

popped = guests.pop(0)
print("Sorry", popped.title() ," the table was full")
popped = guests.pop(0)
print("Sorry", popped.title() ," the table was full")
print(guests)

del guests[-1]
del guests[-1]
del guests[-1]

print(guests)
