import Check_Directories
import os
needed_path = os.path.join(Check_Directories.dir_of_files(), 'List.txt')


def add_name():
    input_value = input("put here name of game\n")
    input_value = input_value.capitalize()
    with open(needed_path, 'a') as file:
        file.write(str(input_value) + "\n")


def print_list_of_names():
    with open(needed_path, 'r') as file:
        print(file.read())


def delete_name():
    choice = input("make a choice\n d - delete one name\n a - delete all list\n")
    if choice in ["d", "a"]:
        if choice == "d":
            with open(needed_path, 'r') as file:
                lines = file.readlines()
                num_of_line = 1
                for line in lines:
                    name = line.strip()
                    print(str(num_of_line) + ")" + name)
                    num_of_line += 1
            line_number = int(input("put here number of line u want to delete\n"))
            if 1 <= line_number <= len(lines):
                lines.pop(line_number - 1)
                with open(needed_path, 'w') as file:
                    file.writelines(lines)
                    print("selected name was deleted")
        else:
            choice = input("are you sure that you want to delete all lines?\ny - yes\nn - no\n")
            if choice == "y":
                with open(needed_path, 'w') as file:
                    file.write('')
                print("history was deleted")


def adder_main():
    i = True
    while i:
        user_choice = input("make a choice:\n""a - add name\nh - print list\nd - delete name\nq - quit\n")
        if user_choice == "a":
            add_name()
        elif user_choice == "q":
            i = False
        elif user_choice == "h":
            print_list_of_names()
        elif user_choice == "d":
            delete_name()
        else:
            print("error,try again\n")
    print("have a good day!")
