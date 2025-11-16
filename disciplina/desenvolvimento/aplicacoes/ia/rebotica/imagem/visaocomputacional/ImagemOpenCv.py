import cv2
import matplotlib
import matplotlib.pyplot as plt
print("Versão do OpenCV",cv2.__version__)
print("Versão do Matplotlib", matplotlib.__version__)

imagem = cv2.imread("./imagens/audi.png")
plt.imshow(imagem)




