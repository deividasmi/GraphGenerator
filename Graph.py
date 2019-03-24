import sys
import random

class Node:

    edges = []
    head = None
    neighbors = 0

    def __init__(self, head):
        self.head = head
        self.edges = []
        self.neighbors = 0


    def add_edge(self, edge):
        self.edges.append(edge)

    def contains_edge(self, edge):
        if self.edges.__contains__(edge):
            return True
        return False

def print_graph(graph):
    for i in range(0, len(graph)):
        print("{}, {}: {}".format(graph[i].head, graph[i].neighbors, graph[i].edges))    

run = True
print("Welcome")
print("Graph Generator 3000")
print("Choose an option:")
print("For generating random oriented graph enter: g")
print("For entering your own oriented graph enter: e")
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
                if(graph[i].neighbors == max_edges):
                    break
                edge_count = random.randint(min_edges, max_edges)
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
            print_graph(graph)
            print("END")
        except:
            print("That is not a valid input. Try again")
    elif option=='e':
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
        print("Coming soon.")
    elif option=='h':
        print("Welcome")
        print("Graph Generator 3000")
        print("Availabale options:")
        print("For generating random oriented graph enter: g")
        print("For entering your own oriented graph enter: e")
        print('For help enter: h')
        print("For quiting enter: q")
    else:
        print("Not an option try again.")