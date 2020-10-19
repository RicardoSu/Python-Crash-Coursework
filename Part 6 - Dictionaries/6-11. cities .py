cities = {
'New York':{
	'state':'NY',
	'population':'8,175,133',
	'fun_fact':'More than 800 languages are spoken in New York City'
}, 
'Los Angeles':{
	'state':'CA',
	'population':'3,792,621',
	'fun_fact':'The famous Hollywood sign originally read “Hollywoodland.”'
}, 
'Chicago':{
	'state':'IL',
	'population':'8,175,133',
	'fun_fact':'The world’s first all-color television station'
}
}

for key,values in cities.items():
	print(f'{key} info:')
	for key,value in values.items():
		print(f'\t {key.title()}: {value}.')