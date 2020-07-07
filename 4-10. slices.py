fav_pizza = ['Neapolitan Pizza','Chicago Pizza','New York-Style Pizza']

print(f'The frist tree otems on this list are:')
print(*fav_pizza,sep='\n')

print(f'The item on the middelon the list is:')
print(fav_pizza[int(len(fav_pizza)/2)])

print("The last item of the list is:")
print(fav_pizza[-1])