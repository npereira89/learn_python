from datetime import datetime
import code
import os.path
from PIL import Image

now = datetime.now()

print(now.strftime("%d/%m/%Y, %H:%M:%S"))
print(now.strftime("%d %B of %Y"))

images = []
path = "C://<your directory>"
valid_files = [".jpg", ".gif", ".png"]

for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_files:
        continue
    image_path = os.path.join(path, f)
    with Image.open(image_path) as img:
        img.show()