a = [ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
	[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
	[21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
	[31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
	[41, 42, 43, 44, 45, 46, 47, 48, 49, 50] ]

def sum(x1,y1,x2,y2) :
	try : 
		ans = 0
		for i in range(y1, y2 + 1) :
			for j in range(x1, x2 + 1) :
				ans += a[i][j]
		return ans
	except IndexError as e:
		print("loi tran mang")