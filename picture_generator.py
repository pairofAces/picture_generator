from PIL import Image, ImageDraw

def picture_generator():
    print("Generating Picture!")

    image_size_px = 128
    image_bg_color = (255, 255, 255)

    image = Image.new(
        "RGB", 
        size=(image_size_px, image_size_px), 
        color=image_bg_color)

    #Draw lines on the image
    draw = ImageDraw.Draw(image)
    draw.line()

    image.save("test_image.png")

if __name__ == "__main__":
    picture_generator()