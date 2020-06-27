for x in range (1,21):
	print(x)
#for x in range (1,1000001):
#	print(x)
one_millon = [value for value in range(1,1000001)]
print(sum(one_millon))
print(max(one_millon))
print(min(one_millon))

#odd_numbers = list(range(1,900,2))
#print(odd_numbers)

for odd in range(1,20,2):
	print(odd)


multiples_3 = [value for value in range(3,31,3)]
print(multiples_3)

multiples = []
for value in range (3,31,3):
	multiples.append(value)
print(multiples)

cube = [value**2 for value in range(1,11)]
print(cube)

cubes =[]
for value in range(1,11):
	cubes.append(value**2)

print(cubes)
