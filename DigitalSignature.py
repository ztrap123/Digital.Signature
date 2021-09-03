
import math
# Tìm Ước Chung Lớn Nhất
def euclid(m, n):
	
	if n == 0:
		return m
	else:
		r = m % n
		return euclid(n, r)
	
	
# Chương trình tìm số nghịch đảo
def exteuclid(a, b):
	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:
		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a
		
	return (r1, t1)

# Nhập 2 số nguyên tố lớn
prime = []
for ps in range(200,1000):
	cou=0
	for i in range(2,int(math.sqrt(ps)+1)):
		if ps%i==0:
			cou+=1
	if cou==0:
		prime.append(ps)
print(prime)
p = int(input())
q = int(input())
n = p * q
Pn = (p-1)*(q-1)

# Tạo khóa mã hóa
# Trong khoảng 1<e<Pn
key = []

for i in range(2, Pn):
	
	gcd = euclid(Pn, i)
	
	if gcd == 1:
		key.append(i)


# Chọn khóa từ danh sách trên
print(key)
e = int(input())

# Lấy số đối của Khóa Z_Pn
r, d = exteuclid(Pn, e)
if r == 1:
	d = int(d)
	print("Khóa giải mã là: ", d)
	
else:
	print("Số nghịch đảo cho\
	khóa mã hóa không tồn tại. \
	Chọn khóa mã hóa khác ")


# Nhập tin nhắn M
M = int(input('Tin nhắn:'))

# Chữ ký S được tạo bởi Alice
S = (M**d) % n

# Alice gửi M và S cho Bob
# Bob tạo tin nhắn M1 bằng chữ ký S, Khóa công khai của Alice e và n.
M1 = (S**e) % n

# Nếu M = M1 thì Bob chấp nhận tin nhắn được gửi từ Alice.

if M == M1:
	print("Vì M = M1, Tin nhắn được\
	gửi từ Alice")
else:
	print("Vì M khác M1, Tin nhắn\
   không gửi từ Alice")
print('M: ',M1)