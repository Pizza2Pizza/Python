import os
import sys
import re
import numpy as np

DIRECTORY = os.path.join("..", "00_beispiele", "mst")

class Baum:
    def __init__(self, n_knoten):
        self.n_knoten = n_knoten
        self.kanten = []

    def n_kanten(self):
        return len(self.kanten)

    def add(self, weight, start_ecke, end_ecke):
        self.kanten.append((weight,start_ecke,end_ecke))

    def show_tree(self):
        for x in self.kanten:
            print(x)

    def total_weight(self):
        weight = 0
        for x in range(0,self.n_kanten()):
            weight = weight + self.kanten[x][0]
        print("Total weight:", weight)


def get_path():
    # the name of the document to read
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        file_path = os.path.join(DIRECTORY, file_name)
        if os.path.exists(file_path):
            return file_path
        else:
            raise Exception("The file doesn't exist")
    else:
        raise Exception("You forgot the name of the file to read")



def create_graph(file_path, mode):
    knoten = 0
    file = open(file_path, "r")

    # to establish the dimensions of the matrix
    comment_pattern = re.compile("^c")
    for line in file:
        if comment_pattern.match(line):
            pass
        else:
            knoten, kanten = re.search(r'^p ([0-9]+) ([0-9]+)', line, flags=re.MULTILINE).groups()
            knoten = int(knoten)
            break

    # create a graph
    graph = []
    nachbarn = []
    for i in range(0, knoten):
        nachbarn.append([])


    # filling the graph
    for line in file:
        i, j, weight = re.search(r'^e ([0-9]+) ([0-9]+) ([0-9]+)', line, flags=re.MULTILINE).groups()
        i = int(i)-1
        j = int(j)-1
        weight = int(weight)
        if not mode:
            nachbarn[i].append((weight, i, j))
            nachbarn[j].append((weight, j, i))
        graph.append((weight, i, j))

    file.close()

    if not mode:
        return graph, knoten, nachbarn
    return graph, knoten





