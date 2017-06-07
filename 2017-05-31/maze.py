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
		self.visited = False

	@staticmethod
	def oposite_direction(direction):
		return (direction + 2) % 4

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
	
	def set_visited(self, visited=True):
		self.visited = visited


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

	def get_neighbour(self, cell, direction):
		assert Cell.LEFT <= direction and direction <= Cell.UP
		if direction == Cell.LEFT:
			row = cell.row
			col = cell.col - 1
		elif direction == Cell.RIGHT:
			row = cell.row
			col = cell.col + 1
		elif direction == Cell.UP:
			row = cell.row + 1
			col = cell.col
		elif direction == Cell.DOWN:
			row = cell.row - 1
			col = cell.col
		if row < 0 or row >= self.rows or \
				col < 0 or col >= self.cols:
			return None
		return self[row, col]

	def drill_wall(self, cell, direction):
		cell.drill_wall(direction)
		neighbour = self.get_neighbour(cell, direction)
		if neighbour is not None:
			oposite = Cell.oposite_direction(direction)
			neighbour.drill_wall(oposite)

	def get_unvisited_neighbours(self, cell):
		neighbours = []
		for direction in range(4):
			neighbour = self.get_neighbour(cell, direction)
			if neighbour is not None and not neighbour.visited:
				neighbours.append(neighbour)
		return neighbours


if __name__=="__main__":
	turtle.speed(0)
	turtle.hideturtle()
	
	b = Board(5, 6)
	c = b[0,0]
	b.drill_wall(c, Cell.UP)

	b.draw()

	
	input("Please enter something: ")

