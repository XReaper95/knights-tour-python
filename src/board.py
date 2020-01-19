import tkinter as tk


class Board:
    def __init__(self, cell_size, board_size):
        self._cell_size = cell_size

        if board_size < 4:
            print("Board size must be 4 or bigger, setting to minimum")
            self.size = 4
        elif board_size > 15:
            print("Board too big, setting to maximum")
            self.size = 15
        else:
            print(f"Creating {board_size}x{board_size} board")
            self.size = board_size

        self._cells = {}
        self._dark_color = '#0e140c'
        self._clear_color = '#a7ab90'
        self._piece_tag = 'k'
        self._img = tk.PhotoImage(file="assets/chess_knight.png")
        self._knight_pos = None

    def generate(self, root_widget):
        black = self._dark_color
        white = self._clear_color
        color = black

        for x in range(self.size):
            if self.size % 2 == 0:
                color = black if color is white else white

            for y in range(0, self.size):
                self._cells[(x, y)] = tk.Canvas(root_widget, bg=color,
                                                width=self._cell_size, height=self._cell_size, highlightthickness=0)
                self._cells[(x, y)].grid(row=x, column=y)
                self._cells[(x, y)].tag_raise(self._piece_tag)

                color = black if color is white else white

    def get_cell(self, cell_x, cell_y):
        if cell_x < self.size and cell_y < self.size:
            return self._cells[(cell_x, cell_y)]
        else:
            print(f"Error creating piece at ({cell_x}, {cell_y}), cell out of board.")
            return None

    def print_cells(self):
        print(f"Cells: {len(self._cells)}")

        for cell_name in self._cells:
            print(cell_name)

    def create_knight(self, cell_x, cell_y):
        if self._knight_pos:
            self._knight_pos.delete(self._piece_tag)

        target_cell = self.get_cell(cell_x, cell_y)
        if target_cell:
            target_cell.create_image((target_cell.winfo_reqwidth() / 2, target_cell.winfo_reqheight() / 2),
                                     image=self._img, tag=self._piece_tag)
            self._knight_pos = target_cell
