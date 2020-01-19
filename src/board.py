import tkinter as tk


class Board:
    def __init__(self, cell_size, board_size):
        self._cell_size = cell_size

        if board_size < 4:
            print("Board size must be 4 or bigger, setting to minimum")
            self._board_size = 4
        else:
            self._board_size = board_size

        self._cells = {}
        self._dark_color = '#0e140c'
        self._clear_color = '#a7ab90'
        self._piece_tag = 'k'
        self._img = tk.PhotoImage(file="assets/chess_knight.png")

    def generate_board(self, root_widget):
        black = self._dark_color
        white = self._clear_color
        color = black

        for x in range(0, self._board_size):
            if self._board_size % 2 == 0:
                color = black if color is white else white

            for y in range(0, self._board_size):
                self._cells[(x, y)] = tk.Canvas(root_widget, bg=color,
                                                width=self._cell_size, height=self._cell_size, highlightthickness=0)
                self._cells[(x, y)].grid(row=x, column=y)
                self._cells[(x, y)].tag_raise(self._piece_tag)

                color = black if color is white else white

    def get_cell(self, cell_x, cell_y):
        return self._cells[(cell_x, cell_y)]

    def print_cells(self):
        for key in self._cells.keys():
            print(key)

    def create_piece(self, cell_x, cell_y):
        target = self._cells[(cell_x, cell_y)]
        target.create_image((target.winfo_reqwidth() / 2, target.winfo_reqheight() / 2),
                            image=self._img, tag=self._piece_tag)


