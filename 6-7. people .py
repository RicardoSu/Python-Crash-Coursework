peoples = {
	'first_name':['felipe','mario','tamiris'],
	'last_name':['flores','armario','narcia'],
	'city':['panama','floripa','sao paulo'],
	'age':['17','29','20']
}
 

felipe = {'first_name':'felipe','last_name':'flores','age':'17','city':'panama'}
mario = {'first_name':'mario','last_name':'armario','age':'29','city':'floripa'}
tamiris = {'first_name':'tamiris','last_name':'narcia','age':'20','city':'sao paulo'}

for people,value in peoples.items():
	print(people,value[0])

for people,value in peoples.items():
	print(people,value[1])

for people,value in peoples.items():
	print(people,value[2])

