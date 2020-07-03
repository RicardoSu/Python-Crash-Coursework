places = ['St Lucia', 'San Francisco',
	 'Amsterdam', 'Rio de Janeiro', 'Costa Rica']

#print original list
print(places)

#print sorted places but does not afftect original list
print(sorted(places))

#making sure that sor was nt saved
print(places)

#print in revese sort
print(sorted(places, reverse=True))


print(sorted(sorted(places, reverse=True)))
places.sort()
print(places)
places.sort(reverse=True)
print(places)