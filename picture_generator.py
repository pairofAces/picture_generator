from PIL import Image

def picture_generator():
    print("Generating Picture!")
    
    image_size_px = 128
    image_bg_color = (255, 255, 255)

    image = Image.new("RGB", (image_size_px, image_size_px), image_bg_color)
    image.save("test_image.png")

if __name__ == "__main__":
    picture_generator()