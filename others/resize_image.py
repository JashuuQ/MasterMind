from PIL import Image

def resize_image():
    original_image = Image.open('button_board/quit.gif')
    aspect_ratio = original_image.width / original_image.height

    new_width = 50
    new_height = int(new_width / aspect_ratio)

    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)

    resized_image.save('button_board/resized_quit.gif')