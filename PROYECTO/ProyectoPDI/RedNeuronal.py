import cv2
import numpy as np
import matplotlib.pyplot as plt

# Rutas (absolutas)
R1 = 'C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Z/Video/' #Guardar el video
R2 = 'C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Z/Frames/' #Guardar los frames del video original
R3 = 'C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Z/Colores/' #Guardar los frames procesados (obtener solo color deseado)
R4 = 'C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Z/Sumas/' #Guardar los frames con el trazo realizado
R5 = 'C:/Users/SZMik/OneDrive/Documentos/Mike/VisualStudio/Z/Suma/' #Guardar imagen final

# Numero que se va a dibujar
clase = 0


#--------------------------------------------PDI---------------------------------------------------


# Funcion para la suma de dos imagenes
def add_images(img1, img2):
    # Realizar la suma elemento por elemento
    result = np.clip(img1.astype(int) + img2.astype(int), 0, 255).astype(np.uint8)
    return result


# Funcion para calcular la distancia entre los pixeles mas cercanos a un color
def distancia(pixelr, r, pixelg, g, pixelb, b):
    return np.sqrt((pixelr - r) ** 2 + (pixelg - g) ** 2 + (pixelb - b) ** 2)


# Funcion para obtener los pixeles mas cercanos a un color
def getUsefulPixel(red, green, blue, color, accepted):
    dim = red.shape # Tamaño de la imagen vectorizada
    filteredImage = np.zeros(dim, dtype=np.uint8) # Nuevo vector
    # Utilizar divide y vencerás
    def divide_and_conquer(start, end):
        if start >= end:
            distance = distancia(color[2], red[start], color[1], green[start], color[0], blue[start])
            if distance < accepted:
                filteredImage[start] = 255
        else:
            mid = (start + end) // 2
            divide_and_conquer(start, mid)
            divide_and_conquer(mid + 1, end)
    divide_and_conquer(0, len(red) - 1)
    
    return filteredImage


# Funcion para redimensionar una imagen
def subsampling(image, new_wid, new_hght):
    wid, hght, channel = image.shape
    # Escala
    scale_x = wid / new_wid
    scale_y = hght / new_hght
    subsampled_image = np.zeros((new_wid, new_hght, 3), np.uint8)
    for y in range(new_hght):
        for x in range(new_wid):
            original_x = int(x * scale_x)
            original_y = int(y * scale_y)
            pixel_r = image[original_x][original_y][0]
            pixel_g = image[original_x][original_y][1]
            pixel_b = image[original_x][original_y][2]
            subsampled_image[x][y][0] = pixel_r
            subsampled_image[x][y][1] = pixel_g
            subsampled_image[x][y][2] = pixel_b
            
    return subsampled_image


# Funcion para realizar suavizado Gaussiano
def SGauss(imagen):
    # Crear kernel gaussiano
    gauss = np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ])
    forma = np.shape(imagen)
    base = np.zeros(forma)
    # Convolucion
    for x in list(range(1, forma[0]-1)):
        for y in list(range(1, forma[1]-1)):
            suma = 0
            for i in list(range(-1, 2)):
                for j in list(range(-1, 2)):
                    suma = imagen[x-i, y-j] * gauss[i+1, j+1]+suma
            base[x, y] = suma
    maxs = np.max(base)
    base = base*255/maxs
    base = base.astype(np.uint8)
    
    return base


# Color al que queremos aproximar
colorDetected = np.array([0, 255, 0])
# Rango de color aceptado
acceptedColor = 180

# Funcion que obtiene los frames con el color deseado
def findColor(image, color, accepted):
    # Tamaño de la imagen
    wid, hght, canal = image.shape 
    # Recuperar canales
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]
    # Vectorizar cada canal
    redV = red_channel.flatten()
    greenV = green_channel.flatten()
    blueV = blue_channel.flatten()
    # Pasar los canales vectorizados a la funcion
    filteredImage = getUsefulPixel(redV, greenV, blueV, color, accepted) # Obtener el vector
    filteredImage = np.reshape(filteredImage, (wid, hght))

    return filteredImage


