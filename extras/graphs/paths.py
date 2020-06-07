def print_graph(graph):
    print('digraph {')
#    for i in range(len(graph)):
    for k in graph:
        for v in graph[k]:
            print(k, '->', v)
    print('}')


def num_path(graph, start, stop):
    if start == stop:
        return 1
    else:
        return sum([num_path(graph, vertex, stop) for vertex in graph[start]])


if __name__ == '__main__':
    graph0 = [[1,2], [2,3], [3], []]
    # A 0
    # Б 1
    # B 2
    # Г 3
    # Д 4
    # E 5
    # Ж 6
    # З 7
    # И 8
    # К 9
    # Л 10
    # M 11

    graph2 = [
        [2, 3],  # A
        [4, 5],  # Б
        [1, 3, 5],
        [5, 6, 7],
        [5, 8],
        [8, 9],
        [9],
        [10],
        [9],
        [11],
        [11],
        [],
    ]

    graph = {
        'А' : ['Б', 'Г'],
        'Б' : ['В', 'Д'],
        'В' : ['Д', 'Е'],
        'Г' : ['В', 'Ж', 'З'],
        'Д' : ['И'],
        'Е' : ['И', 'К'],
        'Ж' : ['К','Л'],
        'З' : ['Л'],
        'И' : ['К', 'М'],
        'К' : ['Л', 'М'],
        'Л' : ['М'],
        'М' : [],
    }

    dict()


#    print_graph(graph)
    print(num_path(graph, 'А', 'М'))
