


class Cell(object):
	UP = 0
	LEFT = 1
	DOWN = 2
	RIGHT = 3

	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.walls = [True, True, True, True]

	
class Board(object):
	
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		
		self.cells = [
			Cell(i // self.cols, i % self.cols) 
			for i in range(self.rows*self.cols)
		]
	
	def __getitem__(self, index):
		n, m = index
		assert 0 <= n and n < self.rows
		assert 0 <= m and m < self.cols
		return self.cells[n * self.cols + m]

