import os
import re
def main_menu():
    while True:
        print("Menú Principal")
        print("1. Opción: Opcion Uno Renombrar Archivos")
        print("2. Opción: Opcion Dos Renombrar Archivos")
        print("3. Fin del Programa")
        
        choice = input("Por favor, elija una opción (1-4): ")
        
        if choice == "1":
            print("Opcion Uno Renombrar Archivos")
            
            def reorder_files(folder_path):
                # Lista todos los archivos en la carpeta
                files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                
                # Ordena los archivos alfabéticamente para mantener un orden predecible
                files.sort()

                # Renombra los archivos para asignar números secuenciales
                for i, filename in enumerate(files):
                    # Obtén la extensión del archivo
                    file_extension = os.path.splitext(filename)[1]
                    # Genera el nuevo nombre del archivo con un número secuencial
                    new_filename = f"{i + 1}{file_extension}"
                    # Renombra el archivo
                    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                    print(f"Renamed {filename} to {new_filename}")

            # Obtener la ruta de la carpeta del usuario
            folder_path = input("Ingrese la ruta de la carpeta: ")

            # Usar la función con la ruta de la carpeta proporcionada por el usuario
            reorder_files(folder_path)
            
            
        elif choice == "2":
            print("Opcion Dos Rellenar Archivos")

            def get_file_number(filename):
                # Extrae el número del nombre del archivo usando una expresión regular
                match = re.match(r"(\d+)", filename)
                return int(match.group(1)) if match else None

            def reorder_files(folder_path):
                # Lista todos los archivos en la carpeta
                files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                
                # Filtra y ordena los archivos por su número
                numbered_files = sorted([f for f in files if get_file_number(f) is not None], key=get_file_number)
                
                # Renombra los archivos para llenar los espacios
                for i, filename in enumerate(numbered_files):
                    current_number = get_file_number(filename)
                    if current_number != i + 1:
                        # Genera el nuevo nombre del archivo
                        new_filename = re.sub(r"^\d+", str(i + 1), filename)
                        # Renombra el archivo
                        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                        print(f"Renamed {filename} to {new_filename}")


            # Usar la función con la ruta de la carpeta

            folder_path = input("Ingrese Aqui La ruta de la carpeta:")
            reorder_files(folder_path)
            
        elif choice == 3:
            print("Saliendo de el programa.")
            break
        
        else:
            print("Este numero no esta en la lista marque otro.")

# Ejecutar el menú principal
main_menu()