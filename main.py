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
        cells[cell_name].tag_raise('k')

        dark = not dark

# for key in cells.keys():
#     print(key)

cell1 = cells[(0, 0)]
cell2 = cells[(1, 1)]
cell3 = cells[(2, 2)]
cell4 = cells[(3, 3)]

cell1.create_line(cell1.winfo_reqwidth() / 2, cell1.winfo_reqheight() / 2, 40, 40, fill='red', width=1.5)
cell2.create_line(cell2.winfo_reqwidth() / 2, cell2.winfo_reqheight() / 2, 0, 0, fill='red', width=1.5)
cell2.create_line(cell2.winfo_reqwidth() / 2, cell2.winfo_reqheight() / 2, 40, 40, fill='red', width=1.5)
cell3.create_line(cell3.winfo_reqwidth() / 2, cell3.winfo_reqheight() / 2, 0, 0, fill='red', width=1.5)
cell3.create_line(cell3.winfo_reqwidth() / 2, cell3.winfo_reqheight() / 2, 40, 40, fill='red', width=1.5)
cell4.create_line(cell4.winfo_reqwidth() / 2, cell4.winfo_reqheight() / 2, 0, 0, fill='red', width=1.5)

create_pieces = list()
create_pieces.append((3, 3))

for cell in create_pieces:
    target = cells[cell]
    target.create_image((target.winfo_reqwidth() / 2, target.winfo_reqheight() / 2), image=img, tag='k')


if __name__ == '__main__':
    center_windows(root)
    root.mainloop()
