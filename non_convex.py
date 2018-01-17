from random import random, getrandbits
from numpy import sqrt

alts = [[10.0, 100.0], [75.0, 75.0], [100.0, 10.0], [200.0, 200.0], [101.0, 150.0], [90.0, 300.0], [169.0, 30.0]]

with open("data_non_convex.dat", "w") as out:
	for n in range(10000):
		r1 = random()
		r2 = sqrt(1.0 - r1 ** 2.0)#1 - r1#random() * 2#sqrt(1.0 - r1 ** 2.0)
		i = 0
		score = []
		for alt in alts:
			i += 1
			score.append(r1 * alt[0] + r2 * alt[1])
		minim = score.index(min(score))
		out.write("{}\n".format(minim))


# if __name__ == '__main__':
# 	x = y = 0.0
# 	def rand(x):
# 		if x < 0.5:
# 			rand = 0.0
# 		else:
# 			if random() < 0.5:
# 				rand = - 1.0
# 			else:
# 				rand = 1.0
# 		return rand

# 	with open("automata.dat", "w") as out:
# 		for n in range(100000):
# 			move_x = rand(random())
# 			x += move_x
# 			if move_x == 0.0:
# 				y += rand(random())
# 			out.write("{} {} {}\n".format(n, x, y))
