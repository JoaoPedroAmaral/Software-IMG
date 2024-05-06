import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np
from tkinter.colorchooser import askcolor



class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Imagem")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<Motion>", self.show_pixel_color)
        self.canvas.bind("<Button-1>", self.change_pixels_color)

        self.image = None
        self.selected_color = None

    def load_image(self, file_path):
        try:
            # Carregar a imagem
            self.image = cv2.imread(file_path)
            if self.image is None:
                raise FileNotFoundError
            # Exibir a imagem no canvas
            self.show_image()
        except FileNotFoundError:
            messagebox.showerror("Erro", "Não foi possível abrir a imagem. Verifique o caminho do arquivo.")

    def show_image(self):
        if self.image is not None:
            try:
                # Converter a imagem para RGB (OpenCV lê em BGR)
                img_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # Converter de BGR para RGB
                # Inverter manualmente os canais de cores (R <-> B)
                img_rgb[:, :, [0, 2]] = img_rgb[:, :, [2, 0]]  # Trocar os canais R e B
                # Converter a imagem para formato suportado pelo Tkinter
                img_tk = self.convert_to_tkinter_photoimage(img_rgb)
                # Exibir a imagem no canvas
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
                self.canvas.image = img_tk  # Manter uma referência para evitar a coleta de lixo
            except cv2.error as e:
                messagebox.showerror("Erro", f"Erro ao converter imagem: {e}")

    def convert_to_tkinter_photoimage(self, img):
        height, width, channels = img.shape
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_tk = Image.fromarray(img_rgb)
        return ImageTk.PhotoImage(img_tk)


    def show_pixel_color(self, event):
        if self.image is not None:
            # Obter as coordenadas do pixel sob o cursor do mouse
            x, y = event.x, event.y
            try:
                # Obter o valor do pixel na imagem
                bgr_color = self.image[y, x]
                # Atualizar a cor selecionada
                self.selected_color = tuple(bgr_color)
                # Atualizar o texto na barra de status
                self.root.status.set(f"RGB: {bgr_color}")
            except IndexError:
                pass

    def change_pixels_color(self, event):
        if self.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        if self.selected_color is None:
            messagebox.showwarning("Aviso", "Nenhuma cor selecionada.")
            return

        # Obter as coordenadas do pixel clicado
        x, y = event.x, event.y
        # Obter a cor do pixel clicado
        clicked_color = self.image[y, x]

        # Abrir a caixa de diálogo para selecionar uma nova cor
        new_color = askcolor(title="Selecione a nova cor")
        if new_color[1] is not None:  # Se o usuário selecionou uma cor
            new_rgb_color = new_color[0]  # Obter a cor RGB selecionada pelo usuário
            # Definir o limite para considerar se duas cores são iguais
            color_threshold = 30  # Valor arbitrário para a diferença de cor

            # Alterar a cor de todos os pixels da imagem que estão dentro do limite de cor
            for i in range(self.image.shape[0]):
                for j in range(self.image.shape[1]):
                    # Calcular a diferença de cor entre o pixel clicado e o pixel atual
                    color_diff = np.linalg.norm(self.image[i, j] - clicked_color)
                    if color_diff < color_threshold:
                        self.image[i, j] = new_rgb_color[::-1]  # Inverter a ordem RGB para BGR

            # Atualizar a imagem no canvas
            self.show_image()
    def rgb_para_cmyk(rgb_color):
        # Normaliza os valores RGB
        r, g, b = [x / 255.0 for x in rgb_color]
        
        # Calcula os valores CMY
        c = 1 - r
        m = 1 - g
        y = 1 - b
        
        # Calcula o valor K
        k = min(c, m, y)
        
        # Evita a divisão por zero
        if k == 1:
            cmyk_color = [0, 0, 0, 1]
        else:
            cmyk_color = [(c - k) / (1 - k), (m - k) / (1 - k), (y - k) / (1 - k), k]
        
        return [int(x * 100) for x in cmyk_color]  # Escala os valores CMYK para o intervalo de 0 a 100

# Função para carregar uma imagem
def open_image(app):
    file_path = "IMG/winx.jpg"
    if file_path:
        app.load_image(file_path)


