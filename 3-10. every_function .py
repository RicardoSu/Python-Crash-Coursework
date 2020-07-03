grocery_list = [
'spinach','arugula', 'kale','broccoli',
'cauliflower','bell peppers', 'zucchini',
'carrots', 'asparagus','cabbage', 'cucumbers',
'celery', 'carrots', 'onions', 'garlic',
]


grocery_list.append('grapes')
grocery_list.insert(len(grocery_list),'lettuce')
print(int(len(grocery_list)))
del grocery_list[(len(grocery_list))-1]
grocery_list.pop()
grocery_list.pop()
grocery_list.remove('onions')

print(grocery_list)

for i in grocery_list:
	print(i.title())
