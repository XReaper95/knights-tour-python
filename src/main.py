from src.knights_tour import KnightsTour
from src.pathfinding.backtracking import Backtracking

if __name__ == '__main__':
    size = 5
    algorithm = Backtracking

    app = KnightsTour(size, algorithm, False)
