from PIL import Image, ImageFilter

class ImageEffects:
    def __init__(self, image_path):
        self.image = Image.open(image_path).convert("RGB")

    def apply_blur(self):
        return self.image.filter(ImageFilter.BLUR)

    def apply_contour(self):
        return self.image.filter(ImageFilter.CONTOUR)

    def apply_both_effects(self):
        blurred = self.apply_blur()
        return blurred.filter(ImageFilter.EMBOSS)
