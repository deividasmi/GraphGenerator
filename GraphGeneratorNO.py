import sys
import random

class Node:


    edges = []
    weights =[]
    head = None
    neighbors = 0
    color=False
    parent=None

    def __init__(self, head):
        self.head = head
        self.weights = []
        self.edges = []
        self.neighbors = 0
        self.color=False
        self.parent=None


    def add_edge(self, edge):
        self.edges.append(edge)


    def add_weight(self, weight):
        self.weights.append(weight)


    def contains_edge(self, edge):
        if self.edges.__contains__(edge):
            return True
        return False
    
    def check_edge(self, edge):
        for i in range(0, len(self.edges)):
            if int(edge) == int(self.edges[i]):
                return True
        return False


class Tree(object):


    def __init__(self, peak):
        self.peak = peak
        self.parent = self
        self.children = []
        self.rank = 0
        self.size = 1


    def add_child(self, tree):
        tree.parent = self
        self.children.append(tree)

    
    def printTree(self):
        print(self.peak)
        for child in self.children:
            child.printTree()            


def find(obj):
        print("find")
        while not obj.parent is obj.peak:
            next_obj = obj.parent
            obj.parent = next_obj.parent
            obj = next_obj
        return obj
        

def union(x, y):
        print("union")
        xRoot = find(x)
        yRoot = find(y)
        if xRoot is yRoot:
            return True
        if xRoot.rank < yRoot.rank:
            xRoot, yRoot = yRoot, xRoot
        yRoot.parent = xRoot
        if xRoot.rank is yRoot.rank:
            xRoot.rank += 1

class Edge():

    peak_a = 0
    peak_b = 0
    weight = 0

    def __init__(self, peaka, peakb, weight):
        self.peak_a = peaka
        self.peak_b = peakb
        self.weight = weight

def print_graph(graph):
    for i in range(0, len(graph)):
        print("{}, {}: {} :: {}".format(graph[i].head, graph[i].neighbors, graph[i].edges, graph[i].weights))    


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
                    return True
            
    else:
        path.append(int(destination))
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


def structure_contains_edge(edges, peak_a, peak_b):
    for i in range(0, len(edges)):
        if edges[i].peak_a == peak_b and edges[i].peak_b == peak_a:
            return True
    return False

def order_edges(edges):
    for i in range(0, len(edges)):
        for j in range(0, len(edges)):
            if edges[i].weight < edges[j].weight:
                temp = edges[i]
                edges[i]=edges[j]
                edges[j]=temp
            

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
                #if(graph[i].neighbors == max_edges):
                 #   break
                edge_count = random.randint(min_edges, max_edges)
                if min_edges == max_edges:
                    edge_count = min_edges
                for j in range(0, edge_count):
                    add = True
                    while add and edge_count > len(graph[i].edges):
                        edge = random.randint(0, point_number-1)
                        if not graph[i].contains_edge(edge):
                            if not graph[edge].contains_edge(i) and edge is not i:
                                graph[i].neighbors = graph[i].neighbors + 1
                                #graph[edge].neighbors = graph[edge].neighbors + 1
                                graph[i].add_edge(edge)
                                graph[edge].add_edge(i)
                                weight = random.randint(0, point_number-1)
                                graph[i].add_weight(weight)
                                graph[edge].add_weight(weight)
                                add = False       
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
    elif option=='s':
        try:
            trees = []
            edges = []
            for i in range(0,len(graph)):
                print(graph[i].head)
                branch = Tree(graph[i].head)
                trees.append(branch)
                for j in range(0, len(graph[i].edges)):
                    if not structure_contains_edge(edges, graph[i].head, graph[i].edges[j]):
                        edges.append(Edge(graph[i].head, graph[i].edges[j], graph[i].weights[j]))
            order_edges(edges)
            for i in range(0, len(edges)):
                print("{} : {} : {}".format(edges[i].peak_a, edges[i].peak_b, edges[i].weight))
            print("testing union")
            union(graph[1], graph[0])

                
        except:
            print("Error: error while creating disjointed structure")
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