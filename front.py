import os


def get_target_language():
    target_lang = input("Ingrese el lenguaje de destino para refactorizar el código: ")
    return target_lang 

def get_target_tech():
    target_tech = input("Ingrese las tecnologías o framework de su nuevo proyecto: ")
    return target_tech

def get_source_directory():
    source_directory = input("Ingrese la ruta de la carpeta de archivos a traducir: ")
    return source_directory

def log_directory_contents(source_directory, log_file_path):
    with open(log_file_path, 'w') as log_file:
        for root, _, files in os.walk(source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                log_file.write(f"{file_path}\n")
    print(f"Contenido de la carpeta registrado en: {log_file_path}")

# Lenguaje para traducción
#target_lang = get_target_language()
#target_tech = get_target_tech()

# Obtener la carpeta de archivos
source_directory = get_source_directory()

# Ruta para guardar el registro de los archivos
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'directory_contents.txt')

# Registrar el contenido de la carpeta
log_directory_contents(source_directory, log_file_path)




