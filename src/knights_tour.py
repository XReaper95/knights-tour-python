import sys
import time
import tkinter as tk

from src.board import Board
from src.utils import center_tkinter_windows


class KnightsTour(tk.Tk):
    def __init__(self, size, path_finder, auto_reset):
        super(KnightsTour, self).__init__()
        self.title("Knight`s tour")
        self.resizable(False, False)

        self._min_size = 5
        self._max_size = 15
        self._movements = self.__calculate_path(path_finder, size)
        self._board = Board(size, self)
        self._step = 0
        self._movement_speed = 200
        self._auto_reset = auto_reset
        self._reset_timer_sec = 2
        self._resetting = False

        self.__run()

    def move_piece(self):
        if self._resetting:
            self._resetting = False
            self._board.erase_path()
            self._board.erase_knight()

        if self._step == len(self._movements):
            if self._auto_reset:
                self._resetting = True
                self._step = 0
                self.after(self._reset_timer_sec * 1000, self.move_piece)
                print(f"Resetting after {self._reset_timer_sec} seconds")
                return
            else:
                self._board.erase_background()
                self._board.erase_knight()
                print("Algorithm finished!")
                return

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

    def __calculate_path(self, path_finder, size):
        if size < self._min_size:
            print(f"Board size must be {self._min_size} or bigger")
            sys.exit(1)
        elif size > self._max_size:
            print("Board too big")
            sys.exit(1)

        algorithm = path_finder(size)
        print(f"Calculating path for {size}x{size} board using '{algorithm.name}'....")
        start = time.time()
        movements = algorithm.get_movements()

        if not movements:
            print("It was not possible to obtain a valid path to solve the problem")
            sys.exit(1)

        end = time.time()
        print(f"Path calculation took {round(end - start, 2)} seconds")

        return movements

    def __center_windows(self):
        center_tkinter_windows(self)

    def __run(self):
        self._board.generate()
        # self._board.print_cells()
        self.after(0, self.move_piece)

        self.__center_windows()
        self.mainloop()
