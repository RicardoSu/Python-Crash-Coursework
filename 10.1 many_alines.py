aliens = []

for alien in range(30):
	alien = {'color':'green','points':'5','speed':'slow'}
	aliens.append(alien)

for alien in aliens[:3]:
	if alien['color']=="green":
		alien['color']="orange"
		alien['points']="10"
		alien['speed']="medium"
	elif alien['color']=="orange":
		alien['color']="red"
		alien['points']="15"
		alien['speed']="fast"
	

for alien in aliens[:5]:
	print(alien)

print("...")

print(f"Total of aliens {len(aliens)}")