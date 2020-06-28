info = {'name':'mario','last_name':'armario','number':'9548881452'}
print(info['name'])
print(info['last_name'])
print(info['number'])
print(info['name'],"is  lazy")
print(f"{info['name']} is super lazy")

languages = {
	'mario':'python',
	'maria' : 'c',
	'kevin':'ruby',
	'xavier':'basic'
}

for name , language in languages.items():
	print(f"{name.title()} favorite language is {language.title()}")

for name in languages:
	print(name.title())
print(f"\n")
for name in languages.keys():
	print(f"{name.title()}")
	
for name in languages.values():
	print(f"{name.title()}")