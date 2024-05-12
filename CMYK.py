import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CMYKEditorApp:
    def __init__(self, root):
        self.root = root


        self.canvas_rgb = tk.Canvas(root, width=200, height=200)
        self.canvas_rgb.pack(side=tk.LEFT)


        self.canvas_cmyk = tk.Canvas(root, width=200, height=200)
        self.canvas_cmyk.pack(side=tk.RIGHT)


        self.image_rgb = None
        self.image_cmyk = None

        self.rgb_label = tk.Label(root, text="Imagem RGB")
        self.rgb_label.pack(side=tk.LEFT)

        

        self.cmyk_label = tk.Label(root, text="Imagem CMYK")
        self.cmyk_label.pack(side=tk.RIGHT)



    def load_image_rgb(self, file_path):
        try:
            # Carregar a imagem RGB
            self.image_rgb = Image.open(file_path)
            # Exibir a imagem RGB no canvas
            self.show_image_rgb()
        except FileNotFoundError:
            messagebox.showerror("Erro", "Não foi possível abrir a imagem RGB. Verifique o caminho do arquivo.")

    def show_image_rgb(self):
        if self.image_rgb is not None:
            try:
                # Converter a imagem RGB para o formato suportado pelo Tkinter
                img_tk_rgb = ImageTk.PhotoImage(self.image_rgb)
                # Exibir a imagem RGB no canvas
                self.canvas_rgb.create_image(0, 0, anchor=tk.NW, image=img_tk_rgb)
                self.canvas_rgb.image_rgb = img_tk_rgb  # Manter uma referência para evitar a coleta de lixo
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao exibir imagem RGB: {e}")

    def convert_rgb_to_cmyk(self):
        if self.image_rgb is not None:
            try:
                # Converter a imagem RGB para o modo CMYK
                self.image_cmyk = self.image_rgb.convert("CMYK")
                # Exibir a imagem CMYK no canvas
                self.show_image_cmyk()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao converter imagem RGB para CMYK: {e}")

    def show_image_cmyk(self):
        if self.image_cmyk is not None:
            try:
                # Converter a imagem CMYK para o formato suportado pelo Tkinter
                img_tk_cmyk = ImageTk.PhotoImage(self.image_cmyk)
                # Exibir a imagem CMYK no canvas
                self.canvas_cmyk.create_image(0, 0, anchor=tk.NW, image=img_tk_cmyk)
                self.canvas_cmyk.image_cmyk = img_tk_cmyk  # Manter uma referência para evitar a coleta de lixo
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao exibir imagem CMYK: {e}")


def open_image_RGB(app):
    file_path = "IMG/winx.png"
    if file_path:
        app.load_image_rgb(file_path)


def compare_images(app):
    app.convert_rgb_to_cmyk()


