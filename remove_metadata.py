import os
from PIL import Image

def remove_metadata(image_path, save_path):
    try:
        with Image.open(image_path) as img:
            # Supprimer les métadonnées en réenregistrant l'image sans EXIF
            img_data = list(img.getdata())
            img_no_metadata = Image.new(img.mode, img.size)
            img_no_metadata.putdata(img_data)
            img_no_metadata.save(save_path)
            print(f"Metadata removed: {save_path}")
    except Exception as e:
        print(f"Failed to process {image_path}: {e}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Chemin de sauvegarde (écraser l'image existante)
                remove_metadata(file_path, file_path)

if __name__ == "__main__":
    src_directory = 'src/articles'
    process_directory(src_directory)

