import os
import time
import Check_Directories
needed_path = os.path.join(Check_Directories.dir_of_folders_of_games())


def create_folders(folder_name):
    folder_path = os.path.join(needed_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder {folder_name} was created")
        time.sleep(0.2)
        return True
    else:
        print(f"Folder {folder_name} already exists")
        time.sleep(0.2)
        return False


def process_file():
    with open(Check_Directories.dir_of_files() + '/Sorted_List.txt', 'r') as file:
        for line in file:
            folder_created = create_folders(line.strip())
            if folder_created:
                file_names = ('description.txt', 'game_mechanics.txt')
                folder_path = os.path.join(needed_path,line.strip())
                for file_name in file_names:
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'w'):
                        pass
            else:
                pass


def folder_creator_main():
    process_file()
