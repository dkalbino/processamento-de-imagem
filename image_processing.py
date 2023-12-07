import cv2
import pytesseract
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

class ImageProcessing:

    def __init__(self):
        print('image processing')

    def gray(self, img_path, num):
        img = cv2.imread(img_path)
        cv2.imshow('original image', img)
        cv2.waitKey(0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        cv2.waitKey(0)
        if(num == 1):
            ImageProcessing.pass_string(gray)
        return gray

    def simple_threshold(self, img_path, mim_threshold, num):
        val, thresh = cv2.threshold(img_path, mim_threshold, 255, cv2.THRESH_BINARY) #pixeis q forem inferiores a mim_threshold serão considerados como 0 e se for maior, sera considerado como 255(branco)
        cv2.imshow('thresh', thresh)

        cv2.waitKey(0)
        if(num == 1):
            ImageProcessing.pass_string(thresh)
        return thresh

    def sharp(self,img, num):
        sharp = np.array([[-1, -1, -1],
                                [-1, 9, -1],
                                [-1, -1, -1]])
         
        shrp = cv2.filter2D(img, -1, sharp)
        cv2.imshow('sharp', shrp)
        cv2.waitKey(0)
        if(num == 1):
            ImageProcessing.pass_string(shrp)
        return sharp

    def mediana(self, img, num):
        root = tk.Tk()
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        root.destroy()
        mediana = cv2.medianBlur(img, 5)
        #mediana = cv2.resize(mediana, (750, 750))
        cv2.imshow('mediana', mediana)
        cv2.waitKey(0)
        if(num == 1):
            ImageProcessing.pass_string(mediana)
        return mediana
    
    def blur(self, img, x, num):
        blur = cv2.blur(img, (x,x), 0)
        cv2.imshow('blur', blur)
        cv2.waitKey(0)
        if(num == 1):
            ImageProcessing.pass_string(blur)
        return blur

    def localizar_texto_imagem(self,imagem_path):

        # Encontrar contornos na imagem binária
        contornos, _ = cv2.findContours(imagem_path, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterar sobre os contornos encontrados
        for contorno in contornos:
            # Calcular a caixa delimitadora do contorno
            x, y, w, h = cv2.boundingRect(contorno)

            # Desenhar um retângulo ao redor do contorno
            cv2.rectangle(imagem_path, (x, y), (x + w, y + h), (200,0,0), 2)

        # Exibir a imagem com os contornos destacados
        cv2.imshow('Contornos de Texto', imagem_path)
        cv2.waitKey(0)

    def pass_string(img):
        text = pytesseract.image_to_boxes(img)
        print(text)
        texto = []

        for x in text:
            a = 'a'
            z = 'z'
            A = 'A'
            Z = 'Z'
            if((ord(x) < ord(a) or ord(x) > ord(z)) and (ord(x) < ord(A) or ord(x) > ord(Z))):
                text = text.replace(x, '')
        
        for char in text:
            texto.append(char)
        
        print(texto)


    
    
    
        
        