from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path)
        return self.image

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)
        else:
            print("Изображение не загружено!")

    def convert_to_png(self, save_path):
        """
        Конвертировать изображение в формат PNG.
        """
        if self.image:
            self.image = self.image.convert("RGBA")
            self.image.save(save_path, "PNG")
        else:
            print("Изображение не загружено!")

    def rotate_image(self, angle=45):
        """
        Повернуть изображение на указанный угол.
        """
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
        else:
            print("Изображение не загружено!")

    def get_image(self):
        """
        Получить текущее изображение.
        """
        if self.image:
            return self.image
        else:
            print("Изображение не загружено!")
            return None
