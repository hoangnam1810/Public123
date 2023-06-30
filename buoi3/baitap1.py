'''
1. cho 2 set
art_student = {'john', 'anne', 'max', 'bob', 'obito'}
math_student = {'max', 'maery', 'david', 'anne', 'john'}
- tìm những sinh viên học cả 2 môn
- tìm những người học vẽ nhưng không học toán
- tìm những người học toán nhưng không học vẽ
- tìm những người bạn học vẽ hay toán không phải cả 2
- tìm tất cả người
'''
# cho 2 set 
'''
art_student = {'john', 'anne', 'max', 'bob', 'obito'}
math_student = {'max', 'maery', 'david', 'anne', 'john'}
'''
# tìm những sinh viên học cả 2 môn
art_student = {'john', 'anne', 'max', 'bob', 'obito'}
math_student = {'max', 'maery', 'david', 'anne', 'john'}
student_learn_all = art_student.intersection(math_student)
print(f'sinh vien hoc ca 2 mon: {student_learn_all}')

# tìm những người học vẽ nhưng không học toán
student_just_art = art_student.difference(math_student)
print(f'sinh vien hoc ve nnhung khong hoc toan: {student_just_art}')

# tìm những người học toán nhưng không học vẽ
student_just_math = math_student.difference(art_student)
print(f'sinh vien hoc ve nnhung khong hoc toan: {student_just_math}')

# tìm những người bạn học vẽ hay toán không phải cả 2
student_decry =  math_student.symmetric_difference(art_student)
print(f'sinh vien hoc ve hoac toan khong phai ca 2: {student_decry} ')

# tìm tất cả người
all_student = math_student.union(art_student)
print(f'tat ca sinh vien: {all_student} ')