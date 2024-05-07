import tkinter as tk
from PIL import Image, ImageTk

class ComparadorTonsCinza:
    def __init__(self, imagem_rgb):
        self.imagem_rgb = Image.open(imagem_rgb).convert("RGB")

    def gerar_tons_cinza(self):
        tons_cinza = []

        # 1° tom: Média dos valores R, G e B
        ton_cinza_media = Image.new("RGB", self.imagem_rgb.size)  # Cria uma nova imagem com as mesmas dimensões que a imagem original
        pixels_media = ton_cinza_media.load()
        r, g, b = self.imagem_rgb.split()
        width, height = self.imagem_rgb.size
        for x in range(width):
            for y in range(height):
                pixel_r = r.getpixel((x, y))
                pixel_g = g.getpixel((x, y))
                pixel_b = b.getpixel((x, y))
                valor_media = (pixel_r + pixel_g + pixel_b) / 3
                pixels_media[x, y] = (int(valor_media), int(valor_media), int(valor_media))
        tons_cinza.append(ton_cinza_media)
        # 2° tom: Menor valor entre R, G e B
        r, g, b = self.imagem_rgb.split()
        menor_valor = Image.new("RGB", self.imagem_rgb.size)  # Cria uma nova imagem com as mesmas dimensões que a imagem original
        pixels_menor_valor = menor_valor.load()
        pixels_r = r.load()
        pixels_g = g.load()
        pixels_b = b.load()
        width, height = self.imagem_rgb.size
        for x in range(width):
            for y in range(height):
                pixel_r = pixels_r[x, y]
                pixel_g = pixels_g[x, y]
                pixel_b = pixels_b[x, y]
                menor_valor_pixel = min(pixel_r, pixel_g, pixel_b)
                pixels_menor_valor[x, y] = (menor_valor_pixel, menor_valor_pixel, menor_valor_pixel)
        tons_cinza.append(menor_valor)
        
        # 3° tom: Ponderação personalizada
        ton_cinza_ponderado = Image.new("RGB", self.imagem_rgb.size)  # Cria uma nova imagem com as mesmas dimensões que a imagem original
        pixels_ponderado = ton_cinza_ponderado.load()
        for x in range(width):
            for y in range(height):
                pixel_r = pixels_r[x, y]
                pixel_g = pixels_g[x, y]
                pixel_b = pixels_b[x, y]
                valor_ponderado = ((0.4 * pixel_r) + (0.35 * pixel_g) + (0.25 * pixel_b)) / 3
                pixels_ponderado[x, y] = (int(valor_ponderado), int(valor_ponderado), int(valor_ponderado))
        tons_cinza.append(ton_cinza_ponderado)

        return tons_cinza


