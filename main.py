import time
import json
from src.camion_int import Camion
from src.post import postear
import keras_cv
import keras_core as keras
import datetime
import cv2

#declaración
###########
with open('data/keys.json', 'r') as f:
    keysJ = json.load(f)
with open('data/camionesL.json', 'r') as ff:
    camionesDict = json.load(ff)
with open('data/rutas.json', 'r') as fr:
    rutas  = json.load(fr)

nombreC = camionesDict[keysJ['camion']]
numeroC = keysJ['numero']
ruta_a = rutas[nombreC][keysJ["ra"]]
ruta_b = rutas[nombreC][keysJ["rb"]]
model = keras_cv.models.YOLOV8Backbone.from_preset(
    "yolo_v8_l_backbone"
)

camion = Camion(nombreC, numeroC, [ruta_a, ruta_b], model)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise TabError ("Error: No se pudo abrir la cámara.")

json_datas = {
                "camion": nombreC,
                "numero": numeroC,
                "clave_acceso": "si",

            }



frenado = False
tiempo_de_freno = 0
t_transferido = False
segs_at = 0
xu_at, yu_at = 0,0
while True:
    xu, yu = camion.actUbi()
    json_datas["llave"] = "u"
    json_datas["valor"] = json.dumps([yu,yu])

    postear(json_datas)

    hora = datetime.datetime.now()

    segs = (hora.hour * 120) + (hora.minute * 60) + hora.second

    if segs - segs_at == 10:
        t_transferido = False
        camion.calcular_velocidad([xu_at, yu_at], [xu, yu], 10)
        json_datas["llave"] = "np"
        json_datas["valor"] = str(camion.get_np())
        postear(json_datas)

    if camion.contarPy():
        _, frame = cap.read()

        camion.contarP(frame)
        cap.release()
    if not t_transferido:
        segs_at = segs
        t_transferido = True

    print("funcionando")
    print(nombreC)
    time.sleep(1)
    #camion.get_velocidad()
    