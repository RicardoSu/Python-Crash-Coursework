def make_car(model, name, **features):
	profile = {}
	profile['model'] = model
	profile['model name'] = name

	for key,value in features.items():
		profile[key] = value

	return profile