import os
import Check_Directories

number_of_folder = None


def work_with_file(selected_folder):
    a = True
    folder_path = os.path.join(Check_Directories.dir_of_folders_of_games(), selected_folder)
    file_to_work_path = os.path.join(folder_path, 'game_mechanics.txt')

    try:
        with open(file_to_work_path, 'r') as file:
            while a:
                user_input = input("do choice:\na - add a mechanic\nd - delete mechanic\ns - see mechanics\nq - quit\n")
                if user_input in ['a', 'd', 'q', 's']:
                    if user_input == 'a':
                        user_input_mechanic = input("put here name of mechanic:\n")
                        user_input_description = input("put here description of game mechanic:\n")
                        mechanic = {user_input_mechanic: user_input_description}
                        with open(file_to_work_path, 'a'):
                            file.write(str(mechanic) + "\n")
                    elif user_input == 'q':
                        a = False
                    elif user_input == 's':
                        with open(file_to_work_path, 'r'):
                            content = file.read()
                            print(content)
                    else:
                        lines = file.readlines()
                        num_of_line = 1
                        for line in lines:
                            name = line.strip()
                            print(str(num_of_line) + ")" + name)
                            num_of_line += 1
                        line_number = int(input("put here number of mechanic u want to delete\n"))
                        if 1 <= line_number <= len(lines):
                            lines.pop(line_number - 1)
                            with open(file_to_work_path, 'w'):
                                file.writelines(lines)
                                print("selected mechanic was deleted")
    except FileNotFoundError:
        print(f"File '{file_to_work_path}' not found. Please check if the file exists.")


def display_folders(folders_to_show):
    global number_of_folder
    directory_path = Check_Directories.dir_of_folders_of_games()
    items = os.listdir(directory_path)

    folders = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]
    sorted_folders = sorted(folders)

    if sorted_folders:
        for idx, folder in enumerate(sorted_folders, start=1):
            print(f"{idx}) {folder}")

        if 'e' in folders_to_show:
            pass

        number_of_folder = input("Choose the number of the folder you want to open:\n ")
        if number_of_folder:
            try:
                number_of_folder = int(number_of_folder)
                selected_folder = sorted_folders[number_of_folder - 1]

                if 'e' in folders_to_show and number_of_folder == len(sorted_folders) + 1:
                    display_empty_folders()
                else:
                    user_input = input("do choice:\nd - open description\n"
                                       "m - open list of game mechanics\n")
                    if user_input in ['d', 'm']:
                        if user_input == 'd':
                            file_path = os.path.join(directory_path, selected_folder, 'description.txt')
                            with open(file_path, 'r') as file:
                                content = file.read()
                                print(content)
                        else:
                            file_path = os.path.join(directory_path, selected_folder, 'game_mechanics.txt')
                            with open(file_path, 'r') as file:
                                content = file.read()
                                print(content)
                            work_with_file(selected_folder)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number.")
    else:
        print("There are no folders.")


def display_empty_folders():
    base_folder = Check_Directories.dir_of_folders_of_games()
    folders = sorted(os.listdir(base_folder))
    x = 1
    for folder_name in folders:
        folder_path = os.path.join(base_folder, folder_name)
        found_empty_file = False
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.getsize(file_path) == 0 and not found_empty_file:
                print(f"{x}) {folder_name}")
                x += 1
                found_empty_file = True


def work_with_folders_main():
    i = True
    while i:
        user_input = input("s - see folders\ne - see empty folders\nq - quit\n")
        if user_input in ['s', 'q', 'e']:
            if user_input == "s":
                display_folders(['e'])
            elif user_input == 'e':
                display_folders(['e'])
            else:
                i = False
    print("bye bye")
