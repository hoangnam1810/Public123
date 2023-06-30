'''
2. tạo ra 1 album nhạc:
- lấy ra giá trị của các key sau: album_name, release_year bằng 2 cách
- thay đổi giá trị của key release_year từ 1971 thành 1973
- xóa phàn tử với keey là track_list
- thêm 1 key mới là amount = 2000 bằng 2 cách
- làm trống dict album_info
'''

import json
# tạo ra 1 album nhạc
album = {'album_name': 'Born Pink',
         'release_year': 2022}
print(json.dumps(album, indent=4))
# cre google

# lấy ra giá trị của các key sau: album_name, release_year bằng 2 cách
# cách 1
name_release = album.values()
print(f'ten album va ngay ra mat: {name_release}')
# cách 2
value = album['album_name']
print(value)

# thay đổi giá trị của key release_year từ 1971 thành 1973
album['release_year'] = '1973'
print(json.dumps(album, indent=4)) 

# xóa phần tử với key là track_list
album = {'album_name': 'Born Pink',
         'track_list': 'Pink Venom',
         'release_year': 2022}
del_track = album.pop('track_list')
print(del_track)
print(json.dumps(album, indent=4)) 

# thêm 1 key mới là amount = 2000 bằng 2 cách
# cách 1
album.update(amount = '2000')
print(json.dumps(album, indent=4)) 
# cách 2
album['amount'] = '2000'
print(json.dumps(album, indent=4))

# làm trống dict album_info
album = {'album_name': 'Born Pink',
         'track_list': 'Pink Venom',
         'release_year': 2022}
album_info = album.clear()
print(album_info)