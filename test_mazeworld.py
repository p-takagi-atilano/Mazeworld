# Paolo Takagi-Atilano: COSC 76, September 27 2017

from MazeworldProblem import MazeworldProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:

# handy function that runs bfs and a* search with all 3 heuristics
def run_all_tests(search_problem):
    print(search_problem.maze)
    print(bfs_search(search_problem))
    print(astar_search(search_problem, null_heuristic))
    print(astar_search(search_problem, search_problem.manhattan_heuristic))
    print(astar_search(search_problem, search_problem.straight_line_heuristic))


# Single Robot tests

# Mazes
test_sr_maze1 = Maze("sr_maze1.maz")
test_sr_maze2 = Maze("sr_maze2.maz")
test_sr_maze3 = Maze("sr_maze3.maz")

# Problems
test_sr_mp1 = MazeworldProblem(test_sr_maze1, (6, 6))
test_sr_mp2 = MazeworldProblem(test_sr_maze2, (12, 6))
test_sr_mp3 = MazeworldProblem(test_sr_maze3, (6, 6))

run_all_tests(test_sr_mp1)
run_all_tests(test_sr_mp2)
run_all_tests(test_sr_mp3)

# Multi Robot Tests

# Mazes
test_mr_maze1 = Maze("my_maze1.maz")
test_mr_maze2 = Maze("my_maze2.maz")
test_mr_maze3 = Maze("my_maze3.maz")

# Problems
test_mr_mp1 = MazeworldProblem(test_mr_maze1, (4, 3, 4, 2, 4, 1))
test_mr_mp2 = MazeworldProblem(test_mr_maze2, (9, 0, 9, 1, 8, 9))
test_mr_mp3 = MazeworldProblem(test_mr_maze3, (0, 0, 0, 1, 0, 2))

run_all_tests(test_mr_mp1)
run_all_tests(test_mr_mp2)
run_all_tests(test_mr_mp3)

