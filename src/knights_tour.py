import tkinter as tk

from src.board import Board
from src.path_finder import calculate_route
from src.utils import center_tkinter_windows


class KnightsTourWindow(tk.Tk):
    def __init__(self, size):
        super(KnightsTourWindow, self).__init__()
        self.title("Knight`s tour")
        self.resizable(False, False)

        self._board = Board(size, self)
        self._movements = calculate_route(size)
        self._step = 0
        self._movement_speed = 600

        self.__start()

    def move_piece(self):
        if self._step == len(self._movements):
            self._step = 0
            self._board.erase_path()

        x, y = self._movements[self._step]

        if self._step > 0:
            step_1 = self._movements[self._step - 1]
            step_2 = self._movements[self._step]
            cell_1 = self._board.get_cell(step_1[0], step_1[1])
            cell_2 = self._board.get_cell(step_2[0], step_2[1])
            self._board.draw_path(cell_1, cell_2)

        self._board.draw_point(self._board.get_cell(x, y))
        self._board.create_knight(x, y)
        self.after(self._movement_speed, self.move_piece)
        self._step += 1

    def __center_windows(self):
        center_tkinter_windows(self)

    def __start(self):
        self._board.generate()
        self._board.print_cells()
        self.after(0, self.move_piece)

        self.__center_windows()
        self.mainloop()
