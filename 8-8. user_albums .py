def make_album(artist,album,track = 0):
	album = {
	'artist': artist.title(),
	'album' : album.title()
	}

	if tracks:
		album['tracks'] = tracks
	return album	
		
print('Press "q" anytime to quit')

artist_names = 'Whats is the name of your artist?'
album_names = 'Whats is the name of your album?'
track = 'How many tarcks?'

while True:
	artist = input(artist_names)
	if artist == 'q':
		break
	album = input(album_names)
	if album == 'q':
		break
	tracks = input(track)
	if tracks == 'q':
		break 
	album = make_album(artist,album,track = 0) 
	print(album)

print("\nThanks for responding!")
def show_messges(input_):
	print(input_)

message = ['ana maria quer sabao', 'pedro quer feijao']
show_messges(message)