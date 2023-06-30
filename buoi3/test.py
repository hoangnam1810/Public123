import json

album = {'album_name': 'Born Pink',
         'release_year': 2022}
print(json.dumps(album, indent=4))

value = album['album_name']
print(value)