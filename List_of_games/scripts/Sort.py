import Check_Directories
needed_dir = Check_Directories.dir_of_files()


def sort_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = list(set(file.readlines()))

    sorted_lines = sorted(lines)

    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)


def sort_main():
    sort_file(needed_dir +'/List.txt', needed_dir + '/Sorted_List.txt')

