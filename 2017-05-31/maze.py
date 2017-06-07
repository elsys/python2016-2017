import turtle


class Cell(object):
	STEP = 20

	LEFT = 0
	DOWN = 1
	RIGHT = 2
	UP = 3

	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.walls = [True, True, True, True]

	def has_wall(self, direction):
		assert self.LEFT <= direction and direction <= self.UP
		return self.walls[direction]
	
	def drill_wall(self, direction):
		assert self.LEFT <= direction and direction <= self.UP
		self.walls[direction] = False

	def build_wall(self, direction):
		assert self.LEFT <= direction and direction <= self.UP
		self.walls[direction] = True
	
	def draw(self):
		turtle.goto(self.col*self.STEP, self.row*self.STEP)
		turtle.setheading(270)
		for direction in range(4):
			if self.has_wall(direction):
				# draw wall
				turtle.pendown()
			else:
				# no wall
				turtle.penup()
			turtle.forward(self.STEP)
			turtle.left(90)
		turtle.penup()
			

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

	def draw(self):
		for row in range(self.rows):
			for col in range(self.cols):
				cell=self[row,col]
				cell.draw()
		


if __name__=="__main__":
	turtle.speed(0)
	turtle.hideturtle()
	
	b = Board(5, 6)
	b.draw()
	
	input("Please enter something: ")

