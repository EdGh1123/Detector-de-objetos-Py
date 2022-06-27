import cv2

class DetectorFondoHomogeneo():
    def __init__(self):
        pass
    def deteccion_objetos(self,ventana_camara):
        gray=cv2.cvtColor(ventana_camara,cv2.COLOR_BGR2GRAY)

        mask=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,19,5)
        delimitacion_contorno, _ =cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        objetos_delimitacion_contorno=[]

        for cnt in delimitacion_contorno:
            area=cv2.contourArea(cnt)
            if area>2000:
                objetos_delimitacion_contorno.append(cnt)
                
        return objetos_delimitacion_contorno