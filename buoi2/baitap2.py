'''
bài tập:
cho danh sách friends = ['jen', 'jack', 'kenny', 'jelly', 'bob', 'henry', 'anne']
lấy ra 4 người bạn đầu tiên trong list
lấy ra 4 người bạn cuối cùng trong list
đảo ngược list
lấy ra những người bạn từ vị trí 1 đến hết
copy danh sách ban đầu thành 1 danh sách mới
lấy ra những người bạn từ vị trí 2 đến gần cuối
'''
# cho danh sách friends = ['jen', 'jack', 'kenny', 'jelly', 'bob', 'henry', 'anne']
friend_list = ['jen', 'jack', 'kenny', 'jelly', 'bob', 'henry', 'anne']
print(f'danh sach ban be: {friend_list}')

# lấy ra 4 người bạn đầu tiên trong list
print(f'lay 4 ten dau{friend_list[0:4]}')

# lấy ra 4 người bạn cuối cùng trong list
print(f'lay 4 ten cuoi{friend_list[-5:-1]}')

# đảo ngược list
friend_list.reverse()
print(f'danh sach sau khi bi dao nguoc {friend_list}')

# lấy ra những người bạn từ vị trí 1 đến hết
friend_list = ['jen', 'jack', 'kenny', 'jelly', 'bob', 'henry', 'anne']
friend_list.remove('jen')
print(f'danh sach lay tu vi tri so 1 {friend_list}')

# copy danh sách ban đầu thành 1 danh sách mới
friend_list_copy = friend_list.copy()
print(f'danh sach copy: {friend_list_copy}')

# lấy ra những người bạn từ vị trí 2 đến gần cuối
friend_list = ['jen', 'jack', 'kenny', 'jelly', 'bob', 'henry', 'anne']
print(f'danh sach tu vi tri so 2 den gan cuoi: {friend_list[2:5]}')