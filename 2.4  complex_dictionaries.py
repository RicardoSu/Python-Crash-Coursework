infos = {
	'amario':{
	'name':'mario',
	'last_name':'armario',
	'number':'9548881452'
	}, 

	'bmaria':{
	'name':'maria',
	'last_name':'biberes',
	'number':'9548881453'	
	},

	'zmark':{
	'name':'mark',
	'last_name':'zifonic',
	'number':'9546821455'
	}
	}

for info in infos.values():
	print(f"{info}")
for info in infos.values():
	print(f"Employee name {info['name']} {info['last_name']} and phone {info['number']} ")
