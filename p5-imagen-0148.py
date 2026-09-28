import cv2
# Leer la imagen con cv2 = Computer vision
img = cv2.imread('Monika.jpg')
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar pixeles (546, 546, 3)
print(img.shape) 
# Mostrando imagen en ventana, barra de titulo 'Monika 0148'
cv2.imshow('Monika 0148', img)
# Tiempo de espera
cv2.waitKey(0)
# Destruir todas las ventanas
cv2.destroyAllWindows()