from lib.Plate import Plate
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
	iterations = 1000

	plate = Plate(xmax=50, ymax=50, top=20, bottom=100, left=10, right=150, initial_temp=20, iter=iterations)
	plate.solve()

	fig, ax = plt.subplots()

	def animate(i):
		ax.clear()
		plt.contourf(plate.grids[i], 8, cmap='rainbow')
		ax.set_title('n = %d' % (i+1,))

		# i == 0 seems to happen twice, so add colorbar when i == 1
		if i == 1:
			plt.colorbar(label='Temperature')


	ani = animation.FuncAnimation(fig, animate, iterations, interval=10, blit=False, repeat=False)

	plt.show()


if __name__ == '__main__':
	main()
