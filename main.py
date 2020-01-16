import tkinter as tk
from utils import center_windows

root = tk.Tk()
root.title("Knight`s tour")
root.resizable = False

cell_size = 45
board_size_factor = 8
dark = False
cells = []
last_label = None
img = tk.PhotoImage(file="chess_knight.png")

if board_size_factor < 4:
    print("Board size must be 4 or bigger, setting to minimum")
    board_size_factor = 4

for x in range(0, board_size_factor):
    dark = not dark
    for y in range(0, board_size_factor):
        color = '#0e140c' if dark else '#a7ab90'
        cell_name = "({0}, {1})".format(x, y)

        last_label = tk.Canvas(root, bg=color, width=cell_size, height=cell_size, name=cell_name)
        last_label.grid(row=x, column=y)

        cells.append(cell_name)
        dark = not dark

last_label.create_image((cell_size / 2, cell_size / 2), image=img)
print(cells)

if __name__ == '__main__':
    center_windows(root)
    root.mainloop()
