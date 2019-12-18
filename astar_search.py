# Paolo Takagi-Atilano: COSC 76, September 27 2017

from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.heuristic + self.transition_cost

    #'''
    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()
    #'''

    # BONUS: Tiebreaker implementation of comparison operator
    '''
    def __lt__(self, other):
        if self.priority == other.priority():
            return self.heuristic - other.heuristic
        return self.priority() - other.priority()
    '''

# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[tuple(start_node.state)] = 0

    solution.nodes_visited = 1
    # you write the rest:
    while pqueue:
        node = heappop(pqueue)
        node.state = tuple(node.state)
        #node.state = node.state

        #solution.nodes_visited += 1

        # check to see if node is a goal node
        if search_problem.goal_test(node.state):
            solution.path = backchain(node)
            solution.cost += node.transition_cost
            return solution
        # check to see if node has been visited before, update w/ new/lower cost if necessary
        elif node.state in visited_cost.keys() and node.transition_cost > visited_cost[node.state]:
            continue

        for child_state in search_problem.get_successors(node.state):
            solution.nodes_visited += 1
            child = AstarNode(child_state, 0, node, 0)  # 0s are just placeholders to keep everything happy
            child.transition_cost = search_problem.cost_func(child)  # assumes search_problem has cost_func function
            child.heuristic = heuristic_fn(child.state)

            if child.state not in visited_cost.keys() or child.transition_cost < visited_cost[child.state]:
                visited_cost[child.state] = child.transition_cost
                pqueue.append(child)

    # no solution found if control reaches this point
    solution.path = []
    solution.cost = "N/A"
    return solution
