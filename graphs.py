graph = {
    'a': ['c','b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}



def depthFirst (graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


depthFirst(graph, 'a')