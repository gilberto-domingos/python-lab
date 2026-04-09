import os

file_path = "/home/gil/python3/natron_effects/file_exist.py"

def check_file():
    try:
        exist = os.path.exists(file_path)
        print(exist)
    except Exception as ex:
     print(f"Erro: {ex}")

check_file()



