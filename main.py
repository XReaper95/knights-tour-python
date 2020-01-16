import tkinter as tk
from utils import center_windows

root = tk.Tk()
root.title("Knight`s tour")

cell_x = 20
cell_y = 13
board_size_factor = 4
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

        last_label = tk.Canvas(root, bg=color, padx=cell_x, pady=cell_y, name=cell_name, image=img)
        last_label.grid(row=x, column=y)

        cells.append(cell_name)
        dark = not dark

print(cells)

if __name__ == '__main__':
    center_windows(root)
    root.mainloop()
