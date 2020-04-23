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

	def iterative(rand_range):
		square_length = size-1
		curr_range = rand_range
		while square_length >= 2:
			# diamond step
			for y in range(0, size-1, square_length):
				for x in range(0, size-1, square_length):
					print(square_length)
					mid_x = (2*x + square_length) // 2
					mid_y = (2*y + square_length) // 2

					grid[mid_y][mid_x] = (grid[y][x] + grid[y][x+square_length] + grid[y+square_length][x] + grid[y+square_length][x+square_length]) / 4
					grid[mid_y][mid_x] += rand.randint(0, rand_range)

			# square step
			for y in range(0, size-1, square_length):
				for x in range(0, size-1, square_length):
					mid_x = (2*x + square_length) // 2
					mid_y = (2*y + square_length) // 2

					grid[mid_y][x] = grid[mid_y][mid_x] + grid[y][x] + grid[y+square_length][x]
					grid[mid_y][x+square_length] = grid[mid_y][mid_x] + grid[y+square_length][x+square_length] + grid[y][x+square_length]
					grid[y][mid_x] = grid[mid_y][mid_x] + grid[y][x] + grid[y][x+square_length]
					grid[y+square_length][mid_x] = grid[mid_y][mid_x] + grid[y+square_length][x] + grid[y+square_length][x+square_length]

					# handle edge elements
					neighbor_dist = mid_x - x
					if x == 0:
						grid[mid_y][x] /= 3
					else:
						grid[mid_y][x] += grid[mid_y][x - neighbor_dist]
						grid[mid_y][x] /= 4

					if y == 0:
						grid[y][mid_x] /= 3
					else:
						grid[y][mid_x] += grid[y - neighbor_dist][mid_x]
						grid[y][mid_x] /= 4

					if x+square_length == size-1:
						grid[mid_y][x+square_length] /= 3
					else:
						grid[mid_y][x+square_length] += grid[mid_y][x+square_length + neighbor_dist]
						grid[mid_y][x+square_length] /= 4

					if y+square_length == size-1:
						grid[y+square_length][mid_x] /= 3
					else:
						grid[y+square_length][mid_x] += grid[y+square_length + neighbor_dist][mid_x]
						grid[y+square_length][mid_x] /= 4

					grid[mid_y][x] += rand.randint(0, rand_range)
					grid[mid_y][x+square_length] += rand.randint(0, rand_range)
					grid[y][mid_x] += rand.randint(0, rand_range)
					grid[y+square_length][mid_x] += rand.randint(0, rand_range)
			
			square_length //= 2
			curr_range //= 2
		


	# grid initialization
	grid[0][0] = 56
	grid[0][size-1] = 56#86
	grid[size-1][0] = 56#43
	grid[size-1][size-1] = 56#89

	#recursion(0, 0, size-1, size-1, 200)
	iterative(200)

	return grid

terrain = diamond_square(9)
print(terrain)
plt.imshow(terrain)
plt.show()