# Grabar el video
captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter(R1 + '1.mp4',cv2.VideoWriter_fourcc(*'mp4v'),60.0,(640,480))
while (captura.isOpened()):
  ret, imagen = captura.read()
  imagen = cv2.flip(imagen,1)
  if ret == True:
    cv2.imshow('Video', imagen)
    salida.write(imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
salida.release()


# Obtener frames del video
capture = cv2.VideoCapture(R1 + '1.mp4')
cont = 0
while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imwrite(R2 + '%04d.jpg' % cont, frame)
        cont += 1
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()


# Obtener trazo
suma = np.zeros((28,28), np.uint8)
for cont in range (cont):
    img = cv2.imread(R2 + '%04d.jpg' %cont)
    maskRed_res = subsampling(img,28,28)
    maskRed = findColor(maskRed_res, colorDetected, acceptedColor)
    suma = add_images(suma, maskRed)
    cv2.imwrite(R3 + '%04d.jpg' % cont, maskRed) # Guarda cada frame con el color obtenido
    cv2.imwrite(R4 + '%04d.jpg' % cont, suma) # Guarda el trazo haciendo la suma de los frames


# Guardar imagen final con suavizado Gaussiano
cv2.imwrite(R5 + 'suma.jpg', SGauss(suma))


#--------------------------------------------FIA---------------------------------------------------


from keras.datasets import mnist

# Cargar los datos desde mnist
(x_train, y_train), (x_testo, y_testo) = mnist.load_data()

# Leer la imagen a utilizar
img = cv2.imread(R5 + 'suma.jpg',0)

# Dimensiones necesarias para pasar la imagen a un arreglo compatible con MNIST
dimensiones = (1, 28, 28)
x_test = np.zeros(dimensiones, dtype=int)

# Asignacion de clase del numero dibujado
y_test = [clase]

# Pasar valores de imagen a arreglo compatible con MNIST
x_testa = np.asarray(img)
for i in range (28):
    for j in range (28):
        x_test[0][i][j] = x_testa[i][j]

# Convertir las imagenes de MNIST y nuestra imagen de entrada a vector de 784 (28 x 28)
X_train = np.reshape( x_train, (x_train.shape[0],x_train.shape[1]*x_train.shape[2]) )
X_test = np.reshape( x_test, (x_test.shape[0],x_test.shape[1]*x_test.shape[2]) )

# Normalizar valores de imágenes para representar la intensidad de 0 a 1
X_train = X_train/255.0
X_test = X_test/255.0


from keras.utils import np_utils

# Representación "one-hot" para multiclases en MNIST y en nuestra clase
nclasses = 10
Y_train = np_utils.to_categorical(y_train,nclasses)
Y_test = np_utils.to_categorical(y_test,nclasses)

# Modelo de entrenamiento
np.random.seed(1) # Aleatorizar entrenamiento 
input_dim = X_train.shape[1] # Capa de entrada (784 valores del vector)
output_dim = Y_train.shape[1] # Capa de salida (10 clases)


from keras.models import Sequential

# Crear el modelo de entrenamiento con el contenedor de secuential
modelo = Sequential()


from keras.layers import Dense

# Regresión multiclase
modelo.add( Dense(15, input_dim=input_dim, activation='relu')) # Capa oculta = 15 neuronas, capa de entrada = 784
modelo.add( Dense(output_dim, activation='softmax')) # Capa de salida = 10 (categorias)


from keras.optimizers import SGD

# Gradiente descendente (taza de aprendizaje de 0.2)
sgd = SGD(lr=0.2)

# Función de error: entropía cruzada
modelo.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy']) # metrics = taza de desempeño

# Entrenamiento
num_iteraciones = 50 # Iteraciones para entrenamiento
batch_size = 1000 # Numero de elementos del entrenamiento
historia = modelo.fit(X_train, Y_train, epochs=num_iteraciones, batch_size=batch_size, verbose=2) # Nos ayudará a graficar el desempeño del modelo

# Imprimir los resultados del entrenamiento
# loss
plt.subplot(1,2,1)
plt.plot(historia.history['loss'])
plt.title('Pérdida vs. iteraciones')
plt.ylabel('Pérdida')
plt.xlabel('Iteración')

#Precisión
plt.subplot(1,2,2)
plt.plot(historia.history['accuracy'])
plt.title('Precisión vs. iteraciones')
plt.ylabel('Precisión')
plt.xlabel('Iteración')

plt.show()

# Probar con datos que no ha visto (set de validación)
puntaje = modelo.evaluate(X_test,Y_test,verbose=0) #X_test = imagen de prueba, Y_test = clase REAL de imagen de prueba
print('\nPrecisión en el set de validación: {:.1f}%'.format(100*puntaje[1])) # Precisión del resultado del modelo

# Predicción de clase del set de validación (imagen de entrada)
Y_pred = np.argmax(modelo.predict(X_test), axis=-1)
ids_imgs = np.random.randint(0,X_test.shape[0],9)

# Imprimir resultado con set de validación y comparación de clases (original y predicha)
idx = ids_imgs[0]
img = X_test[idx,:].reshape(28,28)
cat_original = np.argmax(Y_test[idx,:])
cat_prediccion = Y_pred[idx]
plt.subplot(1,1,1)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Tu numero es: "{}" y se clasifico como: "{}"'.format(cat_original,cat_prediccion))
plt.suptitle('Clasificado')
plt.show()