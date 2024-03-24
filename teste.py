import os.path
from PIL import Image

images = []
path = "C://Users/Nuno/Downloads"
valid_files = [".jpg", ".gif", ".png", ".mp4"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_files:
        continue
    image_path = os.path.join(path, f)
    with Image.open(image_path) as img:
        img.show()
