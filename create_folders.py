import os
import shutil
import json


def organize_files(folder_path, file_data):
    folder_names = set(file_data.values())
    for folder in folder_names:
        folder_dir = os.path.join(folder_path, folder)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
            print(f"Created folder: {folder_dir}")

    for file_name, folder_name in file_data.items():
        if folder_name in folder_names:
            source_file_path = os.path.join(folder_path, file_name)
            target_folder_path = os.path.join(folder_path, folder_name)

            if os.path.exists(source_file_path):

                target_file_path = os.path.join(target_folder_path, file_name)
                shutil.move(source_file_path, target_file_path)
                print(f"Moved {file_name} to {target_folder_path}")
            else:
                print(f"File {file_name} not found in the source folder.")
        else:
            print(f"Folder {folder_name} not found in the list of folder names.")


def create_folders(folder_path):
    with open("paper_folder_mapping.json", "r") as file:
        json_data = json.load(file)
    organize_files(folder_path, json_data)


if __name__ == "__main__":
    os.system("clear")
    folder_path = "/Users/armin/Desktop/HEC/Research/Data Analytics Gorup/LLM fairness"
    create_folders(folder_path)
