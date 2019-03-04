from collections import deque, defaultdict, OrderedDict
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

    def bfs(self, start, end):
        visited = OrderedDict()
        q = deque()
        q.appendleft((None, start))
        while q:
            (v1, v2) = q.pop()
            if visited.get(v2) is None:
                visited[v2] = v1
                if v2 == end:
                    path = deque()
                    current = v2
                    while current is not None:
                        path.appendleft(current)
                        current = visited[current]
                    return list(path)

                for vertex in self.edges[v2]:
                    q.appendleft((v2, vertex))

    def dfs(self, start, end):
        visited = OrderedDict()
        s = []
        s.append((None, start))
        while s:
            (v1, v2) = s.pop()
            if visited.get(v2) is None:
                visited[v2] = v1
                if v2 == end:
                    path = deque()
                    current = v2
                    while current is not None:
                        path.appendleft(current)
                        current = visited[current]
                    return list(path)

                for vertex in self.edges[v2]:
                    s.append((v2, vertex))
