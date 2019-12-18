from Maze import Maze
from time import sleep
from math import sqrt

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.total_robots = int(len(maze.robotloc) / 2)
        self.start_state = list(maze.robotloc)
        self.start_state.insert(0, 0)  # 0th robot goes first
        self.start_state = tuple(self.start_state)

    # returns set of successor states of given state (successor states are tuples)
    def get_successors(self, state):
        successors = set()
        #robot_turn = (state[len(state) - 1]) * 2  # index corresponding to which robot's turn it is to move
        robot_turn = (state[0] * 2) + 1

        # robot passes turn
        state0 = list(state)
        #next_turn = state[len(state) - 1] + 1
        next_turn = state[0] + 1
        if next_turn == self.total_robots:
            next_turn = 0;
        #state0[len(state0) - 1] = next_turn
        state0[0] = next_turn
        if self.is_legal(state0):
            successors.add(tuple(state0))

        # robot moves -1 in x direction
        state1 = list(state0)
        state1[robot_turn] = state1[robot_turn] - 1
        if self.is_legal(state1):
            successors.add(tuple(state1))

        # robot moves +1 in x direction
        state2 = list(state0)
        state2[robot_turn] = state2[robot_turn] + 1
        if self.is_legal(state2):
            successors.add(tuple(state2))

        # robot moves -1 in y direction
        state3 = list(state0)
        state3[robot_turn + 1] = state3[robot_turn + 1] - 1
        if self.is_legal(state3):
            successors.add(tuple(state3))

        # robot moves +1 in y direction
        state4 = list(state0)
        state4[robot_turn + 1] = state4[robot_turn + 1] + 1
        if self.is_legal(state4):
            successors.add(tuple(state4))

        return successors

    # determines if a given state is legal in the current MazeworldProblem problem
    def is_legal(self, state):
        #print("----")
        # iterate through each robot
        for i in range(self.total_robots):
            j = (i * 2) + 1  # corresponding starting index to each robot
            #print("i: ", j)
            #print("j: ", j)
            # robots must be on floors (not walls or off the map)
            if not self.maze.is_floor(state[j], state[j + 1]):
                return False

            # robots are not allowed to be on top of other robots:
            for k in range(j + 2, len(state) - 1, 2):
                #print("k: ", k)
                if state[j] == state[k] and state[j + 1] == state[k + 1]:
                    return False

        return True

    # determines if given state is a goal state
    def goal_test(self, state):
        for i in range(0, len(self.goal_locations), 2):
            j = i + 1
            if not self.goal_locations[i] == state[j]:
                return False
            if not self.goal_locations[i + 1] == state[j + 1]:
                return False
        return True

    #'''
    # cost function, based on fuel expended
    def cost_func(self, node):
        cost = 0
        temp = node
        while temp.parent:
            #print(temp)
            if not self.is_equiv(temp.state, temp.parent.state):  # make sure robot did not pass its turn
                cost += 1
            temp = temp.parent
        return cost
    #'''

    # BONUS: setting cost to be based on time
    '''
    def cost_func(self, node):
        cost = 0
        temp = node
        while temp.parent:
            cost += 1
            temp = temp.parent
        return cost
    '''

    # helper function for cost_func
    # tests to see if two states are effectively equivalent (compares everything except for turn)
    def is_equiv(self, state1, state2):
        for i in range(1, len(state1)):
            if not state1[i] == state2[i]:
                return False
        return True

    # returns manhattan distance to goal from given state
    def manhattan_heuristic(self, state):
        dist = 0
        for i in range(self.total_robots):
            k = i * 2
            j = (i * 2) + 1  # corresponding starting index to each robot

            dist += abs(self.goal_locations[k] - state[j])
            dist += abs(self.goal_locations[k + 1] - state[j + 1])
        return dist

    # returns straight line distance to goal from given state
    def straight_line_heuristic(self, state):
        dist = 0
        for i in range(self.total_robots):
            k = i * 2
            j = (i * 2) + 1  # corresponding starting index to each robot

            tempx = abs(self.goal_locations[k] - state[j])
            tempy = abs(self.goal_locations[k + 1] - state[j + 1])
            dist += sqrt((tempx * tempx) + (tempy * tempy))  # A^2 + B^2 = C^2
        return dist

    def __str__(self):
        string =  "Mazeworld problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(state)
            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.maze)
    print("total robots: ", test_mp.total_robots)

    # this should have zero successors, so I wrote another test below
    print(test_mp.get_successors((2, 1, 0, 1, 1, 2, 1)))
    #print(test_mp.get_successors((1, 0, 1, 1, 2, 1, 2)))
    #print(test_mp.is_equiv((1, 0, 1, 7, 1), (1, 0, 1, 0, 999999)))
    #print(test_mp.start_state)
