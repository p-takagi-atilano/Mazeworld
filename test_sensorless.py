# Paolo Takagi-Atilano: COSC 76, September 27 2017

from SensorlessProblem import SensorlessProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search


def null_heuristic(state):
    return 0

def run_all_tests(search_problem):
    print(search_problem.maze)
    print(bfs_search(search_problem))
    print(astar_search(search_problem, null_heuristic))
    print(astar_search(search_problem, search_problem.state_len_heuristic))
    print(astar_search(search_problem, search_problem.opt_state_len_heuristic))
    print(astar_search(search_problem, search_problem.uniq_x_y_heuristic))


# Mazes
my_maze1 = Maze("my_maze1.maz")
my_maze2 = Maze("sr_maze1.maz")
my_maze3 = Maze("maze3.maz")


# Problems
my_maze1_prob = SensorlessProblem(my_maze1)
my_maze2_prob = SensorlessProblem(my_maze2)
my_maze3_prob = SensorlessProblem(my_maze3)

run_all_tests(my_maze1_prob)
run_all_tests(my_maze2_prob)
run_all_tests(my_maze3_prob)

