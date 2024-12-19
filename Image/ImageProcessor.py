from PIL import ImageFilter, Image

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_sharpen_filter(self):
        """
        Применить фильтр резкости к изображению.
        """
        if self.image:
            if self.image.mode not in ("RGB", "RGBA"):
                self.image = self.image.convert("RGB")
            self.image = self.image.filter(ImageFilter.SHARPEN)
        else:
            print("Изображение не загружено!")

    def add_border(self, border_width=15, color="black"):
        """
        Добавить рамку вокруг изображения.
        """
        if self.image:
            new_width = self.image.width + 2 * border_width
            new_height = self.image.height + 2 * border_width
            new_image = Image.new("RGB", (new_width, new_height), color)
            new_image.paste(self.image, (border_width, border_width))
            self.image = new_image
        else:
            print("Изображение не загружено!")

    def save_image(self, save_path):
        """
        Сохранить обработанное изображение.
        """
        if self.image:
            self.image.save(save_path)
        else:
            print("Изображение не загружено!")
