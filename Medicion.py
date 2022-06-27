#__________________________________________________________________________________
#                                                                                  |
#Eduardo de la hoz, stephania de la Hoz, Jorge Torres, Jairo boneth, Miguel Gomez  |
#__________________________________________________________________________________|

import cv2
import numpy as np
from Detector_Objetos import *


parametros=cv2.aruco.DetectorParameters_create()
Libreria=cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)

detector=DetectorFondoHomogeneo()

cap=cv2.VideoCapture(2,cv2.CAP_DSHOW)
cap.set(3,640)
cap.set(4,480)



while True:

    ret,ventana_camara=cap.read()
    if ret==False: break
    corners,_,_=cv2.aruco.detectMarkers(ventana_camara,Libreria,parameters = parametros)

    if corners:



        corners_ent=np.int0(corners)
        cv2.polylines(ventana_camara,corners_ent,True,(0,0,255),5)
        perimetro_referencia_aruco=cv2.arcLength(corners_ent[0], True)

#calibrar camara con aruco
        proporcion_cm=perimetro_referencia_aruco/30

        delimitacion_contorno=detector.deteccion_objetos(ventana_camara)
 
        for cont in delimitacion_contorno:

           # cv2.polylines(ventana_camara,[cont],True,(255,255,255),2)

            rectangulo=cv2.minAreaRect(cont)
            (x,y),(an,al),angulo=rectangulo

            anchura=an/proporcion_cm
            altura=al/proporcion_cm

            cv2.circle(ventana_camara,(int(x),int(y)),5,(255,255,0),-1)

            rect=cv2.boxPoints(rectangulo)
            rect=np.int0(rect)

            cv2.polylines(ventana_camara,[rect],True,(0,522,0),2)

            cv2.putText(ventana_camara,"anchura: {} cm".format(round(anchura,1)),(int(x),int(y-15)),cv2.LINE_AA,0.8,(0, 42, 255),2)
            cv2.putText(ventana_camara,"Largo: {} cm".format(round(altura, 1)),(int(x),int(y+15)),cv2.LINE_AA,0.8,(255,62,0),2)

    else:


        cv2.putText(ventana_camara,"NO SE DETECTO",(80,150), 2, 2,(39, 49, 255),4,cv2.LINE_AA)
        cv2.putText(ventana_camara,"EL ARUCO",(180,210), 2, 2,(39, 49, 255),4,cv2.LINE_AA)
        cv2.putText(ventana_camara,"DE REFERENCIA",(80,260), 2, 2,(39, 49,255),4,cv2.LINE_AA)
        cv2.rectangle(ventana_camara,(60,80),(600,300),(0,0,255),30)
        cv2.rectangle(ventana_camara,(60,80),(600,300),(255,255,255),10)
        cv2.line(ventana_camara,(590,340),(70,340),(0,0,255),60)
        cv2.putText(ventana_camara,"POR FAVOR POSICIONELO EN LA CAMARA PARA PODER MEDIR",(90,350), 1, 1,(255,255,255),2,cv2.LINE_AA)
        
        


    cv2.imshow('Medicion de Objetos', ventana_camara)
    t=cv2.waitKey(1)
    if t==27:
              break

