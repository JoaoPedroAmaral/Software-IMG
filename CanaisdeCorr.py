from PIL import Image

class RGBFilter:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        if self.image.mode != 'RGB':
            self.image = self.image.convert('RGB')

    def remove_red_channel(self):
        r, g, b = self.image.split()
        zero_channel = r.point(lambda _: 0)
        return Image.merge("RGB", (zero_channel, g, b))

    def remove_green_channel(self):
        r, g, b = self.image.split()
        zero_channel = g.point(lambda _: 0)
        return Image.merge("RGB", (r, zero_channel, b))

    def remove_blue_channel(self):
        r, g, b = self.image.split()
        zero_channel = b.point(lambda _: 0)
        return Image.merge("RGB", (r, g, zero_channel))
