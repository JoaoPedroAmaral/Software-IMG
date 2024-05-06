import cv2
import numpy as np

def cinza_escala_1(image):
    # Convertendo a imagem para escala de cinza usando a média de R, G e B
    return np.mean(image, axis=2).astype(np.uint8)

def cinza_escala_2(image):
    # Convertendo a imagem para escala de cinza usando o valor máximo de R, G ou B
    return np.max(image, axis=2).astype(np.uint8)

def cinza_escala_3(image, weights=(0.3, 0.59, 0.11)):
    # Convertendo a imagem para escala de cinza usando pesos personalizados para R, G e B
    return np.dot(image[..., :3], weights).astype(np.uint8)

def select_image_convert(image_path):
    # Abrindo a imagem
    image = cv2.imread(image_path)

    # Convertendo a imagem para os três tipos de tons de cinza
    imagem_cinza_1 = cinza_escala_1(image)
    imagem_cinza_2 = cinza_escala_2(image)
    imagem_cinza_3 = cinza_escala_3(image)

    # Salvando as imagens em tons de cinza
    cv2.imwrite("imagem_cinza_1.jpg", imagem_cinza_1)
    cv2.imwrite("imagem_cinza_2.jpg", imagem_cinza_2)
    cv2.imwrite("imagem_cinza_3.jpg", imagem_cinza_3)

    # Comparando as imagens
    comparando_imagens_cinza(imagem_cinza_1, imagem_cinza_2, imagem_cinza_3)

def comparando_imagens_cinza(imagem_cinza_1, imagem_cinza_2, imagem_cinza_3):
    # Exemplo de comparação: verificar se as imagens têm a mesma dimensão
    if imagem_cinza_1.shape == imagem_cinza_2.shape == imagem_cinza_3.shape:
        print("As imagens em tons de cinza têm as mesmas dimensões.")
    else:
        print("As imagens em tons de cinza têm dimensões diferentes.")

    # Outras comparações podem ser adicionadas conforme necessário

