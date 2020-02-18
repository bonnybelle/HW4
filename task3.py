# 3. Дается строка - нужно проверить является ли она валидным паролем:
# (1) длина больше 4 символов,
# (2) содержит только маленькие латинские буквы и цифры,
# (3) число букв должно быть нечетным, а цифр четным.

s = input('Password: ')
t1 = len(s)
answer = 'NO'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
alp_cnt = 0
num_cnt = 0
for symbol in s:
    alp_cnt += 1 if symbol in alphabet else 0
    num_cnt += 1 if symbol in numbers else 0
if alp_cnt % 2 > 0 and num_cnt % 2 == 0 and t1 > 4:
    print('That`s a good password')
else:
    print('NO')
