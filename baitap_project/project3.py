USER_MENU = '''
a - thêm sách
l - hiển thị sách
s - tìm kiếm sách
x - xóa sách
u - cập nhật thông tin sách
q - thoát
Lựa chọn của bạn:
=> '''
book_file = 'books.csv'

try:
    with open(book_file, 'x') as file:
        file.read()
except:
    print('khong mo duoc file')


def add_book():
    title = input('nhap ten sach: ').strip().title()
    author = input('nhap ten tac gia: ').strip().title()
    release_year = input('nhap nam xuat ban: ').strip()

    with open(book_file, 'a') as file:
        file.write(f'{title},{author},{release_year}\n')

    return title, author, release_year

def show_book(line):
    title, author, release_year = line.strip().split(',')
    print(f'Title: {title} - Author: {author}, Release year: {release_year}')


def get_book():
    with open(book_file, 'r') as file:
        for line in file:
            show_book(line)


# tìm
def search_book():
    search_title = input('nhap ten sach can tim: ').strip().lower()
    with open(book_file, 'r') as file:
        for line in file:
            title,_,_, = line.strip().split(",")
            if title.lower() in search_title:
                show_book(line)
                break
        else:
            print('khong tim thay thong tin sach')

# cập nhật
def update_book():
    search_title = input('Nhap ten sach can tim: ').strip().title()
    found = False

    with open(book_file, 'r') as file:
        lines = file.readlines()

    with open(book_file, 'w') as file:
        for line in lines:
            title, _, _, = line.strip().split(",")
            if title == search_title:
                new_author = input('Nhap ten tac gia moi: ').strip().title()
                new_release = input('Nhap nam san xuat moi: ').strip().title()
                found = True
                line = f'{title},{new_author},{new_release}\n'
            file.write(line)

    if not found:
        print(f'{search_title} khong ton tai')
    else:
        print('Da cap nhat')


# xóa
def delete_book():
    search_title = input('Nhap ten sach can xoa: ').strip().title()
    found = False

    with open(book_file, 'r') as file:
        lines = file.readlines()

    with open(book_file, 'w') as file:
        for line in lines:
            title, _, _, = line.strip().split(",")
            if title != search_title:
                file.write(line)
            else:
                found = True

    if not found:
        print(f'{search_title} khong ton tai trong danh sach')
    else:
        print(f'Da xoa sach {search_title} khoi danh sach.')

# menu
choice_options = {
    'a': add_book,
    'l': get_book,
    's': search_book,
    'x': delete_book,
    'u': update_book,
}

while True:
    choice = input(USER_MENU).strip().lower()

    if choice == 'q':
        print('Cam on ban da su dung chuong trinh!')
        break

    action = choice_options.get(choice)
    if action:
        action()
    else:
        print('Lua chon khong hop le. Vui long chon lai.')