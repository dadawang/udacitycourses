

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges = []):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node_val = Node(new_node_val)


print 'HHH'
