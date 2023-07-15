# tạo 1 list bất kỳ đếm số phần tử trong list nếu phần tử cuối trong list > 0 thì xóa phần tử đó rồi thêm phần tử nhỏ hơn vào cuối list
lst=[1, 2, 3, 4, 5, 6, -1]
len_lst = len(lst)
print(f'do dai cua list la:{len_lst}')
if lst[-1] > 0:
    l = lst[-1]
    print(f'so lon hon 0 can xoa them so moi ')
    lst.pop()
    print(lst)
else:
    print('so be hon 0')
    m = int(input('nhap so lon hon 0: '))
    lst.append(m)
    print(lst)