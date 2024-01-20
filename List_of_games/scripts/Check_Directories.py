import os


def dir_of_files():
    relative_path = os.path.join('..', 'files')
    folder_of_files = os.path.abspath(relative_path)
    return folder_of_files


def dir_of_folders_of_games():
    relative_path = os.path.join('..', 'folders_of_games')
    folders_of_games = os.path.abspath(relative_path)
    return folders_of_games


