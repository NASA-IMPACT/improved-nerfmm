from PIL import Image
import os


def convert_tif_to_jpg(tif_file, jpg_file, size=(750, 750)):
    """Convert a tif file to a jpg file."""
    im = Image.open(tif_file).convert('RGB')
    im = im.resize((size[0], size[1]), Image.ANTIALIAS)
    print(im.size)
    im.save(jpg_file)


def convert_all_files_in_dir(dir_in_path, dir_out_path):
    """Convert all files in a directory from one extension to another."""
    if not os.path.exists(dir_out_path):
        os.makedirs(dir_out_path)
    
    for file in os.listdir(dir_in_path):
        
        if file.endswith('tif'):
            convert_tif_to_jpg(
                os.path.join(dir_in_path, file),
                os.path.join(dir_out_path, file.replace('tif', 'jpg')))
            
convert_all_files_in_dir('data/JAX', 'data/JAX_jpg')