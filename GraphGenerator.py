import sys
import random

class Node:


    edges = []
    head = None
    neighbors = 0
    color=False
    parent=None

    def __init__(self, head):
        self.head = head
        self.edges = []
        self.neighbors = 0
        self.color=False
        self.parent=None

    def add_edge(self, edge):
        self.edges.append(edge)


    def contains_edge(self, edge):
        if self.edges.__contains__(edge):
            return True
        return False
    
    def check_edge(self, edge):
        for i in range(0, len(self.edges)):
            if int(edge) == int(self.edges[i]):
                return True
        return False


def print_graph(graph):
    for i in range(0, len(graph)):
        print("{}, {}: {}".format(graph[i].head, graph[i].neighbors, graph[i].edges))    


def dfs_visit(graph, index, destination, path, success):
    graph[index].color = True
    if not graph[index].check_edge(destination):
        for i in range(0, len(graph[index].edges)):
            for j in range(0, len(graph)):
                if int(graph[j].head) == int(graph[index].edges[i]):
                    next_hop = j
                    break
            if graph[next_hop].color is False:
                #graph[int(graph[index].edges[i])].parent = graph[index].head
                dfs_visit(graph, next_hop, destination, path, success)
                if len(path)>0:
                    path.append(graph[index].head)
            
    else:
        path.append(destination)
        path.append(graph[index].head)
        success = True
        return success
    


def deep_first_search(graph, source, destination):
    path = []
    success = False
    for i in range(0, len(graph)):
        if int(graph[i].head) == source:
            source = i
    dfs_visit(graph, source, destination, path, success)
    print(path)
            

run = True
print("Welcome")
print("Graph Generator 3000")
print("Choose an option:")
print("For generating random oriented graph enter: g")
print("For entering your own oriented graph enter: e")
print("For finding path enter: f")
print('For help enter: h')
print("For quiting enter: q")
while(run):
    option = input("ENTER OPTION: ")
    if option=='g':
        #generuoti:
        try:
            point_number = int(input("Enter amount of points you want: "))
            min_edges = int(input("Enter minimum amount of edges: "))
            max_edges  = int(input("Enter maximum amount of edges: "))
        
            if point_number < max_edges:
                max_edges = point_number
            graph = []
            for i in range(0, point_number):
                point = Node(i)
                graph.append(point)
            for i in range(0, point_number):
                if(graph[i].neighbors is not max_edges):
                    if max_edges-graph[i].neighbors > min_edges:
                        edge_count = random.randint(min_edges, max_edges-graph[i].neighbors)
                        for j in range(0, edge_count):
                            add = True
                            while add:
                                edge = random.randint(0, point_number-1)
                                if not graph[i].contains_edge(edge):
                                    if not graph[edge].contains_edge(i) and edge is not i and graph[edge].neighbors is not max_edges:
                                        graph[i].neighbors = graph[i].neighbors + 1
                                        graph[edge].neighbors = graph[edge].neighbors + 1
                                        graph[i].add_edge(edge)
                                        add = False
                                empty_slots=True 
                                for k in range(0, len(graph)):
                                    if graph[k].contains_edge(i) and not k==i:
                                        empty_slots=False
                                if not empty_slots:
                                    break
                              
            print_graph(graph)
            print("END")
        except:
            print("That is not a valid input. Try again")
    elif option=='e':
        #1.2 2.3 3.4 4.7 7.3 7.8 7.6 8.1 6.2 6.8 6.9
        user_answ = input("Enter your oriented graph in form n.m n1.m2 eg: 1.2 1.3 3.2 : ")
        try:
            edges = user_answ.strip().split(' ')
            graph = []
            points = edges[0].split('.')
            node=Node(points[0])
            node.add_edge(points[1])
            graph.append(node)
            for i in range(1, len(edges)):
                points = edges[i].split('.')
                node = Node(points[0])
                peak_exists = False
                edge_exists = False
                for j in range(0, len(graph)):
                    if graph[j].head == points[0]:
                        if not graph[j].contains_edge(points[1]):
                            graph[j].add_edge(points[1])
                        peak_exists = True
                    if graph[j].head == points[1]:
                        edge_exists = True
                if not peak_exists:
                    node.add_edge(points[1])
                    graph.append(node)
                if not edge_exists:
                    node = Node(points[1])
                    graph.append(node)
            print_graph(graph)
        except:
            print("Not a valid input. Try again.")
    elif option=='q':
        run = False
    elif option=='f':
        try:
            source=int(input("Enter your starting position: "))
            destination=input("Enter your destination: ")
            deep_first_search(graph, source, destination)
        except:
            print("Not a valid input. Try again.")
    elif option=='h':
        print("Welcome")
        print("Graph Generator 3000")
        print("Availabale options:")
        print("For generating random oriented graph enter: g")
        print("For entering your own oriented graph enter: e")
        print("For finding path enter: f")
        print('For help enter: h')
        print("For quiting enter: q")
    else:
        print("Not an option try again.")