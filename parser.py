import numpy as np
from pathlib import Path
import os

def produce_vertices(num_verts):
    return([i for i in range(num_verts)])


def build_output(vertices, edges, filename):
    with open(filename, 'w+') as f:
        f.write("vertex = [")
        for i in range(len(vertices)):
            if i != len(vertices)-1:
                f.write(str(vertices[i]) + ', ')
            else:
                f.write(str(vertices[i]) + '];\n\n')

        f.write("edges = \n[")
        for i in range(len(edges)):
            if i != len(edges)-1:
                f.write('|' + str(edges[i][0]) + ', ' + str(edges[i][1]) + '\n')
            else:
                f.write('|' +  str(edges[i][0]) + ', ' + str(edges[i][1]) + '|];')


if __name__ == "__main__":

    p = Path('./PACE_unprocessed')

    for filename in list(p.glob("*.gr")):
        num_edges = 0
        num_verts = 0
        edge_tups = []
        with filename.open() as f:
            for line in f.readlines():
                if len(line) > 0 and line[0] != 'c':
                    if line[0] == 'p':
                        num_verts = int(line.split()[2])
                        num_edges = int(line.split()[3])
                    else:
                        edge_tups.append((int(line.split()[0]), int(line.split()[1])))

        build_output(produce_vertices(num_verts), edge_tups, Path(".\PACE_proc",filename.parts[-1][:-3] + ".dzn"))
