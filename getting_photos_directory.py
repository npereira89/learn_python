from datetime import datetime
import code
import os.path
from PIL import Image, UnidentifiedImageError

now = datetime.now()

path = "C://Users//Nuno//Pictures//"
valid_files = [".jpg", ".gif", ".png", ".jpeg", ".webp"]

for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() in valid_files:
        image_path = os.path.join(path, f)
        if os.path.isfile(image_path):
            try:
                img_data = Image.open(image_path)
                img_data.show()
            except UnidentifiedImageError:
                print(f"The path {image_path} is a directory")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
