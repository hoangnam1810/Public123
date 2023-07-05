"""  
bài tập: nhập vào 1 tháng, kiểm tra xem tháng đó có bao nhiêu ngày. nếu là tháng 2 yêu cầu nhập thêm năm, năm không nhuận có 28 ngày, năm nhuận có 29 ngày
 """

month = int(input('nhap thang '))

lst1 = [1, 3, 5, 7, 8, 10, 12]
lst2 = [4, 6, 9, 11]
if month == lst1:
    print('co 31 ngay')
elif month == 2:
    year = int(input('nhap nam'))
    if year % 4 == 0:
        print('nam nhuan co 29 ngay')
    else:
        print('nam thuong co 28 ngay')
else:
    print('co 30 ngay')

