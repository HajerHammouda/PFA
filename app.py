import matplotlib as mpl
mpl.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk


def load_figure(figure, canvas):
	plot = figure.add_subplot(111)
	plot.clear()
	x = arange(0.0, 3.0, 0.01)
	y = sin(2*pi*x)
	plot.plot(x, y)
	canvas.draw()


def main():
	root = tk.Tk()
	root.wm_title("Matplotlib in Tkinter")

	figure = Figure(figsize=(5, 4), dpi=100)
	canvas = FigureCanvasTkAgg(figure, master=root)
	canvas.draw()
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	button = tk.Button(master=root, text="Show Figure", command=lambda: load_figure(figure, canvas))
	button.pack()

	root.mainloop()


if __name__ == '__main__':
	main()
