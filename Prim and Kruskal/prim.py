import os
import sys
import heapq as hq
from tools import create_graph
from tools import get_path
import time
from tools import Baum


def prim(file_path):

    graph, n_knoten, nachbarn = create_graph(file_path, False)


    taken =[0]*n_knoten
    baum = Baum(n_knoten)

    #choose the first edge
    start_node = graph[0][1] #graph[0] is a tuple with (weight, start_node, end_node), we take start_node
    #now we need to look at the neighbours of start_edge and choose next edge according to weight using heap
    heap = []
    for edge in nachbarn[start_node]:
        heap.append(edge)
    hq.heapify(heap)
    taken[start_node] = 1


    while baum.n_kanten() !=n_knoten-1:
        first_element_in_heap = hq.heappop(heap)
        anfang_knote = first_element_in_heap[1]
        end_knote = first_element_in_heap[2]
        if taken[end_knote] == 0:
            baum.add(first_element_in_heap[0],anfang_knote,end_knote)
            taken[end_knote] = 1
            for edge in nachbarn[end_knote]:
                hq.heappush(heap,edge)

    #baum.show_tree()
    baum.total_weight()



if __name__ == "__main__":
    st = time.time()

    path = get_path()
    prim(path)

    et = time.time()
    elapsed_time = (et - st) * 1000
    print('Execution time:', elapsed_time, 'milliseconds')


