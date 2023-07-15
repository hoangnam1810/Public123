'''tạo 1 chương trình cho phép xem, thêm, sửa, xóa, xem, tìm kiếm, cập nhật danh sách các bộ phim
'''
'''
USER_MENU = 
a - thêm 1 bộ phim 
l - hiển thị các bộ phim theo tên
s - tìm kiếm các bộ phim theo tên
x - xóa phim theo tên
u - cập nhật thông tin phim
q - thoát
Lựa chọn của bạn: 
'''

# thêm phim
movies = {}

def add_movie():
    name = input('Nhap ten phim: ')
    prev = movies.keys()
    while name in prev:
        print('ten phim bi trung vui long nhap lai')
        name = input('Nhap ten phim: ')
    director = input('Nhap ten dao dien: ')
    release_year = input('Nhap nam san xuat: ')
# tạo danh sách
    movie = {
        'name': name,
        'director': director,
        'release_year' : release_year
    }
    movies[name] = movie
    print('da them phim')

# hiển thị bộ phim
def display_movies():
    if len(movies) == 0:
        print('khong co phim')
    else:
        for name, movie in movies.items():
            print(f'name: {movie["name"]}')
            print(f'Đạo diễn: {movie["director"]}')
            print(f'Năm sản xuất: {movie["release_year"]}')
# kiếm phim
def search_movies():
    if len(movies) == 0:
        print('khong co phim')
    else:
        tu_khoa = input('nhap tu khoa tim kiem: ')
        for name, movie in movies.items():
            if tu_khoa.lower() in movie['name'].lower():
                print(f'name: {movie["name"]}')
                print(f'Đạo diễn: {movie["director"]}')
                print(f'Năm sản xuất: {movie["release_year"]}')

# sửa thông tin
def update_movie():
    if len(movies) == 0:
        print('khong co phim')
    else:
        name = input('nhap ten phim muon thay the: ')
        if name in movies:
            movie = movies[name]
            print(f'name: {movie["name"]}')
            print(f'director: {movie["director"]}')
            print(f'release_year: {movie["release_year"]}')

# bắt đầu thay thế
            director = input('nhap ten dao dien moi:  ')
            release_year = input('nhap nam san xuat moi: ')
            movie['director'] = director
            movie['release_year'] = release_year

            print('da cap nhat phim')
        else:
            print('khong co phim nay trong danh sach')

# xóa
def delete_movie():
    if len(movies) == 0:
        print('khong co phim')
    else:
        name = input('nhap tu khoa phim muon xoa:  ')
        if name in movies:
            movies.pop(name)
            print('da xoa phim')
        else:
            print('khong co phim nay trong danh sach')

# menu chọn
def user_menu():
    while True:
        print('USER_MENU:')
        print('a - Thêm một bộ phim')
        print('l - Hiển thị danh sách các bộ phim')
        print('s - Tìm kiếm các bộ phim theo tên')
        print('u - Cập nhật thông tin phim')
        print('d - Xóa phim theo tên')
        print('q - Thoát')
        choice = input('Lựa chọn của bạn: ')
        if choice == 'a':
            add_movie()
        elif choice == 'l':
            display_movies()
        elif choice == 's':
            search_movies()
        elif choice == 'u':
            update_movie()
        elif choice == 'd':
            delete_movie()
# nhấn q thì ra khỏi lựa chọn kết thúc chương trình
        elif choice == 'q':
            break
        else:
            print('Lựa chọn không hợp lệ.')

user_menu()
