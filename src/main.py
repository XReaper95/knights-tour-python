import tkinter as tk

from src.board import Board
from src.utils import center_windows

root = tk.Tk()
root.title("Knight`s tour")
root.resizable = False

board = Board(40, 10)
board.generate_board(root)

cell1 = board.get_cell(0, 0)
cell2 = board.get_cell(1, 1)
cell3 = board.get_cell(2, 2)
cell4 = board.get_cell(3, 3)

cell1.create_line(cell1.winfo_reqwidth() / 2, cell1.winfo_reqheight() / 2, 40, 40, fill='red', width=1.5)
cell2.create_line(cell2.winfo_reqwidth() / 2, cell2.winfo_reqheight() / 2, 0, 0, fill='red', width=1.5)
cell2.create_line(cell2.winfo_reqwidth() / 2, cell2.winfo_reqheight() / 2, 40, 40, fill='red', width=1.5)
cell3.create_line(cell3.winfo_reqwidth() / 2, cell3.winfo_reqheight() / 2, 0, 0, fill='red', width=1.5)
cell3.create_line(cell3.winfo_reqwidth() / 2, cell3.winfo_reqheight() / 2, 40, 40, fill='red', width=1.5)
cell4.create_line(cell4.winfo_reqwidth() / 2, cell4.winfo_reqheight() / 2, 0, 0, fill='red', width=1.5)

create_pieces = list()
create_pieces.append((3, 3))

for cell_x, cell_y in create_pieces:
    board.create_piece(cell_x, cell_y)


if __name__ == '__main__':
    center_windows(root)
    root.mainloop()
