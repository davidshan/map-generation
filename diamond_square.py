import random as rand
import numpy as np
import matplotlib.pyplot as plt
import cv2

def diamond_square(n):
	size = 2**n + 1
	grid = np.zeros((size, size))

	#for i in range(size):
	#	column = []
	#	for j in range(size):
	#		column.append(0)
	#	grid.append(column)

	def recursion(start_x, start_y, end_x, end_y, rand_range):
		if end_y - start_y == 1:
			return None

		mid_x = (start_x + end_x) // 2
		mid_y = (start_y + end_y) // 2

		# diamond step

		grid[mid_y][mid_x] = (grid[start_y][start_x] + grid[start_y][end_y] + grid[end_y][start_x] + grid[end_y][end_x]) / 4
		grid[mid_y][mid_x] += rand.randint(0, rand_range)

		# square step
		# TODO: fix bug with mid_y end_x square step getting 0 midpoint ahead of it
		# in calculating average (also end_y mid_x)
		# Two solutions:
			# populate the four midpoints for the four subsquares beforehand, then run
			# the square step recursion on them
			# OR, calculate only using three averages for those.
			# Better to do option #1
		grid[mid_y][start_x] = grid[mid_y][mid_x] + grid[start_y][start_x] + grid[end_y][start_x]
		grid[mid_y][end_x] = grid[mid_y][mid_x] + grid[end_y][end_x] + grid[start_y][end_x]
		grid[start_y][mid_x] = grid[mid_y][mid_x] + grid[start_y][start_x] + grid[start_y][end_x]
		grid[end_y][mid_x] = grid[mid_y][mid_x] + grid[end_y][start_x] + grid[end_y][end_x]

		# handle edge elements
		neighbor_dist = mid_x - start_x
		if start_x == 0:
			grid[mid_y][start_x] /= 3
		else:
			grid[mid_y][start_x] += grid[mid_y][start_x - neighbor_dist]
			grid[mid_y][start_x] /= 4

		if start_y == 0:
			grid[start_y][mid_x] /= 3
		else:
			grid[start_y][mid_x] += grid[start_y - neighbor_dist][mid_x]
			grid[start_y][mid_x] /= 4

		if end_x == size-1:
			grid[mid_y][end_x] /= 3
		else:
			grid[mid_y][end_x] += grid[mid_y][end_x + neighbor_dist]
			grid[mid_y][end_x] /= 4

		if end_y == size-1:
			grid[end_y][mid_x] /= 3
		else:
			grid[end_y][mid_x] += grid[end_y + neighbor_dist][mid_x]
			grid[end_y][mid_x] /= 4

		grid[mid_y][start_x] += rand.randint(0, rand_range)
		grid[mid_y][end_x] += rand.randint(0, rand_range)
		grid[start_y][mid_x] += rand.randint(0, rand_range)
		grid[end_y][mid_x] += rand.randint(0, rand_range)

		# recursive step
		recursion(start_x, start_y, mid_x, mid_y, rand_range // 2)
		recursion(mid_x, start_y, end_x, mid_y, rand_range // 2)
		recursion(start_x, mid_y, mid_x, end_y, rand_range // 2)
		recursion(mid_x, mid_y, end_x, end_y, rand_range // 2)

	# grid initialization
	grid[0][0] = 56
	grid[0][size-1] = 56#86
	grid[size-1][0] = 56#43
	grid[size-1][size-1] = 56#89

	recursion(0, 0, size-1, size-1, 200)

	return grid

terrain = diamond_square(4)
plt.imshow(terrain)
plt.show()