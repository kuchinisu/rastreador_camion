import keras_cv
import keras_core as keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from .gt_coordenadas import detect_coor


class Camion():
    def __init__(self, nombre, numero, ruta, modelo_detect):
        self.nombre = nombre
        self.numero = numero
        self.ruta = ruta
        self.modelo_detect = modelo_detect

        self.estado = "funcional"
        self.num_p = 0
        self.ubi = []
        self.funcional = True
        self.km_ph = 0
        self.km_ph_pas = 0
        self.t_desacelerando = 0
        self.t_detend = 0
        self.frenado = False
        self.contar_personas_pregunta = False
    
    def calcular_velocidad(self, ptsa, ptsb, tiempo):
        dts = (ptsa[1] * ptsa[0]) - (ptsb[1] * ptsb[0])
        self.km_ph = dts / tiempo
        self.km_ph_pas = self.km_ph

        if self.t_detend < 4:
            self.frenado = True

        if self.km_ph < self.km_ph_pas:
            self.t_desacelerando += 1
        elif self.km_ph == self.km_ph_pas:
            self.t_detend += 1
        else:
            if self.t_detend < 4:
                self.contar_personas_pregunta = True
            else:
                self.contar_personas_pregunta = False
                
            self.t_detend = 0
            self.t_desacelerando = 0
        return self.km_ph
    
    def get_velocidad(self):
        return self.km_ph
    
    def contarPy(self):
        return self.contar_personas_pregunta
    
    def get_frenado(self):
        return self.frenado

    def contarP(self, img):
        #imgArray = np.array(img)
        imgT = tf.constant([img/255])

        output_t = self.modelo(imgT)
        
        output_t = tf.nn.softmax(output_t)

        probabilidad_clase_1 = output_t[..., 1]

        umbral_confianza = 0.5
        mascaras_objetos_clase_1 = probabilidad_clase_1 > umbral_confianza

        self.num_p = np.sum(mascaras_objetos_clase_1)
    def get_np(self):
        return self.num_p


    def actUbi(self):
        self.ubi = detect_coor()
        return self.ubi
    
    def get_ubi(self):
        return self.ubi
    
    def set_funcional(self, fun):
        self.funcional = fun
        
        



#################3
