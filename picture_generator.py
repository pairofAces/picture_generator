from PIL import Image

def picture_generator():
    print("Generating Picture!")
    image = Image.new("RGB", (128, 128), (255, 255, 255))
    image.save("test_image.png")

if __name__ == "__main__":
    picture_generator()