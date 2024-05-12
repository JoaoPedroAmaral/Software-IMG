import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance

class ImageAdjuster:
    def __init__(self, master, image_path):
        self.master = master
        self.image_path = image_path
        self.original_image = Image.open(self.image_path).convert("RGB")  # Convertendo para o modo RGB
        self.image = self.original_image.copy()
        self.photo_image = ImageTk.PhotoImage(self.image)
        
        self.label = tk.Label(self.master, image=self.photo_image)
        self.label.pack()
        
        self.brightness_scale = tk.Scale(self.master, label="Brilho", from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.adjust_brightness)
        self.brightness_scale.pack()
        
        self.contrast_scale = tk.Scale(self.master, label="Contraste", from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=self.adjust_contrast)
        self.contrast_scale.pack()

    def adjust_brightness(self, value):
        brightness_factor = float(value)
        adjusted_image = ImageEnhance.Brightness(self.original_image).enhance(brightness_factor)
        self.update_image(adjusted_image)

    def adjust_contrast(self, value):
        contrast_factor = float(value)
        adjusted_image = ImageEnhance.Contrast(self.original_image).enhance(contrast_factor)
        self.update_image(adjusted_image)

    def update_image(self, updated_image):
        self.image = updated_image.copy()
        self.photo_image = ImageTk.PhotoImage(updated_image)
        self.label.config(image=self.photo_image)