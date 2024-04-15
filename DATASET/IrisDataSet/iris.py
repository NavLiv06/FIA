import matplotlib.pyplot as plt
import numpy as np 
np.random.seed (0)

class IrisData(object): 
    def _init_(self):
        #private
        self._data = np.zeros([12,5]) 
        self._label = np.zeros([12])
    
    def permutation(self, mat):
        #self._data = np.random.permutation (mat)
        m1 = np.random.permutation (mat) 
        m2 = np.zeros([12,4])
        arr = np.zeros([12])
        r = len(m2) #Número de filas
        c = len (m2 [0]) #Número de columnas
        for i in range(r):
            for j in range (c):
                m2 [i,j] = m1[i,j] #data 
            arr[i] = m1[i,j+1] #label
            
        return m2, arr
    
    #Función para leer datos de un archivo 
    def load(self, Name):
        try:
            data = open(Name, 'r')
        except:
            print('El archivo no puede abrirse')
            quit()
        
        mat = np.zeros([12,5])
        r = len(mat) #Número de filas
        c = len(mat[0]) #Número de columnas
        print (r,c)
        i=0
        for linea in data:
            linea =linea.rstrip()
            
        for linea in data:
            linea = linea.rstrip() 
            linea = linea.split(',')
            #print('Datos en la línea = ', linea)
            for j in range (c):
                mat[i, j] = linea [j] #data
            i+=1
        data.close()
        #np.copyto (dest, origen)
        np.copyto(self._data, mat) #self._data = mat
        
#main
Iris = IrisData()
Iris.load('irisp.data')
dataset = Iris.data()
#h=5# Number of elements for training
mat_p, label= Iris.permutation(dataset) 
#-#From 150 samples, The first 100 samples will be used as training
#and remaining 50 as a test set