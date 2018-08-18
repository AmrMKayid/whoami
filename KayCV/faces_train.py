import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Loading images
image_dir = os.path.join(BASE_DIR, "images")

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(' ', '_').lower()
            print(label, path)
