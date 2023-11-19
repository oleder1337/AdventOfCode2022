import os


def read_test_input():
    with open("testinput.txt", "r") as f:
        cont = f.read()
        return cont.split("\n")


def read_input():
    with open("input.txt", "r") as f:
        cont = f.read()
        return cont.split("\n")


class Tree:
    def __init__(
        self,
        value,
        coordinate_x,
        coordinate_y,
        parent_row,
        parent_column,
        forrest_y_size,
        forrest_x_size,
    ):
        self.value = value
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.parent_row = parent_row
        self.parent_column = parent_column
        self.forrest_y_size = forrest_y_size
        self.forrest_x_size = forrest_x_size
        self.visible = False
        self.check_if_visible()

    def check_if_visible(self):
        if self.coordinate_x == 0 or self.coordinate_y == 0:
            self.visible = True
        elif (
            self.coordinate_y == self.forrest_y_size
            or self.coordinate_x == self.forrest_x_size
        ):
            self.visible = True
        elif self.value == max(self.parent_row) or self.value == max(
            self.parent_column
        ):
            self.visible = True
        else:
            self.visible = False


def prepare_data(input):
    forrest = []

    for index_x, tree_row in enumerate(input):
        forrest.append([])
        # forrest[index_x].append(t_1)
        for index_y, tree in enumerate(tree_row):
            forrest[index_x].append(tree)

    return forrest, index_x + 1, index_y + 1


def create_forrest(data, x_length, y_length):
    trees = []
    for index_y, row in enumerate(data):
        x_parents = [x for x in row]
        for index_x, column in enumerate(row):
            t = Tree(
                value=column,
                coordinate_x=index_x,
                coordinate_y=index_y,
                parent_row=x_parents,
                parent_column=[x[index_y] for x in data],
                forrest_x_size=x_length,
                forrest_y_size=y_length,
            )
            trees.append(t)
            print(
                f"Tree created! on Coordinates x={t.coordinate_x} y={t.coordinate_y} with value={t.value}"
            )

        print("")
    return trees


def solve_question_1(forrest):
    return len([x for x in forrest if x.visible])


def main():
    input = read_test_input()
    data, x_length, y_length = prepare_data(input=input)

    forrest = create_forrest(data=data, y_length=y_length, x_length=x_length)

    print(f"Amount of visible Trees: {solve_question_1(forrest=forrest)}")


if __name__ == "__main__":
    os.system("clear")
    main()
