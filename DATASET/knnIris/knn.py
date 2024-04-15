from iris import IrisData
import numpy as np

#From 150 samples, The first 100 samples will be used as training 
#and remaining 50 as a test set
class KnnClassifier(object):
    def __init__(self, nNeighbors):
        #public
        self.k = nNeighbors
        #private
        self.__data = []
        self.__label = []
    
    def fit(self, xtrain, ytrain):
         self.__data  = xtrain #data
         self.__label = ytrain #label
    
    def predict(self, xtest, ytest):
        _train = self.__data
        _label = self.__label
        r = len(xtest)    #Número de filas  (Entrenamiento)
        c = len(xtest[0]) #Número de columnas
    
        labels = np.zeros(r)
        distance = self.distEuc(xtest)
        nNeighbors, idx = self.nearest(distance)
        accuracy, confMat = self.count(idx, xtest,ytest)
        return accuracy, confMat

    def count(self, idx, xtest, ytest):
        ytrain = self.__label
        nClass = 3
        accuracy  = 0.0
        confMat = np.zeros([nClass,nClass])
        r = len(ytest)    #Número de filas  (Datos Entrenamiento)
        c = self.k #Número de vecinos (#Número de columnas)
        yt = np.zeros(c, dtype=int)
        #print(xtest)
        print('ytrain (labels):\n', ytrain[idx])
        print('ytest (labels):\n', ytest)
        for i in range (r): #50 Samples for test 
           for j in range(c):  #100
                yt[j] = ytrain[idx[i,j]]
           
           commonLabel = np.bincount(yt).argmax()
           if ytest[i] == commonLabel:
                accuracy +=1
                confMat[ytest[i]-1,ytest[i]-1] +=1
           else:
               confMat[ytest[i]-1,commonLabel-1] +=1
        
        accu = (accuracy / len(ytest))*100
        print('Num Errores: ',r-accuracy )   #r is nframes_probe
        return accu, confMat
    
    def nearest(self, dist):
        k = self.k  #k-neighbors
        #Obtener los k vecinos más cercanos
        r = len(dist)  #Número de filas 
        c = k #Número de vecinos (Número de columas)
        #ordenar la distancias ascendentemente
        distSort = np.sort(dist, axis=1) #print('Ordenado: \n',distSort)
        #indices ordenados ascendentemente de acuerdo a las distancias ordenadas 
        idx = np.argsort(dist)[:r] 
        
        neighbors = np.zeros([r,c])
        index     = np.zeros([r,c], dtype = int)
    
        for i in range (r): # 50
           for j in range(c):  #i 100
               neighbors[i,j] = distSort[i,j]
               index[i,j] = idx[i,j]

        print('neighbors:\n', neighbors)
        print('idx(neighbors):\n', index)
        return neighbors, index

   
    def distEuc(self, xtest): #evaluate Euclidean distance
        _train = self.__data
        _label = self.__label
        rtest = len(xtest)    #Número de filas  (Entrenamiento)
        c = len(xtest[0]) #Número de columnas
        rtrain = len(_train)    #Número de filas  (Entrenamiento)
        distance = np.zeros([rtest,rtrain]) #100x50

        for i in range (rtest): # 50
            for j in range(rtrain):  #i 100
                suma = 0.0
                for k in range(c):  #for all vector elements (cols) k
                    suma = suma + ((xtest[i,k]-_train[j,k])**2)
                distance[i,j] = np.sqrt(suma)
                   
        return distance
    
    def data(self):
        return self.__data
    
    def label(self):
        return self.__label  
    
def split(mat_p, label, _num):
    r = len(mat_p)    #Número de filas  (Entrenamiento)
    c = len(mat_p[0]) #Número de columnas
    num_train = r - _num #Muestras restantes para test
    x_train = np.zeros([num_train, c]) # Training set e.g m[100,4]
    y_train = np.zeros(num_train, dtype=int) #label
    x_test  = np.zeros([_num, c]) # Test set, e.g. m[100]
    y_test  = np.zeros(_num, dtype=int) #label
    
    for i in range(num_train):
        for j in range (c):
           x_train[i,j] = mat_p[i,j] #data
        y_train[i] = label[i] #label
    
    ix = i+1 
    for i in range(_num):
       for j in range(c):
          x_test[i,j] = mat_p[i+ix,j] #data
       y_test[i] = label[i+ix] #label
    
    return x_train, y_train, x_test, y_test

#main
#
Iris = IrisData()
Iris.load('iris.data')
dataset = Iris.data()
#--------------------------------------
n = 50 # Number of elements to test
mat_p, label = Iris.permutation(dataset)
#/*-------------------------
#ytrain and ytest are labels
xtrain, ytrain, xtest, ytest = split(mat_p,label, n)
numNeighbors = 1
knn = KnnClassifier(numNeighbors)
knn.fit(xtrain, ytrain)
accuracy, confMat = knn.predict(xtest,ytest)
print('accuracy:\n', accuracy)
print('Confusion Matrix:\n', confMat)

