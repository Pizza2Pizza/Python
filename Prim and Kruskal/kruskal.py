import os
import sys
import heapq as hq
from tools import create_graph
from tools import get_path
import time
from tools import Baum



def kruskal(file_path):
    graph, n_knoten = create_graph(file_path, True)

    #anzahl_zshgK - anzahl von Knoten in Zusamenhangkomponente
    anzahl_zshgK =[0]*n_knoten
    next_edge_in_ZshgK = [0]*n_knoten
    rep_Knote = [0]*n_knoten

    #initialise a baum
    baum = Baum(n_knoten)

    for knote in range(0,n_knoten):
        anzahl_zshgK[knote] = 1
        next_edge_in_ZshgK[knote] = knote
        rep_Knote[knote] = knote

    #create a heap
    hq.heapify(graph)


    while baum.n_kanten() != n_knoten-1:
        first_element = hq.heappop(graph) #first_element is eine Kante mit (Gewicht, start_Knote, end_Knote)
        #print(first_element)
        start_knote = first_element[1]
        end_knote = first_element[2]

        if rep_Knote[start_knote] != rep_Knote[end_knote]:
            baum.add(first_element[0],start_knote,end_knote)
            if anzahl_zshgK[rep_Knote[start_knote]] < anzahl_zshgK[rep_Knote[end_knote]]:
                min_n = start_knote
                max_n = end_knote
            else:
                min_n = end_knote
                max_n = start_knote
            anzahl_zshgK[rep_Knote[max_n]] = anzahl_zshgK[rep_Knote[max_n]] + anzahl_zshgK[rep_Knote[min_n]]
            current_knote = min_n
            while True:
                rep_Knote[current_knote] = rep_Knote[max_n]
                current_knote = next_edge_in_ZshgK[current_knote]
                if current_knote == min_n:
                    break
            temp = next_edge_in_ZshgK[start_knote]
            next_edge_in_ZshgK[start_knote] = next_edge_in_ZshgK[end_knote]
            next_edge_in_ZshgK[end_knote] = temp
    #print(rep_Knote)
    #baum.show_tree()
    baum.total_weight()

if __name__ == "__main__":
    st = time.time()

    path = get_path()
    kruskal(path)

    et = time.time()
    elapsed_time = (et - st)* 1000
    print('Execution time:', elapsed_time, 'milliseconds')









