def gameOfLife(A):
	
	if not A or not A[0]:
		return

	m, n = len(A), len(A[0])

	for i in range(m):
		for j in range(n):
			cur = 0
			for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
				if x >= 0 and x < m and y >= 0 and y < n:
					if A[x][y] == 1 or A[x][y] == -1 or A[x][y] == -2:
						cur += 1
			if A[i][j] == 1:
				if cur == 2 or cur == 3:
					A[i][j] = -1 # live -> live
				else:
					A[i][j] = -2 # live -> die
			else:
				if cur == 3:
					A[i][j] = -3 # die -> live
				else:
					A[i][j] = -4 # die -> die

	for i in range(m):
		for j in range(n):
			A[i][j] = (1 if A[i][j] == -1 or A[i][j] == -3 else 0) 
    print(A)
a=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
gameOfLife(a)
