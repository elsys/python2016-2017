import unittest
import maze

class BoardTest(unittest.TestCase):

	def setUp(self):
		self.board = maze.Board(5, 7)


	def test_board_size(self):
		self.assertEqual(len(self.board.cells), 5*7)

	def test_board_index(self):
		c = self.board[1,1]
		self.assertTrue(c)

	def test_board_bad_index(self):
		with self.assertRaises(AssertionError):
			self.board[-1, 0]
		with self.assertRaises(AssertionError):
			self.board[0, -1]
		with self.assertRaises(AssertionError):
			self.board[50, 0]
		with self.assertRaises(AssertionError):
			self.board[0, 50]

	def test_cell_position(self):
		c = self.board[1, 1]
		self.assertEqual(1, c.row)
		self.assertEqual(1, c.col)
		
		c = self.board[4, 3]
		self.assertEqual(4, c.row)
		self.assertEqual(3, c.col)
		
	def test_has_wall(self):
		c = self.board[1, 1]
		self.assertTrue(c.has_wall(maze.Cell.UP))
		self.assertTrue(c.has_wall(maze.Cell.DOWN))

	def test_drill_build_wall(self):
		c = self.board[1, 1]
		
		self.assertTrue(c.has_wall(maze.Cell.UP))
		
		c.drill_wall(maze.Cell.UP)
		self.assertFalse(c.has_wall(maze.Cell.UP))

		c.build_wall(maze.Cell.UP)
		self.assertTrue(c.has_wall(maze.Cell.UP))
		
	def test_get_neighbour(self):
		c = self.board[0,0]
		n = self.board.get_neighbour(c, maze.Cell.LEFT)
		self.assertIsNone(n)


if __name__=="__main__":
	unittest.main()

