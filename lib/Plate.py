class Plate:

	def __init__(self, **kwargs):

		import numpy as np

		self.grids = []

		self.iterations = kwargs['iter']

		self.xmax = kwargs['xmax']
		self.ymax = kwargs['ymax']

		self.top = kwargs['top']
		self.bottom = kwargs['bottom']
		self.left = kwargs['left']
		self.right = kwargs['right']

		self.initial_temp = kwargs['initial_temp']

		self.grid = np.zeros((self.xmax, self.ymax))

	def solve(self):
		"""
		Compute the steady-state temperature distribution of the plate.
		Finite-Difference Formulation of Differential Equation
		"""

		import time

		# Manually set boundary temperatures
		self.grid[0, :] = self.top
		self.grid[-1, :] = self.bottom
		self.grid[:, 0] = self.left
		self.grid[:, -1] = self.right

		start = time.time()

		# Take the average temperature of each node's neighbors. More iterations = more accurate solution
		for n in range(self.iterations):
			self.grid[1:-1, 1:-1] = 0.25*(self.grid[:-2, 1:-1] + self.grid[2:, 1:-1] + self.grid[1:-1, :-2] + self.grid[1:-1, 2:])
			#print(self.grid)
			self.grids.append(self.grid.copy())

		# Manually calculate the temperature at the corners
		self.grid[0, 0] = 0.5 * (self.grid[1, 0] + self.grid[0, 1])  # Upper left
		self.grid[-1, 0] = 0.5 * (self.grid[-2, 0] + self.grid[-1, 1])  # Lower left
		self.grid[0, -1] = 0.5 * (self.grid[0, -2] + self.grid[1, -1])  # Upper right
		self.grid[-1, -1] = 0.5 * (self.grid[-1, -2] + self.grid[-2, -1])  # Lower right

		end = time.time() - start

		print('Time elapsed: {time} s'.format(time=end))

	# def solve(self):
	# 	start = self.time.time()
	#
	# 	# Manually set boundary temperatures
	# 	self.grid[0, :] = self.top
	# 	self.grid[-1, :] = self.bottom
	# 	self.grid[:, 0] = self.left
	# 	self.grid[:, -1] = self.right
	#
	# 	# Finally, iterate over grid
	# 	for n in range(self.ITERATIONS):
	# 		for x in range(1, self.xmax - 1):
	# 			for y in range(1, self.ymax - 1):
	# 				self.grid[x, y] = 0.25 * (self.grid[x - 1, y] + self.grid[x, y - 1] + self.grid[x, y + 1] + self.grid[x + 1, y])
	#
	# 	# Manually calculate the temperature at the corners
	# 	self.grid[0, 0] = 0.5 * (self.grid[1, 0] + self.grid[0, 1])  # Upper left
	# 	self.grid[-1, 0] = 0.5 * (self.grid[-2, 0] + self.grid[-1, 1])  # Lower left
	# 	self.grid[0, -1] = 0.5 * (self.grid[0, -2] + self.grid[1, -1])  # Upper right
	# 	self.grid[-1, -1] = 0.5 * (self.grid[-1, -2] + self.grid[-2, -1])  # Lower right
	#
	# 	end = self.time.time() - start
	#
	# 	print('Time elapsed: {time} s'.format(time=end))

