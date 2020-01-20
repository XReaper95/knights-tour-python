from abc import ABC, abstractmethod


class PathFinder(ABC):
    def __init__(self, name, board_size, start_point):
        self.name = name
        self.board_size = board_size
        self.start_point = start_point

    @abstractmethod
    def get_movements(self):
        raise NotImplementedError
