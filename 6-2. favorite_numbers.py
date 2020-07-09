fav_numbers = {'Liam':'21', 'Emma':'3', 'Noah':'6', 'Olivia':'7', 'William':'3'}

del fav_numbers['Liam']
Liam = fav_numbers.get('Liam', "Liam left the chat")
print(Liam)

print(fav_numbers['Olivia'])