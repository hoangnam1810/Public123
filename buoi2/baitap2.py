'''
bài tập:
tạo 1 movie_list chứa các bộ phim đã xem
sử dụng hàm input để nhập vào 1 bộ phim khác không có trong list trên
thêm bộ phim vừa nhập vào cuối danh sách list
in ra bộ phim ở đầu tiên, ở giữa và ở cuối danh sách
tính tổng bộ phim có trong list
xóa bộ phim đầu và cuối trong list
lấy ra và xóa bộ phim cuối trong list
chèn 1 bộ phim bất kì vào đầu danh sách
đếm số bộ phim có tiêu đề là "naruto"
tìm vị trí của bộ phim có tiêu đề là naruto
thêm một danh sách các bộ phim khác vào cuối danh sách movies ban đầu
xóa list
'''
# bài tập 1

# tạo 1 movie_list chứa các bộ phim đã xem
movies_list = ['sasuke','thor','naruto','suzume']
print(f'danh sach phim: {movies_list}')

# sử dụng hàm input để nhập vào 1 bộ phim khác không có trong list trên
movies_add = input('nhap phim: ')
print(movies_add)

# thêm bộ phim vừa nhập vào cuối danh sách list 
movies_list.append(movies_add)
print(movies_list)

# in ra bộ phim ở đầu tiên, ở giữa và ở cuối danh sách
'''đầu tiên'''
first_movie = movies_list[0]
print(first_movie)

'''ở giữa'''
len_mid_movie = len(movies_list)
mid_movie = movies_list[len_mid_movie // 2]
print(mid_movie)

'''ở cuối'''
last_movie = movies_list[-1]
print(last_movie)

'''tong'''
print(f'bo phim dau tien la: {first_movie}, bo phim o giua la: {mid_movie}, bo phim o cuoi la: {last_movie}')

# tính tổng bộ phim có trong list
len_movies = len(movies_list)
print(len_movies)

# xóa bộ phim đầu và cuối trong list
# del movies_list[first_movie,last_movie]
# print(f'sau khi xoa: {movies_list}')
print(movies_list.pop(0))

# lấy ra và xóa bộ phim cuối trong list
movies_list = ['sasuke','thor','naruto','suzume']
pop = movies_list.pop(0)
print(pop)
print(movies_list)

# chèn 1 bộ phim bất kì vào đầu danh sách
i = input('nhap 1 bo phim: ')
movies_list.insert(0,i)
print(movies_list)

# đếm số bộ phim có tiêu đề là "naruto"
movies_count = movies_list.count('naruto')
print(movies_count)

# tìm vị trí của bộ phim có tiêu đề là naruto
slicing_movies = movies_list.index('naruto')
print(slicing_movies)

# thêm một danh sách các bộ phim khác vào cuối danh sách movies ban đầu
extend_movies = ['sakura','kimi no nawa','1 manh']
movies_list.extend(extend_movies)
print(movies_list)

# xóa list
movies_list.clear()
print(movies_list)