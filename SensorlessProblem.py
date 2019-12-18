# Paolo Takagi-Atilano: COSC 76, September 27 2017

from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:

    def __init__(self, maze):
        self.maze = maze
        self.start_state = self.set_start_state()  # this is a belief state
        #self.total_robots = 1  # this problem has 1 robot

    # start state is a robot on every single floor tile of map
    def set_start_state(self):
        states = set()
        for i in range(self.maze.width):       # iterate through x values
            for j in range(self.maze.height):  # iterate through y values
                if self.maze.is_floor(i, j):
                    states.add((0, i, j))
        return states

    # is the state a singleton set?
    def goal_test(self, state):  # this state is a belief state
        return len(state) == 1 and self.maze.is_floor(state[0][1], state[0][2])

    # returns set of successor belief states (belief states are sets of possible states)
    def get_successors(self, belief_state):
        successors = set()

        successors_north = set()
        for state in belief_state:
            state1 = (state[0], state[1] + 1, state[2])
            if self.is_legal(state1):
                successors_north.add(state1)
            else:
                successors_north.add(state)

        successors_south = set()
        for state in belief_state:
            state1 = (state[0], state[1] - 1, state[2])
            if self.is_legal(state1):
                successors_south.add(state1)
            else:
                successors_south.add(state)

        successors_east = set()
        for state in belief_state:
            state1 = (state[0], state[1], state[2] + 1)
            if self.is_legal(state1):
                successors_east.add(state1)
            else:
                successors_east.add(state)

        successors_west = set()
        for state in belief_state:
            state1 = (state[0], state[1], state[2] - 1)
            if self.is_legal(state1):
                successors_west.add(state1)
            else:
                successors_west.add(state)

        successors.add(tuple(successors_north))
        successors.add(tuple(successors_south))
        successors.add(tuple(successors_east))
        successors.add(tuple(successors_west))
        return successors

    # determines whether or not a state is legal (potential singular state, not belief state)
    def is_legal(self, state):
        return self.maze.is_floor(state[1], state[2])

    # cost function
    def cost_func(self, node):
        cost = 0
        temp = node
        while temp.parent:
            #print(temp)
            cost += 1
            temp = temp.parent
        return cost

    # state length heuristic
    def state_len_heuristic(self, state):
        return len(state)

    # optimistic state length heuristic
    def opt_state_len_heuristic(self, state):
        return len(state) / self.maze.width

    # unique x and y values heuristic
    def uniq_x_y_heuristic(self, belief_state):
        x = set()
        y = set()
        for state in belief_state:
            x.add(state[1])
            y.add(state[2])
        return len(x) + len(y)

    def __str__(self):
        string =  "Blind robot problem: "
        return string

    # given a sequence of states (including robot turn), modify the maze and print it out.
    #  (Be careful, this does modify the maze!)
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
    print(test_problem.start_state)
    for successor_belief_state in test_problem.get_successors(test_problem.start_state):
        print(successor_belief_state)
