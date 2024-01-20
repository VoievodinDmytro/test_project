import Adder, folder_creator, Sort, work_with_folders


def case_a():
    Adder.adder_main()


def case_f():
    folder_creator.folder_creator_main()


def case_s():
    Sort.sort_main()


def case_w():
    work_with_folders.work_with_folders_main()


while True:
    user_input = input("choose which script u want to launch:\n"
                   "a - adder\nf - folder creator\ns - sort\n"
                   "w - work with folders\nq - quit\n").lower()

    switch = {
        'a': case_a,
        'f': case_f,
        's': case_s,
        'w': case_w,
        'q': lambda: None
    }
    switch.get(user_input)()

    if user_input == 'q':
        break
