from Image.ImageHandler import ImageHandler
from Image.ImageProcessor import ImageProcessor 

def main_menu():
    print()
    print(" Меню работы с изображением ".center(80,"="))
    print("1. Конвертировать изображение в формат PNG")
    print("2. Повернуть изображение на 45 градусов")
    print("3. Применить фильтр резкости")
    print("4. Добавить рамку к изображению")
    print("5. Сохранить изображение")
    print("6. Показать изображение")
    print("7. Выход")
    return input("Выберите действие: ")

def main():
    # Исходное изображение передаётся в коде
    initial_image_path = "image_5.jpg"  # Укажите путь к вашему изображению
    handler = ImageHandler(initial_image_path)
    handler.load_image()
    processor = ImageProcessor(handler.get_image())

    print("Изображение успешно загружено из пути:", initial_image_path)

    while True:
        choice = main_menu()

        if choice == "1":
            if handler.image:
                save_path = input("Введите путь для сохранения (с расширением .png): ")
                handler.convert_to_png(save_path)
                print(f"Изображение сохранено в формате PNG по пути {save_path}.")
            else:
                print("Изображение не загружено.")

        elif choice == "2":
            if handler.image:
                handler.rotate_image()
                processor = ImageProcessor(handler.get_image())
                print("Изображение повернуто на 45 градусов.")
            else:
                print("Изображение не загружено.")

        elif choice == "3":
            if processor.image:
                processor.apply_sharpen_filter()
                print("Фильтр резкости применён.")
            else:
                print("Изображение не загружено.")

        elif choice == "4":
            if processor.image:
                processor.add_border(border_width=15, color="black")
                print("Рамка добавлена.")
            else:
                print("Изображение не загружено.")

        elif choice == "5":
            if processor.image:
                save_path = input("Введите путь для сохранения обработанного изображения: ")
                processor.save_image(save_path)
                print(f"Изображение сохранено по пути {save_path}.")
            elif handler.image:
                save_path = input("Введите путь для сохранения исходного изображения: ")
                handler.save_image(save_path)
                print(f"Изображение сохранено по пути {save_path}.")
            else:
                print("Изображение не загружено.")

        elif choice == "6":
            if processor.image:
                processor.image.show()
            elif handler.image:
                handler.image.show()
            else:
                print("Изображение не загружено.")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
