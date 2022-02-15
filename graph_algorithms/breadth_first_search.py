# breadth first search algorithm
# author: jeli-t
# https://github.com/jeli-t/algorithms


from queue import Queue


def breadth_first_search(graph, start):
    visited = []
    visited.append(start)
    queue = Queue()
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.put(w)
    return visited


def example_usage():
    graph = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['B', 'D'],
        'D': [],
        'E': ['A']
    }
    visited = breadth_first_search(graph, 'A')
    print(visited)


if __name__ == '__main__':
    example_usage()