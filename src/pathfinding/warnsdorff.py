from src.pathfinding.path_finder import PathFinder


class Warnsdorff(PathFinder):
    def __init__(self, board_size, start_point):
        super().__init__('Warnsdorff', board_size, start_point, 9999)

    def get_movements(self):
        pass

