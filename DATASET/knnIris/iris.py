# Create  by V. Alonso
# 7/06/23

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
#np.random.default_rng()

class IrisData(object):
    def __init__(self):
        #public
        self.numSample = 150
        self.numAttrib = 5
        #private
        self.__data  = [] #np.zeros([12,5])
        self.__label = [] #np.zeros([12])
    
    def data(self):
        return self.__data
       
    def label(self):
        return self.__label 

    def permutation(self, mat):    
        _row = self.numSample
        _col = self.numAttrib
        m1 = np.random.permutation(mat)
        m2  = np.zeros([_row, _col-1])
        arr = np.zeros(_row)
        r = len(m2)    #Número de filas
        c = len(m2[0]) #Número de columnas

        for i in range(r):
          for j in range (c):
              m2[i,j] = m1[i,j] #data
          arr[i]   = m1[i,j+1] #label
       
        return m2, arr

    #Función para leer datos de un archivo
    def load(self, Name):
        try:
           data = open(Name, 'r')
        except:
           print('El archivo no puede abrirse')
           quit()
        _row = self.numSample
        _col = self.numAttrib
        mat  = np.zeros([_row,_col])
        r = len(mat)    #Número de filas
        c = len(mat[0]) #Número de columnas
        print (r,c)
        i = 0
        for linea in data:
            linea = linea.rstrip() 
            linea = linea.split(',')
            #print('Datos en la línea = ',linea)
            for j in range (c):
              mat[i,j] = linea[j] #data
            i+=1
        data.close()   
        #np.copyto(dest, origen) np.zeros([12,5])
        self.__data = np.zeros([_row,_col])
        np.copyto(self.__data, mat)  #self.__data  = mat
     

#main
'''
Iris = IrisData()
Iris.load('irisp.data')
dataset = Iris.data()
mat_p, label = Iris.permutation(dataset)
'''



