def make_album(artist,album,tracks = 0):
	album = {
	'artist': artist.title(),
	'album' : album.title()
	}

	if tracks:
		album['tracks'] = tracks	
		
	return album

album = make_album('Jonh','7 Pistols',1)
print(album)