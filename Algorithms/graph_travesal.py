

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []  
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers


class Graph(object):
    def __init__(self, nodes = None, edges = None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = [] 
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

