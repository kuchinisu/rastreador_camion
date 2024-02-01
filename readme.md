Este es el codigo para el rastreador para los autobuses, actualmente para las pruevas funciona mediante geolocalicación de google cloud en lugar de tratar de accesar al gps del dispositivo.

El algoritmo crea un diccionario que es mandado como json al servidor puente entre los rastreadores de los autobuses y la app para los usuarios

El programa implementa open cv y el modelo YOlO 8 para la deteccion de objetos, busca detectar personas para contar las detecciones y dar información de la cantidad de pasajeros, la logica es identificar cuando el autobus se pone en marcha despues de detenerse en una estación mediante la comparación de sus coordenadas y tomar una imagen con open cv y pasarla por YOLO 8

El programa ofrece información del nombre del camion, el numero, la ruta, la cantidad aproximada de pasajeros, el estado y ubicación a tiempo real al servidor