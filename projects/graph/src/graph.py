from collections import deque
from collections import defaultdict
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(set)

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.edges[v1].add(v2)
        else:
            raise Exception(
                'Both vertices must be created to use them in an edge')

    def bft(self, start):
        visited = set()
        q = deque()
        q.appendleft(start)
        while q:
            current = q.pop()
            if current not in visited:
                visited.add(current)
                print(current)
                for vertex in self.edges[current]:
                    q.appendleft(vertex)

    def dft(self, start):
        visited = set()
        s = []
        s.append(start)
        while s:
            current = s.pop()
            if current not in visited:
                visited.add(current)
                print(current)
                for vertex in self.edges[current]:
                    s.append(vertex)

    def dft_recursive(self, start):
        visited = set()

        def helper(vertex):
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for neighbor in self.edges[vertex]:
                    helper(neighbor)

        helper(start)
