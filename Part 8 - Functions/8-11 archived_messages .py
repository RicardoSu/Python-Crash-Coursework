def send_messages(messages):
	message_list = []
	for message in messages:
		print(message)
		message_list.append(message)
		

	hidden_messages = []

	for message in reversed(message_list):
		hidden = message_list.pop()
		hidden_messages.append(hidden)

	print(message_list)
	print(hidden_messages)

cypher = [
	'EnCt2c3671f5ee35bf8d79d84fed7846ceeba78757ef7c3671f5ee35bf8d79d84fed7w+Flbiu+AgB',
	'msEk1CV9mcL2MN5yKeeOEsaeUJSmfBLgJAvKbQ4LI4gFZkWIAU9OYHRbDtBinIjagiNXdzH81R+IN8',
	'NNeh20AJQvlG9KKn398B8fzvjfGZLkx02iJ+6QUzQoO3b4Ybm5HI5tALhRMgtseyWXpAZgFFBocWS4HY'
]

send_messages(cypher)