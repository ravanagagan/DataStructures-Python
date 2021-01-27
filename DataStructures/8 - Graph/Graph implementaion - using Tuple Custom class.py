# Implementation of Graph using tuples
# Here we are trying to find
# 1. Find all the paths between two nodes
# 2. Finding the shortest path between two nodes(min stops)

# ex:
# d = {
#     'mumbai': ['paris', 'dubai'],
#     'paris': ['dubai', 'new york']
# }

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]  # we used [] because we need dict like shown above in comment
        print("The Graph is: ", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def shortest_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path  # if i pass [path] it wi=ont show shortest path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_paths(node, end, path)
                # if shortest path hap None then any path is shortest only
                # if shortest path have a length more than sp then we will assign sp to shortest path
                # we are getting the length because it is []
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]  # if we use tuples to check the route everytime it will take time so let's convert this to dictionary

    graph_routes = Graph(routes)
    start = "Mumbai"
    end = "New York"
    print(f"Path between {start} and {end}: ", graph_routes.get_paths(start, end))

    start = "Toronto"
    end = "Mumbai"
    print(f"Shortest Path between {start} and {end}: ", graph_routes.shortest_paths(start, end))

    start = "Mumbai"
    end = "New York"
    print(f"Shortest Path between {start} and {end}: ", graph_routes.shortest_paths(start, end))
