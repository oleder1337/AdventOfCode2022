import os


DISK_LIMIT = 70000000
NEEDED_UPDATE_SPACE = 30000000


def read_test_input():
    with open("test_input.txt", "r") as f:
        cont = f.read()
        return cont.split("\n")


def read_input():
    with open("input.txt", "r") as f:
        cont = f.read()
        return cont.split("\n")


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.size = 0
        self.type = "directory"
        self.parent = parent
        self.size = 0

    def add_children(self, child):
        if child not in self.children:
            self.children.append(child)

    def check_if_dir_exists(self, dest_dir):
        child_dirs = [x.name for x in self.children if x.type == "directory"]
        if dest_dir in child_dirs:
            return True
        else:
            return False

    def find_child_dir(self, dest_dir):
        for child in self.children:
            if child.type == "directory" and child.name == dest_dir:
                return child

    def get_parent(self):
        return self.parent


class File:
    def __init__(self, size, parent, name, filetype=None):
        self.name = name
        self.size = int(size)
        self.filetype = filetype
        self.parent = parent
        self.type = "file"


def parse_listing(command, parent: Dir):
    if "dir " in command:
        dir_name = command.split("dir ")[1]
        d = Dir(name=dir_name, parent=parent)
        parent.add_children(child=d)
        return

    else:
        file = command.split(" ")
        file_size = file[0]
        filename = file[1]
        if "." in filename:
            filetype = filename.split(".")[1]
        else:
            filetype = None
        f = File(size=file_size, parent=parent, name=filename, filetype=filetype)
        parent.add_children(child=f)
        return


def get_directory_size(dir: Dir, size):
    for content in dir.children:
        if content.type == "file":
            size += content.size

        else:
            size += get_directory_size(dir=content, size=size)
    return size


def print_dir(directory: Dir, hierarchy=0):
    for i in directory.children:
        s = ""

        for index in range(0, hierarchy):
            s += "\t"
        if i.type == "file":
            s += f"- {i.name} ({i.type}, size={i.size})"
        else:
            s += f"- {i.name} ({i.type}, size={i.size})"
        print(s)
        if i.type == "directory":
            print_dir(directory=i, hierarchy=hierarchy + 1)


def get_dir_sizes(directory: Dir):
    size = 0

    for content in directory.children:
        if content.type == "directory":
            size += get_dir_sizes(directory=content)
        else:
            size += content.size

    directory.size = size
    return size


def solve_question_1(directory: Dir):
    solution = 0
    for dir in directory.children:
        if dir.type == "directory":
            if dir.size < 100000:
                solution += dir.size
            solution += solve_question_1(directory=dir)
    return solution


def solve_question_2(directory: Dir):
    def recursive_directory_runnter(directory: Dir, missing_diskspace):
        possible_deletable_directories = []
        for child in directory.children:
            if child.type == "directory":
                if child.size > missing_diskspace:
                    possible_deletable_directories.append(child)
                possible_deletable_directories.extend(
                    recursive_directory_runnter(
                        directory=child, missing_diskspace=missing_diskspace
                    )
                )
        return possible_deletable_directories

    def select_smallest_directory(possible_deletable_directories: list):
        min_size = max([x.size for x in possible_deletable_directories])

        for dir in possible_deletable_directories:
            if dir.size <= min_size:
                min_size = dir.size
                min_name = dir.name

        return min_name, min_size

    used_diskspace = get_dir_sizes(directory=directory)
    free_diskspace = DISK_LIMIT - used_diskspace
    missing_diskspace = NEEDED_UPDATE_SPACE - free_diskspace
    # print(f"This is the used diskspace: {used_diskspace}")
    # print(f"Free Diskspace: {free_diskspace}")
    # print(f"Missing Diskspace: {missing_diskspace}")
    solution = 0

    possible_deletable_directories = recursive_directory_runnter(
        directory=directory, missing_diskspace=missing_diskspace
    )

    min_name, min_size = select_smallest_directory(
        possible_deletable_directories=possible_deletable_directories
    )

    print(
        f"Solution to Question 2: Directory to be deleted: {min_name} (size={min_size})"
    )


def main():
    data = read_input()

    root = Dir(name="root", parent=None)
    listmode = True
    commandmode = False

    for command in data:
        if "$" in command and listmode:
            commandmode = True
            listmode = False
        if command == "$ ls":
            commandmode = False
            listmode = True
            continue

        if listmode:
            parse_listing(command=command, parent=root)

        if "cd " in command:
            if ".." in command:
                if root.get_parent != None:
                    root = root.get_parent()
                else:
                    continue

            else:
                dest_dir = command.split(" ")[2]
                if root.check_if_dir_exists(dest_dir=dest_dir):
                    root = root.find_child_dir(dest_dir=dest_dir)
                else:
                    d = Dir(name=dest_dir, parent=root)
                    root.add_children(child=d)
                    root = d
    while root.parent != None:
        root = root.parent
    # print_directory(directoy=dir)
    # print(dir.children[0].children)
    # dir_size = get_directory_size(dir=root, size=0)
    # print(dir_size)

    print(f"Complete Directory Sizes: {get_dir_sizes(directory=root)}")
    print_dir(directory=root)
    print("")

    print(f"Solution to Question 1: {solve_question_1(directory=root)}\n")
    solve_question_2(directory=root)


if __name__ == "__main__":
    os.system("clear")
    main()
