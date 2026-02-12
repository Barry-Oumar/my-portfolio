import os
from PIL import Image

def optimize_profile_photo():
    source_path = "static/images/oumar_barry_photo.jpg"
    target_path = "static/images/oumar_barry_photo.webp"
    
    if not os.path.exists(source_path):
        print(f"Error: Source file {source_path} not found.")
        return

    try:
        with Image.open(source_path) as img:
            # Resize if too large (e.g., width > 800px is enough for profile)
            max_width = 800
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"Resized to {max_width}x{new_height}")

            # Save as WebP
            img.save(target_path, "WEBP", quality=85, optimize=True)
            print(f"Successfully saved optimized image to {target_path}")
            
            # Compare sizes
            original_size = os.path.getsize(source_path)
            new_size = os.path.getsize(target_path)
            print(f"Original size: {original_size/1024:.2f} KB")
            print(f"New size: {new_size/1024:.2f} KB")
            print(f"Reduction: {(1 - new_size/original_size)*100:.1f}%")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    optimize_profile_photo()
