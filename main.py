from image_processing import ImageProcessing
import cv2

if __name__ == '__main__':
    imgProcessing = ImageProcessing() 
    
    img = imgProcessing.gray('.vscode/projetos/codes/python/images/img2.png', 0)
    img = imgProcessing.simple_threshold(img, 65 , 1)
    imgProcessing.localizar_texto_imagem(img)
    #img2 = imgProcessing.sharp(img, 0)
    #img = imgProcessing.mediana(img, 0)
    #img = imgProcessing.blur(img, 4, 0)