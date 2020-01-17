import tkinter as tk
from utils import center_windows

root = tk.Tk()
root.title("Knight`s tour")
root.resizable = False

cell_size = 40
board_size_factor = 8
dark = False
cells = {}
img = tk.PhotoImage(file="chess_knight.png")

if board_size_factor < 4:
    print("Board size must be 4 or bigger, setting to minimum")
    board_size_factor = 4

for x in range(0, board_size_factor):
    dark = not dark
    for y in range(0, board_size_factor):
        color = '#0e140c' if dark else '#a7ab90'
        cell_name = (x, y)

        cells[cell_name] = tk.Canvas(root, bg=color, width=cell_size, height=cell_size, highlightthickness=0)
        cells[cell_name].grid(row=x, column=y)

        dark = not dark

create_pieces = list()
create_pieces.append((7, 7))

for cell in create_pieces:
    target = cells[cell]
    target.create_image((target.winfo_reqwidth() / 2, target.winfo_reqheight() / 2), image=img)

for key in cells.keys():
    print(key)

if __name__ == '__main__':
    center_windows(root)
    root.mainloop()
