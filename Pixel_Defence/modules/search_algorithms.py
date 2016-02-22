__author__ = "William Read, Tom Starling"
__revision__ = "17/02/2016"
__version__ = "1.0"


import numpy
from heapq import *

class Generate_Graph():

    def __init__(self,canvas,tiles):
        self.canvas = canvas
        self.tiles = tiles
        self.path = []

        self.graph = []
        self.row = []
        
        for x in range(22):
            for y in range(19):
                colour = self.canvas.itemcget(self.tiles[(y,x)],"fill")
                if colour == "brown":
                    self.row.append(1)
                elif colour == "red":
                    self.row.append(2)
                elif colour == "blue":
                    self.row.append(3)
                else:
                    self.row.append(0)
                
            self.graph.append(self.row)
            self.row = []

        self.graph = numpy.array(self.graph)
        self.start = (0,0)
        self.end = (21,18)

class Search_Path(Generate_Graph):

    def __init__(self, canvas, tiles):
        Generate_Graph.__init__(self,canvas,tiles)
        self.path = self.A_Star()
        for each in tiles:
            colour = self.canvas.itemcget(self.tiles[(each[0],each[1])],"fill")
            if colour == "red" or colour == "blue" or colour == "brown":
                pass
            else:
                self.canvas.itemconfig(self.tiles[(each[0],each[1])],fill="")
                

    def A_Star(self):
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        close_set = set()
        came_from = {}
        gscore = {self.start:0}
        fscore = {self.start:self.heuristic(self.start,self.end)}
        oheap = []

        data = []
        
        heappush(oheap, (fscore[self.start], self.start))

        while oheap:
            current = heappop(oheap)[1]
            data.append(current)
            
            if current == self.end:
                return data

            close_set.add(current)
            for i, j in neighbours:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < 22:
                    if 0 <= neighbor[1] < 19:
                        if self.graph[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = tentative_g_score
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, self.end)
                    heappush(oheap, (fscore[neighbor],neighbor))


    def heuristic(self, a, b):
        return (b[0]-a[0])**2+(b[1]-a[1])**2
        
if __name__ == "__main__":
    pass
