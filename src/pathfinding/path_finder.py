from abc import ABC, abstractmethod


class PathFinder(ABC):
    def __init__(self, name, board_size):
        self.name = name
        self.board_size = board_size

    @abstractmethod
    def get_movements(self):
        raise NotImplementedError
