import os
import random
import argparse


def get_random_wallpaper(folder_path):
    valid_ext = [".jpg","jpeg","png"]
    
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"La carpeta no existe: {folder_path}")
    
    image_files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and
        os.path.splitext(f)[1].lower() in valid_ext
    ]
    
    if not image_files:
        raise ValueError(f"No se encontraron imagenes en la carpeta: {folder_path}")
    
    selected_image = random.choice(image_files)
    return selected_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Selecciona un fondo de pantalla aleatorio")
    parser.add_argument("folder", type=str, help="Ruta de la carpeta con imagenes")
    args = parser.parse_args()
    
    try:
        wallpaper = get_random_wallpaper(args.folder)
        print(f"fondo seleccionado: {wallpaper}")
    except Exception as e:
        print(f"Error: {e}")
