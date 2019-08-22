import numpy as np

class Graphs:

    def __init__(self, ord : int , direction : bool , pondered : bool):

        self.matriz = np.zeros((ord,ord))
        self.ispondered = pondered #true if the grapf is pondered

    def __InitMatriz():
        for item in matriz:
            item = None

    def Insert(v1, v2, ponder = 1):
        if( ispondered ):
            InsertRelation(v1 , v2, ponder)
        else:
            InsertRelation(v1 , v2 , 1)     
            return True

    def InsertRelation(v1 , v2, ponder):
        if matriz[v1-1][v2-1] is not None :
            return False
        else :
            if ispondered:
                matriz[v1-1][v2-1] = ponder
                matriz[v2-1][v1-1] = ponder
            else : 
                matriz[v1-1][v2-1] = 1
                matriz[v2-1][v1-1] = 1

            return True

    def Remove(v1 , v2):
        if v1 > 0 or v1 < ord + 1 and v2 > 0 or v2 < ord : 
            matriz[v1-1][v2-1] = None
            matriz[v2-1][v1-1] = None
        return True

    def NeighborVertives(v):
        if v-1 > ord : return

        list_of_vertices = []
        cont = 0
        for x in matriz[v-1] : 
            if x != None :
                list_of_vertices.append(cont);
            

        return  list_of_vertices
                
        


