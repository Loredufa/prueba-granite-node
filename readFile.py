import os


#lee el archivo directory_contents.txt, que contiene las rutas de los archivos 
def read_and_collect_files():
    # Ruta del archivo que contiene las rutas de los archivos a leer
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'directory_contents.txt')

    # Leer el archivo directory_contents.txt
    with open(log_file_path, 'r') as file:
        file_paths = file.readlines()

    # Variable para almacenar el contenido de todos los archivos
    all_files_content = ""

    # Recorrer cada ruta de archivo en directory_contents.txt
    for file_path in file_paths:
        # Limpiar la ruta del archivo de espacios en blanco o saltos de línea
        file_path = file_path.strip()

        # Verificar si el archivo existe
        if os.path.exists(file_path):
            # Leer el contenido del archivo
            with open(file_path, 'r') as f:
                file_content = f.read()
                all_files_content += f"Contenido del archivo: {file_path}\n\n{file_content}\n\n"
        else:
            all_files_content += f"Archivo no encontrado: {file_path}\n\n"

    return all_files_content
